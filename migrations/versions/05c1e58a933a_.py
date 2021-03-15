"""empty message

Revision ID: 05c1e58a933a
Revises: 7f1c2a93a084
Create Date: 2021-03-14 02:01:53.537713

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05c1e58a933a'
down_revision = '7f1c2a93a084'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('properties', 'bathrooms')
    op.drop_column('properties', 'location')
    op.drop_column('properties', 'description')
    op.drop_column('properties', 'prop_type')
    op.drop_column('properties', 'rooms')
    op.drop_column('properties', 'photo')
    op.drop_column('properties', 'price')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('properties', sa.Column('price', sa.VARCHAR(length=80), autoincrement=False, nullable=True))
    op.add_column('properties', sa.Column('photo', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('properties', sa.Column('rooms', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('properties', sa.Column('prop_type', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('properties', sa.Column('description', sa.VARCHAR(length=80), autoincrement=False, nullable=True))
    op.add_column('properties', sa.Column('location', sa.VARCHAR(length=80), autoincrement=False, nullable=True))
    op.add_column('properties', sa.Column('bathrooms', sa.VARCHAR(length=80), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
