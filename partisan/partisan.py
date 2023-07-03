import requests
import yaml
from yaml.loader import SafeLoader

with open('polarity/api.yaml') as f:
    data = yaml.load(f, Loader=SafeLoader)[0]
    
# Using Huggingface Inference API

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"
headers = {"Authorization": "Bearer " + data['APIKEY']}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
