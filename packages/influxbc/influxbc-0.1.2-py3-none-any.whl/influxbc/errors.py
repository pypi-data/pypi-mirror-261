class InfluxDBClientError(Exception):
    """
    Base class for exceptions
    """


class SchemaError(InfluxDBClientError):
    """
    Raised when a database's schema (e.g. measurements, tags) is not formed as expected
    """


class ReadError(InfluxDBClientError):
    """
    Raised when reading/querying failed
    """


class PollingError(InfluxDBClientError):
    """
    Raised for exceptions in the polling context
    """


class WriteError(InfluxDBClientError):
    """
    Raised when writing failed
    """


class DeleteError(InfluxDBClientError):
    """
    Raised when deleting failed
    """
