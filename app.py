from flask import Flask, request, jsonify
from motorshield import Motor
app =Flask(__name__)

leftm = None
ritem = None
def initial():
    global leftm,ritem
    leftm = Motor("MOTOR2",1)
    ritem = Motor("MOTOR1",1)
@app.route("/",methods=["GET","POST"])
def index():
    if request.args.get("accel") == None:
        return "Hey"
    x_accel= float(request.args.get("x_accel"))
    y_accel= float(request.args.get("y_accel"))
    z_accel= float(request.args.get("z_accel"))
    accel= float(request.args.get("accel"))
    x_mag= float(request.args.get("x_mag"))
    y_mag= float(request.args.get("y_mag"))
    z_mag= float(request.args.get("z_mag"))
    x_rot= float(request.args.get("x_rot"))
    y_rot= float(request.args.get("y_rot"))
    z_rot= float(request.args.get("z_rot"))
    lum= float(request.args.get("lumens"))
    lat= float(request.args.get("lat"))
    lon= float(request.args.get("lon"))
    #150 lumens is the normal lighting 
    if lum < 25:
        leftm.forward(100)
        ritem.forward(100)
    if lum > 100:
        leftm.stop()
        ritem.stop()
    if accel > 2:
        jsonify({
                "face":":O",
                "color":"yellow"
                })
    if abs(x_mag) > 60 or abs(y_mag) > 60 or abs(z_mag) > 60:
        testing= {
                "face" : ":(",
                "brightness": 100,
                "color": "yellow"
                }
        return jsonify(testing)
    if abs(x_rot)  > 7  or abs(y_rot) > 7 or abs(z_rot) > 7 :
         testing= {
                "face" : ":)",
                "brightness" : 75,
                "color" : "cyan"
         }
         return jsonify(testing)
    testing = {
            "face": ":-)",
            "color":"white"
            }
    return jsonify(testing)

if __name__ == "__main__":
    initial()
    app.debug = True
    app.run(host="0.0.0.0")
