"""empty message

Revision ID: c98e41feed23
Revises: e4d19e444bab
Create Date: 2021-02-03 01:40:11.413937

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c98e41feed23'
down_revision = 'e4d19e444bab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('page_status')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('page_status',
    sa.Column('mal_id', sa.INTEGER(), nullable=False),
    sa.Column('category', sa.VARCHAR(length=50), nullable=False),
    sa.Column('last_modified', sa.DATETIME(), nullable=False),
    sa.Column('updating', sa.BOOLEAN(), nullable=True),
    sa.CheckConstraint('updating IN (0, 1)'),
    sa.PrimaryKeyConstraint('mal_id')
    )
    # ### end Alembic commands ###