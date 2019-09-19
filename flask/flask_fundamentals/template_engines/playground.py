from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play')
def root():
    return render_template('play.html')


@app.route('/play/<num>')
def playTheNum(num):
    
    print("this is the number we need" + num)
    return render_template('play2.html', num=int(num))

@app.route('/play/<num>/<colors>/<name>')
def playColors(num, colors, name):
    
    print("this is the number we need" + num)
    print("this is the colors we need" + colors)
    return render_template('play3.html', num=int(num), colors=colors, name=name)




if __name__=="__main__":
    app.run(debug=True)