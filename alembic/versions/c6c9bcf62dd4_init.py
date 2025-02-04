"""init

Revision ID: c6c9bcf62dd4
Revises: 
Create Date: 2024-05-12 14:17:14.908690

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c6c9bcf62dd4'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstName', sa.String(length=100), nullable=False),
    sa.Column('lastName', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('details',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=300), nullable=False),
    sa.Column('icon', sa.String(length=300), nullable=False),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('mileages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mileage', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('payments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=300), nullable=False),
    sa.Column('payload', sa.JSON(), nullable=False),
    sa.Column('bill_photo', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('automobiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('mark', sa.String(length=100), nullable=False),
    sa.Column('model', sa.String(length=100), nullable=False),
    sa.Column('mileage', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['mileage'], ['mileages.id'], name='fk_automobiles_mileages_id_mileage'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('automobiles_mileages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mileage', sa.Integer(), nullable=True),
    sa.Column('automobile', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['automobile'], ['automobiles.id'], name='fk_automobiles_mileages_automobiles_automobile_id', onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['mileage'], ['mileages.id'], name='fk_automobiles_mileages_mileages_mileage_id', onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('automobiles_mileages')
    op.drop_table('automobiles')
    op.drop_table('payments')
    op.drop_table('mileages')
    op.drop_table('details')
    op.drop_table('users')
    # ### end Alembic commands ###
