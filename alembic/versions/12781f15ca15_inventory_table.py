"""Inventory Table

Revision ID: 12781f15ca15
Revises: 
Create Date: 2022-11-20 18:36:26.102135

"""
from alembic import op
from sqlalchemy import INTEGER, VARCHAR, NVARCHAR, Column
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12781f15ca15'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'inventory',
        Column('id', INTEGER, primary_key=True),
        Column('name', VARCHAR, nullable=False),
        Column('price', INTEGER),
        Column('brand', VARCHAR, nullable=False)
    )

def downgrade() -> None:
    op.drop_table('inventory')
