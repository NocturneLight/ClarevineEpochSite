# NOTE: Make sure this file is always in the same location as the requirements.txt file on the server!
import os
import sys
from flask import Flask

sys.path.insert(0, os.path.dirname(__file__))

from ClarevineEpochSite import app
application = app
