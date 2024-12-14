from typing import Any, Optional
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field


class ResponseModel(BaseModel):
    """Base model for standardized API responses.

    Attributes:
        message: message describing the response. Default is "OK"
        data: data given for response
        code: HTTP Status code. Default : 200
    """

    message: str = "OK"
    data: Optional[Any] = None
    code: int = 200

    def result(self) -> JSONResponse:
        return JSONResponse(
            status_code=self.code, content={"message": self.message, "data": self.data}
        )


class SuccessResponse(ResponseModel):
    """Inherits the ResponseModel. Default status code is 200.

    Attributes:
        code: HTTP Status code, because this is a success response class, default is 200. Use valid success code (200-399)
    """

    code: int = Field(ge=200, lt=400, default=200)


class ErrorResponse(ResponseModel):
    """Inherits the ResponseModel. Default status code is 400.

    Attributes:
        code: HTTP Status code. Default is 400.
    """

    code: int = Field(ge=400, default=400)
