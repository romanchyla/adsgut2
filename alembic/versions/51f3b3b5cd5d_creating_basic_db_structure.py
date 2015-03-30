"""Creating basic DB structure

Revision ID: 51f3b3b5cd5d
Revises: None
Create Date: 2014-08-08 20:13:58.241566

"""

# revision identifiers, used by Alembic.
revision = '51f3b3b5cd5d'
down_revision = None

from alembic import op
import sqlalchemy as sa

from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, Date
from sqlalchemy_utils import URLType


def upgrade():
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('confirmed_at', sa.DateTime(), nullable=True),
    sa.Column('last_login_at', sa.DateTime(), nullable=True),
    sa.Column('current_login_at', sa.DateTime(), nullable=True),
    sa.Column('last_login_ip', sa.String(length=100), nullable=True),
    sa.Column('current_login_ip', sa.String(length=100), nullable=True),
    sa.Column('login_count', sa.Integer(), nullable=True),
    sa.Column('registered_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('roles_users',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint()
    )
    op.create_table('permissions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('permissions_users',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('perm_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['perm_id'], ['permissions.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint()
    )
    
    


def downgrade():
    op.drop_table('permissions_users')
    op.drop_table('permissions')
    op.drop_table('roles_users')
    op.drop_table('roles')
    op.drop_table('users')