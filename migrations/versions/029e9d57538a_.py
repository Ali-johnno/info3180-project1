"""empty message

Revision ID: 029e9d57538a
Revises: 05c1e58a933a
Create Date: 2021-03-14 02:02:42.950699

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '029e9d57538a'
down_revision = '05c1e58a933a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('properties', sa.Column('bathrooms', sa.String(), nullable=True))
    op.add_column('properties', sa.Column('description', sa.String(), nullable=True))
    op.add_column('properties', sa.Column('location', sa.String(), nullable=True))
    op.add_column('properties', sa.Column('photo', sa.String(), nullable=True))
    op.add_column('properties', sa.Column('price', sa.String(), nullable=True))
    op.add_column('properties', sa.Column('prop_type', sa.String(), nullable=True))
    op.add_column('properties', sa.Column('rooms', sa.String(), nullable=True))
    op.drop_column('properties', 'title')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('properties', sa.Column('title', sa.VARCHAR(length=80), autoincrement=False, nullable=True))
    op.drop_column('properties', 'rooms')
    op.drop_column('properties', 'prop_type')
    op.drop_column('properties', 'price')
    op.drop_column('properties', 'photo')
    op.drop_column('properties', 'location')
    op.drop_column('properties', 'description')
    op.drop_column('properties', 'bathrooms')
    # ### end Alembic commands ###