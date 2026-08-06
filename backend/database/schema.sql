
-- Agriculture Yield and Crop Recommendation System
-- Database Backup File
-- Purpose:
-- This file contains the database schema
-- for recreating the project database.
-- Database Name: agriculture_db

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    phone_number VARCHAR(15) UNIQUE,
    email VARCHAR(100) UNIQUE,
    state VARCHAR(100),
    district VARCHAR(100),
    land_acres FLOAT,
    land_type VARCHAR(50),
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE predictions (
    prediction_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,

    soil_type VARCHAR(50),
    location VARCHAR(100),
    state VARCHAR(100),
    district VARCHAR(100),

    season VARCHAR(50),
    crop_input VARCHAR(100),

    temperature FLOAT,
    rainfall FLOAT,
    humidity FLOAT,

    land_acres FLOAT,
    land_type VARCHAR(50),

    recommended_crop VARCHAR(100),
    predicted_yield FLOAT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(user_id)
);