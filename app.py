from flask import Flask, render_template, jsonify
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

data = {
    "temperature" : 25.2,
    "humidity" : 73.6,
    "meter" :
    {
        "electricity" :
        {
            "reading" : 12345.6,
            "consumption" : 1.2
        },
        "gas" :
        {
            "reading" : 12345.6789,
            "consumption" : 0.5
        },
        "water" :
        {
            "reading" : 12345.67,
            "consumption" : 0.1
        }
    },
    "boiler" :
    {
        "isRun" : True,
        "temperature" : 28.2,
        "pressure" : 1.6
    }
}

@app.route('/')
def index():
    return render_template('index.html', data=data)

@app.route('/data')
def get_data():
    return jsonify(data)

if __name__ == '__main__':
    app.run()

