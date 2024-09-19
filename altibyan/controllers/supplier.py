import frappe 
from frappe import _


DOMAINS = frappe.get_active_domains()


frappe.whitelist()
def before_insert(self , method , *args, **kwargs):
	make_supplier_name(self)
		

def make_supplier_name(self):
	if not self.supplier_group:
		frappe.throw(_("Please Enter the Supplier Group"))
	
	supplier_group = frappe.get_doc("Supplier Group" , self.supplier_group)
	last_naming = frappe.get_list("Naming Document",{
		"Type":"Supplier" , 
		"group":self.supplier_group
		},['type','group','last_naming'])
	if last_naming:
		last_name = last_naming[0].get('last_naming')
		new_name = int(last_name) + 1
		naming = create_naming_doc("Supplier", self.supplier_group, new_name)
		self.naming = naming
		self.name = naming
	else:
		naming = create_naming_doc("Supplier" , self.supplier_group , f"""{supplier_group.series}{str(1).zfill(int(supplier_group.number_of_digits))} """)
		self.naming = naming
		self.name = naming
		
		

def create_naming_doc(type_doc , group , last_naming):
	doc = frappe.new_doc("Naming Document")
	doc.type = type_doc
	doc.group = group
	doc.last_naming = last_naming
	doc.save(ignore_permissions=True)
	frappe.db.commit()
	print(doc.name)
	return doc.name
