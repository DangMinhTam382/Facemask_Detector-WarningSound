import datetime
from winreg import OpenKey
from cv2 import split
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import string

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize (creds)
name_class = "LVTN"

sheet = client.open("gg_sheet_com")
work_sheet = sheet.worksheet(name_class)

lesson_period = [1,2,3,4,5,6,7,8,9,10,11,12,13]
lesson_start_time = [6,7,8,9,10,11,12,13,14,15,16,17,18]

alphabet_string = string.ascii_uppercase
alphabet_list = list(alphabet_string)

def get_date ():
    Now = datetime.datetime.now()
    date_get = Now.strftime("%d/%m")
    return date_get

def get_time ():
    Now = datetime.datetime.now()
    time_get=["0","0"]
    time_get[0] = str(Now.strftime("%H"))
    time_get[1] = str(Now.strftime("%M"))
    return time_get

def time_check(check_in_time, class_period, i = 0, class_start_time = 0):
    for period in lesson_period:
        if class_period == period:
            class_start_time = int(lesson_start_time[i])
        i = i + 1
    if class_start_time	== 0:
        return "Null"

    if int(check_in_time[0]) < class_start_time:
        return "On time"
    else:
        if int(check_in_time[1]) <= 15:
            return "On time"
        else: 
            return "Late"


# work_sheet.format("",{
#    "backgroundColor": {
#        "red": 1.0,
#        "green": 0.0,
#        "blue": 0.0
#    }
# })

# x = "Late 13:50-16:50"

# str1 = x.split("-")
# print (str1)
# print (get_time())

# if " " in x:
#     print ("oke") 
# else: print ("not oke")



