import warnings
from datetime import datetime
from typing import Optional, Dict, Union, List

import influxdb.exceptions
import pandas as pd
import requests

from . import errors
from .const import (
    INFLUX_DEFAULT_BATCH_SIZE,
)
from ._base import BaseClient, WriteMode, FirstLast


class InfluxDBV1Client(influxdb.DataFrameClient, BaseClient):
    """
    A client for InfluxDB V1.
    Wrapper for the upstream InfluxDB V1 client.
    """

    def __init__(
        self, host: str, port: int, username: str, password: str, database: str
    ):
        """
        :param host: Hostname to connect to InfluxDB, defaults to 'localhost'
        :param port: Port to connect to InfluxDB, defaults to 8086
        :param username: User to connect, defaults to 'root'
        :param password: Password of the user, defaults to 'root'
        :param database: Name of the database to connect to
        """
        super().__init__(
            host=host,
            port=port,
            username=username,
            password=password,
            database=database,
        )
        self.database = database

    # region Meta
    @property
    def client_major(self) -> int:
        """
        The InfluxDB major version the client is primarily made for
        """
        return 1

    # endregion

    # region Schema & Management
    def get_databases(self) -> List[str]:
        """
        List of all databases
        """
        databases = self.get_list_database()
        return [db_dict["name"] for db_dict in databases]

    def get_measurements(
        self,
    ) -> List[str]:
        """
        List of all available measurements in the currently associated database
        :return: List of measurements
        """
        measurements = self.get_list_measurements()
        return [measurement["name"] for measurement in measurements]

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
        query = f'SHOW FIELD KEYS ON "{self.database}"'
        if measurement is not None:
            self._warn_measurement_does_not_exist(measurement)
            query += f' FROM "{measurement}"'
        result = self.query(query=query)
        fields = [f["fieldKey"] for f in result.get_points()]
        return fields

    def get_tag_keys(
        self,
        measurement: Optional[str] = None,
    ) -> List[str]:
        """
        List all available tag keys in a given measurement
        or in all measurements of the entire database.
        :param measurement: Name of the measurement.
            If given, only fields for this particular measurement are returned.
            If not given, fields of all measurements from database are returned.
        :return: List of tag keys
        """
        if measurement is None:
            query = f"SHOW TAG KEYS"
        else:
            self._warn_measurement_does_not_exist(measurement)
            query = f'SHOW TAG KEYS FROM "{measurement}"'

        results = self.query(query=query)[measurement]

        return [tk["tagKey"] for tk in results]

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
            query = f'SHOW TAG VALUES WITH KEY = "{tag_key}"'

        else:
            self._warn_measurement_does_not_exist(measurement)
            if tag_key not in self.get_tag_keys(measurement=measurement):
                msg = (
                    f'Given tag key "{tag_key}" does not exist'
                    f' in measurement "{measurement}".'
                )
                warnings.warn(msg)

            query = (
                f'SHOW TAG VALUES FROM "{measurement}" WITH KEY = "{tag_key}"'
            )

        results = self.query(query=query)
        return [r["value"] for m_res in results for r in m_res]

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

        if measurement is None and (tags is None or len(tags) == 0):
            err_msg = (
                "Deleting by specifying neither measurement nor tags"
                " is not allowed through delete() as it would wipe the"
                " entire bucket."
                " You can drop (and recreate) the bucket instead."
            )
            raise errors.DeleteError(err_msg)

        from_clause = ""
        if measurement is not None:
            if measurement not in self.get_measurements():
                err_msg += f" Given measurement {measurement} does not exist."
                raise errors.SchemaError()
            from_clause = f'FROM "{measurement}"'

        where_clause = ""
        if tags is not None and len(tags) != 0:
            tag_chain = " AND ".join(
                f"\"{tag_key}\" = '{tag_value}'"
                for tag_key, tag_value in tags.items()
            )
            where_clause = f" WHERE {tag_chain}"

        predicate = f"{from_clause}{where_clause}"

        # Raise a warning when the predicate does not match any data
        if measurement is not None:
            select_query = f"SELECT * {predicate}"
            series = self.query(query=select_query)
            if not series:
                msg = f'No data deleted. Predicate was "{predicate}".'
                warnings.warn(msg)

        delete_query = f"DELETE {predicate}"
        self.query(query=delete_query, method="POST")

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
        into a pandas data frame.
        Fields for which in the given date-time range yields no results are
        automatically dropped by the upstream client.
        :param measurement: Name of a measurement to read from
        :param start: Start date-time to read from.
            Valid strings are specified here
            https://docs.influxdata.com/influxdb/v1/query_language/explore-data/#time-syntax
        :param stop: Stop date-time to read.
            Valid strings are specified here
            https://docs.influxdata.com/influxdb/v1/query_language/explore-data/#time-syntax
            If omitted, all data until InfluxDB's internal `now()` is returned.
        :param fields: Sequence of field names to read from.
            Read all fields, if omitted.
        :param tags: Mapping of tag key and value pairs to filter for
        :param limit: If given, limit the resulting rows to the given number
        :return: Results as pandas data frame (empty if no results were found)
        """
        # Fields
        fields_filter = "*::field"
        if fields:
            fields_filter = ", ".join(f'"{field_key}"' for field_key in fields)
        select_from_query = f'SELECT {fields_filter} FROM "{measurement}"'

        # Tags
        tags_filter = ""
        if tags:
            # Select given tags
            tag_conditionals = " AND ".join(
                f"\"{tag_key}\" = '{tag_value}'"
                for tag_key, tag_value in tags.items()
            )
            tags_filter += tag_conditionals

        # Range
        time_filter = ""
        start = self._cast_validate_date_time_string(start)
        if stop is not None:
            stop = self._cast_validate_date_time_string(stop)
        time_filter += f"time >= '{start}'"
        if stop:
            time_filter += f" AND time <= '{stop}'"

        # Concat WHERE query
        if tags_filter:
            where_query = f' WHERE {" AND ".join([tags_filter, time_filter])}'
        else:
            where_query = f" WHERE {time_filter}"

        # Limit
        limit_query = ""
        if limit:
            limit_query = " LIMIT {}".format(limit)

        query = select_from_query + where_query + limit_query

        err_msg = (
            f"Could not read series '{fields}' from measurement"
            f" '{measurement}'. "
        )
        try:
            results = self.query(query=query)
        except influxdb.exceptions.InfluxDBClientError as e:
            err_msg += "(" + str(e) + ")"
            raise errors.ReadError(err_msg) from e

        self._warn_measurement_does_not_exist(measurement)
        try:
            return results[measurement]
        except KeyError:
            return pd.DataFrame()

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
            Valid strings are specified here
            https://docs.influxdata.com/influxdb/v1/query_language/explore-data/#time-syntax
        :param stop: Stop date-time to read.
            Valid strings are specified here
            https://docs.influxdata.com/influxdb/v1/query_language/explore-data/#time-syntax
            If omitted, the first point between start and InfluxDB's internal
            `now()` is returned.
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
        Get the last available point (latest timestamp) from given field
        :param measurement: Name of the measurement to read from
        :param field: Name of the field to read
        :param start: Start date-time to read from.
            Valid strings are specified here
            https://docs.influxdata.com/influxdb/v1/query_language/explore-data/#time-syntax
        :param stop: Stop date-time to read.
            Valid strings are specified here
            https://docs.influxdata.com/influxdb/v1/query_language/explore-data/#time-syntax
            If omitted, the last point between start and InfluxDB's internal
            `now()` is returned.
        :return: First point of the specified field
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
            Valid strings are specified here
            https://docs.influxdata.com/influxdb/v1/query_language/explore-data/#time-syntax
        :param stop: Stop date-time to read.
            If omitted, the first point between start and InfluxDB's internal
            `now()` is returned.
        :return: First point of the specified field
            or an empty series, if none was found
        """
        select_query = (
            f'SELECT {first_or_last.value.upper()}({field}) FROM "{measurement}"'
        )

        # Range
        where_query = " WHERE"
        start = self._cast_validate_date_time_string(start)
        if stop is not None:
            stop = self._cast_validate_date_time_string(stop)
        where_query += f" time >= '{start}'"
        if stop:
            where_query += f" AND time <= '{stop}'"

        query = select_query + where_query
        try:
            result = self.query(query=query, dropna=False)[measurement][
                first_or_last.value.lower()
            ]
        except KeyError:
            result = pd.Series()

        return result

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
        if write_mode != WriteMode.batching.value:
            batch_size = None
        try:
            self.write_points(
                dataframe=data_frame,
                measurement=measurement,
                tags=tags,
                batch_size=batch_size,
            )
        except requests.exceptions.ConnectionError as e:
            raise errors.WriteError(
                "Received a connection error from InfluxDB. "
                "Maybe you are writing too many points?"
            ) from e
        return data_frame

    # endregion
