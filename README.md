# 🩺 AI Dermatologist: Skin Cancer Detection System

> **A full-stack, AI-powered healthcare platform bridging the gap between immediate skin lesion screening and professional clinical care.** > *Developed for the CSI Project Expo by Team 27.*

![Accuracy](https://img.shields.io/badge/Accuracy-97%25-success?style=for-the-badge)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Google Colab](https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![TypeScript](https://img.shields.io/badge/TypeScript-00273F?style=for-the-badge&logo=typescript&logoColor=white)
![Vite](https://img.shields.io/badge/Vite-B73BFE?style=for-the-badge&logo=vite&logoColor=FFD62E)
![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)

---

## 📖 Table of Contents
- [About the Project](#-about-the-project)
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [Getting Started (Local Setup)](#-getting-started)

---

## 💡 About the Project

Skin cancer is the most common cancer globally, but when detected early, the 5-year survival rate for melanoma is a staggering 99%. Unfortunately, wait times for specialists can stretch for months, and generic internet searches only cause unnecessary panic.

**AI Dermatologist** is an accessible, AI-powered preliminary screening platform. We didn't just build a basic scanner; our custom Convolutional Neural Network (CNN) is trained on over **3,000 verified clinical patient images**, achieving an impressive **97% accuracy** in predicting whether a lesion is benign or malignant. Rather than leaving users stranded with a scary result, our platform seamlessly connects them to real medical professionals by generating secure clinical reports and instantly locating nearby hospitals.

---

## ✨ Key Features

- **🤖 AI Image Analysis:** Upload a photo of a skin lesion for instant, clinical-grade classification (Benign/Malignant) powered by our custom TensorFlow model, boasting a **97% detection accuracy**.
- **🗺️ Interactive Body Mapping:** Users can visually pinpoint the exact location of the mole on a body map to build a personalized risk profile.
- **📄 Secure PDF Reports:** Automatically generates downloadable, professional medical reports containing AI confidence metrics and patient history.
- **🔐 Hospital Portal & Secure Share Code:** Each scan generates a unique 6-digit code. Doctors can log into the dedicated Hospital Portal, enter this code, and instantly import the patient's AI report and details before the consultation even begins.
- **🏥 Real-Time Clinical Connection:** Integrated Leaflet maps utilize the Overpass API to instantly locate dermatologists and clinics within a 5-kilometer radius.

---

## 🛠️ Tech Stack

### Frontend & UI
* **React.js & TypeScript:** Core UI framework.
* **Vite:** Lightning-fast frontend build tool.
* **Tailwind CSS & shadcn/ui:** Responsive, modern styling.
* **Framer Motion:** Smooth UI animations.

### Backend & APIs
* **Python & Flask:** Lightweight, high-performance RESTful API.
* **Flask-CORS:** Secure cross-origin communication.
* **Overpass API:** Real-time geographic data for mapping hospitals.

### Machine Learning
* **TensorFlow & Keras:** Custom CNN architecture for image classification.
* **NumPy & Pillow (PIL):** Image processing and matrix transformations.
* **Google Colab:** Cloud GPU training environment used for the 3,000+ images.

### Integrations & Deployment
* **Leaflet.js:** Interactive geographic mapping.
* **jsPDF:** Secure, client-side report generation.
* **Web Storage API:** Local patient database simulation.
* **Vercel:** Serverless frontend hosting.

---

## 🚀 Getting Started

Follow these instructions to run the full-stack application on your local machine. You will need two terminal windows running simultaneously.

### Prerequisites
- Node.js installed
- Python 3.8+ installed

### 1. Clone the Repository
```bash
git clone [https://github.com/CSI-Project-Expo/Team-27-.git](https://github.com/CSI-Project-Expo/Team-27-.git)

### 2. Start the Python AI Backend
Open your first terminal and navigate to the backend directory.

Bash
cd backend

# Install required Python packages
pip install -r requirements.txt

# Run the Flask server
python app.py

### 3. Start the React Frontend
Open a new, second terminal window and navigate to the frontend directory.

Bash
cd frontend

# Install dependencies
npm install

# Start the development server
npm run dev
