"""empty message

Revision ID: 1fc909a7814f
Revises: fb092dcf69f0
Create Date: 2019-03-23 17:00:48.096538

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1fc909a7814f'
down_revision = 'fb092dcf69f0'
branch_labels = None
depends_on = None


def upgrade():
  op.create_table(
    'chat_state',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),

    sa.Column('client_id', sa.String(), nullable=False),
    sa.Column('prompt_key', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
  )


def downgrade():
  op.drop_table('chat_state')
