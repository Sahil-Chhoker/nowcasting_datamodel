"""empty message

Revision ID: 16ced43c1321
Revises: c74d778923e9
Create Date: 2023-12-07 11:26:09.780570

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "16ced43c1321"
down_revision = "c74d778923e9"
branch_labels = None
depends_on = None


def upgrade():  # noqa
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "forecast_value_2022_08",
        sa.Column("uuid", sa.UUID(), server_default=sa.text("gen_random_uuid()"), nullable=False),
        sa.Column("target_time", sa.DateTime(timezone=True), nullable=False),
        sa.Column("expected_power_generation_megawatts", sa.Float, nullable=True),
        sa.Column("adjust_mw", sa.Float(), nullable=True),
        sa.Column("properties", sa.JSON(), nullable=True),
        sa.Column("forecast_id", sa.Integer(), nullable=True),
        sa.Column("created_utc", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(
            ["forecast_id"],
            ["forecast.id"],
        ),
        sa.PrimaryKeyConstraint("uuid", "target_time"),
    )
    op.create_index(
        "forecast_value_2022_08_created_utc_idx",
        "forecast_value_2022_08",
        ["created_utc"],
        unique=False,
    )
    op.create_index(
        "forecast_value_2022_08_forecast_id_idx",
        "forecast_value_2022_08",
        ["forecast_id"],
        unique=False,
    )
    op.create_index(
        "forecast_value_2022_08_target_time_idx",
        "forecast_value_2022_08",
        ["target_time"],
        unique=False,
    )
    op.create_table(
        "forecast_value_2024_01",
        sa.Column("uuid", sa.UUID(), server_default=sa.text("gen_random_uuid()"), nullable=False),
        sa.Column("target_time", sa.DateTime(timezone=True), nullable=False),
        sa.Column("expected_power_generation_megawatts", sa.Float, nullable=True),
        sa.Column("adjust_mw", sa.Float(), nullable=True),
        sa.Column("properties", sa.JSON(), nullable=True),
        sa.Column("forecast_id", sa.Integer(), nullable=True),
        sa.Column("created_utc", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(
            ["forecast_id"],
            ["forecast.id"],
        ),
        sa.PrimaryKeyConstraint("uuid", "target_time"),
    )
    op.create_index(
        "forecast_value_2024_01_created_utc_idx",
        "forecast_value_2024_01",
        ["created_utc"],
        unique=False,
    )
    op.create_index(
        "forecast_value_2024_01_forecast_id_idx",
        "forecast_value_2024_01",
        ["forecast_id"],
        unique=False,
    )
    op.create_index(
        "forecast_value_2024_01_target_time_idx",
        "forecast_value_2024_01",
        ["target_time"],
        unique=False,
    )
    op.create_table(
        "forecast_value_2024_02",
        sa.Column("uuid", sa.UUID(), server_default=sa.text("gen_random_uuid()"), nullable=False),
        sa.Column("target_time", sa.DateTime(timezone=True), nullable=False),
        sa.Column("expected_power_generation_megawatts", sa.Float, nullable=True),
        sa.Column("adjust_mw", sa.Float(), nullable=True),
        sa.Column("properties", sa.JSON(), nullable=True),
        sa.Column("forecast_id", sa.Integer(), nullable=True),
        sa.Column("created_utc", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(
            ["forecast_id"],
            ["forecast.id"],
        ),
        sa.PrimaryKeyConstraint("uuid", "target_time"),
    )
    op.create_index(
        "forecast_value_2024_02_created_utc_idx",
        "forecast_value_2024_02",
        ["created_utc"],
        unique=False,
    )
    op.create_index(
        "forecast_value_2024_02_forecast_id_idx",
        "forecast_value_2024_02",
        ["forecast_id"],
        unique=False,
    )
    op.create_index(
        "forecast_value_2024_02_target_time_idx",
        "forecast_value_2024_02",
        ["target_time"],
        unique=False,
    )
    op.create_table(
        "forecast_value_2024_03",
        sa.Column("uuid", sa.UUID(), server_default=sa.text("gen_random_uuid()"), nullable=False),
        sa.Column("target_time", sa.DateTime(timezone=True), nullable=False),
        sa.Column("expected_power_generation_megawatts", sa.Float, nullable=True),
        sa.Column("adjust_mw", sa.Float(), nullable=True),
        sa.Column("properties", sa.JSON(), nullable=True),
        sa.Column("forecast_id", sa.Integer(), nullable=True),
        sa.Column("created_utc", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(
            ["forecast_id"],
            ["forecast.id"],
        ),
        sa.PrimaryKeyConstraint("uuid", "target_time"),
    )
    op.create_index(
        "forecast_value_2024_03_created_utc_idx",
        "forecast_value_2024_03",
        ["created_utc"],
        unique=False,
    )
    op.create_index(
        "forecast_value_2024_03_forecast_id_idx",
        "forecast_value_2024_03",
        ["forecast_id"],
        unique=False,
    )
    op.create_index(
        "forecast_value_2024_03_target_time_idx",
        "forecast_value_2024_03",
        ["target_time"],
        unique=False,
    )
    op.create_table(
        "forecast_value_2024_04",
        sa.Column("uuid", sa.UUID(), server_default=sa.text("gen_random_uuid()"), nullable=False),
        sa.Column("target_time", sa.DateTime(timezone=True), nullable=False),
        sa.Column("expected_power_generation_megawatts", sa.Float, nullable=True),
        sa.Column("adjust_mw", sa.Float(), nullable=True),
        sa.Column("properties", sa.JSON(), nullable=True),
        sa.Column("forecast_id", sa.Integer(), nullable=True),
        sa.Column("created_utc", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(
            ["forecast_id"],
            ["forecast.id"],
        ),
        sa.PrimaryKeyConstraint("uuid", "target_time"),
    )
    op.create_index(
        "forecast_value_2024_04_created_utc_idx",
        "forecast_value_2024_04",
        ["created_utc"],
        unique=False,
    )
    op.create_index(
        "forecast_value_2024_04_forecast_id_idx",
        "forecast_value_2024_04",
        ["forecast_id"],
        unique=False,
    )
    op.create_index(
        "forecast_value_2024_04_target_time_idx",
        "forecast_value_2024_04",
        ["target_time"],
        unique=False,
    )
    op.create_table(
        "forecast_value_2024_05",
        sa.Column("uuid", sa.UUID(), server_default=sa.text("gen_random_uuid()"), nullable=False),
        sa.Column("target_time", sa.DateTime(timezone=True), nullable=False),
        sa.Column("expected_power_generation_megawatts", sa.Float, nullable=True),
        sa.Column("adjust_mw", sa.Float(), nullable=True),
        sa.Column("properties", sa.JSON(), nullable=True),
        sa.Column("forecast_id", sa.Integer(), nullable=True),
        sa.Column("created_utc", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(
            ["forecast_id"],
            ["forecast.id"],
        ),
        sa.PrimaryKeyConstraint("uuid", "target_time"),
    )
    op.create_index(
        "forecast_value_2024_05_created_utc_idx",
        "forecast_value_2024_05",
        ["created_utc"],
        unique=False,
    )
    op.create_index(
        "forecast_value_2024_05_forecast_id_idx",
        "forecast_value_2024_05",
        ["forecast_id"],
        unique=False,
    )
    op.create_index(
        "forecast_value_2024_05_target_time_idx",
        "forecast_value_2024_05",
        ["target_time"],
        unique=False,
    )
    op.create_table(
        "forecast_value_2024_06",
        sa.Column("uuid", sa.UUID(), server_default=sa.text("gen_random_uuid()"), nullable=False),
        sa.Column("target_time", sa.DateTime(timezone=True), nullable=False),
        sa.Column("expected_power_generation_megawatts", sa.Float, nullable=True),
        sa.Column("adjust_mw", sa.Float(), nullable=True),
        sa.Column("properties", sa.JSON(), nullable=True),
        sa.Column("forecast_id", sa.Integer(), nullable=True),
        sa.Column("created_utc", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(
            ["forecast_id"],
            ["forecast.id"],
        ),
        sa.PrimaryKeyConstraint("uuid", "target_time"),
    )
    op.create_index(
        "forecast_value_2024_06_created_utc_idx",
        "forecast_value_2024_06",
        ["created_utc"],
        unique=False,
    )
    op.create_index(
        "forecast_value_2024_06_forecast_id_idx",
        "forecast_value_2024_06",
        ["forecast_id"],
        unique=False,
    )
    op.create_index(
        "forecast_value_2024_06_target_time_idx",
        "forecast_value_2024_06",
        ["target_time"],
        unique=False,
    )
    op.create_table(
        "forecast_value_2024_07",
        sa.Column("uuid", sa.UUID(), server_default=sa.text("gen_random_uuid()"), nullable=False),
        sa.Column("target_time", sa.DateTime(timezone=True), nullable=False),
        sa.Column("expected_power_generation_megawatts", sa.Float, nullable=True),
        sa.Column("adjust_mw", sa.Float(), nullable=True),
        sa.Column("properties", sa.JSON(), nullable=True),
        sa.Column("forecast_id", sa.Integer(), nullable=True),
        sa.Column("created_utc", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(
            ["forecast_id"],
            ["forecast.id"],
        ),
        sa.PrimaryKeyConstraint("uuid", "target_time"),
    )
    op.create_index(
        "forecast_value_2024_07_created_utc_idx",
        "forecast_value_2024_07",
        ["created_utc"],
        unique=False,
    )
    op.create_index(
        "forecast_value_2024_07_forecast_id_idx",
        "forecast_value_2024_07",
        ["forecast_id"],
        unique=False,
    )
    op.create_index(
        "forecast_value_2024_07_target_time_idx",
        "forecast_value_2024_07",
        ["target_time"],
        unique=False,
    )
    op.create_table(
        "forecast_value_2024_08",
        sa.Column("uuid", sa.UUID(), server_default=sa.text("gen_random_uuid()"), nullable=False),
        sa.Column("target_time", sa.DateTime(timezone=True), nullable=False),
        sa.Column("expected_power_generation_megawatts", sa.Float, nullable=True),
        sa.Column("adjust_mw", sa.Float(), nullable=True),
        sa.Column("properties", sa.JSON(), nullable=True),
        sa.Column("forecast_id", sa.Integer(), nullable=True),
        sa.Column("created_utc", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(
            ["forecast_id"],
            ["forecast.id"],
        ),
        sa.PrimaryKeyConstraint("uuid", "target_time"),
    )
    op.create_index(
        "forecast_value_2024_08_created_utc_idx",
        "forecast_value_2024_08",
        ["created_utc"],
        unique=False,
    )
    op.create_index(
        "forecast_value_2024_08_forecast_id_idx",
        "forecast_value_2024_08",
        ["forecast_id"],
        unique=False,
    )
    op.create_index(
        "forecast_value_2024_08_target_time_idx",
        "forecast_value_2024_08",
        ["target_time"],
        unique=False,
    )
    op.create_table(
        "forecast_value_2024_09",
        sa.Column("uuid", sa.UUID(), server_default=sa.text("gen_random_uuid()"), nullable=False),
        sa.Column("target_time", sa.DateTime(timezone=True), nullable=False),
        sa.Column("expected_power_generation_megawatts", sa.Float, nullable=True),
        sa.Column("adjust_mw", sa.Float(), nullable=True),
        sa.Column("properties", sa.JSON(), nullable=True),
        sa.Column("forecast_id", sa.Integer(), nullable=True),
        sa.Column("created_utc", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(
            ["forecast_id"],
            ["forecast.id"],
        ),
        sa.PrimaryKeyConstraint("uuid", "target_time"),
    )
    op.create_index(
        "forecast_value_2024_09_created_utc_idx",
        "forecast_value_2024_09",
        ["created_utc"],
        unique=False,
    )
    op.create_index(
        "forecast_value_2024_09_forecast_id_idx",
        "forecast_value_2024_09",
        ["forecast_id"],
        unique=False,
    )
    op.create_index(
        "forecast_value_2024_09_target_time_idx",
        "forecast_value_2024_09",
        ["target_time"],
        unique=False,
    )
    op.create_table(
        "forecast_value_2024_10",
        sa.Column("uuid", sa.UUID(), server_default=sa.text("gen_random_uuid()"), nullable=False),
        sa.Column("target_time", sa.DateTime(timezone=True), nullable=False),
        sa.Column("expected_power_generation_megawatts", sa.Float, nullable=True),
        sa.Column("adjust_mw", sa.Float(), nullable=True),
        sa.Column("properties", sa.JSON(), nullable=True),
        sa.Column("forecast_id", sa.Integer(), nullable=True),
        sa.Column("created_utc", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(
            ["forecast_id"],
            ["forecast.id"],
        ),
        sa.PrimaryKeyConstraint("uuid", "target_time"),
    )
    op.create_index(
        "forecast_value_2024_10_created_utc_idx",
        "forecast_value_2024_10",
        ["created_utc"],
        unique=False,
    )
    op.create_index(
        "forecast_value_2024_10_forecast_id_idx",
        "forecast_value_2024_10",
        ["forecast_id"],
        unique=False,
    )
    op.create_index(
        "forecast_value_2024_10_target_time_idx",
        "forecast_value_2024_10",
        ["target_time"],
        unique=False,
    )
    op.create_table(
        "forecast_value_2024_11",
        sa.Column("uuid", sa.UUID(), server_default=sa.text("gen_random_uuid()"), nullable=False),
        sa.Column("target_time", sa.DateTime(timezone=True), nullable=False),
        sa.Column("expected_power_generation_megawatts", sa.Float, nullable=True),
        sa.Column("adjust_mw", sa.Float(), nullable=True),
        sa.Column("properties", sa.JSON(), nullable=True),
        sa.Column("forecast_id", sa.Integer(), nullable=True),
        sa.Column("created_utc", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(
            ["forecast_id"],
            ["forecast.id"],
        ),
        sa.PrimaryKeyConstraint("uuid", "target_time"),
    )
    op.create_index(
        "forecast_value_2024_11_created_utc_idx",
        "forecast_value_2024_11",
        ["created_utc"],
        unique=False,
    )
    op.create_index(
        "forecast_value_2024_11_forecast_id_idx",
        "forecast_value_2024_11",
        ["forecast_id"],
        unique=False,
    )
    op.create_index(
        "forecast_value_2024_11_target_time_idx",
        "forecast_value_2024_11",
        ["target_time"],
        unique=False,
    )
    op.create_table(
        "forecast_value_2024_12",
        sa.Column("uuid", sa.UUID(), server_default=sa.text("gen_random_uuid()"), nullable=False),
        sa.Column("target_time", sa.DateTime(timezone=True), nullable=False),
        sa.Column("expected_power_generation_megawatts", sa.Float, nullable=True),
        sa.Column("adjust_mw", sa.Float(), nullable=True),
        sa.Column("properties", sa.JSON(), nullable=True),
        sa.Column("forecast_id", sa.Integer(), nullable=True),
        sa.Column("created_utc", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(
            ["forecast_id"],
            ["forecast.id"],
        ),
        sa.PrimaryKeyConstraint("uuid", "target_time"),
    )
    op.create_index(
        "forecast_value_2024_12_created_utc_idx",
        "forecast_value_2024_12",
        ["created_utc"],
        unique=False,
    )
    op.create_index(
        "forecast_value_2024_12_forecast_id_idx",
        "forecast_value_2024_12",
        ["forecast_id"],
        unique=False,
    )
    op.create_index(
        "forecast_value_2024_12_target_time_idx",
        "forecast_value_2024_12",
        ["target_time"],
        unique=False,
    )
    op.alter_column(
        "forecast_value_last_seven_days",
        "expected_power_generation_megawatts",
        existing_type=sa.REAL(),
        type_=sa.Float,
        existing_nullable=True,
    )
    op.alter_column(
        "gsp_yield",
        "solar_generation_kw",
        existing_type=sa.NUMERIC(),
        type_=sa.Float(),
        existing_nullable=True,
    )
    op.alter_column(
        "location",
        "installed_capacity_mw",
        existing_type=sa.REAL(),
        type_=sa.Float(),
        existing_nullable=True,
    )

    op.execute(
        "ALTER TABLE forecast_value ATTACH PARTITION forecast_value_2024_01 FOR VALUES FROM ('2024-01-01') TO ('2024-02-01');"  # noqa
    )
    op.execute(
        "ALTER TABLE forecast_value ATTACH PARTITION forecast_value_2024_02 FOR VALUES FROM ('2024-02-01') TO ('2024-03-01');"  # noqa
    )
    op.execute(
        "ALTER TABLE forecast_value ATTACH PARTITION forecast_value_2024_03 FOR VALUES FROM ('2024-03-01') TO ('2024-04-01');"  # noqa
    )
    op.execute(
        "ALTER TABLE forecast_value ATTACH PARTITION forecast_value_2024_04 FOR VALUES FROM ('2024-04-01') TO ('2024-05-01');"  # noqa
    )
    op.execute(
        "ALTER TABLE forecast_value ATTACH PARTITION forecast_value_2024_05 FOR VALUES FROM ('2024-05-01') TO ('2024-06-01');"  # noqa
    )
    op.execute(
        "ALTER TABLE forecast_value ATTACH PARTITION forecast_value_2024_06 FOR VALUES FROM ('2024-06-01') TO ('2024-07-01');"  # noqa
    )
    op.execute(
        "ALTER TABLE forecast_value ATTACH PARTITION forecast_value_2024_07 FOR VALUES FROM ('2024-07-01') TO ('2024-08-01');"  # noqa
    )
    op.execute(
        "ALTER TABLE forecast_value ATTACH PARTITION forecast_value_2024_08 FOR VALUES FROM ('2024-08-01') TO ('2024-09-01');"  # noqa
    )
    op.execute(
        "ALTER TABLE forecast_value ATTACH PARTITION forecast_value_2024_09 FOR VALUES FROM ('2024-09-01') TO ('2024-10-01');"  # noqa
    )
    op.execute(
        "ALTER TABLE forecast_value ATTACH PARTITION forecast_value_2024_10 FOR VALUES FROM ('2024-10-01') TO ('2024-11-01');"  # noqa
    )
    op.execute(
        "ALTER TABLE forecast_value ATTACH PARTITION forecast_value_2024_11 FOR VALUES FROM ('2024-11-01') TO ('2024-12-01');"  # noqa
    )
    op.execute(
        "ALTER TABLE forecast_value ATTACH PARTITION forecast_value_2024_12 FOR VALUES FROM ('2024-12-01') TO ('2025-01-01');"  # noqa
    )
    # ### end Alembic commands ###


def downgrade():  # noqa
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "location",
        "installed_capacity_mw",
        existing_type=sa.Float(),
        type_=sa.REAL(),
        existing_nullable=True,
    )
    op.alter_column(
        "gsp_yield",
        "solar_generation_kw",
        existing_type=sa.Float(),
        type_=sa.NUMERIC(),
        existing_nullable=True,
    )
    op.alter_column(
        "forecast_value_last_seven_days",
        "expected_power_generation_megawatts",
        existing_type=sa.Float(),
        type_=sa.REAL(),
        existing_nullable=True,
    )
    op.drop_index("forecast_value_2024_12_target_time_idx", table_name="forecast_value_2024_12")
    op.drop_index("forecast_value_2024_12_forecast_id_idx", table_name="forecast_value_2024_12")
    op.drop_index("forecast_value_2024_12_created_utc_idx", table_name="forecast_value_2024_12")
    op.drop_table("forecast_value_2024_12")
    op.drop_index("forecast_value_2024_11_target_time_idx", table_name="forecast_value_2024_11")
    op.drop_index("forecast_value_2024_11_forecast_id_idx", table_name="forecast_value_2024_11")
    op.drop_index("forecast_value_2024_11_created_utc_idx", table_name="forecast_value_2024_11")
    op.drop_table("forecast_value_2024_11")
    op.drop_index("forecast_value_2024_10_target_time_idx", table_name="forecast_value_2024_10")
    op.drop_index("forecast_value_2024_10_forecast_id_idx", table_name="forecast_value_2024_10")
    op.drop_index("forecast_value_2024_10_created_utc_idx", table_name="forecast_value_2024_10")
    op.drop_table("forecast_value_2024_10")
    op.drop_index("forecast_value_2024_09_target_time_idx", table_name="forecast_value_2024_09")
    op.drop_index("forecast_value_2024_09_forecast_id_idx", table_name="forecast_value_2024_09")
    op.drop_index("forecast_value_2024_09_created_utc_idx", table_name="forecast_value_2024_09")
    op.drop_table("forecast_value_2024_09")
    op.drop_index("forecast_value_2024_08_target_time_idx", table_name="forecast_value_2024_08")
    op.drop_index("forecast_value_2024_08_forecast_id_idx", table_name="forecast_value_2024_08")
    op.drop_index("forecast_value_2024_08_created_utc_idx", table_name="forecast_value_2024_08")
    op.drop_table("forecast_value_2024_08")
    op.drop_index("forecast_value_2024_07_target_time_idx", table_name="forecast_value_2024_07")
    op.drop_index("forecast_value_2024_07_forecast_id_idx", table_name="forecast_value_2024_07")
    op.drop_index("forecast_value_2024_07_created_utc_idx", table_name="forecast_value_2024_07")
    op.drop_table("forecast_value_2024_07")
    op.drop_index("forecast_value_2024_06_target_time_idx", table_name="forecast_value_2024_06")
    op.drop_index("forecast_value_2024_06_forecast_id_idx", table_name="forecast_value_2024_06")
    op.drop_index("forecast_value_2024_06_created_utc_idx", table_name="forecast_value_2024_06")
    op.drop_table("forecast_value_2024_06")
    op.drop_index("forecast_value_2024_05_target_time_idx", table_name="forecast_value_2024_05")
    op.drop_index("forecast_value_2024_05_forecast_id_idx", table_name="forecast_value_2024_05")
    op.drop_index("forecast_value_2024_05_created_utc_idx", table_name="forecast_value_2024_05")
    op.drop_table("forecast_value_2024_05")
    op.drop_index("forecast_value_2024_04_target_time_idx", table_name="forecast_value_2024_04")
    op.drop_index("forecast_value_2024_04_forecast_id_idx", table_name="forecast_value_2024_04")
    op.drop_index("forecast_value_2024_04_created_utc_idx", table_name="forecast_value_2024_04")
    op.drop_table("forecast_value_2024_04")
    op.drop_index("forecast_value_2024_03_target_time_idx", table_name="forecast_value_2024_03")
    op.drop_index("forecast_value_2024_03_forecast_id_idx", table_name="forecast_value_2024_03")
    op.drop_index("forecast_value_2024_03_created_utc_idx", table_name="forecast_value_2024_03")
    op.drop_table("forecast_value_2024_03")
    op.drop_index("forecast_value_2024_02_target_time_idx", table_name="forecast_value_2024_02")
    op.drop_index("forecast_value_2024_02_forecast_id_idx", table_name="forecast_value_2024_02")
    op.drop_index("forecast_value_2024_02_created_utc_idx", table_name="forecast_value_2024_02")
    op.drop_table("forecast_value_2024_02")
    op.drop_index("forecast_value_2024_01_target_time_idx", table_name="forecast_value_2024_01")
    op.drop_index("forecast_value_2024_01_forecast_id_idx", table_name="forecast_value_2024_01")
    op.drop_index("forecast_value_2024_01_created_utc_idx", table_name="forecast_value_2024_01")
    op.drop_table("forecast_value_2024_01")
    op.drop_index("forecast_value_2022_08_target_time_idx", table_name="forecast_value_2022_08")
    op.drop_index("forecast_value_2022_08_forecast_id_idx", table_name="forecast_value_2022_08")
    op.drop_index("forecast_value_2022_08_created_utc_idx", table_name="forecast_value_2022_08")
    op.drop_table("forecast_value_2022_08")
    # ### end Alembic commands ###
