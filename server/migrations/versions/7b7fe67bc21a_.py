"""empty message

Revision ID: 7b7fe67bc21a
Revises: dc8eb1f03a6b
Create Date: 2019-03-23 22:03:41.235621

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b7fe67bc21a'
down_revision = 'dc8eb1f03a6b'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('client_data', 'prompt_text', nullable=True)


def downgrade():
    pass
