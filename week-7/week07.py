from flask import Flask,request,render_template,session,redirect,flash
from flask import jsonify
from flask import make_response
import mysql.connector
from flask_restful import Api
from flask_restful import Resource
#建立Application 物件,可以設定靜態檔案的路徑
app= Flask(
    __name__,
)
api = Api(app)
#session 加密機制(密鑰)
app.secret_key="any string but secret"
#連線資料庫
mydb=mysql.connector.connect(
    host= "localhost",
    user= "root",
    password="123456",
    charset="utf-8",
    database="week_06",
) 


#網站首頁
@app.route("/")
def index():
    return render_template("week07.html")

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
         flash("提醒：留言不可為空。請輸入留言")
    else:
        sql="INSERT INTO messages (user_id,contents) VALUES (%s,%s)"
        val=(id,content)
        mycursor=mydb.cursor()
        mycursor.execute(sql,val)
        mydb.commit()
    return redirect("/member")


#查詢、修改會員資料API
class return_user_data(Resource):
    #查詢
    def get(self):
        username=request.args.get("username")
        try:
            (session["login"]=="ok") == True                                #會員登入狀態
            mycursor=mydb.cursor()
            sql="SELECT id,name,username FROM accounts WHERE username=%s"
            val=(username,)
            mycursor.execute(sql,val)
            user_data = mycursor.fetchall()
            row_headers=[x[0] for x in mycursor.description] 
            json_data=[]
            for result in user_data:
                json_data.append(dict(zip(row_headers,result)))             #zip()可以把多個list或tuple的相對應位置鏈起來，成為一個list。參考：https://ithelp.ithome.com.tw/articles/10218029
            json_data={"data":json_data[0]}
        except:
            json_data={"data":None}
        finally:
            return jsonify(json_data)
    
    #修改
    def patch(self):
        try:
            if session["login"] !="ok":
                return redirect("/")
            
            req = request.get_json()
            
            if req["name"] == "":
                result={"error":True}
            else:
                #更新資料庫
                new_name = req["name"]
                id = session["userinfo"][0]
                mycursor=mydb.cursor()
                sql="UPDATE accounts SET name=%s WHERE id=%s"
                val=(new_name,id)
                mycursor.execute(sql,val)
                mydb.commit()
                
                #重新定義session["userinfo"] (因為原資料為tuple，不可更動)
                sql_1="SELECT id,name FROM accounts WHERE id=%s"
                val_1=(id,)
                mycursor.execute(sql_1,val_1)
                user = mycursor.fetchall()
                session["userinfo"]= user[0]
                result={"ok":True}
        except:
            result={"error":True}
        finally:
            return jsonify(result)

  
api.add_resource(return_user_data, "/api/member")                           #將 class return_user_data與url 連接起來



#啟動網站伺服器,可透過 port 參數指定埠號
#app.run()     →啟動網站伺服器
app.run(port =3000,debug=True)


