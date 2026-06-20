# 😴 Drowsiness Detection System

An AI-powered real-time drowsiness detection system built using Python, OpenCV, and MediaPipe. The system monitors eye movements through a webcam and detects signs of drowsiness by calculating the Eye Aspect Ratio (EAR). When the eyes remain closed for a predefined duration, an alert is generated to help improve safety and awareness.

## 🚀 Features

* Real-time face detection
* Eye landmark tracking
* Eye Aspect Ratio (EAR) calculation
* Drowsiness alert detection
* Webcam-based monitoring
* Lightweight and easy-to-use implementation

## 🛠️ Technologies Used

* Python
* OpenCV
* MediaPipe
* NumPy

## 📂 Project Structure

```text
Drowsiness-Detection-System/
│
├── drowsinessDetection.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/sakshikaushal09/Drowsiness-Detection-System.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Project

```bash
python drowsinessDetection.py
```

## 🔍 How It Works

1. Captures live video from the webcam.
2. Detects facial landmarks using MediaPipe.
3. Extracts eye landmark coordinates.
4. Calculates the Eye Aspect Ratio (EAR).
5. Monitors eye closure duration.
6. Generates an alert when signs of drowsiness are detected.

## 🎯 Future Enhancements

* Alarm Sound Notification
* Yawning Detection
* Driver Monitoring Dashboard
* SMS/Email Alerts
* Deep Learning-Based Detection
* Mobile Application Support

## 📚 Learning Outcomes

* Computer Vision Fundamentals
* Real-Time Video Processing
* Facial Landmark Detection
* OpenCV Integration
* MediaPipe Face Mesh
* AI-Based Monitoring Systems

## 👩‍💻 Author

**Sakshi Kaushal**

GitHub: sakshikaushal09

---

⭐ If you found this project useful, consider giving it a star.
