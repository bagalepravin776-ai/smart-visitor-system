# 🚀 Smart Visitor System using AWS

A fully serverless visitor management application built on AWS cloud services. The system allows visitors to register through a web interface hosted on Amazon S3, processes requests using AWS Lambda, stores data in DynamoDB, and sends notifications using Amazon SNS.

---

# 📌 Project Overview

The Smart Visitor System is designed to automate visitor registration and notification workflows using a serverless architecture.

Visitors enter their details through a web application. The information is securely processed and stored in the cloud without managing any servers.

---

# 🏗️ Architecture

<img width="1536" height="1024" alt="architecture-diagram png" src="https://github.com/user-attachments/assets/d1daec3a-d5b5-4996-9dab-ead7a52998fc" />


### Architecture Flow

```text
Visitor
   │
   ▼
visitor2512.html (Amazon S3)
   │
   ▼
Amazon API Gateway
   │
   ▼
AWS Lambda
   │
   ├── Amazon DynamoDB
   │
   └── Amazon SNS
```

---

# ☁️ AWS Services Used

| Service            | Purpose                       |
| ------------------ | ----------------------------- |
| Amazon S3          | Static website hosting        |
| Amazon API Gateway | REST API endpoint             |
| AWS Lambda         | Serverless backend processing |
| Amazon DynamoDB    | Visitor data storage          |
| Amazon SNS         | Email notifications           |

---

# 📂 Project Structure

```text
smart-visitor-system/
│
├── README.md
├── architecture-diagram.png
│
├── website/
│   └── visitor2512.html
│
├── lambda-code/
│   └── lambda_function.py
│
├── screenshots/
│   ├── website-homepage.png
│   ├── s3-static-hosting.png
│   ├── api-gateway.png
│   ├── lambda-function.png
│   ├── dynamodb-table.png
│   ├── sns-topic.png
│
```

---

# ⚙️ Working Process

### Step 1

User opens the website hosted on Amazon S3.

### Step 2

User enters visitor information and submits the form.

### Step 3

Amazon API Gateway receives the request.

### Step 4

AWS Lambda processes the request.

### Step 5

Visitor details are stored in Amazon DynamoDB.

### Step 6

Amazon SNS sends an email notification.

### Step 7

Success response is displayed to the user.

---

# 🖥️ Screenshots

## Website Homepage

<img width="1366" height="680" alt="01_website-homepage" src="https://github.com/user-attachments/assets/9d107130-5dee-43ea-9764-f9482a4f44bc" />

---

## S3 Static Website Hosting

<img width="1343" height="637" alt="02_s3-static-hosting" src="https://github.com/user-attachments/assets/a169f9a2-1009-48f9-a3e1-84fc3f497424" />


---

## API Gateway

<img width="1346" height="526" alt="03_api-gateway" src="https://github.com/user-attachments/assets/67ffcdab-d78d-4d46-8ac5-0ecdac328017" />

---

## AWS Lambda Function

<img width="1358" height="487" alt="04_lambda-function" src="https://github.com/user-attachments/assets/f701dee8-96e7-44ab-b1ed-00e16f585d9d" />

---

## DynamoDB Table

<img width="1351" height="607" alt="dynamodb-table" src="https://github.com/user-attachments/assets/e5864078-cd0b-4893-b9a2-b0e9ece899f6" />


---

## SNS Topic

<img width="1349" height="600" alt="sns-topic" src="https://github.com/user-attachments/assets/24344747-fcff-4043-bf01-d4e25293b727" />


---

# ✨ Features

* Serverless Architecture
* Static Website Hosting
* Visitor Registration System
* REST API Integration
* Secure Data Storage
* Email Notifications
* Scalable Design
* Cost-Effective Solution
* Easy Deployment

---

# 🎯 Key Benefits

* No Server Management
* Automatic Scaling
* Highly Available
* Secure AWS Infrastructure
* Fast Response Time
* Low Operational Cost

---

# 📚 Learning Outcomes

Through this project I learned:

* Amazon S3 Static Website Hosting
* API Gateway Integration
* AWS Lambda Functions
* DynamoDB Operations
* SNS Notifications
* IAM Roles and Permissions
* Serverless Application Development

---

# 🔮 Future Enhancements

* Visitor Photo Upload
* Admin Dashboard
* Authentication System
* QR Code Based Entry
* CloudWatch Monitoring
* Visitor Analytics Dashboard

---

# 👨‍💻 Author

**Pravin Bagale**

AWS Cloud & DevOps Enthusiast

---

⭐ If you found this project useful, don't forget to star the repository.
