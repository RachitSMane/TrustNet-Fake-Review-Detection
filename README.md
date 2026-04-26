# FakeReviewDetection-CIE_Ignite
# 🚀 TrustNet – Fake Review Detection System

TrustNet is an AI-powered system designed to detect fake, suspicious, and genuine reviews.  
It helps businesses and users identify fraudulent content and build trust in online platforms.

---

## 📌 Features

- 🔍 Classifies reviews as **Fake, Suspicious, or Genuine**
- 📊 Provides **ML-based probability score**
- 📉 Displays **confidence score**
- 🧠 Explains **why a review is flagged** (emotional tone, duplicates, etc.)
- 📈 Includes a **Fraud Analytics Dashboard**
- 🔐 User authentication system (login/register)
- 💰 SaaS-style **pricing model UI**
- ⚡ Real-time review analysis

---

## 🖥️ Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python (Flask / FastAPI)  
- **Machine Learning:** Scikit-learn / NLP models  
- **Data Handling:** JSON / Custom dataset  
- **Visualization:** Streamlit charts  

---

## 📁 Project Structure

```
TrustNet-Fake-Review-Detection/
│
├── app.py              # Streamlit frontend
├── api.py              # Backend API server
├── model.py            # ML model logic
├── auth.py             # Authentication system
├── utils.py            # Helper functions
├── users.json          # User database
│
├── data/               # Dataset (if any)
├── model/              # Saved ML models
├── testing/            # Testing scripts
│
├── README.md           # Project documentation
└── walkthrough.md      # Project walkthrough
```

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
git clone https://github.com/your-username/TrustNet-Fake-Review-Detection.git

cd TrustNet-Fake-Review-Detection

---

### 2️⃣ Install dependencies
pip install -r requirements.txt


*(If requirements.txt is not available, install manually:)*


pip install streamlit requests scikit-learn pandas numpy

---

### 3️⃣ Run the Backend API
python api.py


OR (if using FastAPI):


uvicorn api:app --reload


👉 Backend should run on:

http://127.0.0.1:8000


---

### 4️⃣ Run the Frontend (Streamlit)


streamlit run app.py


👉 Open in browser:

http://localhost:8501


---

## 🚀 How It Works

1. User enters a review and rating  
2. Frontend sends data to backend API  
3. ML model analyzes:
   - Sentiment
   - Language patterns
   - Duplicate detection  
4. System returns:
   - Classification (Fake / Suspicious / Genuine)
   - Score
   - Probability
   - Explanation  

---

## 📊 Dashboard

The system includes an analytics dashboard showing:
- Total reviews analyzed  
- Fake reviews detected  
- Fraud rate  
- Distribution of review types  

---

## 💡 Use Cases

- 🛒 E-commerce platforms  
- 🏨 Review-based services (hotels, food apps)  
- 📱 Marketplaces  
- 📊 Business analytics teams  

---

## 📈 Future Improvements

- 🔗 Integration with live e-commerce platforms  
- 🤖 Advanced deep learning models (BERT, LLMs)  
- 📡 Real-time API deployment  
- 🧾 Review history tracking  
- 📊 More detailed analytics  

---

## 👥 Team

- Rachit S Mane 
- Ramneek.G 
- Prithvi.W
- Pranav.v.Mennon
- Akash.R
- P.chinni krishna Reddy
---

##  Acknowledgements

Developed as part of the **CIE Ignite Program**, focusing on solving real-world problems using AI and entrepreneurship principles.

---

## 📜 License

This project is for academic and demonstration purposes.