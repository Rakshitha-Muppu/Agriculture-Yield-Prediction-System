from flask import Blueprint, request, jsonify
import pickle

from services.prediction_service import (
    create_prediction,
    get_user_predictions
)

# ==========================
# LOAD MODEL
# ==========================

with open("../ml-model/crop_model.pkl", "rb") as file:
    crop_model = pickle.load(file)

with open("../ml-model/crop_label_encoder.pkl", "rb") as file:
    crop_encoder = pickle.load(file)

# ==========================
# LOAD ENCODERS
# ==========================

with open("../ml-model/state_encoder.pkl", "rb") as file:
    state_encoder = pickle.load(file)

with open("../ml-model/district_encoder.pkl", "rb") as file:
    district_encoder = pickle.load(file)

with open("../ml-model/soil_encoder.pkl", "rb") as file:
    soil_encoder = pickle.load(file)

with open("../ml-model/season_encoder.pkl", "rb") as file:
    season_encoder = pickle.load(file)

with open("../ml-model/previous_crop_encoder.pkl", "rb") as file:
    previous_crop_encoder = pickle.load(file)

# ==========================
# BLUEPRINT
# ==========================

predict_bp = Blueprint("predict", __name__)

# PREDICT
@predict_bp.route("/predict", methods=["POST"])
def predict():
    print("******** PREDICT API HIT ********")
    data = request.get_json()

    print("\n========== REQUEST RECEIVED ==========")
    print("State:", data["state"])
    print("District:", data["district"])
    print("Soil Type:", data["soil_type"])
    print("Season:", data["season"])
    print("Previous Crop:", data["crop_input"])
    print("Temperature:", data["temperature"])
    print("Humidity:", data["humidity"])
    print("Rainfall:", data["rainfall"])

    try:
        state = state_encoder.transform([data["state"]])[0]
        district = district_encoder.transform([data["district"]])[0]
        soil = soil_encoder.transform([data["soil_type"]])[0]
        season = season_encoder.transform([data["season"]])[0]
        previous_crop = previous_crop_encoder.transform([data["crop_input"]])[0]

    except ValueError as e:
        print("\n========== ENCODER ERROR ==========")
        print(e)

        return jsonify({
            "message": str(e)
        }), 400

    crop_features = [[
        state,
        district,
        soil,
        season,
        float(data["temperature"]),
        float(data["humidity"]),
        float(data["rainfall"]),
        previous_crop
    ]]

    prediction = crop_model.predict(crop_features)[0]

    recommended_crop = crop_encoder.inverse_transform([prediction])[0]

    create_prediction(
        data["user_id"],
        data["soil_type"],
        data["location"],
        data["state"],
        data["district"],
        data["season"],
        data["crop_input"],
        data["temperature"],
        data["rainfall"],
        data["humidity"],
        data["land_acres"],
        recommended_crop
    )

    return jsonify({
        "recommended_crop": recommended_crop
    })
# HISTORY
@predict_bp.route("/history/<int:user_id>", methods=["GET"])
def history(user_id):

    predictions = get_user_predictions(user_id)

    for prediction in predictions:
        prediction["created_at"] = prediction["created_at"].strftime("%d/%m/%Y")

    return jsonify(predictions)

# LATEST PREDICTION
@predict_bp.route("/latest_prediction/<int:user_id>", methods=["GET"])
def latest_prediction(user_id):

    predictions = get_user_predictions(user_id)

    if len(predictions) == 0:
        return jsonify({})

    prediction = predictions[0]

    prediction["created_at"] = prediction["created_at"].strftime("%d/%m/%Y")

    return jsonify(prediction)