# flask-auth-app
This is a login and registeration application using flask running on docker storing credentials in the mysql database running the docker
# folders structure
flask-auth-app/
│── app.py                 # Main Flask application
│── Dockerfile             # Docker configuration
│── docker-compose.yml     # Docker Compose configuration
│── requirements.txt       # Python dependencies
│── .env                   # Environment variables (for database credentials)
│
├── static/                # Static files (CSS, images, etc.)
│   ├── style.css          # CSS for styling the app
│
├── templates/             # HTML templates
│   ├── register.html      # Registration page
│   ├── login.html         # Login page
│   ├── home.html          # Home/Dashboard after login
