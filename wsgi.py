import os
from app import app

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 35174))
    app.run(debug=True,host='0.0.0.0', port=port)
