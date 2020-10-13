from .account_api import route as accounts_router
from app.commons.common_util import TypedAPIRouter

accounts_router = TypedAPIRouter(router=accounts_router, prefix='/v1', tags=['登录/校验相关 API'])
