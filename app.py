from flask import Flask, render_template, request, redirect, url_for, send_file
from pytube import YouTube
import instaloader
import os

app = Flask(__name__)
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
            return render_template('download_photo.html', post=post)


if __name__ == '__main__':
    app.debug = True
    app.run()
