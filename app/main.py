import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.routes import router

logging.basicConfig(level=logging.INFO)


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(title="Golden Raspberry Awards API", lifespan=lifespan)
app.include_router(router)
