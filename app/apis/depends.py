import aiohttp, json
from fastapi import Form, status, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, HTTPAuthorizationCredentials, HTTPBearer
from app.commons.common_util import CustomException

auth_schema = HTTPBearer()


async def auth_check(resp):
    resp = await resp.json()
    if resp['status'] == 200:
        return resp['data']['userid']
    else:
        raise CustomException(msg='token validation error', status=status.HTTP_401_UNAUTHORIZED)


auth_schema = HTTPBearer()


async def get_current_user(token: HTTPAuthorizationCredentials = Depends(auth_schema)):
    '''
    通过统一token校验接口校验
    :param token:
    :return:
    '''
    url1 = 'http://account.techlz.com/main/api/tokenCheck'
    url2 = 'http://account2.techlz.com/main/api/tokenCheck'
    headers = {
        "content-type": "multipart/form-data;boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW"
    }
    token = token.credentials
    print('token', token)
    async with aiohttp.ClientSession() as session:
        async with session.post(url1, data=json.dumps({'token': token}), headers=headers) as resp1:
            # 服务器异常切换容灾服务器再请求一次
            if resp1.status == 200:
                data = await auth_check(resp1)
            else:
                async with session.post(url2) as resp2:
                    if resp2.status == 200:
                        data = await auth_check(resp2)
                    else:
                        raise CustomException(msg='token validation error', status=status.HTTP_401_UNAUTHORIZED)
    return data


class WeXinLoginForm:
    def __init__(self,
                 co: str = Form(..., description='版本号'),
                 pkg: str = Form(..., description='包名'),
                 data: str = Form(..., description='用户信息数据（未加密）'),
                 ):
        self.co = co,
        self.pkg = pkg,
        self.data = data
