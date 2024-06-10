from sqlalchemy.orm import Session
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import ObjectDeletedError
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import StaleDataError
import uuid
from core.features.order.DAO import *
from core.features.order.mapeamento import *

import json
import requests
from datetime import datetime

class Model:
    def __init__(self):
        self.session = session