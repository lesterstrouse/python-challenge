from flask import flask, jsonify
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
        f"/api/v1.0/<start>/<end>"
@app.route("/api/v1.0/precipitation")
@app.route("/api/v1.0/stations")
@app.route("/api/v1.0/tobs")
@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
if __name__ == "__main__":
    app.run(debug=True)