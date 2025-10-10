from Flask import Flask

app = Flask(__name__)

@app.route("/info")
def lwinfo():
    return "i am LW from INdia"
   
@app.route("/phone") 
def lwphone():
    return "8947002033"
    
  
app.run(host="0.0.0.0")