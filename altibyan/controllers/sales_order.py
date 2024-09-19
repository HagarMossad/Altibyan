import frappe 
from frappe import _


DOMAINS = frappe.get_active_domains()


frappe.whitelist()
def on_submit(self , method , *args, **kwargs):
	make_matrial_request(self)


def make_matrial_request(self ):
	if "Tebian" in DOMAINS:
		items = self.get("items")
		for item in items:
			if item.projected_qty < 1:
				doc = frappe.new_doc("Material Request")
				doc.material_request_type = "Manufacture"
				doc.transaction_date = self.transaction_date
				doc.schedule_date = self.delivery_date
				doc.set_warehouse = self.set_warehouse
				doc.append("items",{
					"item_code":item.item_code,
					"item_name": item.item_name,
					"schedule_date":item.delivery_date,
					"qty": item.qty,
					"uom":item.uom
				})
				doc.save(ignore_permissions=True)
				doc.submit()
				frappe.db.commit()
				frappe.msgprint(doc.name)