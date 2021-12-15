from os import listdir

drpField = "CDA73249707546749745F00A021AD54F",  # Tên lớp học phần, k đổi
hidFieldId = "CDA73249707546749745F00A021AD54F",

drpCourse = [
    "43A0DC62DD714AA68CDF76F82B71A849",# >An toàn mạng máy tính (3 TC)</option>                                       
    "7CE633E80D544DA3AAFFDCDC056C86C8",# >Chuyên đề cơ sở (2 TC)</option>                                     
    "1C4A875ACDB34882B5F938C5C42C7054",# >Kiến trúc máy tính và hợp ngữ (3 TC)</option>                                     
    "88C94469E08A48969C37DB937EE8944E",# >Kỹ thuật lập trình (2 TC)</option>                                      
    "1B99DD5A806D4B1C9CA329B167057CF8",# >Linux và phần mềm nguồn mở (2 TC)</option>                                     
    "8B2B3B848B9C4CCF893C4592F9E98983",# >Nguyên lý hệ điều hành (2 TC)</option>                                       
    "03ABAAEC464443BAABF77767C11ABCBA",# >Phân tích, thiết kế hệ thống thông tin (2 TC)</option>                                     
    "7817609F3C75403585C527A2CF3F6F47",# >Tiếng Anh chuyên ngành (ATTT) (4 TC)</option>
]
hidCourseCredit = ["3", "2", "3", "2", "2", "2", "2", "4"]  # số tín chỉ
hidMultiStudyType = ["3", "0", "3", "3", "3", "0", "3", "0"]  # pass da sua
hidRegistratedCredit = ["0", "0", "0", "0", "0", "0", "0", "0"]  # pass da sua
hidClientNumberOfCourse = ["0", "0", "0", "0", "0", "0", "0", "0"]
Data_Regis = {
    "__EVENTTARGET": "",
    "__EVENTARGUMENT": "",
    "__LASTFOCUS": "",
    "__VIEWSTATE": "",
    "__VIEWSTATEGENERATOR": "",
    "PageHeader1$drpNgonNgu": "E43296C6F24C4410A894F46D57D2D3AB",
    "PageHeader1$hidisNotify": "0",
    "PageHeader1$hidValueNotify": ".",
    "hidMode": "0",
    "drpAcademicYear": "1655BDBE09F24B37871FE727275D23A9",
    "drpField": "CDA73249707546749745F00A021AD54F",
    "drpCourse": drpCourse[0],
    "drpCourseMark": drpCourse[0],
    "drpWeekDay": "0",
    "hidFieldId": "CDA73249707546749745F00A021AD54F",
    "hidSemester": "2021_2022_2",
    "hidTerm": "1",
    "hidCourseId": drpCourse[0],
    "hidMultiStudyType": "",#hidMultiStudyType
    "hidMaxPeriod": "",
    "hidCourseTuition": "",
    "hidMaxPeriodMode": "",
    "btnUpdate": "Ðăng ký",
    "hidRegistratedCredit": "",#hidRegistratedCredit[0],
    "hidTotalCredit": "",
    "hidCheckMaxCredit": "0",
    "hidParamShowMode": "",
    "hidMaxCredit": "",
    "hidMaxCredit2": "",
    "hidMinCredit": "0",
    "hidMinCredit2": "",
    "hidMaxCredit3": "",
    "hidStudyRank": "",
    "hidStudyLevel": "",
    "hidStudyRankMode": "0",
    "hidCourseCredit": "",#hidCourseCredit[0],
    "hidUpdateMode": "",
    "hidQHSH": "",
    "hidSecondFieldCredit": "0",
    "hidSecondFieldMaxCredit": "",
    "hidUpgradeMark": "1",
    "hidAccountBalance": "0",
    "hidStudentTypeId": "",
    "hidTotalTuition": "0",
    "hidSocialWelfareExceptId": "",
    "hidTuitionCheck": "2",
    "hidMucNoHocPhiToiDa": "0",
    "hidLackGroupCourseId": "",
    "hidSemesterCheckMode": "0",
    "hidClientNumberOfCourse": "",#hidClientNumberOfCourse[0],
    "hidConditionMarkValue": "",
    "hidConditionMarkCode": "",
    "hidCheckCourseNoTuition": "0",
    "hidSecondFieldMaxCreditMode": "1",
    "hidSecondFieldMaxCreditInclude": "0",
    "hidTinhHocPhiSangTacNghiep": "0",
}
# An toan mang
Data_ATM = Data_Regis.copy()
Data_ATM["ATDVDV12"] = "54"
Data_ATM["gridRegistration$ctl04$chkSelect"] = "on"

