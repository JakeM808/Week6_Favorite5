from flask import Flask

# Create an instance of the Flask app
app = Flask(__name__)

#import all of the routes from the routes file into the current package
from app import routes
# Must be imported at bottom of the file