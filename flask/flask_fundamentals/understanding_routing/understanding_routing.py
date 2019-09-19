from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"



@app.route("/")          
def route():
    return  "Hello World"

@app.route("/dojo")          
def dojo():
    return  "Dojo!"

@app.route("/flask")          
def say_flask():
    return  "Hello Flask"

@app.route("/michael")          
def say_michael():
    return  "Hello Michael"









if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
  app.run(debug=True)  