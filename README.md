# ☁️ Cloud-based Real-time DGA Detection Engine  

This project provides a **Flask-based web API** for detecting **Domain Generation Algorithm (DGA)** domains in real time using a pre-trained **LSTM model**. The engine classifies incoming domains as either **DGA (malicious/suspicious)** or **Non-DGA (benign)** and can be deployed as a lightweight cloud service.  

---

## 🚀 Features
- LSTM-based sequence model trained to detect DGA vs benign domains  
- Flask REST API for real-time predictions  
- Simple `/` route for health check  
- `/dgaCheck?domain=<your_domain>` endpoint for DGA detection  
- Returns a clear JSON response with classification result  

---


