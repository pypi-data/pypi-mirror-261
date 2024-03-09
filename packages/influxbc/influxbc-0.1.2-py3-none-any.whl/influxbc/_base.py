import time
import warnings
from abc import ABCMeta, abstractmethod
from datetime import datetime, timedelta
import dateutil.parser
from enum import Enum
from typing import Optional, Union, Dict, List

import pandas as pd
from influxdb_client.client.write_api import WriteType

from . import errors
from .const import (
    DEFAULT_POLL_SLEEP_MS,
    DEFAULT_POLL_VALIDITY_PERIOD,
    INFLUX_DEFAULT_BATCH_SIZE,
)
from .logging import logger

"""
The mode in which the client will write to the InfluxDB instance
In SYNCHRONOUS mode the client will attempt to write the given data in a
single request, synchronously to the client's process. This can lead to
response timeouts when the given data is too much to handle for the
InfluxDB instance.
In BATCHING mode the client will attempt to write the given data in a
multiple requests, synchronously to the client's process. The data will
be split to batches of specified size.
The ASYNCHRONOUS mode is not supported as it is deprecated by
the upstream official clients.
Instead, you might use the official async clients:
* V1: (does not offer async functionality)
* V2:  https://influxdb-client.readthedocs.io/en/stable/usage.html#how-to-use-asyncio
"""
WriteMode = WriteType


class FirstLast(Enum):
    """
    Choice enumeration for querying first or last points from the InfluxDB
    """

    first: str = "first"
    last: str = "last"


