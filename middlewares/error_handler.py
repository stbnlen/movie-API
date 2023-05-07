from fastapi.logger import logger
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import FastAPI, Request, Response, status
from fastapi.responses import JSONResponse
from typing import Union, Callable


class ErrorHandler(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI) -> None:
        super().__init__(app)

    async def dispatch(
        self, request: Request, call_next: Callable
    ) -> Union[Response, JSONResponse]:
        try:
            return await call_next(request)
        except Exception as e:
            logger.exception("An error occurred")
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={"error": str(e)},
            )
