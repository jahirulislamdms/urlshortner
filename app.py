from flask import Flask, request, render_template, redirect
from shortener import generate_short_url

app = Flask(__name__)

# Dictionary to store the mapping between short and long URLs
url_mapping = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    long_url = request.form['long_url']
    short_url = generate_short_url()
    url_mapping[short_url] = long_url
    return render_template('shortened.html', short_url=short_url)

@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    long_url = url_mapping.get(short_url)
    if long_url is not None:
        return redirect(long_url)
    return "URL not found."

if __name__ == '__main__':
    app.run(debug=True)
