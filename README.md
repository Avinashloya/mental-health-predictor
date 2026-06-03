# 🧠 College Mental Health Predictor

> AI-powered mental health risk analysis for college students using Random Forest machine learning models.

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.1-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.6-F7931E?logo=scikitlearn&logoColor=white)](https://scikit-learn.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📌 Project Overview

This project predicts college students' **mental health risk levels** based on daily activity patterns, sleep habits, social behavior, and physiological data. Originally developed as a Jupyter Notebook, it has been converted into a **production-ready Flask web application** and deployed online.

The application uses two **Random Forest** models:
- **Regressor** — predicts the numeric **stress level** (0–100)
- **Classifier** — classifies **mental health risk** (Low / Moderate / High)

Additionally, **anxiety** and **depression** proxy scores are derived from the predicted stress level.

---

## ✨ Features

- 🔮 **Real-time predictions** — enter your metrics and get instant results
- 📊 **Interactive visualization** — Chart.js bar chart showing stress, anxiety, and depression scores
- 🏷️ **Risk classification** — color-coded badges (Low / Moderate / High)
- 💡 **Personalized insights** — possible causes and recommended actions based on your inputs
- 🌙 **Premium dark UI** — modern glassmorphism design with smooth animations
- 📱 **Fully responsive** — works on desktop, tablet, and mobile

---

## 🛠️ Technologies Used

| Category | Technology |
|----------|-----------|
| Backend | Python, Flask |
| ML Models | scikit-learn (Random Forest) |
| Data Processing | Pandas, NumPy |
| Frontend | HTML5, CSS3, JavaScript |
| Visualization | Chart.js |
| Deployment | Gunicorn, Render |
| Version Control | Git, GitHub |

---

## 📦 Installation

### Prerequisites
- Python 3.10+ installed
- pip package manager

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/mental-health-predictor.git
cd mental-health-predictor

# 2. Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py
```

Open your browser and visit: **http://127.0.0.1:5000**

---

## 📊 Dataset Information

| Property | Value |
|----------|-------|
| File | `data/college_mental_health.csv` |
| Rows | 1001 |
| Features | 10 input features + 2 targets |

### Input Features

| Feature | Description | Range |
|---------|------------|-------|
| Daily_Activity_Pattern | Overall daily activity level | 1–10 |
| Study_Hours | Average study hours per day | 0–24 |
| Sleep_Schedules | Average sleep hours per night | 0–24 |
| Class_Attendance | Percentage of classes attended | 0–100 |
| Heart_Rate | Resting heart rate (bpm) | 40–200 |
| Sleep_Quality | Self-rated sleep quality | 1–10 |
| Step_Count | Average daily steps | 0+ |
| Messaging_Frequency | Messages sent per day | 0+ |
| Social_Media_Activity | Social media usage level | 0–10 |
| Club_Event_Participation | Club events per month | 0+ |

### Target Variables

- **Stress_Levels** — continuous (0–100)
- **Mental_Health_Risk** — categorical (Low / Moderate / High)

---

## 🤖 Model Details

| Model | Algorithm | Estimators | Task |
|-------|-----------|-----------|------|
| Stress Predictor | Random Forest Regressor | 200 | Regression |
| Risk Classifier | Random Forest Classifier | 200 | Classification |

Both models are trained on application startup using an 80/20 train-test split with a fixed random seed (42) for reproducibility.

---

## 🚀 Deployment (Render)

### Build Command
```bash
pip install -r requirements.txt
```

### Start Command
```bash
gunicorn app:app
```

### Steps
1. Push the repo to GitHub
2. Sign in to [Render](https://render.com)
3. Click **New → Web Service**
4. Connect your GitHub repository
5. Set the build and start commands above
6. Click **Deploy**

Render will automatically redeploy whenever you push to `main`.

---

## 🔗 Links

- **Live Demo**: [https://mental-health-predictor.onrender.com](https://mental-health-predictor.onrender.com) *(update after deployment)*
- **GitHub**: [https://github.com/YOUR_USERNAME/mental-health-predictor](https://github.com/YOUR_USERNAME/mental-health-predictor)

---

## 🔮 Future Enhancements

- [ ] Save pre-trained models as `.pkl` files for faster startup
- [ ] Add user authentication and history tracking
- [ ] Integrate more ML models (XGBoost, SVM) for comparison
- [ ] Add trend analysis over time
- [ ] Implement PDF report generation
- [ ] Add multi-language support
- [ ] Connect to campus counseling resources API

---

## 📄 Research References

- *Multi-Risk Mental Health Prediction of Students using Machine Learning*
- *Student Mental Health Risk Classification: A Machine Learning Approach using Random Forest*

---

## ⚠️ Disclaimer

This tool is for **educational and informational purposes only**. It is **not** a substitute for professional medical advice, diagnosis, or treatment. If you are experiencing mental health difficulties, please contact a qualified mental health professional or your campus counseling center.

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

<p align="center">Built with 🧠 Machine Learning & ❤️ Flask</p>
