from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
data = Table('data', post_meta,
    Column('mass', Integer, primary_key=True, nullable=False),
    Column('user_id', Integer),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('nickname', String(length=64)),
    Column('email', String(length=120)),
    Column('mass', String(length=120)),
    Column('about_me', String(length=140)),
    Column('last_seen', DateTime),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['data'].create()
    post_meta.tables['user'].columns['mass'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['data'].drop()
    post_meta.tables['user'].columns['mass'].drop()