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
# File Name         :       ./app/models.py
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

import mysql.connector
from mysql.connector import Error
from config import Config

class Address:
    def __init__(self):
        try:
            # Establish database connection using MySQL connector
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="address_sphere"
            )
            if self.connection.is_connected():
                db_info = self.connection.get_server_info()
                print("Connected to MySQL Server version ", db_info)
        except Error as e:
            print("Error while connecting to MySQL", e)

    def get_all_addresses(self):
        """
        Fetch all non-deleted addresses from the database.
        """
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM addresses WHERE is_deleted = 0 OR is_deleted = 1 ")
            records = cursor.fetchall()
            return records
        except Error as e:
            print("Error while fetching data", e)
            return []

    def create_address(self, name, street, city, state, zip_code, country):
        """
        Create a new address in the database.
        """
        try:
            cursor = self.connection.cursor()
            sql = "INSERT INTO addresses (name, street, city, state, zip_code, country) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (name, street, city, state, zip_code, country)
            cursor.execute(sql, val)
            self.connection.commit()
            return cursor.lastrowid
        except Error as e:
            print("Error while inserting data", e)
            return None

    def update_address(self, id, name, street, city, state, zip_code, country):
        """
        Update an existing address in the database.
        """
        try:
            cursor = self.connection.cursor()
            sql = "UPDATE addresses SET name = %s, street = %s, city = %s, state = %s, zip_code = %s, country = %s WHERE id = %s"
            val = (name, street, city, state, zip_code, country, id)
            cursor.execute(sql, val)
            self.connection.commit()
            return cursor.rowcount
        except Error as e:
            print("Error while updating data", e)
            return None

    def delete_address(self, id):
        """
        Soft-delete an address by setting the is_deleted flag.
        """
        try:
            cursor = self.connection.cursor()
            sql = "UPDATE addresses SET is_deleted = 1 WHERE id = %s"
            cursor.execute(sql, (id,))
            self.connection.commit()
            return cursor.rowcount
        except Error as e:
            print("Error while deleting data", e)
            return None

    def restore_address(self, id):
        """
        Restore a soft-deleted address by unsetting the is_deleted flag.
        """
        try:
            cursor = self.connection.cursor()
            sql = "UPDATE addresses SET is_deleted = 0 WHERE id = %s"
            cursor.execute(sql, (id,))
            self.connection.commit()
            return cursor.rowcount
        except Error as e:
            print("Error while restoring data", e)
            return None
    
    def get_address_by_id(self, id):
        """
        Fetch an address by its ID.
        """
        try:
            cursor = self.connection.cursor(dictionary=True)
            sql = "SELECT * FROM addresses WHERE id = %s"
            cursor.execute(sql, (id,))
            record = cursor.fetchone()
            return record
        except Error as e:
            print("Error while fetching data", e)
            return None

    def get_all_active_addresses(self):
        """
        Fetch all active (non-deleted) addresses.
        """
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM addresses WHERE is_deleted = 0")
            records = cursor.fetchall()
            return records
        except Error as e:
            print("Error while fetching data", e)
            return []

    def get_all_deleted_addresses(self):
        """
        Fetch all deleted addresses.
        """
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM addresses WHERE is_deleted = 1")
            records = cursor.fetchall()
            return records
        except Error as e:
            print("Error while fetching data", e)
            return []

###############################################
 