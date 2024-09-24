import frappe 
from frappe import _


DOMAINS = frappe.get_active_domains()


frappe.whitelist()
def before_insert(self , method , *args, **kwargs):
	if "Tebian" in DOMAINS:
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



from frappe.utils import add_days, today
from datetime import datetime



@frappe.whitelist(allow_guest=True)
def class_classification():
	date_today = datetime.strptime(today(), "%Y-%m-%d")
	date_last_month = datetime.strptime(add_days(today(), -30), "%Y-%m-%d")
	customer_class = None
	all_customers = frappe.db.sql(f"""
									SELECT 
										c.name AS name,
										ccl.credit_limit AS credit_limit,
										COALESCE(
											(SELECT 
												SUM(si.grand_total) 
											FROM 
												`tabSales Invoice` si
											WHERE 
												si.customer = c.name
												AND si.status != 'Paid'
												AND si.docstatus = 1), 0) AS grand_total_unpaid,
										COALESCE(
											(SELECT 
												SUM(si.grand_total) 
											FROM 
												`tabSales Invoice` si
											WHERE 
												si.customer = c.name
												AND si.docstatus = 1), 0) AS grand_total_all_invoices,
										(COALESCE(
											(SELECT 
												SUM(si.grand_total) 
											FROM 
												`tabSales Invoice` si
											WHERE 
												si.customer = c.name
												AND si.docstatus = 1), 0) 
										- COALESCE(
											(SELECT 
												SUM(si.grand_total) 
											FROM 
												`tabSales Invoice` si
											WHERE 
												si.customer = c.name
												AND si.status != 'Paid'
												AND si.docstatus = 1), 0)) AS grand_total_paid
									FROM 
										`tabCustomer` c
									JOIN 
										`tabCustomer Credit Limit` ccl 
									ON 
										c.name = ccl.parent 
									WHERE 
										ccl.credit_limit > 0 
										AND c.disabled = 0 
										AND c.is_frozen = 0;
								""", as_dict=1)
	
	for customer in all_customers:
		if float(customer.get("grand_total_paid") or 0) > 0 and float(customer.get("grand_total_unpaid") or 0) > 0 :
			if float(customer.get("grand_total_paid")) * 2 > float(customer.get("credit_limit")):
				customer_class = "Distinguished Customer"

			elif float(customer.get("grand_total_unpaid") or 0) / float(customer.get("grand_total_all_invoices") or 0) > 0.9:
				customer_class = "Continuing Customer"

			elif (float(customer.get("grand_total_unpaid") or 0) / float(customer.get("grand_total_all_invoices") or 0) > 0.2) and (float(customer.get("grand_total_unpaid") or 0) / float(customer.get("grand_total_all_invoices") or 0) < 0.4):
				customer_class = "Late Customer"
				create_tasks(6 , customer.get("name"))

			elif (float(customer.get("grand_total_unpaid") or 0) / float(customer.get("grand_total_all_invoices") or 0) < 0.4) or (float(customer.get("grand_total_all_invoice") or 0) == 0 and float(customer.get("grand_total_unpaid") or 0) > 0):
				customer_class = "Defaulting Customer"
				create_tasks(6 , customer.get("name"))

		elif float(customer.get("grand_total_unpaid") or 0) == 0 and float(customer.get("grand_total_all_invoices") or 0) == 0:
			customer_class = "Stopped Customer"


		customer['customer_class'] = customer_class
		frappe.db.set_value('Customer', customer.get("name"), 'customer_classification', customer_class, update_modified=True)

	return all_customers


def create_tasks(number_of_visits , customer):
	if number_of_visits:
		for i in range(number_of_visits):
			doc = frappe.new_doc("Issue")
			doc.subject = "Visit"
			doc.customer = customer
			doc.save(ignore_permissions=True)
			frappe.db.commit()




