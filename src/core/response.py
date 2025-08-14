from pydantic import BaseModel
from starlette.responses import JSONResponse


class ResponseStructureDetail(BaseModel):
    type: str
    msg: str | None = ""
    loc: list | None = []


class ResponseStructure(BaseModel):
    detail: list[ResponseStructureDetail]


class ErrorResponse(JSONResponse):
    def __init__(
        self,
        content: ResponseStructure,
        status_code: int = 400,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(
            content.model_dump(),
            status_code,
            *args,
            **kwargs,
        )


class OutlineErrorResponse(JSONResponse):
    def __init__(
        self,
        content: ResponseStructure,
        status_code: int = 400,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(
            content.model_dump(),
            status_code,
            *args,
            **kwargs,
        )
