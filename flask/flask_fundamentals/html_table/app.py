from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/users')
def render_users():
 
    users = [
       'first_name' : 'Michael', 'last_name' : Sui,
       'first_name' : 'John', 'last_name' : Ross,
       'first_name' : 'Mark', 'last_name' : Kirk,
       'first_name' : 'Karolina', 'last_name' : Binge
    ]
return render_template("users.html", users = last_name)



if __name__ == "__main__":
    app.run(debug=True)    