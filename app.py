# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Alex" # write your name
    age = "7" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def fatherpage():
    name="Bob"
    age="35"

    return render_template('father.html', name = name , age = age)

# define the route to mother webpage
@app.route("/mother")
def motherpage():
    name="Kate"
    age="31"

    return render_template('mother.html', name = name , age = age)

# define the route to friends webpage
@app.route("/friend")
def friend1page():
    name="James"
    age="6"

    return render_template('friend.html', name = name , age = age)

# add other routes, if you want
@app.route("/friend2")
def friend2page():
    name="Tom"
    age="7"

    return render_template('friend2.html', name = name , age = age)

@app.route("/friend3")
def friend3page():
    name="Michael"
    age="8"

    return render_template('friend3.html', name = name , age = age)


# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
