from __future__ import with_statement

import os
import sys

from alembic import context
from sqlalchemy import create_engine
from logging.config import fileConfig

sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), '..')))

import config  # noqa

try:
    environment = os.environ.get('ENV', 'Development')
    AppConfig = getattr(config, environment)
except AttributeError:
    raise Exception(
        'Configuration environment \'' + environment + '\' does '
        'not exists in the configuration file config.py. Please make '
        'sure to add it or use an existing envirinment.'
    )

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
from models.base import Base  # noqa
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    print('running offline!!!!!!!!!!!!!!!!');
    url = AppConfig.SQLALCHEMY_DATABASE_URI
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    # engine = create_engine(AppConfig.SQLALCHEMY_DATABASE_URI)
    # engine = create_engine('postgresql+psycopg2://postgres:hls901021@/postgres?host=/cloudsql/liusha-hello-world:us-west1:postgres')
    engine = create_engine('postgresql+psycopg2://postgres:hls901021@/postgres?host=/cloudsql/liusha-hello-world:us-west1:wizepool')
    
    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
