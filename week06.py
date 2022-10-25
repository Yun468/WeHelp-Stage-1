from flask import Flask   #載入Flask
from flask import request  #載入 Request物件  →利用Request物件取得相關資訊
from flask import render_template  #載入render_template 函式
from flask import session   #載入session 方法
from flask import redirect
import mysql.connector as myconnector
#建立Application 物件,可以設定靜態檔案的路徑
app= Flask(
    __name__,
)
#session 加密機制(密鑰)
app.secret_key="any string but secret"
#連線資料庫
mydb=myconnector.connect(
    host= "localhost",
    user= "root",
    password="123456",
    charset="utf-8",
    database="week_06",
) 

#透過python 操作 mysql
#mycursor=mydb.cursor()                              #execute(" 欲操作的mysql 指令") 操作mysql 指令
#透過python 創建 database
    # mycursor.execute("CREATE DATABASE week_06")       #execute(" 欲執行的mysql 指令") 執行mysql 指令
#透過python 創建 table
#mycursor.execute("CREATE TABLE accounts (name VARCHAR(255),username VARCHAR(255) NOT NULL,password VARCHAR(255) NOT NULL)")


#網站首頁
@app.route("/")
def index():
    return render_template("week06.html")

#註冊帳號密碼
@app.route("/singup",methods=["POST"])
def account():
    name=request.form["name"]
    username=request.form["username"]
    password=request.form["password"]
    if username=="" or password=="" or name=="":
        return redirect("/error?message=姓名、帳號、密碼不可為空白") 
    else:
        mycursor=mydb.cursor()
        mycursor.execute("SELECT username FROM accounts")
        userexist = mycursor.fetchall()                        #查詢mysql 回傳的資料 → fetchone() / fetchall()
        for user in userexist:
            if username == user[0]:
                return redirect("/error?message=帳號已經被註冊")
            else:
                sql = "INSERT INTO accounts (name,username,password) VALUES (%s,%s,%s)"
                val = (name,username,password)
                mycursor.execute(sql,val)
                mydb.commit()
                return redirect("/")



#輸入帳號密碼(處理/singin路徑的對應函式)
@app.route("/singin",methods=["POST"])
def username():
    username=request.form["username_singin"]
    password=request.form["password_singin"]
    if username=="" or password=="":
        return redirect("/error?message=請輸入帳號、密碼")
    else:
        mycursor=mydb.cursor()
        mycursor.execute("SELECT*FROM accounts")
        userexist = mycursor.fetchall()                             #userexist 是list, 裡面每一項是tuple
        for user in userexist:
            if (username,password) == (user[2],user[3]):
                session["login"]="ok"
                session["userinfo"]= (user[0],user[1],user[2])
                return redirect("/member")
        return redirect("/error?message=帳號或密碼錯誤")


#登入成功
@app.route("/member")
def member():
    if session["login"]!="ok":
        return redirect("/")
    else:
        name=session["userinfo"][1]
        return render_template("answer.html",text_1="歡迎光臨，這是會員頁",text_2=name+"，歡迎登入系統")
#登入失敗
@app.route("/error")
def error():
    message=request.args.get("message")
    return render_template("answer.html",text_1="失敗頁面",text_2=message)

#登出
@app.route("/signout")
def signout():
    session["login"]=None
    session["userinfo"]=None
    return redirect("/")


#啟動網站伺服器,可透過 port 參數指定埠號
#app.run()     →啟動網站伺服器
app.run(port =3000)
