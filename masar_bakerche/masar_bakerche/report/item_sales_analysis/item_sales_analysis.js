// Copyright (c) 2025, KCSC and contributors
// For license information, please see license.txt

frappe.query_reports["Item Sales Analysis"] = {
	"filters": [
		{
			"fieldname": "from",
			"label": __("From Date"),
			"fieldtype": "Date",
			"width": 80,
			"default": frappe.datetime.year_start()
		 },
		 {
			"fieldname": "to",
			"label": __("To Date"),
			"fieldtype": "Date",
			"width": 80,
			"default": frappe.datetime.year_end()
		},

		{
			fieldname: "company",
			label: __("Company"),
			fieldtype: "Link",
			options: "Company",
			default: frappe.defaults.get_user_default("Company"),
			reqd: 1
		},
		{
			fieldname: "pos_profile",
			label: __("POS Profile"),
			fieldtype: "Link",
			options: "POS Profile",
		},
		{
			fieldname:"item_group",
			label: __('Item Group'),
			fieldtype: "Link",
			options: "Item Group",
		},
		{
			fieldname:"item_code",
			label: __('Item Code'),
			fieldtype: "Link",
			options: "Item",
		},
	]
}
