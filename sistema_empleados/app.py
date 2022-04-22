

from flask import Flask

from flask import render_template,request,redirect

from flaskext.mysql import MySQL




app= Flask(__name__)

MySQL=MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='sistema_registro'
MySQL.init_app(app)



#@app.route('/')
#def select():
    
    #insertar informacio
    
 #   sql="INSERT INTO `user`(`name`, `lastname`, `email`, `phone`) VALUES ('[value-2]','[value-3]','[value-4]','[value-5]')"
 #   conn=MySQL.connect()
 #   cursor=conn.cursor()
 #   cursor.execute(sql)
 #   conn.commit()
    
    
 #   return render_template('empleados/index.html')

 #consultar informacio
@app.route('/')
def index():
       
    sql="SELECT * FROM `user`;"
    conn=MySQL.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    user=cursor.fetchall()
    print(user)

    conn.commit()
    
    
    return render_template('empleados/index.html', user=user)

    

@app.route('/destroy/<int:id>')
def destroy(id):
    conn=MySQL.connect()
    cursor=conn.cursor()
    
    cursor.execute("DELETE FROM `user` WHERE id=%s", (id))
    conn.commit()
    return redirect('/')
    
    
@app.route('/edit/<int:id>')
def edit(id):
    
    conn=MySQL.connect()
    cursor=conn.cursor()
    
    cursor.execute("SELECT * FROM user WHERE id=%s",(id))
    
    user=cursor.fetchall()
    conn.commit()
    

      
    
    return render_template('empleados/edit.html',user=user)


@app.route("/update", methods=["POST"])
def update():
       
     _name=request.form['txtname']
     _latsname=request.form['txtlastname']
     _email=request.form['txtemail']
     _phone=request.form['txtphone']
     id=request.form['txtid']
     
     sql=" UPDATE user SET name=%s, lastname=%s, email=%s, phone=%s WHERE id=%s;"
    
     data=(_name,_latsname,_email,_phone,id )
    
    
     conn=MySQL.connect()
     cursor=conn.cursor()
     cursor.execute(sql,data)
     conn.commit()
    
    
    
    
     return redirect("/")



    


@app.route('/create')
def create():
    
    return render_template("empleados/create.html")


@app.route('/store', methods=['POST'])
def storage():
    
    
    _name=request.form["txtname"]
    _latsname=request.form["txtlastname"]
    _email=request.form["txtemail"]
    _phone=request.form["txtphone"]
    
    
    sql="INSERT INTO `user` (`id`, `name`, `lastname`, `email`, `phone`) VALUES (NULL, %s, %s, %s, %s)"
    
    data=(_name, _latsname, _email, _phone)
    
    
    conn=MySQL.connect()
    cursor=conn.cursor()
    cursor.execute(sql,data)
    conn.commit()
    
    
    return redirect('/')
    
    
if __name__=='__main__':
    
     app.run(debug=True)