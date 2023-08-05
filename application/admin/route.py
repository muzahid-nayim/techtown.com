

from flask import Blueprint, render_template,redirect,url_for,flash
from flask_login import login_required, current_user
from application.utils.admin_required import admin_required
from application.admin.form import AddBrandForm,EditBrandForm,ProductForm
from application.models import Brand
from application.models import Product, Connectivity, Body, Display, BackCamera, FrontCamera, Battery, Performance, Storage, Sound, Security, Others
from application import db
from application.utils.helper import save_brand_image,save_product_image
import os
from flask import current_app



admin = Blueprint('admin', __name__)

# START DASHBOARD ROUTE 
@admin.route('/admin-dashboard/')
@login_required 
@admin_required 
def adminDashboard():
    brands = Brand.query.all()
    products = Product.query.all()
    return render_template('admin/dashboard.html', brands=brands, products=products)
# END DASHBOARD ROUTE 


# START  BRAND ROUTE 
@admin.route('/admin-dashboard/brands')
@login_required
@admin_required
def brands():
    brands = Brand.query.all()
    return render_template('admin/brands.html', brands=brands)
# END   BRAND ROUTE 


# START ADD BRAND ROUTE 
@admin.route('/admin-dashboard/add-brand', methods=['GET', 'POST'])
@login_required
@admin_required
def addBrand():
    form = AddBrandForm()

    if form.validate_on_submit():
        existing_brand = Brand.query.filter_by(name=form.brand_name.data).first()
        if existing_brand:
            form.brand_name.errors.append('Brand name already exists.')
        else:
            if form.logo.data:
                logo_filename = save_brand_image(form.logo.data)
            else:
                logo_filename = 'default.jpg'
            brand = Brand(name=form.brand_name.data, logo=logo_filename)
            db.session.add(brand)
            db.session.commit()
            return redirect(url_for('admin.brands'))

    return render_template('admin/add_brand.html', form=form)

# END ADD BRAND ROUTE 


