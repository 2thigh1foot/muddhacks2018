from flask import Flask, request, jsonify
app =Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        print(request.data)
    testing = {
        "face" : ":(",
        "brightness": 50,
        "meta": {
            "time":10,
            "id":314
        }
    }
    return jsonify(testing)

if __name__ == "__main__":
    app.debug = True
    app.run()
