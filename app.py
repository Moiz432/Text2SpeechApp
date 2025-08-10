
from flask import Flask, render_template, request
from gtts import gTTS
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static'

@app.route("/", methods=["GET", "POST"])
def index():
    audio_file = None
    if request.method == "POST":
        text = request.form["text"]
        lang = request.form["lang"]  # selected language

        filename = "output.mp3"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        tts = gTTS(text=text, lang=lang)
        tts.save(filepath)
        
        audio_file = filename
    
    return render_template("index.html", audio_file=audio_file)

if __name__ == "__main__":
    os.makedirs('static', exist_ok=True)
    app.run(debug=True)
