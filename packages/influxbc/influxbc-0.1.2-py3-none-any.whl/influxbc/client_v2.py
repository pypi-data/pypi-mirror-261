import warnings
from datetime import datetime
from typing import Union, Optional, Dict, List

import influxdb_client
import pandas as pd
from influxdb_client import WriteOptions

from . import errors
from .const import (
    INFLUX_EPOCH,
    INFLUX_DEFAULT_BATCH_SIZE,
)
from ._base import BaseClient, WriteMode, FirstLast

AUTOGEN_RETENTION_POLICY = "autogen"


class InfluxDBV2Client(influxdb_client.InfluxDBClient, BaseClient):
    """
    A client for InfluxDB V2.
    For query and write interactions with InfluxDB 1.8 instances,
    use the `from_v18_config` factory.
    """

    def __init__(self, url, token: str, bucket_name: str, **kwargs):
        """
        :param url: URL of the InfluxDB instance
        :param token: Token to authenticate to the InfluxDB API
        :param bucket_name: Name of a bucket to interact with
        """
        influxdb_client.InfluxDBClient.__init__(
            self, url=url, token=token, **kwargs
        )
        self.bucketName = bucket_name
        self.queryAPI = self.query_api()

    @classmethod
    def from_v18_config(
        cls,
        url,
        username: str,
        password: str,
        database: str,
        retention_policy: str = AUTOGEN_RETENTION_POLICY,
    ) -> "InfluxDBV2Client":
        """
        Create a client from a V1 configuration.
        Use this to create a client to connect to a InfluxDB version 1.8 instance.
        For this to work, the Flux compatibility endpoint must be enabled in
        your V1 instance, see:
        https://docs.influxdata.com/influxdb/v1/flux/installation/
        :param url: URL of the InfluxDB V1 instance
        :param username: Username to authenticate with
        :param password: Password to authenticate with
        :param database: Database name to interact with
        :param retention_policy: Optional retention policy for write operations
        :return: InfluxDB client for V1 instances
        """
        token = f"{username}:{password}"
        bucket_name = f"{database}/{retention_policy}"
        org = "-"
        return cls(url=url, token=token, org=org, bucket_name=bucket_name)

    # region Meta
    @property
    def client_major(self) -> int:
        """
        The InfluxDB major version the client is primarily made for
        """
        return 2

    # endregion

    # region Schema & Management
    def get_databases(self) -> List[str]:
        """
        List of all buckets of the organisation
        """
        query = f"""    
        buckets()
        """
        tables = self.queryAPI.query(query=query, org=self.org)

        # Flatten output tables into list of measurements
        buckets_lst = [row.values["name"] for table in tables for row in table]

        return buckets_lst

    get_buckets = get_databases

    def get_measurements(
        self,
    ) -> List[str]:
        """
        List of all available measurements in the currently associated database
        :return: List of measurements
        """
        query = f"""
        import \"influxdata/influxdb/schema\"

        schema.measurements(
            bucket: \"{self.bucketName}\",
            start: {INFLUX_EPOCH}
        )
        """
        tables = self.queryAPI.query(query=query, org=self.org)

        # Flatten output tables into list of measurements
        measurements = [
            row.values["_value"] for table in tables for row in table
        ]

        return measurements

    def get_fields(
        self,
        measurement: Optional[str] = None,
    ) -> List[str]:
        """
        List available fields in a given measurement
        or in all measurements of the entire database
        :param measurement: Name of the measurement.
            If given, only fields for this particular measurement are returned.
            If not given, fields of all measurements from database are returned.
        :return: List of fields
        """

        if measurement is None:
            query = f"""
            import \"influxdata/influxdb/schema\"

            schema.fieldKeys(
                bucket:  \"{self.bucketName}\",
                start: {INFLUX_EPOCH}
            )
            """
        else:
            self._warn_measurement_does_not_exist(measurement)
            query = f"""
            import \"influxdata/influxdb/schema\"

            schema.measurementFieldKeys(
                bucket: \"{self.bucketName}\",
                measurement: \"{measurement}\",
                start: {INFLUX_EPOCH}
            )
            """

        tables = self.queryAPI.query(query=query, org=self.org)

        # Flatten output tables into list
        fields = [row.values["_value"] for table in tables for row in table]

        return fields

    _INTERNAL_TAG_KEYS = ("_measurement", "_start", "_stop", "_field")

    def get_tag_keys(
        self,
        measurement: Optional[str] = None,
    ) -> List[str]:
        """
        List all available tag keys in a given measurement
        or in all measurements of the entire database.
        Filter internal tag keys (s. _INTERNAL_TAG_KEYS).
        :param measurement: Name of the measurement.
            If given, only fields for this particular measurement are returned.
            If not given, fields of all measurements from database are returned.
        :return: List of tag keys
        """

        if measurement is None:
            query = f"""
            import \"influxdata/influxdb/schema\"

            schema.tagKeys(
                bucket:  \"{self.bucketName}\",
                start: {INFLUX_EPOCH}
            )
            """
        else:
            self._warn_measurement_does_not_exist(measurement)

            query = f"""
            import \"influxdata/influxdb/schema\"

            schema.measurementTagKeys(
                bucket: \"{self.bucketName}\",
                measurement: \"{measurement}\",
                start: {INFLUX_EPOCH}
            )

            """

        tables = self.queryAPI.query(query=query, org=self.org)

        # Flatten output tables into list
        tag_keys = [
            row.values["_value"]
            for table in tables
            for row in table
            if row.values["_value"] not in self._INTERNAL_TAG_KEYS
        ]

        return tag_keys

    def get_tag_values(
        self,
        tag_key: str,
        measurement: Optional[str] = None,
    ) -> List[str]:
        """
        List all available tag values that are present for a tag key.
        :param tag_key: Tag key
        :param measurement: Name of the measurement.
            If given, only fields for this particular measurement are returned.
            If not given, fields of all measurements from database are returned.
        :return: List of tag values
        """

        if measurement is None:
            if tag_key not in self.get_tag_keys():
                msg = f'Given tag key "{tag_key}" does not exist.'
                warnings.warn(msg)
            query = f"""
            import \"influxdata/influxdb/schema\"

            schema.tagValues(
                bucket:  \"{self.bucketName}\", 
                tag: \"{tag_key}\",
                start: {INFLUX_EPOCH}
            )
            """
        else:
            self._warn_measurement_does_not_exist(measurement)
            if tag_key not in self.get_tag_keys(measurement=measurement):
                msg = (
                    f'Given tag key "{tag_key}" does not exist'
                    f' in measurement "{measurement}".'
                )
                warnings.warn(msg)

            query = f"""
            import \"influxdata/influxdb/schema\"

            schema.measurementTagValues(
                bucket: \"{self.bucketName}\",
                tag: \"{tag_key}\",
                measurement: \"{measurement}\",
                start: {INFLUX_EPOCH}
            )
            """

        tables = self.queryAPI.query(query=query, org=self.org)

        # Flatten output tables into list
        tag_values = [row.values["_value"] for table in tables for row in table]

        return tag_values

    def delete(
        self,
        measurement: Optional[str] = None,
        tags: Optional[dict] = None,
    ):
        """
        Delete points from a database.
        If given, delete only from a single measurement.
        If given, delete only points where the given tags apply
        in a logical conjunction (AND) criterion.
        If the given measurement does not exist, raise an error.
        If no data matches the measurement/tags combination, raise a warning.
        :param measurement: Measurement to delete from
        :param tags: The tags which will chained for the WHERE criterion
        """
        err_msg = "Cannot delete points."
        start = INFLUX_EPOCH

        if measurement is None and (tags is None or len(tags) == 0):
            err_msg = (
                "Deleting by specifying neither measurement nor tags"
                " is not allowed through delete() as it would wipe the"
                " entire bucket."
                " You can drop (and recreate) the bucket instead."
            )
            raise errors.DeleteError(err_msg)

        predicate_clauses = []
        if measurement is not None:
            if measurement not in self.get_measurements():
                err_msg += f" Given measurement {measurement} does not exist."
                raise errors.SchemaError()
            measurement_clause = f'_measurement="{measurement}"'
            predicate_clauses.append(measurement_clause)

        if tags is not None and len(tags) != 0:
            tags_clause = " AND ".join(
                f'"{tag_key}"="{tag_value}"'
                for tag_key, tag_value in tags.items()
            )
            predicate_clauses.append(tags_clause)

        predicate = " AND ".join(predicate_clauses)

        # Raise a warning when the predicate does not match any data
        if measurement is not None:
            data = self.read_data_frame(
                measurement=measurement,
                start=start,
                tags=tags,
            )
            if data.empty:
                msg = f'No data deleted. Predicate was "{predicate}".'
                warnings.warn(msg)

        self.delete_api().delete(
            start=start,
            stop=datetime.now(),
            predicate=predicate,
            bucket=self.bucketName,
        )

    # endregion

    # region Read Data
    def read_data_frame(
        self,
        measurement: str,
        start: Union[datetime, str],
        stop: Optional[Union[datetime, str]] = None,
        fields: Optional[Union[tuple, list]] = None,
        tags: Optional[Dict[str, str]] = None,
        limit: Optional[int] = None,
    ) -> pd.DataFrame:
        """
        Read single, multiple or all fields from a measurement
        into a pandas DataFrame.
        Fields for which in the given date-time range yields no results are
        automatically dropped by the upstream client.
        :param measurement: Name of a measurement to read from
        :param start: Start date-time to read from.
            Valid strings are specified by the Flux's range() function in
            https://docs.influxdata.com/flux/latest/stdlib/universe/range/
        :param stop: Stop date-time to read.
            If omitted, all data until InfluxDB's internal `now()` is returned.
            In InfluxDB V2, rows/points with timestamps that match this date-time
            are excluded from the results.
            If you want to include the stop timestamp, it is recommended
            to add another nanosecond to it.
        :param fields: Sequence of field names to read from.
            Read all fields, if omitted.
        :param tags: Mapping of tag key and value pairs to filter for
        :param limit: If given, limit the resulting rows to the given number
        :return: Results as pandas data frame (empty if no results were found)
        """
        # From
        from_ = f'from(bucket: "{self.bucketName}")'

        # Range
        start = self._cast_validate_date_time_string(start)
        start_arg = f"start: {start}"
        stop_arg = ""
        if stop is not None:
            stop = self._cast_validate_date_time_string(stop)
            stop_arg = f", stop: {stop}"
        range_ = f"|> range({start_arg}{stop_arg})"

        # Filter
        measurement_filter = (
            f'|> filter(fn: (r) => r._measurement == "{measurement}")'
        )
        tags_filter = ""
        if tags:
            tag_conditionals = [
                f'r.{tag_key} == "{tag_value}"'
                for tag_key, tag_value in tags.items()
            ]
            tags_filter = (
                " |> filter(fn: (r) => " + " and ".join(tag_conditionals) + ")"
            )
        field_filter = ""
        if fields:
            field_conditionals = [f'r._field == "{field}"' for field in fields]
            field_filter = (
                " |> filter(fn: (r) => " + " or ".join(field_conditionals) + ")"
            )
        filters = f"{measurement_filter}{tags_filter}{field_filter}"

        # Limit
        limit_ = ""
        if limit is not None:
            limit_ = f" |> limit(n: {limit})"

        # Merge all tables into a single table ("ungroup")
        group = "|> group()"
        # Create columns from field keys and set time column as row keys
        pivot = (
            '|> pivot(rowKey: ["_time"], columnKey: ["_field"], valueColumn:'
            ' "_value")'
        )

        query = f"{from_} {range_} {filters}{limit_} {group} {pivot}"
        data_frame = self.queryAPI.query_data_frame(
            query, data_frame_index=["_time"]
        )
        data_frame.drop(
            columns=["result", "table", "_start", "_stop"],
            inplace=True,
            errors="ignore",
        )
        data_frame.index.name = None

        return data_frame

    def read_first_point(
        self,
        measurement: str,
        field: str,
        start: Union[datetime, str],
        stop: Optional[Union[datetime, str]] = None,
    ) -> pd.Series:
        """
        Get the first available point (at the earliest timestamp) from given field
        :param measurement: Name of the measurement to read from
        :param field: Name of the field to read
        :param start: Start date-time to read from.
            Valid strings are specified by the Flux's range() function in
            https://docs.influxdata.com/flux/latest/stdlib/universe/range/
        :param stop: Stop date-time to read.
            Valid strings are specified by the Flux's range() function in
            https://docs.influxdata.com/flux/latest/stdlib/universe/range/
            If omitted, the first point between start and InfluxDB's internal
            `now()` is returned.
            In InfluxDB V2, rows/points with timestamps that match this date-time
            are excluded from the results.
            If you want to include the stop timestamp, it is recommended
            to add another nanosecond to it.
        :return: First point of the specified field
            or an empty series, if none was found
        """
        return self._read_first_or_last_point(
            first_or_last=FirstLast.first,
            measurement=measurement,
            field=field,
            start=start,
            stop=stop,
        )

    def read_last_point(
        self,
        measurement: str,
        field: str,
        start: Union[datetime, str],
        stop: Optional[Union[datetime, str]] = None,
    ) -> pd.Series:
        """
        Get the last available point (at the latest timestamp) from given field
        :param measurement: Name of the measurement to read from
        :param field: Name of the field to read
        :param start: Start date-time to read from.
            Valid strings are specified by the Flux's range() function in
            https://docs.influxdata.com/flux/latest/stdlib/universe/range/
        :param stop: Stop date-time to read.
            If omitted, the last point between start and InfluxDB's internal
            `now()` is returned.
            In InfluxDB V2, rows/points with timestamps that match this date-time
            are excluded from the results.
            If you want to include the stop timestamp, it is recommended
            to add another nanosecond to it.
        :return: Last point of the specified field
            or an empty series, if none was found
        """
        return self._read_first_or_last_point(
            first_or_last=FirstLast.last,
            measurement=measurement,
            field=field,
            start=start,
            stop=stop,
        )

    def _read_first_or_last_point(
        self,
        first_or_last: FirstLast,
        measurement: str,
        field: str,
        start: Union[datetime, str],
        stop: Optional[Union[datetime, str]] = None,
    ) -> pd.Series:
        """
        Get the first (at the earliest timestamp) or last (latest timestamp)
        available point from given field
        :param first_or_last: Enum member choice whether to query the first or last point
        :param measurement: Name of the measurement to read from
        :param field: Name of the field to read
        :param start: Start date-time to read from.
            Valid strings are specified by the Flux's range() function in
            https://docs.influxdata.com/flux/latest/stdlib/universe/range/
        :param stop: Stop date-time to read.
            If omitted, the last point between start and InfluxDB's internal
            `now()` is returned.
            In InfluxDB V2, rows/points with timestamps that match this date-time
            are excluded from the results.
            If you want to include the stop timestamp, it is recommended
            to add another nanosecond to it.
        :return: First or last point of the specified field
            or an empty series, if none was found
        """

        from_ = f'from(bucket: "{self.bucketName}")'

        # Range
        start = self._cast_validate_date_time_string(start)
        start_arg = f"start: {start}"
        stop_arg = ""
        if stop is not None:
            stop = self._cast_validate_date_time_string(stop)
            stop_arg = f", stop: {stop}"
        range_ = f"|> range({start_arg}{stop_arg})"

        # Filter
        measurement_filter = (
            f'|> filter(fn: (r) => r._measurement == "{measurement}")'
        )
        field_filter = f'|> filter(fn: (r) => r._field == "{field}")'
        filters = f"{measurement_filter} {field_filter}"

        # Last
        first_or_last_func = f"|> {first_or_last.value}()"

        # Merge all tables into a single table ("ungroup")
        group = "|> group()"
        # Create columns from field keys and set time column as row keys
        pivot = (
            '|> pivot(rowKey: ["_time"], columnKey: ["_field"], valueColumn:'
            ' "_value")'
        )

        query = (
            f"{from_} {range_} {filters} {first_or_last_func} {group} {pivot}"
        )
        data_frame: pd.DataFrame = self.queryAPI.query_data_frame(
            query, data_frame_index=["_time"]
        )
        if data_frame.empty:
            return pd.Series(dtype=object)
        else:
            series = data_frame[field]
            return series

    # endregion

    # region Write Data
    def write_data_frame(
        self,
        data_frame: pd.DataFrame,
        measurement: str,
        tags: Optional[dict] = None,
        write_mode: WriteMode = WriteMode.synchronous.value,
        batch_size: int = INFLUX_DEFAULT_BATCH_SIZE,
    ) -> pd.DataFrame:
        """
        Write single or multiple series from a data frame into a measurement
        :param data_frame: DataFrame with timeseries date
        :param measurement: Measurement to write series into
        :param tags: Tags to add to series data {[tag key]: [tag value]})
        :param write_mode: The mode in which the client will write the given data
        :param batch_size: The number of data points to collect in a batch,
            when using the BATCHING write mode.
            Will be ignored if write_mode is is not BATCHING.
        :return: The data frame passed to the upstream client's write API
        """
        tag_columns = None
        if tags is not None:
            for tag_key, tag_value in tags.items():
                data_frame[tag_key] = tag_value
            tag_columns = list(tags.keys())
        write_options = WriteOptions(
            write_type=write_mode, batch_size=batch_size
        )
        with self.write_api(write_options=write_options) as write_api:
            # noinspection PyTypeChecker
            write_api.write(
                bucket=self.bucketName,
                record=data_frame,
                data_frame_measurement_name=measurement,
                data_frame_tag_columns=tag_columns,
            )
        return data_frame

    # endregion
