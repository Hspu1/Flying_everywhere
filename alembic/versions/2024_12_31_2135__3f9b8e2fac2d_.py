"""empty message

Revision ID: 3f9b8e2fac2d
Revises: 4e2a1eeacf9d
Create Date: 2024-12-31 21:35:38.728542

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3f9b8e2fac2d'
down_revision: Union[str, None] = '4e2a1eeacf9d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('aircraft', sa.Column('weight_in_tons', sa.Integer(), nullable=False))
    op.add_column('aircraft', sa.Column('length_in_meters', sa.Integer(), nullable=False))
    op.drop_column('aircraft', 'weight')
    op.drop_column('aircraft', 'length')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('aircraft', sa.Column('length', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('aircraft', sa.Column('weight', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_column('aircraft', 'length_in_meters')
    op.drop_column('aircraft', 'weight_in_tons')
    # ### end Alembic commands ###