from __future__ import unicode_literals
import frappe
from frappe import _

data = {
	'custom_fields': {
        'Stock Entry Detail':[	
                {
				"label": "Weight Per Unit",
				"fieldname": "weight_per_unit",
				"fieldtype": "Float",
				"insert_after": "retain_sample" ,
				"fetch_from": "item_code.weight_per_unit"
				},
                {
				"label": "Weight UOM",
				"fieldname": "weight_uom",
				"fieldtype": "Link",
                "options":"UOM",
				"insert_after": "weight_per_unit" ,
				"fetch_from": "item_code.weight_uom"
				},
                {
				"label": "has Weight",
				"fieldname": "has_weight",
				"fieldtype": "Check",
				"insert_after": "uom" ,
				},
                {
				"label": "Weight rate",
				"fieldname": "weight_rate",
				"fieldtype": "Float",
				"insert_after": "has_weight" ,
                "fetch_from": "item_code.weight_rate"
				},
                {
				"label": "Total Weight",
				"fieldname": "total_weight",
				"fieldtype": "Float",
				"insert_after": "weight_rate" ,
				},
                {
				"label": "Calculate Weight",
				"fieldname": "calculate_weight",
				"fieldtype": "Check",
				"insert_after": "total_weight" ,
				},
			],
		'Batch':[
            {
                "fieldname":"barcode",
                "fieldtype":"Barcode",
                "insert_after":"expiry_date",
                "label":"Barcode",
                "read_only" : 1
            },

			{
                "fieldname":"item_barcode",
                "fieldtype":"Barcode",
                "insert_after":"manufacturing_date",
                "label":"Item Barcode",
                "read_only" : 1
            }
        ],
        'Customer':[
            {
                "fieldname":"customer_classification",
                "fieldtype":"Select",
                "options":"\nDistinguished Customer\nContinuing Customer\nLate Customer\nDefaulting Customer\nStopped Customer",
                "insert_after":"customer_group",
                "label":_("Customer Classification"),
                "read_only":1
            },
            {
                "fieldname":"naming",
                "fieldtype":"Data",
                "insert_after":"customer_classification",
                "label":_("Naming"),
                "read_only":1
            },
            # {
			# 	"label": "Categories",
			# 	"fieldname": "categories",
			# 	"fieldtype": "Link",
            #     "options":"Categories",
			# 	"insert_after": "market_segment" ,
            # },
            {
				"label": "Commerical Number",
				"fieldname": "commerical_number",
				"fieldtype": "Data",
				"insert_after": "tax_id" ,
            },
            {
				"label": "Customer Name in English",
				"fieldname": "customer_name_in_english",
				"fieldtype": "Data",
				"insert_after": "customer_name" ,
            },
		],
		'Landed Cost Item':[
            {
                "fieldname":"percent",
                "fieldtype":"Percent",
                "insert_after":"amount",
                "label":"Percentage",
                "read_only_depends_on": "eval:parent.distribute_charges_based_on != 'Percent' ;",
                "mandatory_depends_on": "eval:parent.distribute_charges_based_on == 'Percent' ;",
            },
        ],
        "Customer Group":[
            {
				"label": _("Series"),
				"fieldname": "series",
				"fieldtype": "Data",
				"insert_after": "is_group" ,
                "reqd":1
            },
            {
				"label": _("Number of Digits"),
				"fieldname": "number_of_digits",
				"fieldtype": "Float",
				"insert_after": "series" ,
                "reqd":1
            },
        ],
        "Supplier":[
            {
                "fieldname":"naming",
                "fieldtype":"Data",
                "insert_after":"supplier_group",
                "label":_("Naming"),
                "read_only":1
            },
        ],
        "Supplier Group":[
            {
				"label": _("Series"),
				"fieldname": "series",
				"fieldtype": "Data",
				"insert_after": "is_group" ,
                "reqd":1
            },
            {
				"label": _("Number of Digits"),
				"fieldname": "number_of_digits",
				"fieldtype": "Float",
				"insert_after": "series" ,
                "reqd":1
            },
        ],
		'Sales Order':[
            {
                "fieldname":"scan_batch_barcode",
                "fieldtype":"Data",
                "insert_after":"scan_barcode",
                "label":"Scan Batch Barcode",
                "options":"Barcode"
            },
        ],
		'Item':[	
                {
				"label": "Width",
				"fieldname": "width",
				"fieldtype": "Float",
				"insert_after": "stock_uom" ,
                "read_only" : 1
				},
                {
				"label": "Length",
				"fieldname": "length",
				"fieldtype": "Float",
				"insert_after": "width" ,
				"read_only" : 1
				},
                {
				"label": "Height",
				"fieldname": "height",
				"fieldtype": "Float",
				"insert_after": "length" ,
				"read_only" : 1
				},
                {
					"label": "Total",
					"fieldname": "total",
					"fieldtype": "Float",
					"insert_after": "height" ,
					"read_only" : 1
				},
                {
				"label": "Weight Rate",
				"fieldname": "weight_rate",
				"fieldtype": "Float",
				"insert_after": "stock_uom" ,
				},
                 {
				"label": "Calculate Weight",
				"fieldname": "calculate_weight",
				"fieldtype": "Check",
				"insert_after": "weight_rate" ,
				},
		],
		'Stock Settings':[
            {
                "fieldname":"default_uom",
                "fieldtype":"Link",
                "insert_after":"item_group",
                "label":"Default UOM",
                "options" : "UOM"
            },
        ],
        'Delivery Note':[
            {
                "fieldname":"send_otp",
                "fieldtype":"Select",
                "insert_after":"is_return",
                "label":"OTP",
                "options":"\nSMS\nWhatsapp"
            },
            {
                "fieldname":"otp",
                "fieldtype":"Data",
                "insert_after":"send_otp",
                "label":"OTP",
                "hidden":1
            },
            {
                "fieldname":"verification_otp",
                "fieldtype":"Data",
                "insert_after":"is_return",
                "label":_("Verification OTP"),
            },
        ],
        'Sales Invoice':[
            {
                "fieldname":"send_otp",
                "fieldtype":"Select",
                "insert_after":"is_debit_note",
                "label":"OTP",
                "options":"\nSMS\nWhatsapp"
            },
            {
                "fieldname":"otp",
                "fieldtype":"Data",
                "insert_after":"send_otp",
                "label":"OTP",
                "hidden":1
            },
            {
                "fieldname":"verification_otp",
                "fieldtype":"Data",
                "insert_after":"is_return",
                "label":_("Verification OTP"),
            },
        ],
	},
      
        
		"properties": [
		{
            "doctype": "Landed Cost Voucher",
			"doctype_or_field": "DocField",
			"fieldname": "distribute_charges_based_on",
			"property": "options",
			"property_type": "Small Text",
			"value": "Qty\nAmount\nPercent\nDistribute Manually"
        },
		{
			"doctype": "Sales Order",
			"doctype_or_field": "DocField",
			"fieldname": "scan_barcode",
			"property": "hidden",
			"property_type": "Check",
			"value": "1"
        },
	],  
}
	