from flask import Flask, request, render_template
import joblib
import pandas as pd

app = Flask(__name__, static_url_path='', static_folder='static',)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        stations = request.form['stations']
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        nb = joblib.load('nb.joblib')

        data = {'Latitude(deg)': [latitude], 'Longitude(deg)': [longitude], 'No_of_Stations': [stations]}
        row = pd.DataFrame.from_dict(data)
        y_pred = nb.predict(row)[0]

        labels = ['Minor', 'Moderate', 'Strong', 'Major']
        magnitude = labels[y_pred]
        return render_template('index.html', pred=magnitude)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)