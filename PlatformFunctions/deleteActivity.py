import requests
from login.User import User

url = 'https://www.gdzyz.cn/api/wx/mission/transformState.do'
# url = 'https://www.gdzyz.cn/api/sitemsg/list4admin.do'

data = {
    'missionId': None,
    'state': '1003'
}

headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'www.gdzyz.cn',
    'Origin': 'https://www.gdzyz.cn',
    'Referer': 'https://www.gdzyz.cn/mission/manage/listActive.do?type=1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39',
}


def deleteActivity(admin: User, missionId):
    status = admin.hasLoginStatus()
    if not status:
        return False

    data['missionId'] = missionId

    session = admin.getSession()
    response = session.post(url=url, data=data, headers=headers)
    print(response.text)
    if response.status_code == 404:
        return False
    else:
        return True


if __name__ == "__main__":
    admin = User("", "")
    admin.login()
    # admin.openManager()
    deleteActivity(admin, "6176935")
