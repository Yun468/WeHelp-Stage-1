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

#輸入帳號密碼(處理/singin路徑的對應函式)
@app.route("/singin",methods=["POST"])
def account():
    account=request.form["account"]
    password=request.form["password"]
    if account=="test" and password=="test":
        session["login"]="ok"
        return redirect("/member/")
    elif account=="" or password=="":
        return redirect("/error?message=請輸入帳號、密碼")
    else:
        return redirect("/error?message=帳號或密碼錯誤")

#登入成功
@app.route("/member/")
def member():
    if session["login"]!="ok":
        return redirect("/")
    else:
        return render_template("answer.html",text_1="歡迎光臨，這是會員頁",text_2="恭喜您，成功登入系統")
#登入失敗
@app.route("/error")
def error():
    message=request.args.get("message")
    return render_template("answer.html",text_1="失敗頁",text_2=message)

#登出
@app.route("/signout")
def signout():
    session["login"]=None
    return redirect("/")


#啟動網站伺服器,可透過 port 參數指定埠號
#app.run()     →啟動網站伺服器
app.run(port =3000)
