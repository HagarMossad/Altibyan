import frappe 
from frappe import _


DOMAINS = frappe.get_active_domains()


frappe.whitelist()
def before_insert(self , method , *args, **kwargs):
	make_customer_name(self)
		

def make_customer_name(self):
	if not self.customer_group:
		frappe.throw(_("Please Enter the Customer Group"))
	
	customer_group = frappe.get_doc("Customer Group" , self.customer_group)
	last_naming = frappe.get_list("Naming Document",{
		"Type":"Customer" , 
		"group":self.customer_group
		},['type','group','last_naming'])
	if last_naming:
		last_name = last_naming[0].get('last_naming')
		new_name = int(last_name) + 1
		naming = create_naming_doc("Customer", self.customer_group, new_name)
		self.naming = naming
		self.name = naming
	else:
		naming = create_naming_doc("Customer" , self.customer_group , f"""{customer_group.series}{str(1).zfill(int(customer_group.number_of_digits))} """)
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
