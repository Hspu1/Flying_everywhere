"""empty message

Revision ID: e8aeafb1db65
Revises: 
Create Date: 2024-12-31 19:43:04.223708

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e8aeafb1db65'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('aircraft',
            sa.Column('aircraft_id', sa.Integer(), autoincrement=True, nullable=False),
            sa.Column('name', sa.String(length=20), nullable=False),
            sa.Column('weight', sa.Integer(), nullable=False),
            sa.Column('length', sa.Integer(), nullable=False),
            sa.PrimaryKeyConstraint('aircraft_id')
    )
    op.create_index(op.f('ix_aircraft_name'), 'aircraft', ['name'], unique=True)
    op.create_table('flight',
            sa.Column('flight_id', sa.Integer(), autoincrement=True, nullable=False),
            sa.Column('flight_name', sa.String(length=30), nullable=False),
            sa.Column('departure_country', sa.String(length=50), nullable=False),
            sa.Column('departure_city', sa.String(length=50), nullable=False),
            sa.Column('departure_date_time', sa.DateTime(), nullable=False, comment='format -> YYYY-MM-DD HH:MI:SS'),
            sa.Column('arrival_country', sa.String(length=50), nullable=False),
            sa.Column('arrival_city', sa.String(length=50), nullable=False),
            sa.Column('arrival_date_time', sa.DateTime(), nullable=False, comment='format -> YYYY-MM-DD HH:MI:SS'),
            sa.Column('aircraft_name', sa.String(), nullable=True),
            sa.Column('ticket_cost', sa.Integer(), nullable=False),
            sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
            sa.ForeignKeyConstraint(['aircraft_name'], ['aircraft.name'], ),
            sa.PrimaryKeyConstraint('flight_id')
    )
    op.create_index(op.f('ix_flight_flight_name'), 'flight', ['flight_name'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_flight_flight_name'), table_name='flight')
    op.drop_table('flight')
    op.drop_index(op.f('ix_aircraft_name'), table_name='aircraft')
    op.drop_table('aircraft')
    # ### end Alembic commands ###
