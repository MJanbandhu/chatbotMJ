import os
import json
from keras.models import load_model

# Define base directory and paths to data and model directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
MODELS_DIR = os.path.join(BASE_DIR, 'models')
INTENTS_FILE = os.path.join(DATA_DIR, 'intents.json')
MODEL_FILE = os.path.join(MODELS_DIR, 'chatbot_model.h5')

print("Base directory:", BASE_DIR)
print("Data directory:", DATA_DIR)
print("Models directory:", MODELS_DIR)
print("Intents file path:", INTENTS_FILE)
print("Model file path:", MODEL_FILE)

# Check if files exist
print("Intents file exists:", os.path.exists(INTENTS_FILE))
print("Model file exists:", os.path.exists(MODEL_FILE))

# Load intents data if the file exists
if os.path.exists(INTENTS_FILE):
    try:
        with open(INTENTS_FILE) as file:
            intents = json.load(file)
    except Exception as e:
        print("Error loading intents file:", e)
        intents = {}
else:
    print("Intents file not found!")
    intents = {}

# Load trained model if the file exists
if os.path.exists(MODEL_FILE):
    try:
        model = load_model(MODEL_FILE)
    except Exception as e:
        print("Error loading model file:", e)
        model = None
else:
    print("Model file not found!")
    model = None

# Make sure the model is not None before proceeding
if model is not None:
    print("Model loaded successfully!")
else:
    print("Unable to load model. Exiting.")
    exit()

# Now you can continue with the rest of your code
