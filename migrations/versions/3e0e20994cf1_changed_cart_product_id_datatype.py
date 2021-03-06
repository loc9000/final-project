"""Changed cart.product_id datatype

Revision ID: 3e0e20994cf1
Revises: 1578cff1c968
Create Date: 2022-06-02 16:55:16.461581

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e0e20994cf1'
down_revision = '1578cff1c968'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cart', sa.Column('product_id', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cart', 'product_id')
    # ### end Alembic commands ###
