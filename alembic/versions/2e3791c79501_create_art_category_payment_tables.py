"""create art, category & payment tables

Revision ID: 2e3791c79501
Revises: b8359611099e
Create Date: 2019-12-24 14:14:04.370105

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e3791c79501'
down_revision = 'b8359611099e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('arts',
    sa.Column('date_created', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('date_updated', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('no', sa.String(), nullable=False),
    sa.Column('category', sa.String(), nullable=False),
    sa.Column('label', sa.String(), nullable=False),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('details', sa.Text(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('owner', sa.BIGINT(), nullable=False),
    sa.PrimaryKeyConstraint('no')
    )
    op.create_table('categories',
    sa.Column('date_created', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('date_updated', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('no', sa.String(), nullable=False),
    sa.Column('category', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('no')
    )
    op.create_table('payments',
    sa.Column('date_created', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('date_updated', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('no', sa.String(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.Column('payment_method', sa.String(), nullable=False),
    sa.Column('transfer_no', sa.String(), nullable=False),
    sa.Column('item', sa.String(), nullable=False),
    sa.Column('owner', sa.BIGINT(), nullable=False),
    sa.PrimaryKeyConstraint('no')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('payments')
    op.drop_table('categories')
    op.drop_table('arts')
    # ### end Alembic commands ###