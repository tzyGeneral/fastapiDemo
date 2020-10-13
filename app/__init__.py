from inspect import getmembers
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from tortoise.contrib.fastapi import register_tortoise
from app.dbs.database import DATABASE_URL
from config import Settings
from app.commons.common_util import TypedAPIRouter, CustomException


def conf_init(app: FastAPI):
    print(f'Start app with {Settings.ENVIRONMENT} environment')
    if Settings.ENVIRONMENT == 'production':
        app.docs_url = None
        app.redoc_url = None
        app.debug = False


def db_init(app: FastAPI):
    register_tortoise(
        app,
        db_url=DATABASE_URL,
        modules={"models": ["app.models.model"]},
        generate_schemas=False,
        add_exception_handlers=True,
    )


def exception_init(app: FastAPI):
    @app.exception_handler(CustomException)
    async def unicorn_exception_handler(request: Request, exc: CustomException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"status": exc.status, "msg": exc.msg, "data": []},
        )


def router_init(app: FastAPI):
    from app import apis

    routers = [o[1] for o in getmembers(apis) if isinstance(o[1], TypedAPIRouter)]

    for router in routers:
        app.include_router(**router.dict())


def create_app():
    app = FastAPI(title='Demo', description='接口文档', version='1.0.0')

    # 加载配置
    conf_init(app)

    # 连接数据库
    db_init(app)

    # 初始化路由配置
    router_init(app)

    # 自定义exc
    exception_init(app)

    return app
