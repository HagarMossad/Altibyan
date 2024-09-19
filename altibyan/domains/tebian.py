from __future__ import unicode_literals
import frappe
from frappe import _

data = {
	'custom_fields': {
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
				}
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
	},  
}