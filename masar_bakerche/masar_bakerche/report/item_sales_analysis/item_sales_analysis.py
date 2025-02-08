# Copyright (c) 2025, KCSC and contributors
# For license information, please see license.txt

# import frappe

from __future__ import unicode_literals
from frappe import _
import frappe

def execute(filters=None):
	return get_columns(), get_data(filters)

def get_data(filters):
	_from, to = filters.get('from'), filters.get('to') #date range
	#Conditions
	conditions = " AND 1=1 "
	if(filters.get('item_code')):conditions += f" AND tpii.item_code = '{filters.get('item_code')}' "
	if(filters.get('item_group')):conditions += f" AND tpii.item_group='{filters.get('item_group')}' "
	if(filters.get('pos_profile')):conditions += f" AND tpi.pos_profile LIKE '%{filters.get('pos_profile')}' "
	# if(filters.get('customer_group')):conditions += f" AND tc.customer_group='{filters.get('customer_group')}' "

	data = frappe.db.sql(f""" select tpi.pos_profile, tpii.item_group, tpii.item_code, tpii.qty, tpii.rate, tpii.amount 
							from `tabPOS Invoice` tpi 
							inner join `tabPOS Invoice Item` tpii on tpi.name = tpii.parent 
							where tpi.docstatus = 1   AND
								(tpi.posting_date BETWEEN '{_from}' AND '{to}')
								{conditions};""")
	return data





	# return data

def get_columns():
	return [
	   "POS Profile: Data/POS Profile:200",
	   "Item Group: Data:200",
	   "Item Code: Link/Item:200",
       "Quantity: Data:200",
	   "Rate: Data:200",
	   "Amount: Data:200"

	]
