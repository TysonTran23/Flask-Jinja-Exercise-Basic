from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)

app.config['SECRET_KEY'] = 'chickensarecool'
debug = DebugToolbarExtension(app)

@app.route('/home')
def home_page():

    prompts = story.prompts

    return render_template('home.html', prompts=prompts)

@app.route('/story')
def story_page():

    text = story.generate(request.args)

    return render_template('story.html', text=text)