import json
import pickle

__locations = None
__data_columns = None
__model = None

def get_location_names():
  return __locations

def load_saved_artifacts():
  print("Loading saved artifacts...start")
  global __locations
  global __data_columns

  with open('../model/columns.json', 'r') as f:
    __data_columns = json.load(f)['data_columns']
    __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk

  with open('../model/bangalore_home_prices_model.pickle', 'rb') as f:
    __model = pickle.load(f)

  print("Artifacts loaded")

if __name__ == '__main__':
  # Test the function
  load_saved_artifacts()
  print(get_location_names())