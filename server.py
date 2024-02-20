"""
Module for the Emotion Detector server.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion detector')

@app.route("/emotionDetector")
def emo_detector():
    """
    Route for emotion detection.

    Returns:
        str: The response based on emotion analysis.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    emotion = response['dominant_emotion']
    if emotion is not None:
        return (
            f"For the given statement, the system response is "
            f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, "
            f"and 'sadness': {sadness}. The dominant emotion is {emotion}."
        )
    return "Invalid text! Please try again!"

@app.route("/")
def render_index_page():
    """
    Route for rendering the index page.

    Returns:
        str: Rendered HTML page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
