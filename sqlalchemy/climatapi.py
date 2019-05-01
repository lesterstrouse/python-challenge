import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from flask import flask, jsonify
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station
# Create our session (link) from Python to the DB
session = Session(engine)
lastdate =  engine.execute("SELECT max(date) FROM measurement")
for row in lastdate:
#    lastdat = dt.datetime.fromisoformat(row[0])
     lastdat = dt.datetime.strptime(row[0],'%Y-%m-%d')
begindat = lastdat - dt.timedelta(days = 365)
begindate = dt.datetime.strftime(begindat,'%Y-%m-%d')
app = flask(__name__)
# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>")
@app.route("/api/v1.0/precipitation")
def precip():
    return jsonify(dict(session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= f"{begindate}").all()))
@app.route("/api/v1.0/stations")
def station(): 
    return jsonify(session.query(Station.station).all())
@app.route("/api/v1.0/tobs")
def tobs():
    return jsonify(session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= f"{begindate}").all())
@app.route("/api/v1.0/<start>")
def minmax():
    return jsonify(session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= {start}).all())
@app.route("/api/v1.0/<start>/<end>")
def minmaxint():
    return jsonify(session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= {start}).filter(Measurement.date <= {end}).all())
if __name__ == "__main__":
    app.run(debug=True)