# application/admin/route.py

from flask import Blueprint, render_template,redirect,url_for
from flask_login import login_required, current_user
from application.utils.admin_required import admin_required
from application.admin.form import AddBrandForm
from application.admin.form import EditBrandForm
from application.models import Brand
from application import db
from application.utils.helper import save_brand_image
import os
from flask import current_app



admin = Blueprint('admin', __name__)

# START DASHBOARD ROUTE 
@admin.route('/admin-dashboard/')
@login_required  # This ensures that only authenticated users can access the dashboard route
@admin_required  # This ensures that only users with the 'admin' role can access the dashboard route
def adminDashboard():
    brands = Brand.query.all()
    return render_template('admin/dashboard.html', brands=brands)
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
        # Check if the brand name already exists in the database
        existing_brand = Brand.query.filter_by(name=form.name.data).first()
        if existing_brand:
            form.name.errors.append('Brand name already exists.')
        else:
            if form.logo.data:  # Check if the logo field is populated with data
                logo_filename = save_brand_image(form.logo.data)
            else:
                logo_filename = 'default.jpg'
            brand = Brand(name=form.name.data, logo=logo_filename)
            db.session.add(brand)
            db.session.commit()
            # Optional: Redirect to a different page or show a success message
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
        existing_brand = Brand.query.filter(Brand.id != brand.id, Brand.name == form.name.data).first()
        if existing_brand:
            form.name.errors.append('Brand name already exists.')
        else:
            if form.logo.data: 
                # Delete the previous logo image if it exists
                if brand.logo != 'default.jpg':
                    old_logo_path = os.path.join(current_app.root_path, 'static', 'brand_logos', brand.logo)
                    os.remove(old_logo_path)

                logo_filename = save_brand_image(form.logo.data)
            else:
                logo_filename = brand.logo  
            brand.name = form.name.data
            brand.logo = logo_filename
            db.session.commit()
            return redirect(url_for('admin.brands'))

    form.name.data = brand.name

    return render_template('admin/edit_brand.html', form=form, brand=brand)

# END EDIT BRAND ROUTE

# START DELETE BRAND ROUTE 
@admin.route('/brands/delete/<int:brand_id>', methods=['POST', 'DELETE'])
def delete_brand(brand_id):
    brand = Brand.query.get_or_404(brand_id)
    
    # Delete the brand logo file from the folder
    if brand.logo and brand.logo != 'default.jpg':
        logo_path = os.path.join(current_app.root_path, 'static', 'brand_logos', brand.logo)
        if os.path.exists(logo_path):
            os.remove(logo_path)

    # Delete the brand from the database
    db.session.delete(brand)
    db.session.commit()

    return redirect(url_for('admin.brands'))
# END DELETE BRAND ROUTE 

# START PRODUCTS ROUTE 
@admin.route('/admin-dashboard/products')
@login_required
@admin_required
def products():
    return render_template('admin/products.html')
# END PRODUCTS ROUTE 
