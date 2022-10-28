from flask import Flask   #載入Flask
from flask import request  #載入 Request物件  →利用Request物件取得相關資訊
from flask import render_template  #載入render_template 函式
from flask import session   #載入session 方法
from flask import redirect
from flask import flash
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
    mycursor=mydb.cursor()
    if username=="" or password=="" or name=="":
        return redirect("/error?message=姓名、帳號、密碼不可為空白") 
    else:
        sql=("SELECT username FROM accounts WHERE username=(%s)")
        signup_name=(username,)
        mycursor.execute(sql,signup_name)
        userexist= mycursor.fetchone()
        if userexist !=None:
            return redirect("/error?message=帳號已經被註冊")
        else:
            sql ="INSERT INTO accounts (name,username,password) VALUES (%s,%s,%s)"
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
        mycursor = mydb.cursor()
        sql="SELECT id,name FROM accounts WHERE username=%s AND password=%s"
        val=(username,password)
        mycursor.execute(sql,val)
        userexist = mycursor.fetchall()
        if userexist != None:
            session["login"]="ok"                           #userexist = [(id,name),]
            session["userinfo"]= userexist[0]               #userexist 是list / userexist[0] 是tuple / id 是int / name 是str
            return redirect("/member")
        else:            
            return redirect("/error?message=帳號或密碼錯誤")


#登入成功
@app.route("/member")
def member():
    if session["login"]!="ok" or session["login"] ==None :
        return redirect("/")
    else:
        name=session["userinfo"][1]
        mycursor=mydb.cursor()
        mycursor.execute ("SELECT accounts.username,messages.contents FROM accounts INNER JOIN messages ON accounts.id = messages.user_id")
        result=mycursor.fetchall()
        return render_template("answer.html",text_1="歡迎光臨，這是會員頁",text_2=name+"，歡迎登入系統",text_3=result)
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

#留言功能
@app.route("/message",methods=["POST"])
def message():
    id=session["userinfo"][0]                       #userinfo = (id,name)
    content=request.form["content"]
    if content == "":
         flash("提醒:留言不可為空。請輸入留言")
    else:
        sql="INSERT INTO messages (user_id,contents) VALUES (%s,%s)"
        val=(id,content)
        mycursor=mydb.cursor()
        mycursor.execute(sql,val)
        mydb.commit()
    return redirect("/member")


#啟動網站伺服器,可透過 port 參數指定埠號
#app.run()     →啟動網站伺服器
app.run(port =3000)
