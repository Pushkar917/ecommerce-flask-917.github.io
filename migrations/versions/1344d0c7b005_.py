"""empty message

Revision ID: 1344d0c7b005
Revises: 
Create Date: 2020-11-05 13:07:56.930669

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1344d0c7b005'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('brands',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=256), nullable=True),
    sa.Column('username', sa.String(length=256), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=90), nullable=False),
    sa.Column('price', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('discount', sa.Integer(), nullable=True),
    sa.Column('stock', sa.Integer(), nullable=False),
    sa.Column('colors', sa.Text(), nullable=False),
    sa.Column('desc', sa.Text(), nullable=False),
    sa.Column('pub_date', sa.DateTime(), nullable=True),
    sa.Column('brand_id', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('image_1', sa.String(length=150), nullable=False),
    sa.Column('image_2', sa.String(length=150), nullable=False),
    sa.Column('image_3', sa.String(length=150), nullable=False),
    sa.ForeignKeyConstraint(['brand_id'], ['brands.id'], ),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_table('users')
    op.drop_table('category')
    op.drop_table('brands')
    # ### end Alembic commands ###
