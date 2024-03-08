"""

Add model_id in mertric_value

Revision ID: 37c68fd8e65c
Revises: 489955d7a5a0
Create Date: 2023-04-14 15:05:00.205258

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "37c68fd8e65c"
down_revision = "489955d7a5a0"
branch_labels = None
depends_on = None


def upgrade():  # noqa
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("metric_value", sa.Column("model_id", sa.Integer(), nullable=True))
    op.create_index(op.f("ix_metric_value_model_id"), "metric_value", ["model_id"], unique=False)
    op.create_foreign_key(None, "metric_value", "model", ["model_id"], ["id"])
    # ### end Alembic commands ###


def downgrade():  # noqa
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "metric_value", type_="foreignkey")
    op.drop_index(op.f("ix_metric_value_model_id"), table_name="metric_value")
    op.drop_column("metric_value", "model_id")
    # ### end Alembic commands ###
