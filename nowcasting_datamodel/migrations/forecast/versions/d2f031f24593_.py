"""empty message

Revision ID: d2f031f24593
Revises: 14e1747b9710
Create Date: 2022-03-21 15:56:09.757720

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd2f031f24593'
down_revision = '14e1747b9710'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gsp_yield',
    sa.Column('created_utc', sa.DateTime(timezone=True), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('datetime_utc', sa.DateTime(), nullable=True),
    sa.Column('solar_generation_kw', sa.String(), nullable=True),
    sa.Column('regime', sa.String(), nullable=True),
    sa.Column('location_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['location_id'], ['location.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_gsp_yield_datetime_utc'), 'gsp_yield', ['datetime_utc'], unique=False)
    op.create_index('ix_gsp_yield_datetime_utc_desc', 'gsp_yield', [sa.text('datetime_utc DESC')], unique=False)
    op.create_index(op.f('ix_gsp_yield_location_id'), 'gsp_yield', ['location_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_gsp_yield_location_id'), table_name='gsp_yield')
    op.drop_index('ix_gsp_yield_datetime_utc_desc', table_name='gsp_yield')
    op.drop_index(op.f('ix_gsp_yield_datetime_utc'), table_name='gsp_yield')
    op.drop_table('gsp_yield')
    # ### end Alembic commands ###
