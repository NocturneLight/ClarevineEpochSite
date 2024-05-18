"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

# Adds utilities.py to the application package.
from .backend.utilities import utilities
app.register_blueprint(utilities)

# Ignore the warning. Removing the line of code breaks the website.
import ClarevineEpochSite.views