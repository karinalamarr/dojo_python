from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")



if __name__ == __"main__":
    app.run(debug=True)