Data_ATM["drpCourse"] = drpCourse[0]
Data_ATM["drpCourseMark"] = drpCourse[0]
Data_ATM["hidCourseId"] = drpCourse[0]
Data_ATM["hidCourseCredit"] = hidCourseCredit[0]
Data_ATM["hidMultiStudyType"] = hidMultiStudyType[0]
Data_ATM["hidRegistratedCredit"] = hidRegistratedCredit[0]
Data_ATM["hidClientNumberOfCourse"] = hidClientNumberOfCourse[0]

# >Chuyên đề cơ sở (2 TC)</option>
Data_CDCS = Data_Regis.copy()

Data_CDCS["drpCourse"] = drpCourse[1]
Data_CDCS["drpCourseMark"] = drpCourse[1]
Data_CDCS["hidCourseId"] = drpCourse[1]
Data_CDCS["hidCourseCredit"] = hidCourseCredit[1]
Data_CDCS["hidMultiStudyType"] = hidMultiStudyType[1]
Data_CDCS["hidRegistratedCredit"] = hidRegistratedCredit[1]
Data_CDCS["hidClientNumberOfCourse"] = hidClientNumberOfCourse[1]

# >Kiến trúc máy tính và hợp ngữ (3 TC)</option>
Data_KTMT = Data_Regis.copy()

Data_KTMT["drpCourse"] = drpCourse[2]
Data_KTMT["drpCourseMark"] = drpCourse[2]
Data_KTMT["hidCourseId"] = drpCourse[2]
Data_KTMT["hidCourseCredit"] = hidCourseCredit[2]
Data_KTMT["hidMultiStudyType"] = hidMultiStudyType[2]
Data_KTMT["hidRegistratedCredit"] = hidRegistratedCredit[2]
Data_KTMT["hidClientNumberOfCourse"] = hidClientNumberOfCourse[2]

# >Kỹ thuật lập trình (2 TC)</option>
Data_KTLT = Data_Regis.copy()

Data_KTLT["drpCourse"] = drpCourse[3]
Data_KTLT["drpCourseMark"] = drpCourse[3]
Data_KTLT["hidCourseId"] = drpCourse[3]
Data_KTLT["hidCourseCredit"] = hidCourseCredit[3]
Data_KTLT["hidMultiStudyType"] = hidMultiStudyType[3]
Data_KTLT["hidRegistratedCredit"] = hidRegistratedCredit[3]
Data_KTLT["hidClientNumberOfCourse"] = hidClientNumberOfCourse[3]

# >Linux và phần mềm nguồn mở (2 TC)</option>
Data_LINUX = Data_Regis.copy()

Data_LINUX["drpCourse"] = drpCourse[4]
Data_LINUX["drpCourseMark"] = drpCourse[4]
Data_LINUX["hidCourseId"] = drpCourse[4]
Data_LINUX["hidCourseCredit"] = hidCourseCredit[4]
Data_LINUX["hidMultiStudyType"] = hidMultiStudyType[4]
Data_LINUX["hidRegistratedCredit"] = hidRegistratedCredit[4]
Data_LINUX["hidClientNumberOfCourse"] = hidClientNumberOfCourse[4]

# >Nguyên lý hệ điều hành (2 TC)</option>
Data_HDH = Data_Regis.copy()

Data_HDH["drpCourse"] = drpCourse[5]
Data_HDH["drpCourseMark"] = drpCourse[5]
Data_HDH["hidCourseId"] = drpCourse[5]
Data_HDH["hidCourseCredit"] = hidCourseCredit[5]
Data_HDH["hidMultiStudyType"] = hidMultiStudyType[5]
Data_HDH["hidRegistratedCredit"] = hidRegistratedCredit[5]
Data_HDH["hidClientNumberOfCourse"] = hidClientNumberOfCourse[5]

# >Phân tích, thiết kế hệ thống thông tin (2 TC)</op
Data_HTTT = Data_Regis.copy()

Data_HTTT["drpCourse"] = drpCourse[6]
Data_HTTT["drpCourseMark"] = drpCourse[6]
Data_HTTT["hidCourseId"] = drpCourse[6]
Data_HTTT["hidCourseCredit"] = hidCourseCredit[6]
Data_HTTT["hidMultiStudyType"] = hidMultiStudyType[6]
Data_HTTT["hidRegistratedCredit"] = hidRegistratedCredit[6]
Data_HTTT["hidClientNumberOfCourse"] = hidClientNumberOfCourse[6]

# >Tiếng Anh chuyên ngành (ATTT) (4 TC)</option>
Data_ENG4 = Data_Regis.copy()

Data_ENG4["drpCourse"] = drpCourse[7]
Data_ENG4["drpCourseMark"] = drpCourse[7]
Data_ENG4["hidCourseId"] = drpCourse[7]
Data_ENG4["hidCourseCredit"] = hidCourseCredit[7]
Data_ENG4["hidMultiStudyType"] = hidMultiStudyType[7]
Data_ENG4["hidRegistratedCredit"] = hidRegistratedCredit[7]
Data_ENG4["hidClientNumberOfCourse"] = hidClientNumberOfCourse[7]
