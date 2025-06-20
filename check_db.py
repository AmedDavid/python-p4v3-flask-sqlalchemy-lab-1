#!/usr/bin/env python3

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from server.app import app
from server.models import db, Earthquake

with app.app_context():
    print(Earthquake.query.all())