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


# print(Data_CDCS)


Data_GetCourse = {

    "__EVENTTARGET": "",
    "__EVENTARGUMENT": "",
    "__LASTFOCUS": "",
    "__VIEWSTATE": "5KjTJfduzbNoO9N2NXknwHt7yBqnqIUUZyzrhQOhL2zfakZ+Xeasla/cars7jjIFZInyjySEoBCCCyS1dFZTqFadSaSrBIzjT4k800/zmnzqy9f+aw2iieiYh7OxNXfHgv0EQrsEVLkSaxfeghRBybmnuFTQ0tTD+K08xmqlQ1DU2vIciw9FsCtB+S31ZO8aenXfYmA602rSJsHiWetZHn19J9gAybSA7zOrkQyhXo0qpSfT6fIWwef08gTC5XmZJ2QckUISnHf3N7IY7myUp+BX/K6JtWPYXYDPCINXRkbf//RdmKzTsvQumpRjH3Q2uAHb8YzUlwP+GnEpRzQRmXoewqqoo+yX+7G3600Dvm6cO6f5qEIPlCtiZY0xZH86gWE3SL/pGj+nnS1D0JKJK1RB2zJ7rKlGgtnHjy8zLX5C2uSK3guJRBWMbFRid8gQqoAzD2vLy77Z69FzD59MhaLPt0LH/bh6LhN9t5OEFHbzxMGbqWHV2DximjTs+h6076V/8h3IBzzY0ruHuG9vHTNxG4NYwobmUIv2v3A+ckvPdrUwF/pgM8mrwGoyOBKTWJh6OisEViDGJHqxXE4QlpucdGffAd2xgMnIkvtd8qCcI0/ikL4gJI8dn/GkOdUOg9RP3/StCVWhcDbMsCwfntJiXBRU1LY/bpMorRjeol21u6VkcPO7SGoW73msVbzVYULzyZBjpsjI3bDe0PhzXNlV/CeE15OE03TtNHq3Jtta+tveBXcv5RCb1NmiiE6DmxWUAx8qejXCMSae9KfFiaQ2VEHqV0tRixLBlF9hWX+YGsoZDyKVX3gdTR/5B8sTsDpZgwC1sTh6akr12AIiN93Ro4eSmj+r7kPR828JS/UL7/N4UEXXFouH1zyI3ItzSJzDZ97m2W5BaGPnMhSDX88awdAjrIlPE3hN0Yr1HrETGu/lJwtVnDgkkYNSqVBLyXj/vaZ1cNEvbUbKYjomTrX15gjxg6QMjkXMTPqAe9jmb4tonZ2+CP8LWJFuCBG9JiMdglMnpUtfOvJvLX3RkIBctJ6IV5NGwB5c9Nn5g3bwv0HV7gBsIFMBfDvidYQGLWxPul0NOmMasehdFZYZosYFBNE2frmzQYz+ivzj3osKgGTAJMt1vh2/WwYiMCPGE4ja0ayp0Sih5w2NTwPa/7TiLbPQAx7d+q6xbyrAIrPszwhABldGVGyX11A481IF18fhlXko+f991KNTUJR3+6DDmnMpJ57Fp9p2VoaILJzXXGs890xNIhMlIrZESK3PHwzd6Ua6tRN+m8KK+QEQBL+m3hLCo8PboEP07Ii6ZyATzoOGbykLerE/zkcH0Q4tJ7thTXN9kYR2CxkASSH5Yap9E0AW3NucDX3h8Yq+1RQTC9VAf2nG3WUfODxkVwDRuFk1iLMqLr20QkoiGEn+C1D1/GhLb0rdPwQ0/e2ddcvOH4/CxWgqUwNfP3DFOunrjvU+h6FnyY2/hj0sB9EsN45f0lhgnst2J/eX2woQ59qrij/XnJ54wAkIN77HXHv7RNiulLQ32gVoHqed50twkPMIsSBYZcf8SnzQWp63nx7LEfN1PB0bugp3kgZD3bHt1rWw4N2T4Wso811tvV56EHXHh1idazblIe6TrqEWulLNTY+nOWZZJQQDeqnWslMhBLRUNoYjc9tMdCH7LT8b/Oh4VYpRo+DgHOB3DYoRsdsgd1I4pwik8O0SqGm2N6EG6tVtdhwpzY6JwH6mOw+Axl3Pib5N9cnrgonZ+aYc7vyqa6m/MLTU8ZGnK7qRRMRdwJQHCWJs1KgmkMRr5LuCbIEgn56miZyw9aTtdYUATx8tCN7tHv0kWF3xKhZX7Srmsmu0yRT8eCnfe0zyu9GIhpyDQ+ZWSoGkagxnRcJ2V/G0hBvfHVy4NpcZr7BU2LNnlb8JWyGMPa2VHT9h34YXUPQ/HguBPTp6bu2jNE8ZefGdFyAiJJc8vlZWwqzK10Sg34R6bAhxN/zpApwxJqMEiPcmDdxJQCoeyZfnoCgo1q40cPdx9+s55WK0bKyn3CJy0OSnhR9zN5OH7QWfj2m4pnrowJIVM3UkNOXhPZOmzg9kx35o2iqwnf8VpFKv4q9jH9UFv6Qk3gZM5cBc346ewba0z4RKlsnNPMh5x5XRwiG7KyPKVmcSXJJnVUNWhsdyud6uPLkGhsgWPebD/1gEVfomE2yvnjFuWsg2VzZOZRFWsajkS1WzQ85np/1ACY3E05LUtAIHy+PKZkf0X2m0JZnajdx9KYFywPrpIhs8Nf7Vf8M63e/EemZUr6RC0tsonAWpPqkDPJv6VTpMZsQ4Y5BmRykXI0Lo10Yb4kGdtoKgnlhv4onFlvIbWpTSaFXbjTrWz5Nx3MfGS/qLo/CGpJM/9fJ0a9ZuqyB53uUySMmC1FxubkWTmY9FnHVQCr+3ieJ94ySD/nC7ZKfADipOOpFIWOduGSF7Pr+7tlEZUX/0dvrFz5xQVXw3t1W5fXryP71fTfvoWcjdzk3jI0lkdrWXv0OcN4iPUfwEIdwoqpwxzl8Y0UOa5oA0sUKBWw1/1BU1N9kjNdIxIVQa1ACXJXUt3P5nKCuOCnpdBjTBTrr00tP7bmzvaEioJudfA9W2uJwDhIs4oWg5oYPDwNV0bH44Vm2rvk7scVXq18kju+aCWWxUfp7QmfOoNW4hSBpKXgHtSgkS/I48+DFxUXdHGt5yvhsujAAJIr+8EVPRkgxlW63mL1hJm8qlX5wVfavTRSPG8fDmTmhaHML6ST35Ki38MnVXCEQl6usobCv+HAt8NuI5Nm48vlkTrqeLISJtwjad1k7Z6x3BPdandDDUECnqQPgmlkpHWJ9PpSRODaXjuYfCFxpcnNzGFlgRt4Zv+NOiTTwFw0re30RUXt451wBJoPuiKZTsiYbqhipCYaKFLMHOQk+O3ZZLxRucZwuNY83OkhUzGB5I27PWApk2Q3dE0xGZjclTH9jLJyNepuu9Zh2g07d8u7mJvPjdbhgvc7kuzCZHDsZ9weQIMEjd/mxJfSkn4wS1e3juX0ERPW2bhS0BRMF2re1RYy/cXlOnzJBFhnbEq+kqnDd9I+TybWTakjDXb0cWFqzfrPA50RoLNyBgCRI3NFqcgTH+Br5U5yc+XDhbvWhvj/DgAVEfjpyLk7FAbn+NKB63RykiyUI1nm2xnb7gmqHyscQ3JnPtx0FYD373HH2Shpq864LO1kMfIeeJB5KeAKt70moRFXY2/Zy07zzfKbnHZXpCdceuVqK+902jOoraBoN2Rq8u3hIAGcXWIgEg0NIe6DL6FY9NiIEdMQFz/f6/qBxedNxrF/GNUhwJkm4DN/d1qHeVGhruTygdQg/3k8Ee0GUGtjbERb3xci1Um7RBEnu0qr0fm7VtTFmasW8/xSNXn/JZjNZjq+1ILjjgDC5fdSqn5f2W++ZGjrJKbGqqDZkLBVKoFeHD0Ffp4Ec6sBxlkpCALhPzzAM/Hq/uMtPCPuHukCdu00aZcR6d5qnIOEa9JJSQQ1G0Z3e4QYvCf0pf0+/Sqd6m1/WHA6PxOBRGhYRVnZxtRTh6Ki9gH2yaHt8gXEcjrMSfZjwiuKmF3GT8ugBNl+oR5HGYnvZaNm66yOAZDTIYpK0uNe63L19sPreiwQRrgiT728KFkiySxMu9kEsQpNNH6yJEEzvzRAfKDuttfmMyPfUfsV1pMqyYAgHUANocxmU4TanG/Wm+WenoehZ2kYEkYu7sqZL9eKhaW9MfHZihytWdTLBbmIAio+i2fbuA0exDSjx3+joVf9A3LoGRgWY9eawS46MWsO/s1WL7++5b8kG8ErZefETvL+aftAC1JdhxEulyjLCZJQWOvikxUlIbaXJMaBn2R96404fimb/pESxAGVni/vkDeTRxzqds44u72XbKZldLxbsMfFD3GEeZcNiVcZ3l3FQCiFMnfj7K+jQz0dOC1TUIcW1LDagkJbGA9hGfzlJ+od44+g6aE/al+un32D/B+oyeVNnrFSPRXd3VOiMub4tcoSiSYpjkpLkgW3TelNv1rBlztr2pAsr/fnUqA2e8aDEwy4AtMh1JkBg7eJaBztu7MTpuTPXsX7w0PUS3hkQu/Bby++pgQckg5hPZRqitT5nw/EJMYIUQhoymTCNJLnUom+qsT8jrkDyLNH2IXQWHMKjnvDEW6SIAGjPXELjDDIYSQqY/ckNO1rKToT4v16G26knxS/pau4BO5jGqWkq5h4mapfXZ/9Pfky6WJkRbxo0WSwUY8+aI+sOpuAgClz0sgL1bLcyysMdGSzjr7yVaDJqA/1ejP4K4OhgTovH9OsLgpbQNzTA0/79zN4RTDQDK3cRiYmM0r9jVlsPVf1sbtJA1WEcxp5zrmjKRmj7tLbFQudygYUharfNZIDieBBeGXirlx4DHf1XUdr10U0eiU6uNvWtH/+hZ7lg0nKSI2rO/9S31LR7p09jhiMS9q0Y0xE6l/2XZ57d2hPw+eI3Z+UgOPeszsc9GeGBaz/flixyAa9DJ7QHxwJN43tgzR421DPNPUmp35eSKreGUlAxWRID1xqbgztJipicdFpoCrBM2VcU4WKKt6WHIqStUSRmKSr0Phma8dN5YToC5AXGo3ibzu2c+tMv6CJHRrcrWKIjtAHp0NpwFn+o7t1yJrqdxTTG0b+ADXuSqivDPsOv6wA8Sb2lgipgh8vG8T4aNG8kRvLg/3zNCWP42q9VlctWuRzByp8HLoJJdn+Qi/JCHUbTgf3crGRYoS5VXIpJ0UQmqpYgMBEGuwRYKK96Yw4YUXKtzm/jdQbV1HtDvtx1RTD0sllSq5FEYK5JJ/USOls9hZ3GUJNqEHL2o7bPWwKNAWJt0iFwp+kRgIJnitkAXbywkGlfZYwz73T3W7Ah2HybJOk11xNFEMBNE9/boKxoAeZ3rXqrHpmXoq/163GwgcQ1GZVS20V8Pqay/xVYMbvlL72AjZVFKcO7lDspdymJVpUc5JR2buGiIoHKlOMlmFtpqzAwMnNaHK7/2u55CBM8MVIJ/LGkwZPPJNIg753QlkDLT+UJLTUe53L+yIdlNAXzaJ4rALI3UBoO4pDVSo+4iX7ET/luvfCbgChOwi7U60G54oy7QRCrv8FvEFbD2RA9hDYAeILr2CRzfzyCZ9T1ZS+dQl0RTu0vuT0SRjkC2+p/DsPIxXoE00x7n7rghp14TpHXHtb9IcRZrjzEOc45irEqBFmZ3qWcyj2i69yXeZRS1xEdDh3kimlGNZKUjiXssLXBZMKPA0MKK/UCD1pdzZ91m7VnYOgWRBdtpPkA8my22Owg8TkQtaFKm1+K4qw9uknd9fno82nahqI7I7qUc9RMfjvDW4dZ4ehUHVYna3teUtWOUOrxRyf8NKP78phhd1YBC9A8ZVpMFfbjK2ek6Ih1JmH6IiGmfo86pm6UlBHKQhMatVPdcH8m088Hh86gpw2U14R+L+9MjvczK24Kg3vDeiscGwtfVBOmiJx6bSLx1RY7oa77C5c3EkfVAOga3FGcC+apb2YdtIW0aIrlP+rL9oEhW2ZaGObtS3tLf8vNbEG1i8c7CYTnG87moByJFvUYVt4Dtc2II6LuW0NGyry7CEJVh3PueRzpdu21ou07E8MDO73WbCOZspG5tJcZuHBJbSo54ZBK5Pdz6glytPiGbrwK9Qh7KVFqP3kUQYUSKnlEcp6FbiKXnd1qTkv36hK42mJGIBD4CICuTFrZ3dtM2T4efB3xpAmNW8+UX9fbgeN2IKvujowEs20MY3hz+kq5EYVrvVNw4q0oimPCyT/7IneYVhTf5qoALnRtO4beMnBdmfCxdpR49T2SwH1WjDODm7k3fCu6V3JtTLN6Di+AkT1Y48NfAxGApwMeyy4mAjzjCna3SWAS0U89fJErY1iKjHI/Fopv2xc3E58Wmv05/s+u6u9XYRgZCLaRhVx2hDgX6S61RihENBROCNxZAajLuV9LEi6dPXuZnb17XgT65OG2RM6CLzNbGSNJDgvGYN/p+8aX7lqTu+B+G6H3uSwjpJOQTJogomqTWNXE3mVfqOf64bCtDabj7NVatZWuA1y3mOKF50cUfjvURnTSbJ334AE8Cb3TA3fD7T8/VLMpT2KPZ7RFJINuY2JpTmuW5JlKK+qMy9LEI3MbLYenc8rWkSLrn+pPWNwKPlqDO3e3IlpOFAtLX9PO+3seBV2PbZAR8GdN24CMPBmk3h6HwBK9w4pRNcepKdfaYMPypbC3uvrWAvfaHOTRPF6l73LKUjFOcb3/S00VZYIwVvUM+Q446Dxsq2eXARznyR6K+BOIOr8Q7puWI/YCdGQqQeswqB8wmcYJCxLHVdhhxL0wJoiJdPifMJDDlR0zabenxHZzpKyZ6vgeFihyuKN2L4HVytCSMdktNmcICVZATF9CMBMFi1IPlPqPWL+V3/CT/lhDMQ1yxO/b8AEIrKrBpf4S8MBmgzw/43e02gbK7Ne4hyZvkWF5kLAn5p4GpDodM7XGWc3QPPKWrWPUJa6u9PFqG0EfZ7k+c+F47+gPDqv0K2uQRPoyHykGUPFhmmYMBBADZYOYkSV6kr7PfaHGEcd6WXpJuCtR8pIlmF780zueZDXSzeYWpYTLuMD7vr2bqaZG5sXWkhOOO6xXmBJuD3JuAsGnRomQ2eekTjoVyxgGVOrQwiednnvb9CJ0slzlXm0ZnXIqS7QmZ7qICFADD2bmajCIYWRgTtxMjwg1CVlMsxTndsMFbwtI+hX09drwoWvglABwxAoopdxOGbc9XER7vSHM5nSYNhBcGLaIsvh07aLCgIYFlVGQQnPMWaFMHUSlEaWbUIfFNgtiFaZ/WZZkI1HWp0KSpZAe2QpBrl94EP8sW4KEv/70zMtOQ/kzUQZjc0GXk6Syl40evbMX2qapmRp2mYa0bzgsqIeKVW8lnyOLWAFGIPRfS1BOQdHcOPfDPRKdD45p52c2oICRps30Q0GRTiU2UCFAfrjDc15egeMrjP5Qq66d7yhnnov/TjNX8Ob7JobmTJFXVQkf/W3cDadtAQaxXw0urOdBPfbFMQgFYVKp+HvOEmcTrNFlwwucY9VaxcZlYRmlFdQDQfREXScbYtDimzxKnh+VQv1auh/YEqHyWpXzVNlzQFPbN1TeFFL/GEfn7AGnDSd1W0S8HdH5DP8WIJ9UKn2YtxtgsPzO5Xj9Umgjk0iXDc/Y4jxh5dRHUARw0OqbAEwLdzBuUPX5qmQnrwCfV7sNDNdCz9BI6NZDB+oZrmZ+P8LXzqgfQvZAje0ZJaDYW/LrfHYEnTvV9/eZeulaPnNpCkjZA1KVFeuw61ZX166aHrKJ+R/2cMcl++vCBTQj36shmV7kiMPZxg5NFn6L5GVyzqLo84LJ0lga5r5m/50bUhzDrUXDhZolXg7GfuDbo5xe/bYdZFtBl27kBi/Mp6OrWW0sEApIFuW7xo4tw32Xa+PnW/K/TNtDuzZ2V+hILP1PBArBUKs9fuhKqzjNo8SYwGhT0qAullz4427v9vANjKWEeGDb+YTB0gHB0B1wnp3aKp7qYcHH7WrVSd1DHFlLz5mPgYf+hoA==",
    "__VIEWSTATEGENERATOR": "EA1EB2D4",
    "PageHeader1$drpNgonNgu": "E43296C6F24C4410A894F46D57D2D3AB",
    "PageHeader1$hidisNotify": "0",
    "PageHeader1$hidValueNotify": ".",
    "hidMode": "0",
    "drpAcademicYear": "1655BDBE09F24B37871FE727275D23A9",
    "drpField": "CDA73249707546749745F00A021AD54F",
    "drpCourse": drpCourse[1],
    "drpWeekDay": "0",
    "btnViewCourseClass": "Hiển thị lớp",
    "hidFieldId": "CDA73249707546749745F00A021AD54F",
    "hidSemester": "2021_2022_2",
    "hidTerm": "1",
    "hidCourseId": "",
    "hidMultiStudyType": "",
    "hidMaxPeriod": "",
    "hidCourseTuition": "",
    "hidMaxPeriodMode": "",
    "hidRegistratedCredit": hidRegistratedCredit[0],
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
    "hidCourseCredit": "",
    "hidUpdateMode": "",
    "hidQHSH": "",
    "hidSecondFieldCredit": "0",
    "hidSecondFieldMaxCredit": "",
    "hidUpgradeMark": "1",
    "hidAccountBalance": "0",
    "hidStudentTypeId": "",
    "hidTotalTuition": "0",
    "hidSocialWelfareExceptId": "",
    "hidTuitionCheck": "",  # "2",
    "hidMucNoHocPhiToiDa": "0",
    "hidLackGroupCourseId": "",
    "hidSemesterCheckMode": "0",
    "hidClientNumberOfCourse": "0",
    "hidConditionMarkValue": "",  # "5.4",
    "hidConditionMarkCode": "",  # "5.4",
    "hidCheckCourseNoTuition": "0",
    "hidSecondFieldMaxCreditMode": "",  # "1",
    "hidSecondFieldMaxCreditInclude": "0",
    "hidTinhHocPhiSangTacNghiep": "0",
}
# "gridRegistration$ctl02$hidMultiStudyTypeClass":"1,3",
# "gridRegistration$ctl02$hidClassGroup":"Nhóm_34",
# "gridRegistration$ctl03$hidMultiStudyTypeClass":"1,3",
# "gridRegistration$ctl03$hidClassGroup":"Nhóm_34",
# "gridRegistration$ctl04$hidMultiStudyTypeClass":"2,3",
# "gridRegistration$ctl04$hidClassGroup":"Nhóm_34",
# "gridRegistration$ctl05$hidMultiStudyTypeClass":"1,3",
# "gridRegistration$ctl05$hidClassGroup":"Nhóm_33",
# "gridRegistration$ctl06$hidMultiStudyTypeClass":"1,3",
# "gridRegistration$ctl06$hidClassGroup":"Nhóm_33",
# "gridRegistration$ctl07$hidMultiStudyTypeClass":"2,3",
# "gridRegistration$ctl07$hidClassGroup":"Nhóm_33",
# "gridRegistration$ctl08$hidMultiStudyTypeClass":"1,3",
# "gridRegistration$ctl08$hidClassGroup":"Nhóm_32",
# "gridRegistration$ctl09$hidMultiStudyTypeClass":"1,3",
# "gridRegistration$ctl09$hidClassGroup":"Nhóm_32",
# "gridRegistration$ctl10$hidMultiStudyTypeClass":"2,3",
# "gridRegistration$ctl10$hidClassGroup":"Nhóm_32",
# "gridRegistration$ctl11$hidMultiStudyTypeClass":"1,3",
# "gridRegistration$ctl11$hidClassGroup":"Nhóm_31",
# "gridRegistration$ctl12$hidMultiStudyTypeClass":"1,3",
# "gridRegistration$ctl12$hidClassGroup":"Nhóm_31",
# "gridRegistration$ctl13$hidMultiStudyTypeClass":"2,3",
# "gridRegistration$ctl13$hidClassGroup":"Nhóm_31",
# "gridRegistration$ctl14$hidMultiStudyTypeClass":"1,3",
# "gridRegistration$ctl14$hidClassGroup":"Nhóm_30",
# "gridRegistration$ctl15$hidMultiStudyTypeClass":"1,3",
# "gridRegistration$ctl15$hidClassGroup":"Nhóm_30",
# "gridRegistration$ctl16$hidMultiStudyTypeClass":"2,3",
# "gridRegistration$ctl16$hidClassGroup":"Nhóm_30",
# "gridRegistration$ctl17$hidMultiStudyTypeClass":"1,3",
# "gridRegistration$ctl17$hidClassGroup":"Nhóm_29",
# "gridRegistration$ctl18$hidMultiStudyTypeClass":"1,3",
# "gridRegistration$ctl18$hidClassGroup":"Nhóm_29",
# "gridRegistration$ctl19$hidMultiStudyTypeClass":"2,3",
# "gridRegistration$ctl19$hidClassGroup":"Nhóm_29",
