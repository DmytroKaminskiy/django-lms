import sqlalchemy

metadata = sqlalchemy.MetaData()

zoom_events = sqlalchemy.Table(
    "zoom_events",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("event", sqlalchemy.String),
    sqlalchemy.Column("event_ts", sqlalchemy.BigInteger),
    sqlalchemy.Column("payload", sqlalchemy.JSON),
)