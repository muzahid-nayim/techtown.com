"""empty message

Revision ID: 69455a648010
Revises: 
Create Date: 2023-08-03 09:23:30.649809

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69455a648010'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('brand',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('logo', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_release', sa.String(length=100), nullable=True),
    sa.Column('colors', sa.String(length=100), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('manufactured_by', sa.String(length=100), nullable=True),
    sa.Column('made_in', sa.String(length=100), nullable=True),
    sa.Column('model', sa.String(length=100), nullable=True),
    sa.Column('image_file', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('back_camera',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('resolution', sa.String(length=100), nullable=True),
    sa.Column('features', sa.String(length=100), nullable=True),
    sa.Column('video_recording', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('battery',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('type_capacity', sa.String(length=100), nullable=True),
    sa.Column('fast_charging', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('body',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('style', sa.String(length=100), nullable=True),
    sa.Column('material', sa.String(length=100), nullable=True),
    sa.Column('water_resistance', sa.String(length=100), nullable=True),
    sa.Column('dimensions', sa.String(length=100), nullable=True),
    sa.Column('weight', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('connectivity',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('network', sa.String(length=100), nullable=True),
    sa.Column('sim', sa.String(length=100), nullable=True),
    sa.Column('wlan', sa.String(length=100), nullable=True),
    sa.Column('bluetooth', sa.String(length=100), nullable=True),
    sa.Column('gps', sa.String(length=100), nullable=True),
    sa.Column('radio', sa.String(length=100), nullable=True),
    sa.Column('usb', sa.String(length=100), nullable=True),
    sa.Column('otg', sa.Boolean(), nullable=True),
    sa.Column('usb_type_c', sa.Boolean(), nullable=True),
    sa.Column('nfc', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('display',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('size', sa.String(length=100), nullable=True),
    sa.Column('resolution', sa.String(length=100), nullable=True),
    sa.Column('technology', sa.String(length=100), nullable=True),
    sa.Column('protection', sa.String(length=100), nullable=True),
    sa.Column('features', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('front_camera',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('resolution', sa.String(length=100), nullable=True),
    sa.Column('features', sa.String(length=100), nullable=True),
    sa.Column('video_recording', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('others',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('notification_light', sa.String(length=100), nullable=True),
    sa.Column('sensors', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('performance',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('operating_system', sa.String(length=100), nullable=True),
    sa.Column('chipset', sa.String(length=100), nullable=True),
    sa.Column('processor', sa.String(length=100), nullable=True),
    sa.Column('speed', sa.String(length=100), nullable=True),
    sa.Column('gpu', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('security',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('fingerprint', sa.String(length=100), nullable=True),
    sa.Column('face_unlock', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sound',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('jack_3_5mm', sa.String(length=100), nullable=True),
    sa.Column('features', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('storage',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('ram', sa.String(length=100), nullable=True),
    sa.Column('rom', sa.String(length=100), nullable=True),
    sa.Column('microsd_slot', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('storage')
    op.drop_table('sound')
    op.drop_table('security')
    op.drop_table('performance')
    op.drop_table('others')
    op.drop_table('front_camera')
    op.drop_table('display')
    op.drop_table('connectivity')
    op.drop_table('body')
    op.drop_table('battery')
    op.drop_table('back_camera')
    op.drop_table('product')
    op.drop_table('brand')
    # ### end Alembic commands ###