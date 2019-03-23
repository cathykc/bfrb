"""empty message

Revision ID: fb092dcf69f0
Revises:
Create Date: 2019-03-23 16:50:16.842880

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb092dcf69f0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
  op.create_table(
    'client_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),

    sa.Column('client_id', sa.String(), nullable=False),
    sa.Column('config_id', sa.String(), nullable=False),
    sa.Column('prompt_key', sa.String(), nullable=False),
    sa.Column('prompt_text', sa.String(), nullable=False),
    sa.Column('response', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
  )


def downgrade():
  op.drop_table('client_data')
