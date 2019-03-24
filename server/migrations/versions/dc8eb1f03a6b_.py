"""empty message

Revision ID: dc8eb1f03a6b
Revises: 1cf8346a76d6
Create Date: 2019-03-23 19:05:52.321424

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc8eb1f03a6b'
down_revision = '1cf8346a76d6'
branch_labels = None
depends_on = None


def upgrade():
  op.create_table(
    'therapy_configs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),

    sa.Column('name', sa.String(), nullable=False),
    sa.Column('config', sa.JSON(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
  )


def downgrade():
  op.drop_table('therapy_configs')

