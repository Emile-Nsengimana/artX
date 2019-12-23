"""constraint keys

Revision ID: b5f8736b5a23
Revises: 2e3791c79501
Create Date: 2019-12-24 17:05:54.679254

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b5f8736b5a23'
down_revision = '2e3791c79501'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'arts', 'users', ['owner'], ['user_id'])
    op.drop_column('arts', 'category')
    op.create_foreign_key(None, 'categories', 'arts', ['category'], ['no'])
    op.create_foreign_key(None, 'payments', 'users', ['owner'], ['user_id'])
    op.create_foreign_key(None, 'payments', 'arts', ['item'], ['no'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'payments', type_='foreignkey')
    op.drop_constraint(None, 'payments', type_='foreignkey')
    op.drop_constraint(None, 'categories', type_='foreignkey')
    op.add_column('arts', sa.Column('category', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'arts', type_='foreignkey')
    # ### end Alembic commands ###