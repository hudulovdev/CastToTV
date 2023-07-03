from flask import Flask, render_template, request
from PyCasting import PyCasting

app = Flask(__name__)

# Initialize the PyCasting instance
casting = PyCasting()

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the cast page
@app.route('/cast', methods=['POST'])
def cast():
    # Get the video URL from the form input
    video_url = request.form['video_url']
    
    # Cast the video to the TV
    casting.cast(video_url)
    
    return 'Casting to TV...'

if __name__ == '__main__':
    app.run(debug=True)
