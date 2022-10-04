import urllib.request as req   #載入urllib request
elem=[]
def getData(url):                                   #定義一個函式,讓使用者透過呼叫函式,模擬瀏覽器發送請求
    request=req.Request(url,headers={               #建立一個Request 物件,模擬瀏覽器要送出的資訊
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    })

    with req.urlopen(request) as response:       #用urllib.request.urlopen()去接收response 
        response=response.read().decode("utf-8")    #將接收到的資訊用read()+decode()打開解析,再用一個變數代表解析後的資料
    
    import bs4
    root=bs4.BeautifulSoup(response,"html.parser")      #用BeautifulSoup解讀html文件
    titles=root.find_all("div",class_="title")   


    for title in titles:   
        if title.a !=None:
            elem.append(str(title.a.string))      #str()   →將bs4的格式轉成python的string


    nextPage=root.find("a",string="‹ 上頁")   
    return nextPage["href"]                       #將上一頁的href值回傳到函式(此處的herf都沒有"https://www.ptt.cc/")




pageUrl="https://www.ptt.cc/bbs/movie/index.html"   #目標網站第一頁網址

count=0
while count<10:                                      #要取幾頁
    pageUrl="https://www.ptt.cc/"+getData(pageUrl)
    count+=1

with open("movie.txt","w",encoding="utf-8") as file:
    for titleG in elem:
        if "[好雷]" in titleG and "Re: " not in titleG:
            file.write(titleG+"\n")

    for titleN in elem:
        if "[普雷]" in titleN and "Re: " not in titleN:
            file.write(titleN+"\n")

    for titleB in elem:
        if "[負雷]" in titleB and "Re: " not in titleB:
            file.write(titleB+"\n")






