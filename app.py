from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
from PIL import Image
import numpy as np

app = Flask(__name__)
# Allow your React app to talk to Python
CORS(app) 

# Load your specific .h5 model 
print("Loading AI Model...")
model = tf.keras.models.load_model('skin_cancer_cnn.h5')
print("Model Loaded Successfully!")

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    try:
        # 1. Read the image sent from React
        file = request.files['file']
        img = Image.open(file.stream).convert('RGB')
        
        # 2. Preprocess the image (Ensure 224x224 matches your model's training)
        img = img.resize((224, 224))
        img_array = np.array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array.astype('float32') / 255.0

        # 3. Ask the AI for a prediction
        prediction = model.predict(img_array)
        
        # 4. Format the result
        malignant_prob = float(prediction[0][0])
        is_malignant = malignant_prob > 0.5

        label = "Malignant" if is_malignant else "Benign"
        confidence = malignant_prob * 100 if is_malignant else (1 - malignant_prob) * 100

        return jsonify({
            'label': label,
            'confidence': confidence
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)