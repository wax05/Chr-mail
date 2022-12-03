from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# project module
from route.route import UserRoute

app = Flask(__name__)

##db info setting
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:0000@localhost:3306/unknowntree"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

## db set
db = SQLAlchemy()
db.init_app(app)

app.register_blueprint(UserRoute)

if __name__ == '__main__':
    app.run("0.0.0.0:5000",debug=True)