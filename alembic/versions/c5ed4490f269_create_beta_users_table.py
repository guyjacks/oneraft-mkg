"""create beta_users table

Revision ID: c5ed4490f269
Revises:
Create Date: 2016-01-31 22:47:08.573675

"""

# revision identifiers, used by Alembic.
revision = 'c5ed4490f269'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'beta_users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('first', sa.String(50), nullable=False),
        sa.Column('last', sa.String(50), nullable=False),
        sa.Column('email', sa.String(255), nullable=False),
        sa.Column('charity', sa.Boolean, nullable=False, default=False),
        sa.Column('sponsor', sa.Boolean, nullable=False, default=False),
        sa.Column('created', sa.DateTime, nullable=False)
    )


def downgrade():
    op.drop_table('beta_users')
