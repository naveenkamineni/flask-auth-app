# Flask Authentication App ((Registeration--> flask --> MySQL)-(Login--> flask <--> MySQL)-Docker + AWS EC2)

## 🚀 Overview
This is a **User Registration & Login** application built with **Flask**, running inside a **Docker container**, and storing user credentials in a **MySQL database**. The entire setup is deployed on an **AWS EC2 instance**.

---

## 🔹 Features
✅ **User Registration & Login**  
✅ **Flask-based Web Application**  
✅ **MySQL Database for Credential Storage**  
✅ **Dockerized for Easy Deployment**  
✅ **Hosted on AWS EC2**  

---

## 🛠️ Prerequisites
Before you begin, ensure you have the following:

- **AWS EC2 instance** (Amazon Linux recommended)
- **Docker installed on EC2**
- **Security Group allowing inbound traffic on ports 5000 & 3306**

---

## 🔹 Step 1: Install Docker on AWS EC2

Run the following commands to install Docker:
```bash
sudo yum update -y
sudo yum install docker -y
sudo service docker start
sudo usermod -aG docker ec2-user
```

✅ **Verify Docker installation:**
```bash
docker ps
```

---

## 🔹 Step 2: Clone the Flask Authentication App Repository

```bash
git clone https://github.com/naveenkamineni/flask-auth-app.git
cd flask-auth-app
```

---

## 🔹 Step 3: Set Up MySQL Database in Docker

Pull and run MySQL as a Docker container:
```bash
docker run -itd --name mysql-db -p 3306:3306 \
-e MYSQL_ROOT_PASSWORD=rootpassword \
-e MYSQL_DATABASE=flask_auth \
-e MYSQL_USER=flaskuser \
-e MYSQL_PASSWORD=flaskpass \
mysql:latest
```

✅ **Check if MySQL is running:**
```bash
docker ps
```

---

## 🔹 Step 4: Build and Run the Flask App

1️⃣ **Build the Docker Image**
```bash
docker build --no-cache -t flask-auth .
```

2️⃣ **Run the Flask Container and Link to MySQL**
```bash
docker run -itd --name flask-auth-app -p 5000:5000 --link mysql-db:mysql flask-auth
```

---

## 🔹 Step 5: Access the Flask App in Browser
Once the container is running, open your browser and go to:

🌍 `http://{EC2-PUBLIC-IP}:5000/`

💡 If you face issues:
- **Ensure the Flask container is running** (`docker ps`)
- **Check container logs** (`docker logs flask-auth-app`)
- **Verify security group settings** (ports 5000 & 3306 must be open)

---

## 🎯 Expected UI
Once the setup is successful, you should see the following UI:

![Flask Auth App](https://github.com/user-attachments/assets/656b3064-410c-4cec-afe3-288d98ea3563)

---

## ✅ Troubleshooting
If you cannot access the UI:
1. Ensure the container is running:
   ```bash
   docker ps
   ```
2. If the container is not running, check logs:
   ```bash
   docker logs flask-auth-app
   ```
3. Restart the Flask application if needed:
   ```bash
   docker restart flask-auth-app
   ```
4. Make sure the **EC2 security group** allows traffic on **port 5000**.

---

## 🎉 Conclusion
You have successfully deployed the **Flask Authentication App** on an AWS EC2 instance using Docker! 🚀

🔹 **Fully containerized setup**  
🔹 **Secure user authentication**  
🔹 **Scalable deployment**  

Happy Coding! 🎯


