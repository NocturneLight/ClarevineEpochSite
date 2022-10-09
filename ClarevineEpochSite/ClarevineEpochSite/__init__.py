"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

# Adds utilities.py to the application package.
from .backend.utilities import utilities
app.register_blueprint(utilities)

import ClarevineEpochSite.views
