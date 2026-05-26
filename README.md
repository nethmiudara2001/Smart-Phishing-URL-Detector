# 🛡️ Smart Phishing URL Detector

Welcome to the Smart Phishing URL Detector — a lightweight, full-stack Python web application designed to analyze web addresses for common phishing indicators and heuristics. Built with Flask, Python, HTML, and CSS, this project is ideal for learners, network administrators, and anyone curious about lightweight cyber security tools in web development.

## ✨ Features

- 🔍 Analyze any URL instantly through a clean web interface.
- 📊 Dynamic risk scoring based on structural safety checks.
- 🛠️ Full breakdown of flagged security reasons provided on screen.
- 🐍 Flask-powered backend architecture with local request routing.
- 🧮 Simple rule-based logic — perfect for learning cyber defense patterns.

<img width="1093" height="590" alt="image" src="https://github.com/user-attachments/assets/707cbb58-4a0e-4080-adeb-1d0ef0b17b61" />


## 🛠️ How It Works

### 🔑 Analysis Process

1. Enter any suspicious URL string into the search input box.
2. The URL layout is read and broken down using Python parsing scripts.
3. The string is evaluated character-by-character against structural heuristic indicators.
4. The calculated risk indicators are added together to build a final score.

> 💡 This basic heuristic engine uses structural rules like HTTPS verification and character checks but is best used for educational baseline testing.

<img width="1095" height="835" alt="image" src="https://github.com/user-attachments/assets/4ca0677d-ae2a-43cb-b662-1b4584775c19" />
<img width="1093" height="837" alt="image" src="https://github.com/user-attachments/assets/f3f3a00e-5756-43f7-8b98-f220540fa386" />



### 📊 Evaluation Process

1. If the URL scores low, it is classified and rendered as Safe.
2. If the URL scores medium, it is classified and rendered as Suspicious.
3. If the URL scores high, it is classified and rendered as Dangerous.

---

## 🚀 Getting Started

### 🧩 Prerequisites

- Python 3.x installed on your computer.
- Flask framework dependency package.

### 🛠️ Setup Instructions

```bash
git clone [https://github.com/nethmiudara2001/Smart-Phishing-URL-Detector.git](https://github.com/nethmiudara2001/Smart-Phishing-URL-Detector.git)
cd Smart-Phishing-URL-Detector
pip install flask
python app.py
