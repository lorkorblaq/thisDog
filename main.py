from flask import Flask, render_template, Blueprint
from home import home_page

app = Flask(__name__)

app.register_blueprint(home_page, url_prefix="")


if __name__ == "__main__":
    app.run(port=8080, debug=True)
