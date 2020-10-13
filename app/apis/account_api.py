from fastapi import APIRouter
from app.apis.depends import *

route = APIRouter()


@route.post('/login', name='登录')
async def login(form_data: WeXinLoginForm = Depends()):
    print(form_data.username, form_data.password)
    return {"access_token": "access_token", "token_type": "bearer", 'status': status.HTTP_200_OK, 'msg': 'ok',
            'data': []}


# @route.post('/token', description='供openapi Authorize使用')
# async def get_token(form_data: OAuth2PasswordRequestForm = Depends()):
#     print(form_data.__dict__)
#     return {"access_token": "access_token", "token_type": "bearer", 'status': status.HTTP_200_OK, 'msg': 'ok',
#             'data': []}


@route.get('/test', name='测试')
# async def test(currUser=Depends(get_current_user)):
#     return {"data": "hello world"}
async def test(ok: str = None, id: str = None):
    return {"data": "hello world", "ok": ok, "id": id}