#!/usr/bin/en
# -*- coding: utf-8 -*-

"""
    This file is part of aialchemyhub_in
    (https://github.com/satya25/aialchemyhub_in).

    aialchemyhub_in is free software repository:
    You can redistribute it and/or modify it under
    the terms of the MIT License.

    aialchemyhub_in is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    MIT License for more details.

    You should have received a copy of the MIT License along with
    aialchemyhub_in.  If not, see <https://opensource.org/licenses/MIT>.
"""

# ----------------------------------------------------------------------------
# File Name         :       ./app/routes.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Nov 15, 2024
# version           :       1.0
# Release           :       R1
#
# Dependencies      :       Flask, mysql-connector-python, flasgger et al
#
# Installation      :       $ pip install requirements.txt
#
# Usage             :       python ../run.py
#
# ---------------------------------------------------------------------------
#
# Credits and Acknowledgements
#
# - Special thanks to the Python community for their excellent library:
#   https://www.python.org/community/
#
# - The APIs used in this script is documented here:
#   
#
# - Code Snippet(s) adapted from    :   -- NOT Applicable --
#
# - Dataset(s) sourced  from        :   -- NOT Applicable --
#
#
# - Inspiration for xxx drawn from:
#   
#
# Thank you to the creators and maintainers of these resources!
#
# ---------------------------------------------------------------------------
#
# - Content Removal Requests
#
#   If you are the owner or creator of any content used in this script and
#   would like it to be removed, please contact me at:  spnigam25@yahoo.com
#   I will promptly remove the content upon request.
#
# ---------------------------------------------------------------------------

from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash
from .models import Address

# Define the Blueprint for address-related routes
address_bp = Blueprint('address_bp', __name__)

# Route to get all addresses
@address_bp.route('/addresses', methods=['GET'])
def get_addresses():
    address = Address()
    addresses = address.get_all_addresses()
    return jsonify(addresses)

# Route to get only active addresses
@address_bp.route('/addresses/active', methods=['GET'])
def get_active_addresses():
    address = Address()
    active_addresses = address.get_all_active_addresses()
    return jsonify(active_addresses)

# Route to get only deleted addresses
@address_bp.route('/addresses/deleted', methods=['GET'])
def get_deleted_addresses():
    address = Address()
    deleted_addresses = address.get_all_deleted_addresses()
    return jsonify(deleted_addresses)

# Route to create a new address
@address_bp.route('/addresses', methods=['POST'])
def create_address():
    data = request.get_json()
    name = data['name']
    street = data['street']
    city = data['city']
    state = data['state']
    zip_code = data['zip_code']
    country = data['country']
    address = Address()
    address_id = address.create_address(name, street, city, state, zip_code, country)
    return jsonify({"message": "Address created", "id": address_id}), 201

# Route to update an existing address
@address_bp.route('/addresses/<int:id>', methods=['PUT'])
def update_address(id):
    data = request.get_json()
    name = data['name']
    street = data['street']
    city = data['city']
    state = data['state']
    zip_code = data['zip_code']
    country = data['country']
    address = Address()
    rows_affected = address.update_address(id, name, street, city, state, zip_code, country)
    return jsonify({"message": "Address updated", "rows_affected": rows_affected})

# Route to delete an existing address (soft-delete)
@address_bp.route('/addresses/<int:id>', methods=['DELETE'])
def delete_address(id):
    address = Address()
    rows_affected = address.delete_address(id)
    return jsonify({"message": "Address deleted", "rows_affected": rows_affected})

# Route to restore a soft-deleted address
@address_bp.route('/addresses/<int:id>/restore', methods=['PUT'])
def restore_address(id):
    address = Address()
    rows_affected = address.restore_address(id)
    return jsonify({"message": "Address restored", "rows_affected": rows_affected})

# Route to get the total number of records
@address_bp.route('/addresses/total', methods=['GET'])
def get_total_records():
    address = Address()
    total_records = len(address.get_all_addresses())
    return jsonify({"total_records": total_records})

# Route to get the total number of active records
@address_bp.route('/addresses/active/total', methods=['GET'])
def get_total_active_records():
    address = Address()
    total_active_records = len(address.get_all_active_addresses())
    return jsonify({"total_active_records": total_active_records})

# Route to get the total number of deleted records
@address_bp.route('/addresses/deleted/total', methods=['GET'])
def get_total_deleted_records():
    address = Address()
    total_deleted_records = len(address.get_all_deleted_addresses())
    return jsonify({"total_deleted_records": total_deleted_records})

# Placeholder for future endpoints
### Future end-points / routes shall be added below:


'''

### routes.py

from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash
from .models import Address 
  
address_bp = Blueprint('address_bp', __name__) 


@address_bp.route('/addresses', methods=['GET'])
def get_addresses():
    address = Address()
    addresses = address.get_all_addresses()
    return jsonify(addresses)
    
#### Two additional end points must come here
  
# New route to get only active addresses
@address_bp.route('/addresses/active', methods=['GET'])
def get_active_addresses():
    address = Address()
    active_addresses = address.get_all_active_addresses()
    return jsonify(active_addresses)

# New route to get only deleted addresses
@address_bp.route('/addresses/deleted', methods=['GET'])
def get_deleted_addresses():
    address = Address()
    deleted_addresses = address.get_all_deleted_addresses()
    return jsonify(deleted_addresses)
  

#### Rest of the existing APIs #####

@address_bp.route('/addresses', methods=['POST'])
def create_address():
    data = request.get_json()
    name = data['name']
    street = data['street']
    city = data['city']
    state = data['state']
    zip_code = data['zip_code']
    country = data['country']
    address = Address()
    address_id = address.create_address(name, street, city, state, zip_code, country)
    return jsonify({"message": "Address created", "id": address_id}), 201

@address_bp.route('/addresses/<int:id>', methods=['PUT'])
def update_address(id):
    data = request.get_json()
    name = data['name']
    street = data['street']
    city = data['city']
    state = data['state']
    zip_code = data['zip_code']
    country = data['country']
    address = Address()
    rows_affected = address.update_address(id, name, street, city, state, zip_code, country)
    return jsonify({"message": "Address updated", "rows_affected": rows_affected})

@address_bp.route('/addresses/<int:id>', methods=['DELETE'])
def delete_address(id):
    address = Address()
    rows_affected = address.delete_address(id)
    return jsonify({"message": "Address deleted", "rows_affected": rows_affected})

@address_bp.route('/addresses/<int:id>/restore', methods=['PUT'])
def restore_address(id):
    address = Address()
    rows_affected = address.restore_address(id)
    return jsonify({"message": "Address restored", "rows_affected": rows_affected})
 
### Future end-points / routes shall be added below:
 

# Route to get total number of records
@address_bp.route('/addresses/total', methods=['GET'])
def get_total_records():
    address = Address()
    total_records = len(address.get_all_addresses())
    return jsonify({"total_records": total_records})

# Route to get total number of active records
@address_bp.route('/addresses/active/total', methods=['GET'])
def get_total_active_records():
    address = Address()
    total_active_records = len(address.get_all_active_addresses())
    return jsonify({"total_active_records": total_active_records})

# Route to get total number of deleted records
@address_bp.route('/addresses/deleted/total', methods=['GET'])
def get_total_deleted_records():
    address = Address()
    total_deleted_records = len(address.get_all_deleted_addresses())
    return jsonify({"total_deleted_records": total_deleted_records})

'''