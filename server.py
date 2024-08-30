"""
Emotion Detection Flask App
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route('/emotionDetector')
def emotion_analyzer():
    """
    Analyze the emotions present in the given text.
    Retrieves text from the request arguments, processes it through the
    emotion detector, and returns the analyzed emotions as a formatted string.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    if text_to_analyze and text_to_analyze.strip() and not text_to_analyze.isdigit():
        response = emotion_detector(text_to_analyze)

        response_data = {
            'anger': response.get('anger'),
            'disgust': response.get('disgust'),
            'fear': response.get('fear'),
            'joy': response.get('joy'),
            'sadness': response.get('sadness'),
            'dominant_emotion': response.get('dominant_emotion')
        }

        if response_data['dominant_emotion'] is None:
            return "Invalid text! Please try again!"

        formatted_response = (
            f"For the given statement, the system response is 'anger': {response_data['anger']}, "
            f"'disgust': {response_data['disgust']}, 'fear': {response_data['fear']}, "
            f"'joy': {response_data['joy']} and 'sadness': {response_data['sadness']}. "
            f"The dominant emotion is {response_data['dominant_emotion']}."
        )

        return formatted_response

    return "Invalid text! Please try again!"

@app.route("/")
def render_index_page():
    """
    Render the index page of the application.
    This function initiates the rendering of the main application
    page over the Flask channel.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

# To run the project: python3.11 server.py
# Test: I think I am having fun


# IBM code:
# from flask import Flask, render_template, request
# from EmotionDetection.emotion_detection import emotion_detector

# app = Flask("Emotion Detector")

# @app.route("/emotionDetector")
# def emotion_detector_function():
#     text_to_analyze = request.args.get('textToAnalyze')
#     response = emotion_detector(text_to_analyze)
#     response_text = f"For the given statement, the system response is 'anger': \
#                     {response['anger']}, 'disgust': {response['disgust']}, \
#                     'fear': {response['fear']}, 'joy': {response['joy']}, \
#                     'sadness': {response['sadness']}. The dominant emotion is \
#                     {response['dominant_emotion']}."
#     return response_text

# @app.route("/")
# def render_index_page():
#     return render_template('index.html')

# if __name__ == "__main__":
#     app.run(host = "0.0.0.0", port = 5000)


# @app.route("/emotionDetector")
# def emotion_detector_function():
#     text_to_analyze = request.args.get('textToAnalyze')
#     response = emotion_detector(text_to_analyze)

#     if response['dominant_emotion'] is None:
#         response_text = "Invalid Input! Please try again."
#     else:
#         response_text = f"For the given statement, the system response is 'anger': \
#                     {response['anger']}, 'disgust': {response['disgust']}, \
#                     'fear': {response['fear']}, 'joy': {response['joy']}, \
#                     'sadness': {response['sadness']}. The dominant emotion is \
#                     {response['dominant_emotion']}."

#     return response_text