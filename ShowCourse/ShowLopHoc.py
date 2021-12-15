import json
import time
from os import name, times
from bs4.element import Tag
import requests
from bs4 import BeautifulSoup
import Data_ShowLop


Data_Login ={
    "_EVENTTARGET":"",
    "__EVENTARGUMENT:":"",
    "__LASTFOCUS:":"",
    "__VIEWSTATE":"",
    "__VIEWSTATEGENERATOR":"",
    "PageHeader1$drpNgonNgu":"E43296C6F24C4410A894F46D57D2D3AB",
    "PageHeader1$hidisNotify":"0",
    "PageHeader1$hidValueNotify":".",   
    "txtUserName":"AT160104",
    "txtPassword":"c30da15801bffa50160bc1743df35dca",#Buộc phải mã hóa 
    "btnSubmit":"",
    "hidUserId":"",
    "hidUserFullName":"",
    "hidTrainingSystemId":"",
}
urls = "http://qldt.actvn.edu.vn/CMCSoft.IU.Web.Info/Login.aspx"
fName = "ShowCourse\ShowLopHoc"
headers = {
    'Accept-Encoding': 'gzip, deflate', 
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43',
    }
ffheader = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'en-US,en;q=0.9',
'Connection': 'keep-alive',
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'qldt.actvn.edu.vn',
'Origin': 'http://qldt.actvn.edu.vn',
'Referer': 'http://qldt.actvn.edu.vn/CMCSoft.IU.Web.Info/Login.aspx',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 Edg/96.0.1054.53'
}
with requests.Session() as s:
    print(s.cookies.get_dict())
    #s.headers=ffheader
    response = s.post(urls,data = Data_Login)
    print(f'Login: {response.history}')
    with open('ShowCourse\Login.html', 'wb') as fd:
        fd.write(response.text.encode())
    with open('ShowCourse\Login.html', 'r',encoding="UTF-8") as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')
        viewstate = soup.find(id="__VIEWSTATE").get("value")
    for i in range(0,8):
        Data = Data_ShowLop.Data_GetCourse.copy()
        Data["__VIEWSTATE"] = viewstate
        Data["drpCourse"] = Data_ShowLop.drpCourse[i] 
        response = s.post(url="http://qldt.actvn.edu.vn/CMCSoft.IU.Web.Info/StudyRegister/StudyRegister.aspx",data=Data)
        print(f'{i}.Code: {response.status_code}')
        print(response.history)
        FileName = fName + f'{i}.html'
        with open(FileName, 'wb') as fd:
            fd.write(response.text.encode())
