"""modify user table

Revision ID: 62b83a09d1b4
Revises: 80d06607a18a
Create Date: 2019-12-31 11:01:45.107250

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62b83a09d1b4'
down_revision = '80d06607a18a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(), nullable=True))
    op.add_column('users', sa.Column('password', sa.String(), nullable=False))
    op.add_column('users', sa.Column('status', sa.String(), nullable=True))
    op.add_column('users', sa.Column('street_no', sa.String(), nullable=True))
    op.add_column('users', sa.Column('username', sa.String(), nullable=False))
    op.create_unique_constraint(None, 'users', ['username'])
    op.create_unique_constraint(None, 'users', ['email'])
    op.drop_column('users', 'address_2')
    op.drop_column('users', 'state')
    op.drop_column('users', 'address_1')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('address_1', sa.VARCHAR(),
                  autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('state', sa.VARCHAR(),
                  autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('address_2', sa.VARCHAR(),
                  autoincrement=False, nullable=True))
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'username')
    op.drop_column('users', 'street_no')
    op.drop_column('users', 'status')
    op.drop_column('users', 'password')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###
