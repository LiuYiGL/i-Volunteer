from typing import Optional

from login.User import User
from PlatformFunctions.deleteActivity import deleteActivity


def loginMenu() -> Optional[User]:
    print("========== 欢迎来到网安志愿站专属管理后台 ==========")
    print("| 目前的功能:                                   |")
    print("|     1.删除任意活动                            |")
    print('================================================')
    print()
    username = input("请输入管理员登录账号：")
    password = input("请输入管理员登录密码：", )

    user = User(username, password)
    print("正在登录，自动通过验证码中...")
    user.login()
    if user.hasLoginStatus():
        print("登录成功！")
        return user
    else:
        print("登录失败，请重新登录")
        return None


def deleteActivityMenu(user: User):
    print("=" * 20)
    missionId = input("请输入活动编号：")
    if deleteActivity(user, missionId):
        print("本活动撤销成功！")
    else:
        print("本活动撤销失败！")
    print("=" * 20)


def functionMenu(user: User):
    print("========== 欢迎来到网安志愿站专属管理后台 ==========")
    print("| 目前的功能:                                   |")
    print("|     1.删除任意活动                            |")
    print("|                                              |")
    print("|     0.退出后台                                |")
    print("|             《待后续干事研发》                 |")
    print('================================================')

    while True:
        choose = input("请选择功能：")
        if choose == "1":
            deleteActivityMenu(user)
        elif choose == "0":
            break
        else:
            print("输入有误！")


if __name__ == '__main__':

    admin: User

    # 登录页面：
    while True:
        admin = loginMenu()
        if admin is not None:
            break

    # 进入功能页面
    functionMenu(admin)

    # 退出登录
    admin.logout()
