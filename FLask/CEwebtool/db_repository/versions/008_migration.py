from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
data = Table('data', post_meta,
    Column('mass', Integer, primary_key=True, nullable=False),
    Column('timestamp', DateTime),
    Column('user_id', Integer),
    Column('language', String(length=5)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['data'].columns['language'].create()
    post_meta.tables['data'].columns['timestamp'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['data'].columns['language'].drop()
    post_meta.tables['data'].columns['timestamp'].drop()
