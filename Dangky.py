import os
from bs4.element import Tag

import requests
from bs4 import BeautifulSoup
import DataRegis
user = ["AT160104","asd","asdd"]
Data_Login ={
    "_EVENTTARGET":"",
    "__EVENTARGUMENT:":"",
    "__LASTFOCUS:":"",
    "__VIEWSTATE":"",
    "__VIEWSTATEGENERATOR":"",
    "PageHeader1$drpNgonNgu":"E43296C6F24C4410A894F46D57D2D3AB",
    "PageHeader1$hidisNotify":"0",
    "PageHeader1$hidValueNotify":".",   
    "txtUserName":user[0],
    "txtPassword":"c30da15801bffa50160bc1743df35dca",#Buộc phải mã hóa 
    "btnSubmit":"",
    "hidUserId":"",
    "hidUserFullName":"",
    "hidTrainingSystemId":"",
}
url = "http://qldt.actvn.edu.vn/CMCSoft.IU.Web.Info/Login.aspx"
# response = requests.get(url)
with requests.Session() as s:
    response = s.post(url,data = Data_Login)
    print(f'Login: {response.status_code}')
    with open('Login.html', 'wb') as fd:
        fd.write(response.text.encode())
    response = s.post(url="http://qldt.actvn.edu.vn/CMCSoft.IU.Web.Info/StudyRegister/StudyRegister.aspx",data = DataRegis.Data_ATM)
    print(f'0.ATM: {response.status_code}')
    # response = s.post(url="http://qldt.actvn.edu.vn/CMCSoft.IU.Web.Info/StudyRegister/StudyRegister.aspx",data = DataRegis.Data_CDCS)
    # print(f'1. CDCS: {response.status_code}')
    # response = s.post(url="http://qldt.actvn.edu.vn/CMCSoft.IU.Web.Info/StudyRegister/StudyRegister.aspx",data = DataRegis.Data_KTMT)
    # print(f'2. KTMT: {response.status_code}')
    # response = s.post(url="http://qldt.actvn.edu.vn/CMCSoft.IU.Web.Info/StudyRegister/StudyRegister.aspx",data = DataRegis.Data_KTLT)
    # print(f'3. KTLT: {response.status_code}')
    # response = s.post(url="http://qldt.actvn.edu.vn/CMCSoft.IU.Web.Info/StudyRegister/StudyRegister.aspx",data = DataRegis.Data_LINUX)
    # print(f'4. LINUX: {response.status_code}')
    # response = s.post(url="http://qldt.actvn.edu.vn/CMCSoft.IU.Web.Info/StudyRegister/StudyRegister.aspx",data = DataRegis.Data_HDH)
    # print(f'5. HDH: {response.status_code}')
    # response = s.post(url="http://qldt.actvn.edu.vn/CMCSoft.IU.Web.Info/StudyRegister/StudyRegister.aspx",data = DataRegis.Data_HTTT)
    # print(f'6. HTTT: {response.status_code}')
    # response = s.post(url="http://qldt.actvn.edu.vn/CMCSoft.IU.Web.Info/StudyRegister/StudyRegister.aspx",data = DataRegis.Data_ENG4)
    # print(f'7. ENG4: {response.status_code}')
    with open('Dangky.html', 'wb') as fd:
            fd.write(response.text.encode())
    

    # gets = s.get("http://qldt.actvn.edu.vn/CMCSoft.IU.Web.info/StudyRegister/StudyRegister.aspx")
    # with open('Dangky.html', 'wb') as fd:
    #        fd.write(gets.text.encode())
    # print(f'Login: {response.status_code}')

#  ***************************************code lấy dữ liệu*********************************************
# with open('HienThiLop.html', 'r',encoding="UTF-8") as f:
#     #contents = f.read()
#     soup = BeautifulSoup(f, 'lxml')
#     with open('AntoanmangParse.html', 'wb') as fp:
#         for hidden in soup.find_all(attrs={"type":"hidden"}):
#             #fp.write(hidden.encode())
#             zName = hidden.get("name")
#             zValue = hidden.get("value")
#             if (zName == "__VIEWSTATE" or zName=="__VIEWSTATEGENERATOR"):
#                 zValue = ""
#             fp.write(f'"{zName}":"{zValue}",'.encode())
#             fp.write("\n".encode())
#             #print(hidden)



