import os
from alembic import command, config

import db
from models import *
from db import Base, engine


def initialize_database():
    """Initializes database, including creating tables and setting latest alembic revision"""
    Base.metadata.create_all(engine)
    alembic_ini = os.path.join(
        os.path.abspath(os.path.dirname(db.__file__) + "/../.."), "alembic.ini"
    )
    alembic_config = config.Config(alembic_ini)
    command.stamp(alembic_config, "head")


if __name__ == "__main__":
    initialize_database()
