from flask import flask
app = flask(__name__)
# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return "Welcome to my 'Home' page!"
@app.route("/api/v1.0")
@app.route("/api/v1.0")
@app.route("/api/v1.0")
@app.route("/api/v1.0")
@app.route("/api/v1.0")
