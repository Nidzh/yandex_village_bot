from fastapi import FastAPI, Request, status
from loguru import logger
from pydantic import ValidationError

from src.core.exceptions import APPException
from src.core.response import ErrorResponse, ResponseStructure, ResponseStructureDetail


async def validation_exception_handler(request: Request, exc: ValidationError):
    logger.exception(exc)
    detail: list = exc.errors()
    return ErrorResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content=ResponseStructure(detail=detail))


async def custom_exception_handler(request: Request, exc: APPException):
    detail: list = [ResponseStructureDetail(type=exc.type, msg=exc.detail, loc=exc.loc)]
    return ErrorResponse(status_code=exc.status_code, content=ResponseStructure(detail=detail))


async def base_exception_handler(request: Request, exc: Exception):
    logger.exception(exc)
    detail: list = [ResponseStructureDetail(type="server.error", msg="An error occurred")]
    return ErrorResponse(status_code=500, content=ResponseStructure(detail=detail))


def setup_exception_handlers(app: FastAPI):
    app.add_exception_handler(ValidationError, validation_exception_handler)
    app.add_exception_handler(APPException, custom_exception_handler)
    app.add_exception_handler(Exception, base_exception_handler)
