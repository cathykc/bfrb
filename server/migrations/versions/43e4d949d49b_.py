"""empty message

Revision ID: 43e4d949d49b
Revises: a70a32a64767
Create Date: 2018-05-10 00:56:53.475968

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '43e4d949d49b'
down_revision = 'a70a32a64767'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('fb_id', sa.String(), nullable=False))

def downgrade():
    op.drop_column('users', 'fb_id')
