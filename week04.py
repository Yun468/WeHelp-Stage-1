from flask import Flask   #載入Flask
from flask import request  #載入 Request物件  →利用Request物件取得相關資訊
from flask import render_template  #載入render_template 函式
from flask import session   #載入session 方法
from flask import redirect
#建立Application 物件,可以設定靜態檔案的路徑
app= Flask(
    __name__,
)

#session 加密機制(密鑰)
app.secret_key="any string but secret"



#網站首頁
@app.route("/")
def index():
  return render_template("week04.html")

#處理路徑的對應函式
@app.route("/singin",methods=["POST"])
def account():
    account=request.form["account"]
    password=request.form["password"]
    session["data_1"]=account
    session["data_2"]=password
    if account=="test" and password=="test":
        return redirect("/member/")
    else:
        return redirect("/error")

@app.route("/member/")
def member():
    if session["data_1"]!="test" or session["data_2"]!="test":
        return redirect("/")
    else:
        return render_template("answer.html",text_1="歡迎光臨，這是會員頁",text_2="恭喜您，成功登入系統")
@app.route("/error")
def error():
    account=session["data_1"]
    password=session["data_2"]
    if  account=="":
        text_2=request.args.get("message","請輸入帳號、密碼")
        return render_template("answer.html",text_1="失敗頁",text_2=text_2)
    elif password=="":
        text_2=request.args.get("message","請輸入帳號、密碼")
        return render_template("answer.html",text_1="失敗頁",text_2=text_2)
    else:
        text_2=request.args.get("message","帳號或密碼錯誤")
        return render_template("answer.html",text_1="失敗頁",text_2=text_2)

@app.route("/signout")
def signout():
    session["data_1"]=None
    session["data_2"]=None
    return redirect("/")
    print(session["data_1"])


#啟動網站伺服器,可透過 port 參數指定埠號
#app.run()     →啟動網站伺服器
app.run(port =3000)
