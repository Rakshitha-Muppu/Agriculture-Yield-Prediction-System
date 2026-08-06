import pandas as pd
import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# LOAD DATASET

df = pd.read_csv("../dataset/indian_crop_recommendation.csv")

# ENCODE INPUT COLUMNS

state_encoder = LabelEncoder()
district_encoder = LabelEncoder()
soil_encoder = LabelEncoder()
season_encoder = LabelEncoder()
previous_crop_encoder = LabelEncoder()

df["State"] = state_encoder.fit_transform(df["State"])
df["District"] = district_encoder.fit_transform(df["District"])
df["Soil_Type"] = soil_encoder.fit_transform(df["Soil_Type"])
df["Season"] = season_encoder.fit_transform(df["Season"])
df["Previous_Crop"] = previous_crop_encoder.fit_transform(df["Previous_Crop"])

# ENCODE OUTPUT COLUMN

crop_encoder = LabelEncoder()

df["Recommended_Crop"] = crop_encoder.fit_transform(
    df["Recommended_Crop"]
)

# FEATURES

X = df[
    [
        "State",
        "District",
        "Soil_Type",
        "Season",
        "Temperature",
        "Humidity",
        "Rainfall",
        "Previous_Crop"
    ]
]

y = df["Recommended_Crop"]

# TRAIN TEST SPLIT

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# TRAIN MODEL
model = RandomForestClassifier(
    n_estimators=300,
    random_state=42
)

model.fit(X_train, y_train)

# TEST MODEL

pred = model.predict(X_test)

accuracy = accuracy_score(y_test, pred)

print(f"\nAccuracy : {accuracy * 100:.2f}%")

# SAVE MODEL

with open("../ml-model/crop_model.pkl", "wb") as file:
    pickle.dump(model, file)

# Save output label encoder

with open("../ml-model/crop_label_encoder.pkl", "wb") as file:
    pickle.dump(crop_encoder, file)

# Save input encoders

with open("../ml-model/state_encoder.pkl", "wb") as file:
    pickle.dump(state_encoder, file)

with open("../ml-model/district_encoder.pkl", "wb") as file:
    pickle.dump(district_encoder, file)

with open("../ml-model/soil_encoder.pkl", "wb") as file:
    pickle.dump(soil_encoder, file)

with open("../ml-model/season_encoder.pkl", "wb") as file:
    pickle.dump(season_encoder, file)

with open("../ml-model/previous_crop_encoder.pkl", "wb") as file:
    pickle.dump(previous_crop_encoder, file)

print("\nModel Saved Successfully.")