from fuzzywuzzy import fuzz
import json
import nltk
from nltk.stem import WordNetLemmatizer
import random

nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

def load_intents(file_path):
    with open(file_path, 'r') as file:
        intents = json.load(file)
    return intents

def preprocess(sentence):
    words = nltk.word_tokenize(sentence)
    return [lemmatizer.lemmatize(word.lower()) for word in words]

def get_response(user_input):
    intents = load_intents('data/intents.json')
    user_input = ' '.join(preprocess(user_input))
    
    best_matches = []
    threshold = 70
    
    # Mencari semua matches yang melewati threshold
    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            pattern = ' '.join(preprocess(pattern))
            score = fuzz.partial_ratio(user_input, pattern)
            
            if score > threshold:
                best_matches.append((score, intent["responses"]))
    
    # Jika ada matches yang ditemukan
    if best_matches:
        # Urutkan berdasarkan score tertinggi
        best_matches.sort(reverse=True)
        highest_score_responses = best_matches[0][1]
        
        # Pilih response secara random dari responses yang memiliki score tertinggi
        return {"response": [random.choice(highest_score_responses)]}
    
    # Jika tidak ada match, cari intent dengan tag "default"
    for intent in intents["intents"]:
        if intent.get("tag") == "default":
            return {"response": [random.choice(intent["responses"])]}
    
    # Fallback jika tidak ada intent default
    return {"response": ["Maaf, saya tidak mengerti. Bisa coba ditanyakan dengan cara lain?"]}