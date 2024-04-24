import nltk
from nltk.stem import WordNetLemmatizer
import numpy as np
from keras.models import load_model
import json
import random
import os 

# Load NLTK data
nltk.download('punkt')
nltk.download('wordnet')

# Define file paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
MODELS_DIR = os.path.join(BASE_DIR, 'models')
INTENTS_FILE = os.path.join(DATA_DIR, 'intents.json')
MODEL_FILE = os.path.join(MODELS_DIR, 'chatbot_model.h5')

# Load intents data
# with open('data/intents.json') as file:
    # intents = json.load(file)
# Load intents data
with open(INTENTS_FILE) as file:
    intents = json.load(file)

# Load trained model
# model = load_model('models/chatbot_model.h5')
# Load trained model
model = load_model(MODEL_FILE)

# Load words, classes, and lemmatizer
words = []
classes = []
documents = []
ignore_words = ['?', '!']
lemmatizer = WordNetLemmatizer()

for intent in intents['intents']:
    for pattern in intent['patterns']:
        w = nltk.word_tokenize(pattern)
        words.extend(w)
        documents.append((w, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))
classes = sorted(list(set(classes)))

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bow(sentence, words, show_details=True):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    print("found in bag: %s" % w)
    return(np.array(bag))

def predict_class(sentence, model):
    p = bow(sentence, words, show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def get_response(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result

def chatbot_response(msg):
    ints = predict_class(msg, model)
    res = get_response(ints, intents)
    return res

# Chat loop
print("Chatbot is running. Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        break
    response = chatbot_response(user_input)
    print("Bot:", response)
