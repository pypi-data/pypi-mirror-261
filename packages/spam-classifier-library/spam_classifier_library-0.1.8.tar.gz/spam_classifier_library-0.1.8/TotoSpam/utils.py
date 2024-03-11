import json
import torch
from .model import RNNSpamClassifier
from .vectorizer import TextVectorizer
import os
import git

def save_model(model, path):
    torch.save(model.state_dict(), path)

def load_model(input_size, hidden_size, output_size):
    local_path = "./modelsAndVec"

    if not os.path.exists(local_path):
        git.Repo.clone_from("https://github.com/CodeNeuralist/SpamModel.git", local_path)
        
    model_path = os.path.join(local_path, "model.pth")
    model = RNNSpamClassifier(input_size, hidden_size, output_size)
    model.load_state_dict(torch.load(model_path))
    model.eval()
    return model


def save_vectorizer(vectorizer, path):
    vectorizer_params = {
        "stop_words": list(vectorizer.vectorizer.stop_words_),
        "lowercase": vectorizer.vectorizer.lowercase,
        "max_df": vectorizer.vectorizer.max_df,
        "min_df": vectorizer.vectorizer.min_df,
        "max_features": vectorizer.vectorizer.max_features,
        "vocabulary": vectorizer.vectorizer.vocabulary_,
    }
    with open(path, 'w') as file:
        json.dump(vectorizer_params, file)

def load_vectorizer():
    with open("./modelsAndVec/vectorizer.json", 'r') as file:
        vectorizer_params = json.load(file)
    return TextVectorizer(**vectorizer_params)

def classify_sentence(sentence, model, vectorizer):
    sentence_vec = vectorizer.transform([sentence])

    sentence_tensor = torch.tensor(sentence_vec.toarray(), dtype=torch.float32)

    with torch.no_grad():
        output = model(sentence_tensor.unsqueeze(0))  # Добавляем размерность пакета
        predicted_label = torch.round(output.squeeze()).item()

    return "Предложение классифицировано как спам." if predicted_label == 1 else "Предложение классифицировано как не спам."

def is_spam(text, model, vectorizer):
    text_vec = vectorizer.transform([text])
    text_tensor = torch.tensor(text_vec.toarray(), dtype=torch.float32)

    with torch.no_grad():
        output = model(text_tensor.unsqueeze(0))
        predicted_label = torch.round(output.squeeze()).item()

    return predicted_label == 1
