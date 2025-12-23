from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
  response = jsonify({
    'locations': util.get_location_names()
  })
  response.headers.add('Access-Control-Allow-Origin', '*')

  return "Hello, World!"

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
  sqft = float(request.form['total_sqft'])
  bath = int(request.form['bath'])
  bhk = int(request.form['bhk'])
  location = request.form['location']

  estimated_price = util.get_estimated_price(location, sqft, bath, bhk)

  response = jsonify({
    'estimated_price': estimated_price
  })

  response.headers.add('Access-Control-Allow-Origin', '*')

  return response

if __name__ == '__main__':
  print("Starting flask server for home price prediction...")
  app.run()