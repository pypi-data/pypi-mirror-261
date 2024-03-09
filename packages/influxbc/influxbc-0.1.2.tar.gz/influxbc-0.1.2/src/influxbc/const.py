import pandas as pd

# Default milliseconds to sleep between polls
DEFAULT_POLL_SLEEP_MS = 60_000
# Default time delta for how much older a point can be to be taken by a poll
DEFAULT_POLL_VALIDITY_PERIOD = pd.Timedelta("0s")

# region InfluxDBs internal constants
# InfluxDB's internal Epoch
INFLUX_EPOCH = "1970-01-01T00:00:00Z"
# InfluxDB's internal databases/buckets
INFLUX_V1_INT_DB = "_internal"
INFLUX_V2_INT_DB_MONIT = "_monitoring"
INFLUX_V2_INT_DB_TASKS = "_tasks"
INFLUX_DEFAULT_BATCH_SIZE = 1_000
# endregion
