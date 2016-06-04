"""empty message

Revision ID: 234dd0c42dfb
Revises: 5a38298967ce
Create Date: 2016-06-02 23:11:49.732908

"""

# revision identifiers, used by Alembic.
revision = '234dd0c42dfb'
down_revision = '5a38298967ce'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('title', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blogs', 'title')
    ### end Alembic commands ###