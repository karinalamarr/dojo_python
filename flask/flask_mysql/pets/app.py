from flask import Flask, render_template, request, redirect
from mysqlpets import connectToMySQL
app = Flask(__name__)


@app.route('/')
def index():
    mysql = connectToMySQL('pets')
    pets = mysql.query_db('SELECT * FROM pets.pets;')
    print (pets)
    return render_template("index.html")

@app.route('/create_pets', methods=["POST"])
def add_pet_to_db():
    mysql = connectToMySQL("pets")
    
    query = "INSERT INTO pets(name, age, breed, color, created_at, updated_at_) VALUES (%(n)s, %(a)s, %(b)s, %(c)s, NOW(), NOW());"
    data = {
                "n": request.form['nome'],
                "a": request.form['idade'],
                "b": request.form['raca'],
                "c": request.form['cor']
    }
    
    # mysql_db = connectToMySQL('pets')
    # user_id = mysql.query_db (query, data)
    # return redirect('/users/' + str(user_id))


    # new_pets_id = msql.query_db(query, data)
    #     return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)