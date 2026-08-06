# 🌾 KrishiAI - AI Powered Crop Recommendation System

## 📌 Project Overview

KrishiAI is a Machine Learning-based Crop Recommendation System that helps farmers identify the most suitable crop based on location, soil type, season, previous crop, and current weather conditions.

The system combines real-time weather information with a trained Random Forest Machine Learning model to generate accurate crop recommendations. User information and prediction history are securely stored in a MySQL database for future reference.

---

# Problem Statement

Choosing the right crop is one of the biggest challenges faced by farmers. Crop selection depends on several environmental and agricultural factors such as:

- Location
- Soil Type
- Season
- Previous Crop
- Temperature
- Humidity
- Rainfall

Selecting an unsuitable crop can reduce productivity and increase financial loss.

---

# 💡 Proposed Solution

KrishiAI recommends the most suitable crop by combining:

- Location (State & District)
- Soil Type
- Season
- Previous Crop
- Weather Conditions

The system automatically fetches real-time weather data and predicts the best crop using a trained Random Forest Machine Learning model.

---

# 🏗 System Architecture

```text
User
   │
   ▼
Frontend (HTML, CSS, JavaScript)
   │
   ▼
Flask REST API
   │
   ▼
Machine Learning Model (Random Forest)
   │
   ▼
MySQL Database
   │
   ▼
Prediction History
```

---

# ✨ Features

- 👤 User Registration & Login
- 📍 Automatic Location Detection
- 🌦 Live Weather Data Integration
- 🌱 AI-Based Crop Recommendation
- 🧠 Random Forest Prediction Model
- 📜 Prediction History
- 💾 MySQL Database Storage
- 🎨 Responsive User Interface

---

# 📝 User Inputs

The system collects the following inputs:

- State
- District
- Soil Type
- Season
- Previous Crop
- Temperature *(Auto-filled)*
- Humidity *(Auto-filled)*
- Rainfall *(Auto-filled)*
- Land Area

---

# 📤 Output

The system predicts:

- 🌾 Recommended Crop

The prediction is also stored in the database for future reference.

---

# 🤖 Machine Learning Model

### Algorithm Used

- Random Forest Classifier

### Dataset Features

- State
- District
- Soil Type
- Season
- Temperature
- Humidity
- Rainfall
- Previous Crop

### Target

- Recommended Crop

### Model Accuracy

**76.30%**

---

# 🛠 Technologies Used

## Frontend

- HTML5
- CSS3
- JavaScript

## Backend

- Python
- Flask

## Machine Learning

- Scikit-learn
- Pandas
- NumPy
- Pickle

## Database

- MySQL

## APIs

- Open-Meteo Weather API
- Open-Meteo Geocoding API

---

# 🔄 Workflow

1. User logs into the system.
2. User enters agricultural details.
3. Weather information is fetched automatically based on the selected location.
4. The backend prepares the input data for the Machine Learning model.
5. The Random Forest model predicts the most suitable crop.
6. The recommended crop is displayed to the user.
7. Prediction history is stored in the MySQL database.

---

# 📂 Dataset

The model is trained using an Indian Crop Recommendation Dataset containing records from multiple Indian states and districts.

### Dataset Columns

- State
- District
- Soil_Type
- Season
- Temperature
- Humidity
- Rainfall
- Previous_Crop
- Recommended_Crop

---

# 📈 Future Enhancements

- Fertilizer Recommendation System
- Crop Disease Detection using Deep Learning
- Mobile Application
- Multi-language Support
- Market Price Prediction
- Integration with IoT-Based Soil Sensors