from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os

app = Flask(__name__)

# 🔹 Load environment variables
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'mysecretkey')
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST', 'localhost')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER', 'root')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD', 'password')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB', 'flask_auth')

# 🔹 Initialize MySQL & Bcrypt
mysql = MySQL(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"

# 🔹 User Model for Flask-Login
class User(UserMixin):
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

# 🔹 Create users table
def create_users_table():
    with app.app_context():
        try:
            cur = mysql.connection.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    email VARCHAR(100) UNIQUE NOT NULL,
                    password VARCHAR(255) NOT NULL
                )
            """)
            mysql.connection.commit()
            cur.close()
            print("✅ Users table created successfully!")
        except Exception as e:
            print(f"❌ Error creating table: {e}")

# 🔹 Load user for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, name, email FROM users WHERE id = %s", (user_id,))
    user_data = cur.fetchone()
    cur.close()
    
    if user_data:
        return User(id=user_data[0], name=user_data[1], email=user_data[2])
    return None

# 🔹 Route: Home
@app.route('/')
def home():
    return render_template("index.html")

# 🔹 Route: Register User
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        cur = mysql.connection.cursor()
        try:
            cur.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", 
                        (name, email, hashed_password))
            mysql.connection.commit()
            flash("✅ Registration successful! Please log in.", "success")
            return redirect(url_for('login'))
        except Exception as e:
            flash(f"❌ Error: {e}", "danger")
        finally:
            cur.close()

    return render_template("register.html")

# 🔹 Route: Login User
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("SELECT id, name, email, password FROM users WHERE email = %s", (email,))
        user_data = cur.fetchone()
        cur.close()

        if user_data and bcrypt.check_password_hash(user_data[3], password):
            user = User(id=user_data[0], name=user_data[1], email=user_data[2])
            login_user(user)
            flash("✅ Login successful!", "success")
            return redirect(url_for('dashboard'))
        else:
            flash("❌ Invalid email or password!", "danger")

    return render_template("login.html")

# 🔹 Route: Dashboard (Protected)
@app.route('/dashboard')
@login_required
def dashboard():
    return f"Welcome {current_user.name}! This is your dashboard."

# 🔹 Route: Logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("✅ Logged out successfully!", "info")
    return redirect(url_for('login'))

# 🔹 Run Flask App
if __name__ == '__main__':
    with app.app_context():
        create_users_table()
    app.run(host='0.0.0.0', port=5000, debug=True)

