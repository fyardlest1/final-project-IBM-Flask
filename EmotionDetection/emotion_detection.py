import requests  
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Custom header specifying the model ID for the emotion analysis service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Sending a POST request to the emotion analysis API
    response = requests.post(url, json=myobj, headers=header)

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    
    # If the response status code is 200, extract the emotion scores from the response
    if response.status_code == 200:
        # Extracting the emotion scores
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        anger_score = emotions.get('anger', 0)
        disgust_score = emotions.get('disgust', 0)
        fear_score = emotions.get('fear', 0)
        joy_score = emotions.get('joy', 0)
        sadness_score = emotions.get('sadness', 0)
        
        # Determine the dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)

        # Return the formatted output
        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
    elif response.status_code == 400:
        # In case of an error, return None for all values
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

# Testing the code
# result = emotion_analyzer("I love this new technology")
# print(result)

# python3.11
# from emotion_detection import emotion_detector
# emotion_detector('I love this new technology')
# emotion_detector('I am so happy I am doing this')
# from EmotionDetection.emotion_detection import emotion_detector
# emotion_detector('I hate working long hours')
# import unittest
