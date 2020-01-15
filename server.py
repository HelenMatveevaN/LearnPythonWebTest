from flask import Flask, render_template
from rndPhrase import get_random_phrase
from rndPicture import get_random_picture

app = Flask(__name__)

@app.route("/index.html")
def rndPhrase():
    page_title = "Случайная фраза из списка"
    phrase = get_random_phrase()
    return render_template('index.html', page_title=page_title, phrase=phrase)

@app.route("/picture.html")
def rndPicture():
    page_title = "Случайная картинка из папки ПК"
    picture = get_random_picture()
    return render_template('picture.html', page_title=page_title, picture=picture)

if __name__=="__main__":
    app.run(debug=True)