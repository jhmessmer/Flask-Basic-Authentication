import datetime

"""Application entry point."""
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0")

    """changes made to the forked repository below"""

