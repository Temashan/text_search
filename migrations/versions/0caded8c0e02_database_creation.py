"""Database creation

Revision ID: 0caded8c0e02
Revises: 
Create Date: 2023-06-13 15:24:30.268843

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0caded8c0e02'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('docs',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('rubrics', sa.String(length=45), nullable=False),
    sa.Column('texts', sa.Text(), nullable=False),
    sa.Column('created_date', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('docs')
    # ### end Alembic commands ###
