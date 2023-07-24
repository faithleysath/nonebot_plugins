"""add time-weight table

Revision ID: 5f3370328e44
Revises: a333d6224193
Create Date: 2022-05-31 22:05:13.235981

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "5f3370328e44"
down_revision = "a333d6224193"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "schedule_time_weight",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("target_id", sa.Integer(), nullable=True),
        sa.Column("start_time", sa.Time(), nullable=True),
        sa.Column("end_time", sa.Time(), nullable=True),
        sa.Column("weight", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["target_id"],
            ["target.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("target", schema=None) as batch_op:
        batch_op.add_column(sa.Column("default_schedule_weight", sa.Integer(), nullable=True))
        batch_op.drop_column("last_schedule_time")

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("target", schema=None) as batch_op:
        batch_op.add_column(sa.Column("last_schedule_time", sa.DATETIME(), nullable=True))
        batch_op.drop_column("default_schedule_weight")

    op.drop_table("schedule_time_weight")
    # ### end Alembic commands ###
