"""empty message

Revision ID: 1cf8346a76d6
Revises: 1fc909a7814f
Create Date: 2019-03-23 17:24:13.864874

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1cf8346a76d6'
down_revision = '1fc909a7814f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('client_data', sa.Column('session_id', sa.Integer(), nullable=False))

def downgrade():
    op.drop_column('client_data', 'session_id')

