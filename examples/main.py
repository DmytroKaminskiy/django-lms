from fastapi import FastAPI, Request
from fastapi.exceptions import HTTPException
import os
import databases
import sqlalchemy

from models import zoom_events

from schemas import ZoomEventCreate

app = FastAPI()

POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']
POSTGRES_USER = os.environ['POSTGRES_USER']
POSTGRES_DB = os.environ['POSTGRES_DB']
POSTGRES_HOST = os.environ['POSTGRES_HOST']
POSTGRES_PORT = os.environ['POSTGRES_PORT']


DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

database = databases.Database(DATABASE_URL)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.post("/")
async def root(zoom_event: ZoomEventCreate, request: Request):
    authorization = os.environ['ZOOM_AUTHORIZATION_TOKEN']  # TODO move to env vars

    if request.headers['authorization'] != authorization:
        raise HTTPException(status_code=400, detail="Invalid Authorization Token")

    query = zoom_events.insert().values(
        event=zoom_event.event,
        event_ts=zoom_event.event_ts,
        payload=zoom_event.payload,
    )
    await database.execute(query)

    return {}


'''
sawatzke45274@fakemail.io
awdbajwd#^w3ttdfw7e6^&^#WFVvsegeg
http

https

sqlalchemy
1. ORM - sync
2. Core - sync, async

'''

{
    'event': 'meeting.ended',
    'payload': {
        'account_id': 'Mim5io4NSTaKCZiQU1erqg',
        'object': {
            'duration': 327685,
            'start_time': '2022-05-29T14:39:03Z',
            'timezone': '',
            'end_time': '2022-05-29T14:39:08Z',
            'topic': "Dmytro NotKaminksyi's Zoom Meeting",
            'id': '97309149249',
            'type': 1,
            'uuid': 'cLUSeRFjRcKSccqmNxD4uA==',
            'host_id': 'Zjc5evnCSV6JzM1eOCKiQw',
        },
    },
    'event_ts': 1653835148457,
}
