from flask import Flask

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app.routes import index
from app.routes import get_hero_specs
from app.routes import get_hero_address