"""Migrates the incident metadata json

Revision ID: cfd62f719c84
Revises: 9b4a5ff08170
Create Date: 2020-05-26 20:17:47.707953

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "cfd62f719c84"
down_revision = "9b4a5ff08170"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("incident_type", "plugin_metadata")
    op.add_column("incident_type", sa.Column("plugin_metadata", sa.JSON(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
