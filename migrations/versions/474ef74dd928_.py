"""empty message

Revision ID: 474ef74dd928
Revises: 6efa7b991483
Create Date: 2021-03-08 17:04:16.105581

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '474ef74dd928'
down_revision = '6efa7b991483'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('anime',
    sa.Column('mal_id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=200), nullable=True),
    sa.Column('image_url', sa.String(length=200), nullable=True),
    sa.Column('local_image_url', sa.String(length=50), nullable=True),
    sa.Column('title', sa.String(length=200), nullable=False),
    sa.Column('title_english', sa.String(length=200), nullable=True),
    sa.Column('title_japanese', sa.String(length=200), nullable=True),
    sa.Column('format_type', sa.String(length=50), nullable=True),
    sa.Column('source', sa.String(length=50), nullable=True),
    sa.Column('episodes', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(length=50), nullable=True),
    sa.Column('aired_from', sa.DateTime(), nullable=True),
    sa.Column('aired_to', sa.DateTime(), nullable=True),
    sa.Column('score', sa.Float(), nullable=True),
    sa.Column('scored_by', sa.Integer(), nullable=True),
    sa.Column('rank', sa.Integer(), nullable=True),
    sa.Column('popularity', sa.Integer(), nullable=True),
    sa.Column('members', sa.Integer(), nullable=True),
    sa.Column('favorites', sa.Integer(), nullable=True),
    sa.Column('premiered', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('mal_id')
    )
    op.create_table('character',
    sa.Column('mal_id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=200), nullable=True),
    sa.Column('image_url', sa.String(length=200), nullable=True),
    sa.Column('local_image_url', sa.String(length=50), nullable=True),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('member_favorites', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('mal_id')
    )
    op.create_table('manga',
    sa.Column('mal_id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=200), nullable=True),
    sa.Column('title', sa.String(length=200), nullable=False),
    sa.Column('title_english', sa.String(length=200), nullable=True),
    sa.Column('title_japanese', sa.String(length=200), nullable=True),
    sa.Column('image_url', sa.String(length=200), nullable=True),
    sa.Column('local_image_url', sa.String(length=50), nullable=True),
    sa.Column('status', sa.String(length=50), nullable=True),
    sa.Column('work_type', sa.String(length=50), nullable=True),
    sa.Column('volumes', sa.Integer(), nullable=True),
    sa.Column('chapters', sa.Integer(), nullable=True),
    sa.Column('publishing', sa.String(length=50), nullable=True),
    sa.Column('published_from', sa.DateTime(), nullable=True),
    sa.Column('published_to', sa.DateTime(), nullable=True),
    sa.Column('rank', sa.Integer(), nullable=True),
    sa.Column('score', sa.Float(), nullable=True),
    sa.Column('scored_by', sa.Integer(), nullable=True),
    sa.Column('popularity', sa.Integer(), nullable=True),
    sa.Column('members', sa.Integer(), nullable=True),
    sa.Column('favorites', sa.Integer(), nullable=True),
    sa.Column('serialization', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('mal_id')
    )
    op.create_table('page_status',
    sa.Column('id', sa.String(length=50), nullable=False),
    sa.Column('mal_id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(length=50), nullable=False),
    sa.Column('exists', sa.Boolean(), nullable=False),
    sa.Column('last_modified', sa.DateTime(), nullable=True),
    sa.Column('updating', sa.Boolean(), nullable=True),
    sa.Column('scheduled_to_update', sa.Boolean(), nullable=True),
    sa.Column('scheduled_time', sa.DateTime(), nullable=True),
    sa.Column('task_id', sa.String(length=100), nullable=True),
    sa.Column('update_failed', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('person',
    sa.Column('mal_id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=200), nullable=True),
    sa.Column('image_url', sa.String(length=200), nullable=True),
    sa.Column('local_image_url', sa.String(length=50), nullable=True),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('given_name', sa.String(length=200), nullable=True),
    sa.Column('family_name', sa.String(length=200), nullable=True),
    sa.Column('birthday', sa.DateTime(), nullable=True),
    sa.Column('member_favorites', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('mal_id')
    )
    op.create_table('studio',
    sa.Column('mal_id', sa.Integer(), nullable=False),
    sa.Column('work_type', sa.String(length=100), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('url', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('mal_id')
    )
    op.create_table('characters',
    sa.Column('character_id', sa.Integer(), nullable=False),
    sa.Column('anime_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['anime_id'], ['anime.mal_id'], ),
    sa.ForeignKeyConstraint(['character_id'], ['character.mal_id'], ),
    sa.PrimaryKeyConstraint('character_id', 'anime_id')
    )
    op.create_table('manga_author',
    sa.Column('id', sa.String(length=200), nullable=False),
    sa.Column('position', sa.String(length=100), nullable=True),
    sa.Column('author_type', sa.String(length=100), nullable=True),
    sa.Column('person_id', sa.Integer(), nullable=True),
    sa.Column('manga_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['manga_id'], ['manga.mal_id'], ),
    sa.ForeignKeyConstraint(['person_id'], ['person.mal_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('staff_member',
    sa.Column('id', sa.String(length=200), nullable=False),
    sa.Column('position', sa.String(length=200), nullable=False),
    sa.Column('person_id', sa.Integer(), nullable=True),
    sa.Column('anime_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['anime_id'], ['anime.mal_id'], ),
    sa.ForeignKeyConstraint(['person_id'], ['person.mal_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('studios',
    sa.Column('studio_id', sa.Integer(), nullable=False),
    sa.Column('anime_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['anime_id'], ['anime.mal_id'], ),
    sa.ForeignKeyConstraint(['studio_id'], ['studio.mal_id'], ),
    sa.PrimaryKeyConstraint('studio_id', 'anime_id')
    )
    op.create_table('voice_actor',
    sa.Column('id', sa.String(length=200), nullable=False),
    sa.Column('role', sa.String(length=100), nullable=False),
    sa.Column('language', sa.String(length=100), nullable=True),
    sa.Column('anime_id', sa.Integer(), nullable=True),
    sa.Column('person_id', sa.Integer(), nullable=True),
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['anime_id'], ['anime.mal_id'], ),
    sa.ForeignKeyConstraint(['character_id'], ['character.mal_id'], ),
    sa.ForeignKeyConstraint(['person_id'], ['person.mal_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('voice_actor')
    op.drop_table('studios')
    op.drop_table('staff_member')
    op.drop_table('manga_author')
    op.drop_table('characters')
    op.drop_table('studio')
    op.drop_table('person')
    op.drop_table('page_status')
    op.drop_table('manga')
    op.drop_table('character')
    op.drop_table('anime')
    # ### end Alembic commands ###