class BaseClient(metaclass=ABCMeta):
    # region Meta
    @property
    @abstractmethod
    def client_major(self) -> int:
        """
        The InfluxDB major version the client is primarily made for
        """
        raise NotImplemented

    # endregion

    # region Schema & Management
    @abstractmethod
    def get_databases(self) -> List[str]:
        """
        List of all available databases
        """
        raise NotImplemented

    @abstractmethod
    def get_measurements(
        self,
    ) -> List[str]:
        """
        List of all available measurements in the currently associated database
        :return: List of measurements
        """
        raise NotImplemented

    def _warn_measurement_does_not_exist(self, measurement: str):
        if measurement not in self.get_measurements():
            msg = f"Given measurement {measurement} does not exist."
            warnings.warn(msg)

    @abstractmethod
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
        raise NotImplemented

    @abstractmethod
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
        raise NotImplemented

    @abstractmethod
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
        raise NotImplemented

    @abstractmethod
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
        raise NotImplemented

    # endregion

    # region Read Data
    @classmethod
    def _cast_validate_date_time(
        cls, date_time: Union[datetime, str]
    ) -> datetime:
        """
        Cast a date-time given as either string or datetime representation to
        a date-time format valid in InfluxDB queries
        """
        err_msg = "Invalid date-time."
        try:
            if isinstance(date_time, str):
                date_time_ = dateutil.parser.parse(date_time)
            else:
                date_time_ = date_time
        except dateutil.parser.ParserError:
            err_msg += f" Cannot parse '{date_time}'."
            raise errors.InfluxDBClientError(err_msg)

        if date_time_.tzinfo is None:
            err_msg += f" Given date-time {repr(date_time_)} is timezone-naive."
            raise errors.InfluxDBClientError(err_msg)

        return date_time_

    @classmethod
    def _cast_validate_date_time_string(
        cls, date_time: Union[datetime, str]
    ) -> str:
        """
        Cast a date-time given as either string or datetime representation to
        as string format valid in InfluxDB queries
        """
        date_time_ = cls._cast_validate_date_time(date_time=date_time)
        return date_time_.isoformat()

    @abstractmethod
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
        :param stop: Stop date-time to read.
            If omitted, all data until InfluxDB's internal `now()` is returned.
        :param fields: Sequence of field names to read from.
            Read all fields, if omitted.
        :param tags: Mapping of tag key and value pairs to filter for
        :param limit: If given, limit the resulting rows to the given number
        :return: Results as pandas data frame (empty if no results were found)
        """
        raise NotImplemented

    @abstractmethod
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
        :param stop: Stop date-time to read.
            If omitted, the first point between start and InfluxDB's internal
            `now()` is returned.
        :return: First point of the specified field
            or an empty series, if none was found
        """
        raise NotImplemented

    @abstractmethod
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
        :param stop: Stop date-time to read.
            If omitted, the last point between start and InfluxDB's internal
            `now()` is returned.
        :return: Last point of the specified field
            or an empty series, if none was found
        """
        raise NotImplemented

    def poll_field(
        self,
        measurement: str,
        field: str,
        start: Union[datetime, str],
        stop: Optional[Union[datetime, str]] = None,
        stop_is_inclusive: bool = False,
        return_first: bool = False,
        validity_period: timedelta = DEFAULT_POLL_VALIDITY_PERIOD,
        sleep_time_ms: int = DEFAULT_POLL_SLEEP_MS,
        timeout: Optional[timedelta] = None,
    ) -> pd.Series:
        """
        Poll for data in a field within the given date-time range
        or for the first found result.
        Considering the validity period, if given, request data from the
        InfluxDB until both a valid start and stop point are available.
        Return the series for this field and the available date-time range.
        :param measurement: Name of the measurement to read from
        :param field: Name of the field to read
        :param start: Start date-time to read from.
        :param stop: Stop date-time to read.
            If omitted, the last point between start and InfluxDB's internal
            `now()` is returned.
            In InfluxDB V2, rows with timestamps that match this date-time
            are excluded.
        :param stop_is_inclusive: If True, try to include the exact
            stop date-time (considering a given validity period)
        :param return_first: If True, return the first available point
            (considering a given validity period)
        :param validity_period: If given, consider available points earlier
            than the given start (and stop) date-time.
            Giving a zero-timedelta has the same effect as giving stop_is_inclusive.
        :param sleep_time_ms: Time to sleep between requests in milliseconds
        :param timeout: If given and no valid points are available until
            timeout, raise a PollingError
        :return: The found data within a valid date-time range
        """
        start = self._cast_validate_date_time(start)
        if stop is not None:
            stop = self._cast_validate_date_time(stop)

        consider_timeout = timeout is not None
        polling_start = datetime.now()

        if stop is None and return_first is False:
            msg = (
                "For polling a field, either specify a stop date-time"
                " or pass return_first as True."
            )
            raise errors.PollingError(msg)

        # Get the first available and valid point
        valid_start = start - validity_period
        while True:
            first_entry = self.read_first_point(
                measurement=measurement,
                field=field,
                start=valid_start,
                stop=stop,
            )
            if not first_entry.empty:
                first_timestamp = first_entry.index.min()
                if valid_start <= first_timestamp <= start:
                    break

            if consider_timeout and (
                datetime.now() >= (polling_start + timeout)
            ):
                msg = (
                    f"Timeout for finding a valid start point for start {start}"
                    f" within a validity period of {validity_period}"
                    f" in measurement '{measurement}' and field '{field}'."
                )
                raise errors.PollingError(msg)
            logger.debug(
                f"No valid start point available. Sleeping {sleep_time_ms} ms..."
            )
            time.sleep(sleep_time_ms / 1000)

        # Get the latest valid start point
        if validity_period and first_timestamp < start:
            first_entry = self.read_last_point(
                measurement=measurement,
                field=field,
                start=first_timestamp,
                stop=start,
            )
            first_timestamp = first_entry.index.max()

        if return_first is True:
            return first_entry

        # Get the latest valid stop point
        last_timestamp = stop
        last_entry = pd.Series(dtype=object)
        if stop is not None:
            while True:
                if stop_is_inclusive or validity_period.total_seconds() == 0:
                    # Try to get the exact stop point
                    last_entry = self.read_first_point(
                        measurement=measurement, field=field, start=stop
                    )
                    if not last_entry.empty:
                        last_timestamp = last_entry.index.min()
                        if last_timestamp == stop:
                            break
                # Try to get a stop point inside the validity period
                if validity_period:
                    valid_stop = stop - validity_period
                    last_entry = self.read_last_point(
                        measurement=measurement,
                        field=field,
                        start=valid_stop,
                        stop=stop,
                    )
                    if not last_entry.empty:
                        last_timestamp = last_entry.index.min()
                        break
                if consider_timeout and (
                    datetime.now() >= (polling_start + timeout)
                ):
                    msg = (
                        f"Timeout for finding a valid stop point for stop {stop}"
                        f" within a validity period of {validity_period}"
                        f" in measurement '{measurement}' and field '{field}'."
                    )
                    raise errors.PollingError(msg)
                logger.debug(
                    "No valid stop point available."
                    f" Sleeping {sleep_time_ms} ms..."
                )
                time.sleep(sleep_time_ms / 1000)

        # Get the entire data
        if first_timestamp != last_timestamp:
            result = self.read_data_frame(
                measurement=measurement,
                start=first_timestamp,
                stop=last_timestamp,
                fields=(field,),
            )[field]
            result.loc[last_timestamp] = last_entry[last_timestamp]
        else:  # The valid data may be a single point
            result = first_entry
        return result

    # endregion

    # region Write Data
    @abstractmethod
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
        raise NotImplemented

    # endregion
