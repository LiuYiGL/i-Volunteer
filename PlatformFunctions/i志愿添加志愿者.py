import json
import requests

session = requests.session()

url = 'https://www.gdzyz.cn/api/mission/manage/inviteUserList.do'

# 用Cookie实现管理员身份认证
headers = {

}

missionId = input("请输入活动编号：")

data = {
    'missionId': missionId,
    'zzName': '',
    'districtId': '',
    'subDistrict': 'true',
    'userName': '',
    'idcardCode': '',
    'mobile': '',
    'gender': '',
    'pageIndex': '1',
    'pageSize': '10',
}

# 志愿者列表
volunteer_list = [
    {'name': '姓名', 'idcardCode': '身份证号'},
    {'name': '姓名', 'idcardCode': '身份证号'},
    {'name': '姓名', 'idcardCode': '身份证号'}
]

# 获取userId 列表
userId_list = []

# 要先通过身份证号获取i志愿后台的userId
for i, volunteer in enumerate(volunteer_list):
    print(volunteer['name'])
    data['idcardCode'] = volunteer['idcardCode']
    response = session.post(url=url, data=data, headers=headers)
    content = json.loads(response.text)
    info_list = content.get('records')
    volunteer_list[i]['userId'] = info_list[0].get('userId')

    print('第' + (i + 1).__str__() + '个志愿者的基本信息如下')
    print(volunteer)
    flag = input('是否添加？（回车键确认）')
    if flag == '':
        volunteer_list[i]['ackAdd'] = 'True'
    else:
        exit()

print(volunteer_list)

# 添加志愿者
url = 'https://www.gdzyz.cn/api/mission/manage/enlistUser4His.do'
data = {
    'missionId': missionId,
    'userId': '',
}

for i, volunteer in enumerate(volunteer_list):
    data['userId'] = volunteer.get('userId')
    # print(volunteer)
    if volunteer_list[i]['ackAdd']:
        print('正在添加' + volunteer_list[i]['name'])
    response = session.post(url=url, data=data, headers=headers)
    content = response.text
    volunteer_list[i]['msg'] = content

print(volunteer_list)
