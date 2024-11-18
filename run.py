from flask import Flask, render_template, request, redirect, url_for, flash

from config import Config
from app.routes import address_bp
from app.models import Address
import os

app = Flask(__name__, template_folder='app/templates')  # Explicitly setting the template folder
app.config.from_object(Config)

# Register the blueprint for API endpoints with a URL prefix
app.register_blueprint(address_bp, url_prefix='/api')
 
# Route to render the new home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to render the address list page
@app.route('/addresses', methods=['GET'])
def address_list():
    address = Address()
    active_addresses = address.get_all_active_addresses()  # Fetch only active addresses
    deleted_addresses = address.get_all_deleted_addresses()  # Fetch only deleted addresses
    return render_template('address_list.html', active_addresses=active_addresses, deleted_addresses=deleted_addresses)
 

# Route to render the create address form
@app.route('/create', methods=['GET'])
def render_create_address():
    return render_template('create_address.html')

# Route to handle the create address form submission
@app.route('/create', methods=['POST'])
def handle_create_address():
    name = request.form['name']
    street = request.form['street']
    city = request.form['city']
    state = request.form['state']
    zip_code = request.form['zip_code']
    country = request.form['country']
    address = Address()
    address_id = address.create_address(name, street, city, state, zip_code, country)
    flash('Address created successfully!', 'success')
    return redirect(url_for('home'))
    
# Route to render the edit address form
@app.route('/edit/<int:id>', methods=['GET'])
def render_edit_address(id):
    address = Address()
    address_data = address.get_address_by_id(id)  # Assuming this method exists
    return render_template('edit_address.html', address=address_data)
 
# Route to handle the edit address form submission
@app.route('/edit/<int:id>', methods=['POST'])
def handle_edit_address(id):
    name = request.form['name']
    street = request.form['street']
    city = request.form['city']
    state = request.form['state']
    zip_code = request.form['zip_code']
    country = request.form['country']
    address = Address()
    address.update_address(id, name, street, city, state, zip_code, country)
    flash('Address updated successfully!', 'success')
    return redirect(url_for('home')) 

# Route to render the view address page
@app.route('/view/<int:id>', methods=['GET'])
def view_address(id):
    address = Address()
    address_data = address.get_address_by_id(id)  # Using the method to fetch address by ID
    return render_template('view_address.html', address=address_data)

# Route to handle the delete address action
@app.route('/delete/<int:id>', methods=['GET'])
def delete_address(id):
    address = Address()
    address.delete_address(id)
    flash('Address deleted successfully!', 'success')
    return redirect(url_for('home'))

# Route to handle the restore address action
@app.route('/restore/<int:id>', methods=['GET'])
def restore_address(id):
    address = Address()
    address.restore_address(id)
    flash('Address restored successfully!', 'success')
    return redirect(url_for('home'))

    
if __name__ == '__main__':
    port = int(os.getenv('PORT', 4444))
    app.run(debug=True, port=port)

 
 

'''
 from flask import Flask, render_template, request, redirect, url_for, flash
from config import Config
from app.routes import address_bp
from app.models import Address
import os

app = Flask(__name__, template_folder='app/templates')  # Explicitly setting the template folder
app.config.from_object(Config)

# Register the blueprint for API endpoints with a URL prefix
app.register_blueprint(address_bp, url_prefix='/api')

# Simple route to render the home page
@app.route('/')
def home():
    address = Address()
    addresses = address.get_all_addresses()  # Fetch all addresses to display in the table
    return render_template('index.html', addresses=addresses)

# Route to render the create address form
@app.route('/create', methods=['GET'])
def render_create_address():
    return render_template('create_address.html')

# Route to handle the create address form submission
@app.route('/create', methods=['POST'])
def handle_create_address():
    name = request.form['name']
    street = request.form['street']
    city = request.form['city']
    state = request.form['state']
    zip_code = request.form['zip_code']
    country = request.form['country']
    address = Address()
    address_id = address.create_address(name, street, city, state, zip_code, country)
    flash('Address created successfully!', 'success')
    return redirect(url_for('home'))

# Route to render the edit address form
@app.route('/edit/<int:id>', methods=['GET'])
def render_edit_address(id):
    address = Address()
    address_data = address.get_address_by_id(id)  # Using the newly added method
    return render_template('edit_address.html', address=address_data)

# Route to handle the edit address form submission
@app.route('/edit/<int:id>', methods=['POST'])
def handle_edit_address(id):
    name = request.form['name']
    street = request.form['street']
    city = request.form['city']
    state = request.form['state']
    zip_code = request.form['zip_code']
    country = request.form['country']
    address = Address()
    address.update_address(id, name, street, city, state, zip_code, country)
    flash('Address updated successfully!', 'success')
    return redirect(url_for('home'))

# Route to render the view address page
@app.route('/view/<int:id>', methods=['GET'])
def view_address(id):
    address = Address()
    address_data = address.get_address_by_id(id)  # Using the method to fetch address by ID
    return render_template('view_address.html', address=address_data)

# Route to handle the delete address action
@app.route('/delete/<int:id>', methods=['GET'])
def delete_address(id):
    address = Address()
    address.delete_address(id)
    flash('Address deleted successfully!', 'success')
    return redirect(url_for('home'))


if __name__ == '__main__':
    port = int(os.getenv('PORT', 4444))
    app.run(debug=True, port=port)

 
'''