import requests
from model.adviceModel import Advice

def get_advice():

    url = "https://api.adviceslip.com/advice"
    request = requests.get(url)

    if request.status_code == 200:
        data_json = request.json()
        phrase_id = data_json['slip']['id']
        phrase_advice = data_json['slip']['advice']
        object_advice = Advice(phrase_id, phrase_advice)
        print("ID:", object_advice.phrase_id)
        print("Advice:", object_advice.phrase_advice)
        return object_advice
    else:
        print(f"request falied: {request.status_code}")
        return None

