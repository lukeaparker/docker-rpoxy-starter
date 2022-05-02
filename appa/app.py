from flask import Flask
from os import environ

# Initilize appb
app = Flask(__name__)

# Appb landing page
@app.route("/", methods=['GET'])
def appa():
    return 'Welcome to Appa!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', 
        port=os.environ.get('FLASK_RUN_PORT'))