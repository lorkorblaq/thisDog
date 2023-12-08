from flask import Flask, render_template, Blueprint
from home import home
app = Flask(__name__)
app.register_blueprint(second, url_prefix="")

if __name__ == "__main__":
    app.run(debug=True)