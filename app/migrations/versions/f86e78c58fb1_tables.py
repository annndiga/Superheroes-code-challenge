"""tables

Revision ID: f86e78c58fb1
Revises: 
Create Date: 2023-09-25 15:19:59.915166

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f86e78c58fb1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('heroes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('super_name', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('powers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('hero_powers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('strength', sa.String(length=255), nullable=True),
    sa.Column('hero_id', sa.Integer(), nullable=True),
    sa.Column('power_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['hero_id'], ['heroes.id'], ),
    sa.ForeignKeyConstraint(['power_id'], ['powers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hero_powers')
    op.drop_table('powers')
    op.drop_table('heroes')
    # ### end Alembic commands ###
