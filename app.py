from flask import Flask, jsonify
from flask_cors import CORS
from banner import get_banner_food
from foods import get_food
from sea import get_sea
from temple import get_temple


app = Flask(__name__)
CORS(app)

# Banner
@app.route('/api/banner', methods=['GET'])
def get_all_banners():  # Renamed function to avoid conflict
    return get_banner_food()

@app.route('/api/banner/<int:banner_id>', methods=['GET'])
def get_banner_by_id(banner_id):
    # Assuming `banner` is a list of banner data imported from somewhere
    from banner import banner  # Import explicitly if needed
    found_banner = None
    for b in banner:  # Use 'b' to iterate through banner list
        if b['id'] == banner_id:
            found_banner = b
            break
    if found_banner:
        return jsonify({"status": 200, "message": "Banner retrieved successfully", "data": found_banner})
    return jsonify({"status": 404, "message": "Banner not found", "data": None})


@app.route('/api/foods', methods=['GET'])
def foods():
    return get_food()

@app.route('/api/foods/<int:food_id>', methods=['GET'])
def get_food_by_id(food_id):
    from foods import foods
    found_food = None
    for f in foods:
        if f['id'] == food_id:
            found_food = f
            break
    if found_food:
        return jsonify({"status": 200, "message": "Foods retrived successfully", "data": found_food})
    return jsonify({"status": 404, "message": "Foods not found", "data": None})

@app.route('/api/sea', methods=['GET'])
def sea():
    return get_sea()

@app.route('/api/sea/<int:sea_id>', methods=['GET'])
def get_sea_by_id(sea_id):
    from sea import sea
    found_sea = None
    for s in sea:
        if s['id'] == sea_id:
            found_sea = s
            break
    if found_sea:
        return jsonify({"status": 200, "message": "Foods retrieved succesffuly", "data": found_sea})
    return jsonify({"status": 404, "message": "Sea not found", "data": None})
    

@app.route('/api/temple', methods=['GET'])
def temple():
    return get_temple()

@app.route('/api/temple/<int:temple_id>', methods=["GET"])
def get_temple_by_id(temple_id):
    from temple import temple
    found_temple = None
    for t in temple:
        if t['id'] == temple_id:
            found_temple = t
            break
    if found_temple:
        return jsonify({"status": 200, "message": "Temple retrieved successfully", "data": found_temple})
    return jsonify({"status": 404, "message": "Temple not found", "data": None})



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=35174)