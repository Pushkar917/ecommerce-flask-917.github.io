"""empty message

Revision ID: e7d126d4ae81
Revises: 1344d0c7b005
Create Date: 2020-11-13 09:15:57.480656

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7d126d4ae81'
down_revision = '1344d0c7b005'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Customers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=256), nullable=True),
    sa.Column('email', sa.String(length=256), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('country', sa.Text(), nullable=False),
    sa.Column('state', sa.Text(), nullable=False),
    sa.Column('city', sa.Text(), nullable=False),
    sa.Column('contact', sa.Text(), nullable=False),
    sa.Column('address', sa.Text(), nullable=False),
    sa.Column('zipcode', sa.Text(), nullable=False),
    sa.Column('image', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Customers_username'), 'Customers', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_Customers_username'), table_name='Customers')
    op.drop_table('Customers')
    # ### end Alembic commands ###
