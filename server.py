from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route('/emotionDetector')
def emotion_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Check if the user entered valid text
    if text_to_analyze and text_to_analyze.strip() and not text_to_analyze.isdigit():
        # Pass the text to the emotion_analyzer function and store the response
        response = emotion_detector(text_to_analyze)
        
        # # Prepare the response data
        # response_data = {
        #     'anger': response['anger'],
        #     'disgust': response['disgust'],
        #     'fear': response['fear'],
        #     'joy': response['joy'],
        #     'sadness': response['sadness'],
        #     'dominant_emotion': response['dominant_emotion']
        # }

        # Extract the dominant_emotion from the response
        dominant_emotion = response['dominant_emotion']

        if dominant_emotion is None:
            return "Please enter valid text."
        else:
            # Format the response as a string
            formatted_response = (f"For the given statement, the system response is 'anger': {response_data['anger']}, "
                                f"'disgust': {response['disgust']}, 'fear': {response_data['fear']}, "
                                f"'joy': {response_data['joy']} and 'sadness': {response_data['sadness']}. "
                                f"The dominant emotion is {response_data['dominant_emotion']}.")
            
            # Return the formatted response as plain text
            return formatted_response


@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")


if __name__ == "__main__":
    ''' 
    This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(host="0.0.0.0", port=5000)

# run the project: python3.11 server.py
# Test: I think I am having fun