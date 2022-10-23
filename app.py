from io import BytesIO
from flask import Flask, render_template, url_for, request
import invoiceMaker
import postToIPFS
import postToJSON

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/createInvoice',methods = ["POST"])
def createInvoice():
    invoice = request.json["invoice"]
    vendor = request.json["vendor"]
    payer = request.json["payer"]
    totalAmount = request.json["totalAmount"]
    item = request.json["item"]
    invoiceMaker.createInvoice(invoice,vendor,payer,totalAmount,item)
    postedToIPFS = postToIPFS.postToIPFS()
    timestampHash = postedToIPFS['Timestamp']
    imageHash = postedToIPFS['IpfsHash']
    jsonHash = postToJSON.postToJSON(item, vendor, timestampHash,totalAmount,imageHash)

    return jsonHash


if __name__ == "__main__":
    app.run(debug=True)



