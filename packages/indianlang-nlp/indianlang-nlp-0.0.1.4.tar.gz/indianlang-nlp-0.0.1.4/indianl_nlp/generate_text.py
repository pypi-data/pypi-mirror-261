from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
import pickle
import gdown
import zipfile
import os

max_sq_ken = {
    "marathi": 66,
    "hindi": 33,
    "sanskrit": 35,
    "english": 155,
    "hinglish": 342
}


def download_and_extract():
    # Check if the directory exists
    model_dir = './indianl_nlp/'
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    # Define Google Drive URL for the zip file
    zip_url = 'https://drive.google.com/file/d/1dPMtWlCpeQ2wUGx8ycPeEjqjKzhIFeMo'
    zip_file_path = f'{model_dir}/models.zip'
    gdown.download(id="1dPMtWlCpeQ2wUGx8ycPeEjqjKzhIFeMo",output="models.zip", quiet=False)

    with zipfile.ZipFile(f'models.zip', 'r') as zip_ref:
            zip_ref.extractall(model_dir)
    
    os.remove("models.zip")

def load_language_model(language):
    model_dir = './indianl_nlp/models'
    model_path = f'{model_dir}/{language}/model.h5'
    tokenizer_path = f'{model_dir}/{language}/tokenizer.pkl'

    # Check if the model directory exists, if not, download and extract the zip file
    if not os.path.exists(model_path) or not os.path.exists(tokenizer_path):
        download_and_extract()

    # Load the model and tokenizer
    model = load_model(model_path)
    with open(tokenizer_path, "rb") as tokenizer_file:
        tokenizer = pickle.load(tokenizer_file)
    
    return model, tokenizer


def generate_text(seed_text, next_words, language):
    model, tokenizer = load_language_model(language)
    text = []
    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen=max_sq_ken[language]-1, padding='pre')
        y_pred_prob = model.predict(token_list,verbose=0)  # Predict probabilities for each class
        y_pred = y_pred_prob.argmax(axis=-1)  # Get the index with the highest probability
        predicted_word = ''
        for word, index in tokenizer.word_index.items():
            if index == y_pred:
                predicted_word = word
                break
        seed_text = seed_text + ' ' + predicted_word
        text.append(predicted_word)
    return ' '.join(text)
