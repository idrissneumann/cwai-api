from drivers.model_driver import ModelDriver
from models.prompt import Prompt
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
from utils.logger import log_msg

_sentiment_model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
_sentiment_model = AutoModelForSequenceClassification.from_pretrained(
    _sentiment_model_name)
_sentiment_tokenizer = AutoTokenizer.from_pretrained(_sentiment_model_name)

emotion_mapping = {
    1: 'anger',
    2: 'dislike',
    3: 'neutral',
    4: 'like',
    5: 'love'
}


class NlptownsentimentDriver(ModelDriver):
    def load_model(self):
        log_msg("INFO", "[Nlptownsentiment] loading model...")

    def generate_response(self, prompt: Prompt):
        inputs = _sentiment_tokenizer(prompt.message, return_tensors="pt")
        outputs = _sentiment_model(**inputs)
        probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
        predicted_class = torch.argmax(probs).item() + 1
        predicted_emotion = emotion_mapping[predicted_class]
        return {"response": ["The predicted emotion is: {}, score: {}".format(predicted_emotion, predicted_class)], "score": predicted_class}
