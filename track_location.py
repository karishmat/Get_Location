import flask
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def get_location():
    latitude = ''
    longitude = ''
    if flask.request.method == "POST":
        latitude = request.form['inputLatitude']
        longitude = request.form['inputLongitude']
    return render_template('location.html', latitude= latitude, longitude=longitude)


if __name__ == '__main__':
    app.run()
