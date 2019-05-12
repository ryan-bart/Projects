import requests
import pandas as pd
import time

IPofInterest = input("Enter an IP address: ")

url = "https://ipapi.co/"+IPofInterest+"/json/"

IP_info_dic = requests.get(url).json()
#print(IP_info_dic)

print("Tracking IP.........")
print("")
time.sleep(3)

try:
    print("IP Address: "+IP_info_dic['ip'])
    print("Organization: "+IP_info_dic['org'])
    print("Location: "+IP_info_dic['city']+", "+IP_info_dic['region']+', '+IP_info_dic['country'])
    print("Zip Code: "+IP_info_dic['postal'])
    print("Latitude: %4.3f" %IP_info_dic['latitude'])
    print("Longitude: %4.3f" %IP_info_dic['longitude'])

except: True