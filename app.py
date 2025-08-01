from flask import Flask, render_template, request, redirect 
from flask_mysqldb import MySQL 
from flask_mail import Mail, Message 
from flask_sqlalchemy import SQLAlchemy 
from flask_admin import Admin 
from flask_admin.contrib.sqla import ModelView 
from random import randint
import time, datetime 



# flask-mysql connection 
app = Flask(__name__) 
 
app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root' 
app.config['MYSQL_PASSWORD'] = '0810' 
app.config['MYSQL_DB'] = 'ticketbox' 
 
mysql = MySQL(app) 

# otp mail connection 
app.config["MAIL_SERVER"] = 'smtp.gmail.com' 
app.config["MAIL_PORT"] = 465 
app.config["MAIL_USERNAME"] = 'ticketbox4567@gmail.com' 
app.config['MAIL_PASSWORD'] = 'jbbbmerdghkmkcsd' 
app.config['MAIL_USE_TLS'] = False 
app.config['MAIL_USE_SSL'] = True 
 
mail = Mail(app) 
 
#flask-sqlalchemy connection 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:0810@localhost/ticketbox' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY'] = 'tisasecret' 
 
db = SQLAlchemy(app) 
 
#admin module 
admin = Admin(app) 
 
#tables in admin 
class User(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    username = db.Column(db.String(30)) 
    password = db.Column(db.String(8)) 
    mobile_number = db.Column(db.BigInteger) 
    email = db.Column(db.String(50)) 
 
admin.add_view(ModelView(User, db.session, category="Users")) 
 
class Administrator(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    admin_name = db.Column(db.String(30)) 
    admin_password = db.Column(db.String(8)) 
    admin_email = db.Column(db.String(50)) 
 
admin.add_view(ModelView(Administrator, db.session, category="Admins")) 
 
class User_Log(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    username = db.Column(db.String(30)) 
    login_time = db.Column(db.DateTime) 
    city_selected = db.Column(db.String(20)) 
    movie_selected = db.Column(db.String(50)) 
    theatre_selected = db.Column(db.String(50)) 
    date_selected = db.Column(db.DateTime) 
    number_of_tickets = db.Column(db.String(10)) 
    seats_selected = db.Column(db.String(100)) 
    amount_paid = db.Column(db.Integer) 
    bank = db.Column(db.String(30)) 
    card_type = db.Column(db.String(30)) 
    card_number = db.Column(db.String(25)) 
    expiration_date = db.Column(db.String(5)) 
    cvv_number = db.Column(db.String(3)) 
    name_on_card = db.Column(db.String(50)) 
 
admin.add_view(ModelView(User_Log, db.session, category="Users")) 
 
class Admin_Login(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    admin_name = db.Column(db.String(30)) 
    login_time = db.Column(db.DateTime) 
 
admin.add_view(ModelView(Admin_Login, db.session, category="Admins")) 
 
class Cities(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    city = db.Column(db.String(20)) 
    movies = db.Column(db.String(500)) 
 
admin.add_view(ModelView(Cities, db.session)) 
class Chennai(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    movies = db.Column(db.String(20)) 
    theatres = db.Column(db.String(500)) 
 
admin.add_view(ModelView(Chennai, db.session, category="Theatres")) 
 
class Mumbai(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    movies = db.Column(db.String(20)) 
    theatres = db.Column(db.String(500)) 
 
admin.add_view(ModelView(Mumbai, db.session, category="Theatres")) 
 
class Bangalore(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    movies = db.Column(db.String(20)) 
    theatres = db.Column(db.String(500)) 
 
admin.add_view(ModelView(Bangalore, db.session, category="Theatres")) 
 
class Delhi(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    movies = db.Column(db.String(20)) 
    theatres = db.Column(db.String(500)) 
 
admin.add_view(ModelView(Delhi, db.session, category="Theatres")) 
 
class Sunday(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    movie = db.Column(db.String(50)) 
    theatre = db.Column(db.String(50)) 
    date = db.Column(db.DateTime) 
    seats = db.Column(db.String(10)) 
 
admin.add_view(ModelView(Sunday, db.session, category= "Seat_Availability")) 
 
class Monday(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    movie = db.Column(db.String(50)) 
    theatre = db.Column(db.String(50)) 
    date = db.Column(db.DateTime) 
    seats = db.Column(db.String(10)) 
 
admin.add_view(ModelView(Monday, db.session, category= "Seat_Availability")) 
 
class Tuesday(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    movie = db.Column(db.String(50)) 
    theatre = db.Column(db.String(50)) 
    date = db.Column(db.DateTime) 
    seats = db.Column(db.String(10)) 
 
admin.add_view(ModelView(Tuesday, db.session, category= "Seat_Availability")) 
 
class Wednesday(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    movie = db.Column(db.String(50)) 
    theatre = db.Column(db.String(50)) 
    date = db.Column(db.DateTime) 
    seats = db.Column(db.String(10)) 
 
admin.add_view(ModelView(Wednesday, db.session, category= "Seat_Availability")) 
 
class Thursday(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    movie = db.Column(db.String(50)) 
    theatre = db.Column(db.String(50)) 
    date = db.Column(db.DateTime) 
    seats = db.Column(db.String(10)) 
 
admin.add_view(ModelView(Thursday, db.session, category= "Seat_Availability")) 
 
class Friday(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    movie = db.Column(db.String(50)) 
    theatre = db.Column(db.String(50)) 
    date = db.Column(db.DateTime) 
    seats = db.Column(db.String(10)) 
 
admin.add_view(ModelView(Friday, db.session, category= "Seat_Availability")) 
 
class Saturday(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    movie = db.Column(db.String(50)) 
    theatre = db.Column(db.String(50)) 
    date = db.Column(db.DateTime) 
    seats = db.Column(db.String(10)) 
 
admin.add_view(ModelView(Saturday, db.session, category= "Seat_Availability")) 
 
class Chennai_Timings(db.Model): 
    id = db.Column(db.Integer, primary_key = True) 
    movie = db.Column(db.String(60)) 
    theatre = db.Column(db.String(50)) 
    timings = db.Column(db.String(200)) 
 
admin.add_view(ModelView(Chennai_Timings, db.session, category="Timings")) 
 
class Mumbai_Timings(db.Model): 
    id = db.Column(db.Integer, primary_key = True) 
    movie = db.Column(db.String(60)) 
    theatre = db.Column(db.String(50)) 
    timings = db.Column(db.String(200)) 
 
admin.add_view(ModelView(Mumbai_Timings, db.session, category="Timings")) 
 
class Bangalore_Timings(db.Model): 
    id = db.Column(db.Integer, primary_key = True) 
    movie = db.Column(db.String(60)) 
    theatre = db.Column(db.String(50)) 
    timings = db.Column(db.String(200)) 
 
admin.add_view(ModelView(Bangalore_Timings, db.session, category="Timings")) 
 
class Delhi_Timings(db.Model): 
    id = db.Column(db.Integer, primary_key = True) 
    movie = db.Column(db.String(60)) 
    theatre = db.Column(db.String(50)) 
    timings = db.Column(db.String(200)) 
 
admin.add_view(ModelView(Delhi_Timings, db.session, category="Timings")) 
 
class Seats(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    movie = db.Column(db.String(60)) 
    theatre = db.Column(db.String(50)) 
    date = db.Column(db.DateTime) 
    seats_selected = db.Column(db.String(300)) 
 
admin.add_view(ModelView(Seats, db.session)) 
 
 
# homepage render 
@app.route('/') 
def home(): 
    return render_template('home.html') 
 
# sign up page render + OTP generation 
@app.route('/signup', methods=['GET', 'POST']) 
def signup(): 
    if request.method == "POST": 
        details = request.form 
        global username 
        username = details['uname'] 
        passw = details['psswd'] 
        mobile = details['num'] 
        global email 
        email = details['em'] 
        confirm = details['pass'] 
        global otp 
        otp = randint(000000, 999999) 
        cur = mysql.connection.cursor() 
        cur.execute( 
            "SELECT * FROM user where username = %s", (username,)) 
        name = cur.fetchone() 
        if name is None: 
            if len(passw) == 8: 
                if confirm == passw: 
                    cur.execute( 
                        "INSERT INTO user(Username, Password, Mobile_number, Email) VALUES (%s, %s, %s , %s)", (username, passw, mobile, email)) 
                    mysql.connection.commit() 
                    cur.close() 
                    message = Message( 
                        'Verfication code for TicketBox', sender='ticketbox4567@gmail.com', recipients=[email]) 
                    message.body = "Your 6-digit OTP code is " + str(otp) 
                    mail.send(message) 
                    return render_template('verification.html') 
                else: 
                    return "<center><h1>Password was not confirmed</h1><br><a href='http://127.0.0.1:5000/signup'>Back to Sign Up</a></h1></center>" 
            else: 
                return "<center><h1>Password is not 8 characters</h1><br><a href='http://127.0.0.1:5000/signup'>Back to Sign Up</a></h1></center>" 
        else: 
            return "<center><h1>Username is already taken<br><a href='http://127.0.0.1:5000/signup'>Back to Sign Up</a></h1></center>" 
    return render_template('signup.html') 
 
# cancellation login request 
@app.route('/cancellationlogin', methods=['POST', 'GET']) 
def cancellationlogin(): 
    if request.method == 'POST': 
        del_usname = request.form["del_username"] 
        del_pass = request.form["del_password"] 
        del_now = time.strftime('%Y-%m-%d %H:%M:%S') 
        cur = mysql.connection.cursor() 
        cur.execute("SELECT * FROM User WHERE username = %s and password = %s",(del_usname,del_pass)) 
        global query_del 
        query_del = cur.fetchone() 
        if query_del is not None:
            a=("SELECT city_selected,movie_selected,theatre_selected,date_selected,number_of_tickets,seats_selected FROM User__Log where bank is not null and Username=%s and date_selected>%s", 
            (del_usname,del_now))
            print(a)
            cur.execute( 
            "SELECT city_selected,movie_selected,theatre_selected,date_selected,number_of_tickets,seats_selected FROM User__Log where bank is not null") 
            quer = cur.fetchall() 
            if quer is not None: 
                li = list(quer) 
                print(li)
                deleted_items = [] 
                for i in li: 
                    item  = list(i) 
                    deleted_items.append(item) 
                return render_template('cancellation.html',deleted_items=deleted_items) 
            elif quer is None: 
                return "<center><h1>You have not booked any tickets</h1></center>" 
        elif query_del is None: 
            return "<center><h1>You have not signed up<a href='http://127.0.0.1:5000/signup'>Click here to Sign Up</a></h1></center>" 
    return render_template('cancellationlogin.html') 
 
#cancellation process 
@app.route('/cancellation',methods=['POST', 'GET']) 
def cancellation(): 
    if request.method == 'POST': 
        del_items = str(request.form.getlist("deleted_items")) 
        cur= mysql.connection.cursor() 
        x = del_items[2:-2]   
        y = x.split("', '") 
        for i in y: 
            z = i.split("|") 
            cur.execute("DELETE FROM User__log where city_selected = %s and movie_selected = %s and theatre_selected = %s and date_selected= %s and seats_selected = %s" 
            ,(z[0],z[1],z[2],z[3],z[5])) 
            mysql.connection.commit() 
            date = z[3][:10] 
            days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'] 
            day = datetime.datetime.strptime(date, '%Y-%m-%d').weekday() 
            delete_daytable = days[day] 
            a = "SELECT Seats FROM " + delete_daytable + " WHERE Theatre = '" + z[2] +"' and date='"+date+ "' AND Movie = '" + z[1] + "'" 
            cur = mysql.connection.cursor() 
            print(a)
            cur.execute(a) 
            query = cur.fetchall() 
            q = str(query) 
            seatnum = int(q[3:-5]) 
            seats = str(seatnum + int(z[4])) 
            query = "UPDATE " + delete_daytable +" SET Seats = " + seats + " WHERE Theatre = '" + z[2] +"' and date='"+date+ "' AND Movie = '" + z[1] + "'"
            print(query)
            cur.execute(query) 
            mysql.connection.commit() 
            cur.execute("DELETE FROM Seats WHERE Movie = %s and Theatre = %s and Date = %s and seats_selected = %s",(z[1],z[2],z[3],z[5])) 
            mysql.connection.commit() 
            a = list(query_del) 
            del_email = a[4] 
            message = Message( 
            'Ticket Cancellation', sender='ticketbox4567@gmail.com', recipients=[del_email]) 
            message.html = "<h1>Your tickets for " + z[1] + " at " + z[2] + " on " + z[3] + " for seats " + z[5] + " have been cancelled.</h1>" 
            mail.send(message) 
        return render_template('cancellationend.html') 
    return render_template('cancellation.html') 
 
# OTP verification(customers) 
@app.route('/verification', methods=['POST', 'GET']) 
def validate(): 
    if request.method == "POST": 
        user_otp = request.form['otp'] 
        if otp == int(user_otp): 
            return render_template('login.html') 
        else: 
            return "<center><h1>Your OTP is invalid<br><a href='http://127.0.0.1:5000/login'>Back to Login</a></h1></center>" 
    return render_template('verification.html') 
 
# login page render 
@app.route('/login', methods=['POST', 'GET']) 
def login(): 
    if request.method == "POST": 
        global usname 
        usname = request.form['username'] 
        passwd = request.form['password'] 
        global otp1 
        otp1 = randint(00000, 99999) 
        cur = mysql.connection.cursor() 
        cur.execute( 
            "SELECT * FROM Administrator WHERE admin_name = %s AND admin_password = %s", (usname, passwd)) 
        account = cur.fetchone() 
        if account is None: 
            cur.execute( 
                'SELECT * FROM user WHERE username = %s AND password = %s', (usname, passwd)) 
            acc = cur.fetchone() 
            if acc is None: 
                return "<center><h1>Your username or password is invalid<br><a href='http://127.0.0.1:5000/login'>Back to Login</a></h1></center>" 
            else: 
                global now 
                now = time.strftime('%Y-%m-%d %H:%M:%S') 
                cur.execute( 
                    "INSERT into User__Log (Username, Login_time) VALUES (%s, %s)", (usname, now)) 
                mysql.connection.commit() 
                cur.close() 
            return redirect('http://127.0.0.1:5000/cities', code=302) 
        else: 
            lt = time.strftime('%Y-%m-%d %H:%M:%S') 
            cur.execute( 
                "INSERT into Admin__Login (admin_name, login_time) VALUES (%s, %s)", (usname, lt)) 
            mysql.connection.commit() 
            cur.close() 
            s = list(account) 
            email = s[3] 
            message = Message( 
                'Admin Verification for TicketBox', sender='ticketbox4567@gmail.com', recipients=[email] 
            ) 
            message.body = "Your 5-digit OTP code is " + str(otp1) 
            mail.send(message) 
            return render_template('adminverification.html', admin=usname) 
    return render_template('login.html') 
 
# admin verification 
@app.route('/adminverification', methods=['POST', 'GET']) 
def adminvalidate(): 
    if request.method == "POST": 
        user_otp = request.form['otpad'] 
        if otp1 == int(user_otp): 
            return redirect('http://127.0.0.1:5000/admin/', code=302) 
        else: 
            return "<center><h1>Your OTP is invalid<br><a href='http://127.0.0.1:5000/login'>Back to Login</a></h1></center>" 
    return render_template('adminverification.html') 
 
#city and movies page render 
@app.route('/cities', methods=['GET', 'POST']) 
def cities(): 
    if request.method == "POST": 
        global city 
        city = request.form["city"] 
        cur = mysql.connection.cursor() 
        cur.execute("UPDATE User__Log SET city_selected = %s WHERE Login_time = %s",(city,now)) 
        mysql.connection.commit() 
        cur.execute("SELECT Movies FROM Cities where City = %s", (city,)) 
        query = cur.fetchall() 
        a = str(query) 
        b = a[3:-5] 
        mov = b.split(',') 
        return render_template('movies.html', mov=mov, city=city) 
    elif request.method == "GET": 
        cur = mysql.connection.cursor() 
        cur.execute("SELECT City FROM Cities") 
        data = cur.fetchall() 
        new = list(data) 
        li = [] 
        for x in new: 
            ap = x[0] 
            li.append(ap) 
    return render_template('cities.html', name=usname, li=li) 
 
#movie updation in user_log table 
@app.route('/movies', methods=['GET','POST']) 
def movie(): 
    if request.method == "POST": 
        global movies 
        movies = request.form['movie'] 
        cur = mysql.connection.cursor() 
        cur.execute("UPDATE User__Log SET movie_selected = %s WHERE Login_time = %s",(movies,now)) 
        mysql.connection.commit() 
    return redirect('http://127.0.0.1:5000/theatres', code=302) 
 
#theatres and timing page render 
@app.route('/theatres', methods=['POST','GET']) 
def theatres(): 
    if request.method == "POST": 
        global theatre 
        theatre = request.form["theatre"] 
        cur = mysql.connection.cursor() 
        cur.execute("UPDATE User__Log SET theatre_selected = %s WHERE Login_time = %s",(theatre,now)) 
        mysql.connection.commit() 
         
        
        times = [] 
        return render_template('timings.html', times=times, movie=movies, theatre=theatre) 
    elif request.method == "GET": 
        cur = mysql.connection.cursor() 
        cur.execute("SELECT city_selected from User__Log where Login_time = %s",(now,)) 
        q = cur.fetchall() 
        query = str(q) 
        cityop = query[3:-5] 
        
        a = "select theatres from "+cityop+" where movies='"+movies.lstrip()+"'"
        cur.execute(a) 
        print(a)
        theatre = cur.fetchall() 
        new = str(theatre) 
        li = new[3:-5] 
        th = li.split(',') 
        
    return render_template('theatres.html', th=th, movies=movies) 
 
#date to day conversion 
@app.route('/timings', methods=['POST', 'GET']) 
def timings(): 
    if request.method == 'POST': 
        global date
        date = request.form["dateselected"] 
        print(date)
        print(datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%A"))
        cur = mysql.connection.cursor() 
        cur.execute("UPDATE User__Log SET date_selected = %s WHERE Login_time = %s",(date,now)) 
        mysql.connection.commit() 
        global daytable 
        daytable = datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%A")
    return redirect('http://127.0.0.1:5000/seatavailability', code=302) 
 
# display number of seats and entering number of seats 
@app.route('/seatavailability', methods=['POST', 'GET']) 
def seatavailability(): 
    if request.method == "POST": 
        global seat 
        seat = int(request.form["seats"]) 
        a = "SELECT Seats FROM " + daytable + " WHERE Theatre = '" + theatre +"' AND date='"+date+"' AND Movie = '" + movies + "'" 
        cur = mysql.connection.cursor() 
        cur.execute(a) 
        query = cur.fetchall() 
        q = str(query) 
        seatnum = int(q[3:-5]) 
        global seats_in
        seats_in = seatnum - seat 
        
        return redirect('http://127.0.0.1:5000/booked', code=302) 
    elif request.method == 'GET': 
        a = "SELECT Seats FROM " + daytable + " WHERE Theatre = '" + theatre +"' AND date='"+date+"' AND Movie = '" + movies + "'"
        print(a) 
        cur = mysql.connection.cursor() 
        cur.execute(a) 
        query = cur.fetchall() 
        q = str(query) 
        seatnum = q[3:-5]  
        global newdate 
        print(query)
        
        print(seatnum) 
        newdate = date 
        cur.execute("UPDATE User__Log SET date_selected = %s WHERE Login_time = %s",(newdate,now)) 
        mysql.connection.commit() 
    return render_template('seatavailability.html',date=newdate,theatre=theatre,seatnum = seatnum,movies=movies) 
 
#choosing seats 
@app.route('/booked', methods=['POST', 'GET']) 
def booked(): 
    if request.method == 'POST': 
        seats = request.form.getlist("seat_selected") 
        global seatslist 
        seatslist = "" 
        amount=0 
        for i in seats: 
            seatslist = seatslist+i+',' 
            if i[0] in ['A', 'B', 'C', 'D', 'E', 'F','G']: 
                amount+=180 
            else: 
                amount+=120 
        cur = mysql.connection.cursor() 
        cur.execute("UPDATE User__Log SET amount_paid = %s , seats_selected = %s WHERE Login_time = %s",(amount,seatslist,now)) 
        
        cur.execute("INSERT into Seats (Movie,Theatre,Date,Seats_Selected) VALUES (%s,%s,%s,%s)",(movies,theatre,newdate,seatslist))
        
        b = "UPDATE " + daytable + " SET Seats = '"+ str(seats_in) +"' WHERE Theatre = '" + theatre +"' AND date='"+date+"' AND Movie = '" + movies + "'" 
        print(b)
        cur.execute(b) 
       
        cur.execute("UPDATE User__Log SET number_of_tickets = %s WHERE Login_time = %s",(str(seat),now))  
        mysql.connection.commit() 
        return render_template('payment.html',amount=amount) 
    elif request.method == 'GET': 
        cur= mysql.connection.cursor() 
        cur.execute("SELECT Seats_selected from Seats WHERE Movie = %s and Theatre = %s and Date = %s",(movies,theatre,newdate)) 
        query = str(cur.fetchall()) 
        w = query[2:-4] 
        x = w.split(',), (') 
        select="" 
        for j in x: 
            z = j[1:-1] 
            select = select+z 
        selected=select.split(',') 
    return render_template('seats.html', selected=selected) 
 
#payment page 
@app.route('/payment', methods=['GET', 'POST']) 
def payment(): 
    if request.method == "POST": 
        details = request.form 
        banks = details['banks'] 
        cards = details['cards'] 
        cardno = details['cardno'] 
        expdate = details['expdate'] 
        cvvno = ''
        name = details['name_card'] 
        cur = mysql.connection.cursor() 
        cur.execute("SELECT * from User where username = %s",(usname,)) 
        query = cur.fetchone() 
        a = list(query) 
        global user_email 
        user_email = a[4] 
        global pay_otp 
        pay_otp = randint(000000, 999999) 
        cur.execute("UPDATE User__Log SET bank = %s, card_type = %s, card_number = %s,expiration_date = %s, cvv_number = %s, name_on_card = %s WHERE Login_time = %s",  
        (banks,cards,cardno,expdate,cvvno,name,now)) 
        mysql.connection.commit() 
        cur.close() 
        message = Message( 
            'Payment Verification code for TicketBox', sender='ticketbox4567@gmail.com', recipients=[user_email]) 
        message.body = "Your 6-digit OTP code is " + str(pay_otp) 
        mail.send(message) 
        return redirect("http://127.0.0.1:5000/otp") 
    return render_template('payment.html') 
 
#otp verification for payment 
@app.route('/otp', methods=['POST', 'GET']) 
def paymentverification(): 
    if request.method == "POST": 
        use_otp = request.form['payment_otp'] 
        if pay_otp == int(use_otp): 
            message = Message('Confirmation Mail',sender='ticketbox4567@gmail.com', recipients=[user_email]) 
            message.html = "<h1>Your ticket has been booked!<br> City: " + city +"<br> Theatre: " + theatre + "<br> Movie: " + movies + "<br> Timings: " + str(newdate) + "<br> Seats: " + seatslist + "</h1>" 
            mail.send(message) 
            return render_template('done.html') 
        else: 
            return "<center><h1>Your OTP is invalid<br><a href='http://127.0.0.1:5000/payment'>Back toPayment</a></h1></center>" 
    return render_template('otp.html') 
 
if __name__ == '__main__': 
    app.run(debug=True)