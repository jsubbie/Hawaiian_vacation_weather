# Flask App for Hawaii Data 

# from flask import Flask, jsonify
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    "Hawaii Data."
    return (
        f"Available Links:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs</br>"
        f"/api/v1.0/'start date as YYYY-MM-DD'</br>"
        f"/api/v1.0/'start date as YYYY-MM-DD'/'end date as YYYY-MM-DD'</br>"
    )

if __name__ == '__main__':
    app.run(debug=True)

# prior year's prcp

@app.route("/api.v1.0/precipitation")
def precip():
    
    query = session.query(measurements.date, func.sum(measurements.prcp).label("prcp")). \
    group_by(measurements.date).order_by(measurements.id.desc()).limit(365).all()

    prcp = []
    for rain_drop in query:
        drop_top = {}
        drop_top["Date"] = rain_drop.date
        drop_top["Total Precip"] = rain_drop.prcp
        prcp.append(drop_top)

    return jsonify(prcp)

if __name__ == '__main__':
    app.run(debug=True)

# station info 

@app.route("/api/v1.0/stations")
def stations():

    stat = session.query(stations).all()
    
    stations_info = []
    for looping in stat:
        blank = {}
        blank["Station"] = looping.station
        blank["Name"] = looping.name
        blank["Latitude"] = looping.latitude
        blank["Longitude"] = looping.longitude
        blank["Elevation"] = looping.elevation
        station_info.append(blank)
    
    return jsonify(stations_info)

if __name__ == '__main__':
    app.run(debug=True)

# tob info

@app.route("/api/v1.0/tobs")
def tobs():
    
    query = session.query(measurements.station, measurements.date, measurements.tobs).filter(measurements.date >= "2016-01-01"). \
        filter(measurements.date < "2017-01-01").all()
   
    heat_index = []
    for hot in query:
        heat = {}
        heat["Station ID"] = hot.station
        heat["Date"] = hot.date
        heat["Temp Observed"] = hot.tobs
        Bring.append(heat_index)
    
    return jsonify(heat_index)

if __name__ == '__main__':
    app.run(debug=True)    


# temp from start date 

@app.route("/api/v1.0/<start>")
def temps(start='2016-01-01'):
    
    min_temp = session.query(func.min(measurements.tobs)).filter(measurements.date >= start).all()
    max_temp = session.query(func.max(measurements.tobs)).filter(measurements.date >= start).all()
    avg_temp = session.query(func.avg(measurements.tobs)).filter(measurements.date >= start).all()
    
    min_temp_str = str(min_temp[0][0])
    max_temp_str = str(max_temp[0][0])
    avg_temp_str = str(avg_temp[0][0])
    
    temps = [{
            'Min Temp': min_temp_str,
            'Max Temp': max_temp_str,
            'Average Temp': avg_temp_str
    }]
    
    return jsonify(temps)

if __name__ == '__main__':
    app.run(debug=True)

# temps from date range 

@app.route("/api/v1.0/<start>/<end>")
def temps(start='', end=''):
    
    min_temp = session.query(func.min(measurements.tobs)).filter(measurements.date >= start).\
            filter(Measurement.date <= end).all()
    max_temp = session.query(func.max(measurements.tobs)).filter(measurements.date >= start).\
            filter(Measurement.date <= end).all()
    avg_temp = session.query(func.avg(measurements.tobs)).filter(measurements.date >= start).\
            filter(measurements.date <= end).all()
    
    min_temp_str = str(min_temp[0][0])
    max_temp_str = str(max_temp[0][0])
    avg_temp_str = str(avg_temp[0][0])
    
    temps = [{
            'Min Temp': min_temp_str,
            'Max Temp': max_temp_str,
            'Average Temp': avg_temp_str
    }]
    
    return jsonify(temps)

if __name__ == '__main__':
    app.run(debug=True)        