# START EDIT BRAND ROUTE
@admin.route('/admin-dashboard/edit-brand/<int:brand_id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_brand(brand_id):
    brand = Brand.query.get_or_404(brand_id)
    form = EditBrandForm()

    if form.validate_on_submit():
        existing_brand = Brand.query.filter(Brand.name == form.brand_name.data).first()
        if existing_brand:
            form.brand_name.errors.append('Brand name already exists.')
        else:
            if form.logo.data: 
                if brand.logo != 'default.jpg':
                    old_logo_path = os.path.join(current_app.root_path, 'static', 'brand_logos', brand.logo)
                    os.remove(old_logo_path)

                logo_filename = save_brand_image(form.logo.data)
            else:
                logo_filename = brand.logo  
            brand.name = form.brand_name.data
            brand.logo = logo_filename
            db.session.commit()
            return redirect(url_for('admin.brands'))

    form.brand_name.data = brand.name
    return render_template('admin/edit_brand.html', form=form, brand=brand)

# END EDIT BRAND ROUTE

# START DELETE BRAND ROUTE 
@login_required
@admin_required
@admin.route('/brands/delete/<int:brand_id>', methods=['POST', 'DELETE'])
def delete_brand(brand_id):
    brand = Brand.query.get_or_404(brand_id)

    if brand.logo and brand.logo != 'default.jpg':
        logo_path = os.path.join(current_app.root_path, 'static', 'brand_logos', brand.logo)
        if os.path.exists(logo_path):
            os.remove(logo_path)
            
    db.session.delete(brand)
    db.session.commit()

    return redirect(url_for('admin.brands'))
# END DELETE BRAND ROUTE 

def get_brand_name(brand_id):
    brand = Brand.query.get(brand_id)
    if brand:
        return brand.name
    return None

# START PRODUCTS ROUTE 
@admin.route('/admin-dashboard/products')
@login_required
@admin_required
def products():
    products = Product.query.all()
    return render_template('admin/products.html', products=products, get_brand_name=get_brand_name)
# END PRODUCTS ROUTE 


# START ADD PRODUCT ROUTE 
@login_required
@admin_required
@admin.route('/admin-dashboard/add-product', methods=['GET', 'POST'])
def add_product():
    form = ProductForm()
    
    brand_choices = [(brand.id, brand.name) for brand in Brand.query.all()]
    form.manufactured_by.choices = brand_choices

    if form.validate_on_submit():
        # Create the main Product record
        if form.image.data:
            image_filename = save_product_image(form.image.data)
        else:
            image_filename = 'default.jpg'
        product = Product(
            first_release=form.first_release.data,
            colors=form.colors.data,
            manufactured_by=form.manufactured_by.data,
            made_in=form.made_in.data,
            price=form.price.data,
            model=form.model.data,
            image_file=image_filename
        )
        db.session.add(product)
        db.session.commit()

        # Create the related records in other tables
        connectivity = Connectivity(
            product_id=product.id,
            network=form.network.data,
            sim=form.sim.data,
            wlan=form.wlan.data,
            bluetooth=form.bluetooth.data,
            gps=form.gps.data,
            radio=form.radio.data,
            usb=form.usb.data,
            otg=form.otg.data,
            usb_type_c=form.usb_type_c.data,
            nfc=form.nfc.data
        )
        db.session.add(connectivity)

        body = Body(
            product_id=product.id,
            style=form.style.data,
            material=form.material.data,
            water_resistance=form.water_resistance.data,
            dimensions=form.dimensions.data,
            weight=form.weight.data
        )
        db.session.add(body)

        display = Display(
            product_id=product.id,
            size=form.size.data,
            resolution=form.resolution.data,
            technology=form.technology.data,
            protection=form.protection.data,
            features=form.features_display.data
        )
        db.session.add(display)

        back_camera = BackCamera(
            product_id=product.id,
            resolution=form.resolution_back.data,
            features=form.features_back.data,
            video_recording=form.video_recording_back.data
        )
        db.session.add(back_camera)

        front_camera = FrontCamera(
            product_id=product.id,
            resolution=form.resolution_front.data,
            features=form.features_front.data,
            video_recording=form.video_recording_front.data
        )
        db.session.add(front_camera)

        battery = Battery(
            product_id=product.id,
            type_capacity=form.type_capacity.data,
            fast_charging=form.fast_charging.data
        )
        db.session.add(battery)

        performance = Performance(
            product_id=product.id,
            operating_system=form.os.data,
            chipset=form.chipset.data,
            processor=form.processor.data,
            speed=form.speed.data,
            gpu=form.gpu.data
        )
        db.session.add(performance)

        storage = Storage(
            product_id=product.id,
            ram=form.ram.data,
            rom=form.rom.data,
            microsd_slot=form.microsd_slot.data
        )
        db.session.add(storage)

        sound = Sound(
            product_id=product.id,
            jack_3_5mm=form.mm_jack.data,
            features=form.features_sound.data
        )
        db.session.add(sound)

        security = Security(
            product_id=product.id,
            fingerprint=form.fingerprint.data,
            face_unlock=form.face_unlock.data
        )
        db.session.add(security)

        others = Others(
            product_id=product.id,
            notification_light=form.notification_light.data,
            sensors=form.sensors.data
        )
        db.session.add(others)

        db.session.commit()

        flash('Product added successfully!', 'success')
        return redirect(url_for('admin.products'))

    return render_template('admin/add_product.html', form=form)
# END ADD PRODUCT ROUTE 


# START EDIT PRODUCT ROUTE 
@login_required
@admin_required
@admin.route('/admin-dashboard/edit-product/<int:product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)
    
    form = ProductForm()

    brands = Brand.query.all()
    form.manufactured_by.choices = [(brand.id, brand.name) for brand in brands]
    
    if form.validate_on_submit():
        # Update the main Product record
        product.first_release = form.first_release.data
        product.colors = form.colors.data
        product.manufactured_by = form.manufactured_by.data
        product.made_in = form.made_in.data
        product.price = form.price.data
        product.model = form.model.data

        # Update the image if a new one is provided
        if form.image.data:
            image_filename = save_product_image(form.image.data)
            if product.image_file != 'default.jpg':
                image_path = os.path.join(current_app.root_path, 'static', 'product_images', product.image_file)
                if os.path.exists(image_path):
                    os.remove(image_path)
            product.image_file = image_filename

        # Update the related records in other tables
        connectivity = Connectivity.query.filter_by(product_id=product.id).first()
        if connectivity:
            connectivity.network = form.network.data
            connectivity.sim = form.sim.data
            connectivity.wlan = form.wlan.data
            connectivity.bluetooth = form.bluetooth.data
            connectivity.gps = form.gps.data
            connectivity.radio = form.radio.data
            connectivity.usb = form.usb.data
            connectivity.otg = form.otg.data
            connectivity.usb_type_c = form.usb_type_c.data
            connectivity.nfc = form.nfc.data

        body = Body.query.filter_by(product_id=product.id).first()
        if body:
            body.style = form.style.data
            body.material = form.material.data
            body.water_resistance = form.water_resistance.data
            body.dimensions = form.dimensions.data
            body.weight = form.weight.data

        display = Display.query.filter_by(product_id=product.id).first()
        if display:
            display.size = form.size.data
            display.resolution = form.resolution.data
            display.technology = form.technology.data
            display.protection = form.protection.data
            display.features = form.features_display.data

        back_camera = BackCamera.query.filter_by(product_id=product.id).first()
        if back_camera:
            back_camera.resolution = form.resolution_back.data
            back_camera.features = form.features_back.data
            back_camera.video_recording = form.video_recording_back.data

        front_camera = FrontCamera.query.filter_by(product_id=product.id).first()
        if front_camera:
            front_camera.resolution = form.resolution_front.data
            front_camera.features = form.features_front.data
            front_camera.video_recording = form.video_recording_front.data

        battery = Battery.query.filter_by(product_id=product.id).first()
        if battery:
            battery.type_capacity = form.type_capacity.data
            battery.fast_charging = form.fast_charging.data

        performance = Performance.query.filter_by(product_id=product.id).first()
        if performance:
            performance.operating_system = form.os.data
            performance.chipset = form.chipset.data
            performance.processor = form.processor.data
            performance.speed = form.speed.data
            performance.gpu = form.gpu.data

        storage = Storage.query.filter_by(product_id=product.id).first()
        if storage:
            storage.ram = form.ram.data
            storage.rom = form.rom.data
            storage.microsd_slot = form.microsd_slot.data

        sound = Sound.query.filter_by(product_id=product.id).first()
        if sound:
            sound.jack_3_5mm = form.mm_jack.data
            sound.features = form.features_sound.data

        security = Security.query.filter_by(product_id=product.id).first()
        if security:
            security.fingerprint = form.fingerprint.data
            security.face_unlock = form.face_unlock.data

        others = Others.query.filter_by(product_id=product.id).first()
        if others:
            others.notification_light = form.notification_light.data
            others.sensors = form.sensors.data

        db.session.commit()

        flash('Product updated successfully!', 'success')
        return redirect(url_for('admin.products'))
    else:
        form.first_release.data = product.first_release
        form.colors.data = product.colors
        form.manufactured_by.data = product.manufactured_by
        form.made_in.data = product.made_in
        form.price.data = product.price
        form.model.data = product.model

        if product.connectivity:
            form.network.data = product.connectivity.network
            form.sim.data = product.connectivity.sim
            form.wlan.data = product.connectivity.wlan
            form.bluetooth.data = product.connectivity.bluetooth
            form.gps.data = product.connectivity.gps
            form.radio.data = product.connectivity.radio
            form.usb.data = product.connectivity.usb
            form.otg.data = product.connectivity.otg
            form.usb_type_c.data = product.connectivity.usb_type_c
            form.nfc.data = product.connectivity.nfc

        if product.body:
            form.style.data = product.body.style
            form.material.data = product.body.material
            form.water_resistance.data = product.body.water_resistance
            form.dimensions.data = product.body.dimensions
            form.weight.data = product.body.weight

        if product.display:
            form.size.data = product.display.size
            form.resolution.data = product.display.resolution
            form.technology.data = product.display.technology
            form.protection.data = product.display.protection
            form.features_display.data = product.display.features

        if product.back_camera:
            form.resolution_back.data = product.back_camera.resolution
            form.features_back.data = product.back_camera.features
            form.video_recording_back.data = product.back_camera.video_recording

        if product.front_camera:
            form.resolution_front.data = product.front_camera.resolution
            form.features_front.data = product.front_camera.features
            form.video_recording_front.data = product.front_camera.video_recording

        if product.battery:
            form.type_capacity.data = product.battery.type_capacity
            form.fast_charging.data = product.battery.fast_charging

        if product.performance:
            form.os.data = product.performance.operating_system
            form.chipset.data = product.performance.chipset
            form.processor.data = product.performance.processor
            form.speed.data = product.performance.speed
            form.gpu.data = product.performance.gpu

        if product.storage:
            form.ram.data = product.storage.ram
            form.rom.data = product.storage.rom
            form.microsd_slot.data = product.storage.microsd_slot

        if product.sound:
            form.mm_jack.data = product.sound.jack_3_5mm
            form.features_sound.data = product.sound.features

        if product.security:
            form.fingerprint.data = product.security.fingerprint
            form.face_unlock.data = product.security.face_unlock

        if product.others:
            form.notification_light.data = product.others.notification_light
            form.sensors.data = product.others.sensors



    return render_template('admin/edit_product.html', form=form,)
                          

# END EDIT PRODUCT ROUTE 



# START DELETE ROUTE 
@login_required
@admin_required
@admin.route('/product/delete/<int:product_id>', methods=['GET','POST'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)

    connectivity = Connectivity.query.filter_by(product_id=product_id).first()
    if connectivity:
        db.session.delete(connectivity)

    body = Body.query.filter_by(product_id=product_id).first()
    if body:
        db.session.delete(body)

    display = Display.query.filter_by(product_id=product_id).first()
    if display:
        db.session.delete(display)

    back_camera = BackCamera.query.filter_by(product_id=product_id).first()
    if back_camera:
        db.session.delete(back_camera)

    front_camera = FrontCamera.query.filter_by(product_id=product_id).first()
    if front_camera:
        db.session.delete(front_camera)

    battery = Battery.query.filter_by(product_id=product_id).first()
    if battery:
        db.session.delete(battery)

    performance = Performance.query.filter_by(product_id=product_id).first()
    if performance:
        db.session.delete(performance)

    storage = Storage.query.filter_by(product_id=product_id).first()
    if storage:
        db.session.delete(storage)

    sound = Sound.query.filter_by(product_id=product_id).first()
    if sound:
        db.session.delete(sound)

    security = Security.query.filter_by(product_id=product_id).first()
    if security:
        db.session.delete(security)

    others = Others.query.filter_by(product_id=product_id).first()
    if others:
        db.session.delete(others)

    if product.image_file and product.image_file != 'default.jpg':
        image_path = os.path.join(current_app.root_path, 'static', 'product_images', product.image_file )
        if os.path.exists(image_path):
            os.remove(image_path)

    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('admin.products'))
# END  DELETE ROUTE 