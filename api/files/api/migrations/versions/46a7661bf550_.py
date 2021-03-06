"""empty message

Revision ID: 46a7661bf550
Revises: 4587ab57e009
Create Date: 2016-07-26 14:23:22.840607

"""

# revision identifiers, used by Alembic.
revision = '46a7661bf550'
down_revision = '4587ab57e009'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('google_cloud_billing_bucket')
    op.drop_table('google_cloud_project')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('google_cloud_billing_bucket',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('id_project', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=224), nullable=False),
    sa.ForeignKeyConstraint(['id_project'], [u'google_cloud_project.id'], name=u'google_cloud_billing_bucket_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    op.create_table('google_cloud_project',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('id_identity', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('code', mysql.VARCHAR(length=64), nullable=False),
    sa.Column('number', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=64), nullable=False),
    sa.ForeignKeyConstraint(['id_identity'], [u'google_cloud_identity.id'], name=u'google_cloud_project_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    ### end Alembic commands ###
