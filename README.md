# 🚀 Credit Card Fraud Detection API

## 📌 Overview

This project is a **machine learning-based fraud detection system** that predicts fraudulent credit card transactions using a trained Random Forest model. The model is deployed as a **FastAPI-based REST API** on **Railway**.

## 📂 Project Structure

```
CREDIT_CARD_FRAUD_DETECTION/
│-- data/                 # Raw and processed dataset (ignored in Git)
│-- logs/                 # Logs for monitoring API requests
│-- models/               # Trained ML models
│-- notebooks/            # Data exploration & feature engineering notebooks
│-- reports/              # Analysis reports
│-- src/                  # API source code
│   │-- api.py            # FastAPI application
│-- venv/                 # Virtual environment (ignored in Git)
│-- requirements.txt      # Dependencies
│-- Procfile              # Deployment command for Railway
│-- README.md             # Project documentation
```

## 📊 Dataset

The dataset used is **highly imbalanced**, containing anonymized transaction features (`V1-V28`), `Time`, `Amount`, and a `Class` label:

- `Class = 0` → Legitimate Transaction
- `Class = 1` → Fraudulent Transaction

## 🚀 Installation & Setup

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/ashkan3171/Full_Fraud_Detection.git
cd Full_Fraud_Detection
```

### **2️⃣ Create a Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

### **3️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

### **4️⃣ Run the API Locally**

```bash
uvicorn src.api:app --host 0.0.0.0 --port 8000 --reload
```

✅ The API will be available at: `http://127.0.0.1:8000/docs`

## 📡 Deployment (Railway)

### **1️⃣ Push to GitHub**

```bash
git add .
git commit -m "Deploying to Railway"
git push origin main
```

### **2️⃣ Deploy on Railway**

1. Go to **[Railway.app](https://railway.app/)** and create an account.
2. Click **New Project → Deploy from GitHub**.
3. Select your **Full_Fraud_Detection** repository.
4. Set environment variables in Railway:
   ```
   PORT = 8000
   PYTHON_VERSION = 3.9
   ```
5. Click **Deploy**.

✅ The API will be available at: `https://your-project-name.up.railway.app/docs`

## 🎯 API Endpoints

### **1️⃣ Check API Health**

```bash
GET /
```

✅ Response:

```json
{ "message": "API is running" }
```

### **2️⃣ Predict Fraud**

```bash
POST /predict
```

#### **Example Request:**

```json
{
  "V17": -3.5,
  "V14": -4.2,
  "V12": -3.8,
  "V10": -5.0,
  "V4": 2.1,
  "V11": -2.5,
  "V16": 0.5,
  "V3": 1.2,
  "V18": -1.0,
  "V9": 0.2,
  "Amount": 45.6,
  "Time": 50000
}
```

#### **Example Response:**

```json
{ "fraud_prediction": 1 }
```

(1 = Fraudulent, 0 = Legitimate)

## 🛠 Technologies Used

- **Python** (Machine Learning & API Development)
- **FastAPI** (Web Framework for API)
- **Scikit-learn** (ML Model Training)
- **Uvicorn** (ASGI Server for FastAPI)
- **Pandas & NumPy** (Data Processing)
- **Railway** (Cloud Deployment)

## 🤝 Contribution

Feel free to open issues and pull requests!

---

🚀 **Author:** Ashkan Sheikhansari  
📌 **GitHub:** [ashkan3171](https://github.com/ashkan3171)  
📡 **Deployed API:** `https://fullfrauddetection-production.up.railway.app`
