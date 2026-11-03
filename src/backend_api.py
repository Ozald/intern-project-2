from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

df = pd.read_csv('cars.csv')

@app.route('/')
def index():
    return jsonify({"message": "Welcome to my First API!"})

@app.route('/api/cars', methods=['GET'])
def get_cars():
    return jsonify(df.head(10).to_dict(orient='records'))

@app.route('/api/manufacturers', methods=['GET'])
def get_manufacturers():
    manufacturers = df['CarName'].apply(lambda x: x.split()[0].lower()).unique().tolist()
    return jsonify(manufacturers)

@app.route('/api/cars/prices', methods=['GET'])
def get_car_prices():
    return jsonify(df[['CarName', 'price']].to_dict(orient='records'))

if __name__ == "__main__":
    app.run(debug=True, port=8080)