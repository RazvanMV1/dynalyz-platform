from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'app'))
from app.models.base import Base  # <== metadata
from app.models import user, signal, market_data  # asigură-te că le importi

# Load .env
from dotenv import load_dotenv
load_dotenv()

config = context.config
fileConfig(config.config_file_name)

config.set_main_option("sqlalchemy.url", os.getenv("DATABASE_URL"))
target_metadata = Base.metadata

def run_migrations_offline():
    context.configure(url=os.getenv("DATABASE_URL"), target_metadata=target_metadata,
                      literal_binds=True, dialect_opts={"paramstyle": "named"})
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(config.get_section(config.config_ini_section),
                                     prefix="sqlalchemy.", poolclass=pool.NullPool)
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
