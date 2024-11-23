from flask import jsonify

sea = [
  {
    'id': 1,
    'sea_name': '',
    'sea_image': '',
    'deatil': {
      'sea_image': '',
      'sea_name': '',
      'description': '',
      'location': ''
    }
  }
]

def get_sea():
  response = {
        "status": 200,
        "message": "sea retrieved successfully",
        "data": sea,
    }
  return jsonify(response)