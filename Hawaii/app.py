import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
# create engine to hawaii.sqlite
engine = create_engine("sqlite:///../Resources/hawaii.sqlite")


# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
print(Base.classes.keys())

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return (
        f"Welcome to the Hawaii Climate Analysis Homepage<br/>"
        f"The avaiable API's are as follows:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        )


# Create the route for precipitation.

@app.route("/api/v1.0/precipitation")

# Create the query.

def precipitation():
    # Print request to terminal
    print("'Precipitation' page request recieved...")

    # Calculate the date one year from the last date in data set.
    previous_year = dt.date(2017,8,23) - dt.timedelta(days=365)

    # Query for the date and precipitation for the last year
    result = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= previous_year).all()
     
    # Close the session
    session.close()

    # Convert the query results to a dictionary using `date` as the key and `prcp` as the value.
    precipitation = {date: prcp for date, prcp in result}

    # Return the JSON representation of the dictionary
    return jsonify(precipitation)

# Create the route for stations.

@app.route("/api/v1.0/stations")

# Create the query to return a list of the stations.

def station_list():

    # Print request to terminal
    print("'Station' page request recieved...")
   
    s_list = session.query(Station.station).all()

    # Close the session

    session.close()

    # Use the ravel function to unravel the s_list and convert it to a list

    station_list = list(np.ravel(s_list))

    # Return the JSON of the list

    return jsonify(stations=station_list)

 # Create the route for tempreture observations (tobs).   

@app.route("/api/v1.0/tobs")

# Create the query to return the dates and temperature observations of the most active station for the previous year of data.

def tobs_list():

    # Print request to terminal
    print("'Tempreture Observations' page request recieved...")

    # Calculate the date one year from the last date in data set.
    previous_year = dt.date(2017,8,23) - dt.timedelta(days=365)    

# Query the station 'USC00519281' for all tempreture observations from the last year
    t_list = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= previous_year).all()

    # Close session    

    session.close()

    # Use the ravel function to unravel the s_list and convert it to a list
    tobs_list = list(np.ravel(t_list))

    # Return the JSON of the list
    return jsonify(temps=tobs_list)

# Create the route for TMIN, TAVG & TMAX   

if __name__ == "__main__":
    app.run(debug=True)
