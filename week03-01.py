import urllib.request as req
url="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json" 
with req.urlopen(url) as response:
    data=response.read().decode("utf-8")

import json
Datas=json.loads(data)
items=Datas["result"]["results"]


with open("data.csv","w",encoding="utf-8") as file:
    for i in items: 
        stitle=i["stitle"]
        address=i["address"][5:8]
        longitude=i["longitude"]
        latitude=i["latitude"]
        first_picture="http"+(i["file"].split("http")[1])
        xpostDate=i["xpostDate"][0:4]
        if int(xpostDate)>=2015:
            file.write(stitle+','+address+','+longitude+','+latitude+','+first_picture+"\n")





# 2015日期
# xpostDate   →items["xpostDate"][0:4]
# 景點名稱,區域,經度,緯度,第一張圖檔網址
# "stitle"    →items["stitle"]
# "address"   →address1=items["address"][5:8]               
# "longitude" →items["longitude"]
# "latitude"  →items["atitude"]
# "file"      →first_picture=items[index]["file"].split("http")[1]