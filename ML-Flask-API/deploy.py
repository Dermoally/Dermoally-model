from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
from PIL import Image
import os
from datetime import datetime
from functools import wraps
import random

app = Flask(__name__)

# Load the trained model (adjust the path as needed)
model = tf.keras.models.load_model('dermoally-modelv6.h5', compile=False)

# Labels should match those used in your training
labels = ['Acne', 'ActinicKeratosis', 'Blackheads', 'Herpes', 'Keloid', 'KeratosisSeborrheic', 'Milia', 'Pityriasis versicolor', 'Ringworm']

def authenticate_user(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Dummy user ID for testing
        request.id_user = 1
        return f(*args, **kwargs)

    return decorated_function

@app.route('/')
def home():
    message = "Welcome to our image classification API. Please register and login to access the endpoints."
    return jsonify(message)

@app.route('/predict', methods=['POST'])
@authenticate_user
def predict():
    user_id = request.id_user
    predictions = []

    file_key = 'file'

    if file_key not in request.files:
        return jsonify({'error': f'No {file_key} provided'}), 400

    file = request.files[file_key]
    image = Image.open(file)

    if image.mode != 'RGB':
        image = image.convert('RGB')

    image = image.resize((224, 224))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)

    # Perform prediction
    prediction = model.predict(image)[0]
    predicted_labels = [{'label': labels[j], 'accuracy': round(float(pred), 2)} for j, pred in enumerate(prediction)]
    predictions.append(predicted_labels)

    # Generate unique filename using timestamp and user ID
    timestamp = datetime.now().strftime('%Y-%m-%d_%H%M%S')
    unique_filename = f"image_{timestamp}_{user_id}.jpg"

    # Dummy image URL for testing
    image_url = f"https://dummyimage.com/300/{unique_filename}"

    current_time = datetime.now()

    # Dummy insertion into database (not actual)
    id_image = 1  # Dummy ID for testing

    # Analyze predictions to compute skin_health score
    analyze_values = [max(prediction[i]['accuracy'] for prediction in predictions) for i in range(len(labels))]

    above_threshold = sum(value > 0.5 for value in analyze_values)
    if above_threshold == 0:
        skin_health = 100
    elif above_threshold == 1:
        skin_health = random.randint(90, 95)
    elif above_threshold in [2, 3]:
        skin_health = random.randint(85, 89)
    elif above_threshold == 4:
        skin_health = random.randint(80, 84)
    else:
        skin_health = random.randint(75, 79)

    # Dummy insertion into database (not actual)
    prediction_results = {
        'date': current_time.strftime('%Y-%m-%d %H:%M:%S'),
        'image_url': image_url,
        'result_analyze': dict(zip(labels, analyze_values)),
        'skin_health': skin_health
    }

    return jsonify(prediction_results)

@app.route('/history', methods=['GET'])
@authenticate_user
def history():
    user_id = request.id_user

    # Dummy history data for testing
    dummy_history = [
        {
            'date': '2024-06-13 15:30:00',
            'image_url': 'https://dummyimage.com/300/image_2024-06-13_153000_1.jpg',
            'result_analyze': {
                'Acne': 0.2,
                'ActinicKeratosis': 0.1,
                'Blackheads': 0.05,
                'Herpes': 0.0,
                'Keloid': 0.0,
                'KeratosisSeborrheic': 0.3,
                'Milia': 0.1,
                'Pityriasis versicolor': 0.0,
                'Ringworm': 0.25
            },
            'skin_health': 92
        },
        {
            'date': '2024-06-12 14:45:00',
            'image_url': 'https://dummyimage.com/400/image_2024-06-12_144500_1.jpg',
            'result_analyze': {
                'Acne': 0.1,
                'ActinicKeratosis': 0.05,
                'Blackheads': 0.01,
                'Herpes': 0.0,
                'Keloid': 0.0,
                'KeratosisSeborrheic': 0.6,
                'Milia': 0.05,
                'Pityriasis versicolor': 0.1,
                'Ringworm': 0.08
            },
            'skin_health': 87
        }
        # Add more dummy history data as needed
    ]

    return jsonify(dummy_history)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
