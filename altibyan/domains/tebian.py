from __future__ import unicode_literals
import frappe
from frappe import _

data = {
	'custom_fields': {
		'Batch':[
            {
                "fieldname":"barcode",
                "fieldtype":"Data",
                "insert_after":"expiry_date",
                "label":"Barcode",
               
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
	},
		"properties": [
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