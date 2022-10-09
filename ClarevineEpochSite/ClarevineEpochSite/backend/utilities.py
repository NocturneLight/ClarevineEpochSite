from flask import Blueprint
from datetime import datetime

utilities = Blueprint("utilities", __name__)

'''
Gets the current date and time as a dictionary
that we can use part or all of on the website.
'''
@utilities.app_context_processor
def injectNow():
    return {'now': datetime.utcnow()}
