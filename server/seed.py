#!/usr/bin/env python3

import sys
from pathlib import Path
# Add project root to sys.path
sys.path.append(str(Path(__file__).parent.parent))

from server.app import app
from server.models import db, Earthquake

with app.app_context():
    # Delete all rows in the "earthquakes" table
    Earthquake.query.delete()

    # Add several Earthquake instances to the "earthquakes" table
    db.session.add(Earthquake(magnitude=9.5, location="Chile", year=1960))
    db.session.add(Earthquake(magnitude=9.2, location="Alaska", year=1964))
    db.session.add(Earthquake(magnitude=8.6, location="Alaska", year=1946))
    db.session.add(Earthquake(magnitude=8.5, location="Banda Sea", year=1934))
    db.session.add(Earthquake(magnitude=8.4, location="Chile", year=1922))

    # Commit the transaction
    db.session.commit()