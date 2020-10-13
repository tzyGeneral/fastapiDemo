import typing
from pydantic import BaseModel
from fastapi import APIRouter
from starlette.status import HTTP_200_OK
from fastapi.params import Depends
from fastapi.responses import Response


class TypedAPIRouter(BaseModel):
    """ Typed APIRouter. Needed for initalizer """

    router: APIRouter
    prefix: str = str()
    tags: typing.List[str] = []
    dependencies: typing.List[Depends] = []
    responses: typing.Dict[
        typing.Union[int, str], typing.Dict[str, typing.Any]
    ] = dict()
    default_response_class: typing.Optional[typing.Type[Response]] = None

    class Config:
        arbitrary_types_allowed = True


class CustomException(Exception):
    # 自定义exc
    def __init__(self, status: int, msg: str, status_code: int = HTTP_200_OK):
        self.status = status
        self.msg = msg
        self.status_code = status_code
