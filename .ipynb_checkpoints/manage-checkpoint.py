from flask.cli import FlaskGroup
from main.py import app
from api.api import db

cli = FlaskGroup(app)

@cli.command("initdb")
def initdb():
    """Initialize the database."""
    db.create_all()
    print("Database initialized.")

if __name__ == "__main__":
    cli()
