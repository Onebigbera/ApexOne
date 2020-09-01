# -*- coding:utf-8 -*
import  requests,json


url = "https://apexone.apexglobe.com/apex-one/api/tracking/search"

data = {'hawbNo': 'LAXTS01677'}


resa = requests.post(url,data=data,verify=False)
print(resa.text)


json_data = json.loads(resa.text)
if json_data:
    detaiL_data = json_data['data']
    print(detaiL_data)
    # 公司详情id
    ata = detaiL_data['ata']
    print(ata)
    print(type(ata))

    # # 资质数量
    # zizhiNum = detaiL_data['comQual']
    # regPersonNum = detaiL_data['regPersonNum']
    # organizationCode = detaiL_data["organizationCode"]
    # # 项目数量
    # projectNum = detaiL_data["performanceFourLib"]
    # # 组织机构代码
    # company_code = detaiL_data["creditCode"]
    # # 备案地
    # company_address = detaiL_data["regionFullname"]-
