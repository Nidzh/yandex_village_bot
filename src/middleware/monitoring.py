from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator


def setup_monitoring_and_healthcheck(app: FastAPI, include_in_schema: bool = False):
    """
    Настраивает инструментарий Prometheus для сбора метрик из приложения FastAPI.
    Настраивает путь /healthcheck для Consul.
    """

    @app.get("/healthcheck", include_in_schema=include_in_schema)
    async def healthcheck():
        return {"message": "Health!"}

    Instrumentator().instrument(app).expose(app, include_in_schema=include_in_schema)
