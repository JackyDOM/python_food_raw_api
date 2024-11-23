from flask import Flask, jsonify
from flask_cors import CORS
from banner import get_banner_food
from foods import get_food
from sea import get_sea


app = Flask(__name__)
CORS(app)

# Banner
@app.route('/api/banner', methods=['GET'])
def banner():
    return get_banner_food()

@app.route('/api/foods', methods=['GET'])
def foods():
    return get_food()

@app.route('/api/sea', methods=['GET'])
def sea():
    return get_sea()




if __name__ == '__main__':
    app.run(debug=True)