from flask import Flask
app = Flask(__name__)


@app.route('/')
def saymyname():
    return 'Hey! This was written by Sean Pascual'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
