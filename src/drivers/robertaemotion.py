from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer
import numpy as np
from scipy.special import softmax
from drivers.model_driver import ModelDriver
from models.prompt import Prompt
from utils.logger import log_msg

_model_name = "cardiffnlp/twitter-roberta-base-emotion"
_roberta_tokenizer = AutoTokenizer.from_pretrained(_model_name)
_roberta_model = AutoModelForSequenceClassification.from_pretrained(_model_name)
_roberta_model.save_pretrained(_model_name)
_roberta_tokenizer.save_pretrained(_model_name)

_roberta_labels = [
    "anger", 
    "joy", 
    "optimism", 
    "sadness"
]

class RobertaemotionDriver(ModelDriver):
    def load_model(self):
        log_msg("INFO", "[Robertaemotion] loading model...")

    def generate_response(self, prompt: Prompt):
        text = prompt.message
        encoded_input = _roberta_tokenizer(text, return_tensors='pt')
        output = _roberta_model(**encoded_input)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)
        ranking = np.argsort(scores)
        ranking = ranking[::-1]
        emotions = []
        for i in range(scores.shape[0]):
            label = _roberta_labels[ranking[i]]
            score = np.round(scores[ranking[i]], 4)
            emotions.append({label: score})
        return {"response": ["The predicted emotions are: {}".format(emotions)], "scores": emotions}
