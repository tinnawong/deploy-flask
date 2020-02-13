from app import app

@app.route("/api/user")
def getUserData():
    return "api to get data"