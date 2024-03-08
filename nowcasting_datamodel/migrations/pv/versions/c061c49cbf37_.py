"""Add correct_data columns to pvsystem

Revision ID: c061c49cbf37
Revises: ade0a67b3567
Create Date: 2022-06-08 18:42:48.890956

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "c061c49cbf37"
down_revision = "ade0a67b3567"
branch_labels = None
depends_on = None


def upgrade():  # noqa
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("pv_system", sa.Column("correct_data", sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():  # noqa
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("pv_system", "correct_data")
    # ### end Alembic commands ###
