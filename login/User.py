import json

import requests
from login.Constant import Constant
import hashlib
from aip import AipOcr


# 获得验证码的rc值
def getURLofRC(session: requests.Session):
    response = session.get(Constant.URL_HOME)
    exit()


def getVerificationCode(session: requests.Session):
    # 获取验证码
    response = session.get(Constant.URL_Verification_Code)
    # 二进制数据
    image = response.content

    # 保存照片仅供参考
    # with open('code.jpg', 'wb') as fp:
    #     fp.write(image)

    client = AipOcr(Constant.APP_ID, Constant.API_KEY, Constant.SECRET_KEY)

    #  调用通用文字识别, 图片参数为本地图片
    results = client.basicGeneral(image)

    try:
        code = results['words_result'][0]['words']
    except:
        code = '验证码匹配失败'

    print("验证码：" + code)
    return code


class User:
    __username: str
    __session: requests.Session = None

    __data = {
        "loginType": '2',
        'userName': '',
        'idcardType': '255',
        'password': ''
    }

    # 检查用户登录状态
    def hasLoginStatus(self, session=None):
        if session is None:
            session = self.__session
            if session is None:
                return False

        # 检查登录状况
        response = session.get(Constant.URL_CHECK_USER_STATUS)
        json_loads = json.loads(response.text)
        if json_loads["code"] == '1':
            return True
        else:
            self.__session = None
            return False

    def login(self):
        if self.__username is None:
            return None

        # 获得一个Http会话
        session = requests.session()

        # 获取验证码（自动验证）
        self.__data['captchaCode'] = getVerificationCode(session)

        # 登录
        session.post(url=Constant.URL_LOGIN, headers=header, data=self.__data)
        if self.hasLoginStatus(session=session):
            self.__session = session
        else:
            session.close()

    def getSession(self) -> requests.Session:
        return self.__session

    def logout(self):
        if self.__session is not None:
            self.__session.close()
            self.__session = None

    def __init__(self, username, password):
        self.__username = username

        # 设置登录信息
        md5 = hashlib.md5()
        md5.update(password.encode('utf-8'))

        self.__data['userName'] = username
        self.__data['password'] = md5.hexdigest()


header = {
    "User-Agent": Constant.USER_AGENT
}

if __name__ == "__main__":
    admin = User('17707759943', 'lol20011014')
    admin.login()
    print(admin.hasLoginStatus())
