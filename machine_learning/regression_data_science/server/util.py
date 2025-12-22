import json
import pickle
import os
import numpy as np

__locations = None
__data_columns = None
__model = None

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

columns_path = os.path.join(BASE_DIR, "..", "model", "columns.json")
model_path = os.path.join(BASE_DIR, "..", "model", "bangalore_home_prices_model.pickle")


def get_estimated_price(location, sqft, bath, bhk):
  try:
    loc_index = __data_columns.index(location.lower())
  except:
    loc_index = -1

  x = np.zeros(len(__data_columns))
  x[0] = sqft
  x[1] = bath
  x[2] = bhk
  if loc_index >= 0:
    x[loc_index] = 1

  return round(__model.predict([x])[0], 2)

def get_location_names():
  return __locations

def load_saved_artifacts():
  print("Loading saved artifacts...start")
  global __locations
  global __data_columns
  global __model

  with open(columns_path, 'r') as f:
    __data_columns = json.load(f)['data_columns']
    __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk

  with open(model_path, 'rb') as f:
    __model = pickle.load(f)

  print("Artifacts loaded")

if __name__ == '__main__':
  # Test the function
  load_saved_artifacts()
  print(get_location_names())
  print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
  print(get_estimated_price('Indira Nagar', 1000, 3, 3))