from flask import Flask, escape, request, render_template
import pickle

vector = pickle.load(open("vectorizer.pkl", 'rb'))
model = pickle.load(open("finalized_model.pkl", 'rb'))
from flask import Flask, render_template, request, redirect, url_for, send_file
from pytube import YouTube
import instaloader
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == "POST":
        news = str(request.form['news'])
        print(news)

        predict = model.predict(vector.transform([news]))[0]
        print(predict)

        return render_template("prediction.html", prediction_text="News headline is -> {}".format(predict))


L = instaloader.Instaloader()
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        return redirect(url_for('preview', url=url))
    return render_template('index.html')

@app.route('/preview', methods=['POST'])
def preview():
    input_value = request.form['url']
    video_type=None
    post = instaloader.Post.from_shortcode(L.context, input_value.split("/")[-2])
    if post.is_video:
            return render_template('download_video.html', post=post)
    else:
        return render_template("prediction.html")
            return render_template('download_photo.html', post=post)


if __name__ == '__main__':
    app.debug = True
    app.run()
