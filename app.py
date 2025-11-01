from flask import Flask

app = Flask(__name__)

@app.route("/info")
def lwinfo():
    return "i am Abhishek Jain From Kota New"
   
@app.route("/phone") 
def lwphone():
    return "12121212sd"
    
  
app.run(host="0.0.0.0")