"""followers

Revision ID: 221b14d2b2b2
Revises: b321e2452895
Create Date: 2023-02-24 14:46:12.231607

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '221b14d2b2b2'
down_revision = 'b321e2452895'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
