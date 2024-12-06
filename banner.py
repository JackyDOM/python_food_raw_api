from flask import jsonify

banner = [
  {
    'id': 1,
    'name': 'ម្ហូបអាហារ',
    'image_banner': 'https://toursbyjeeps.com/wp-content/uploads/2020/12/Untitled-3.jpg',
  },
  {
    'id': 2,
    'name': 'កន្លែងដើរលេង',
    'image_banner': 'https://www.popular.com.kh/wp-content/uploads/2020/07/Kompot1.jpg',
  },
  {
    'id': 3,
    'name': 'ប្រាសាទ',
    'image_banner': 'https://infotainment.ams.com.kh/wp-content/uploads/2023/02/Untitled-1-1.jpg',
  },
  {
    'id': 4,
    'name': 'ហាងកាហ្វេ',
    'image_banner': 'https://www.visitkampot.info/__asset/ckfinder/userfiles/files/252334386_911175556168320_4918950357825285243_n.jpg',
  },
  {
    'id': 5,
    'name': 'សណ្ណាគារ',
    'image_banner': 'https://cf.bstatic.com/xdata/images/hotel/max1024x768/571257890.jpg?k=3006583ba2f25781702ce24232b390fc3c3faaaff0a298daf1ee8ea1e9845b3f&o=&hp=1',
  },
]

def get_banner_food():
  response = {
        "status": 200,
        "message": "Banners retrieved successfully",
        "data": banner,
    }
  return jsonify(response)