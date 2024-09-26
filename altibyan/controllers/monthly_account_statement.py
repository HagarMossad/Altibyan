import frappe 
from frappe import _
from altibyan.api import send_whatsapp_message , send_sms_message
DOMAINS = frappe.get_active_domains()

@frappe.whitelist()
def send_whattsapp(name, customer):
    if "Tebian" in DOMAINS:
        to_number = frappe.get_value("Customer", customer,'mobile_no')

        base_url = frappe.utils.get_url()
    
        doc_link = f"{base_url}/app/monthly_account_statement/{name}"
        send_whatsapp_message( to_number, doc_link )


@frappe.whitelist()
def send_sms(name, customer):
    if "Tebian" in DOMAINS:
        to_number = frappe.get_value("Customer", customer,'mobile_no')

        base_url = frappe.utils.get_url()
    
        doc_link = f"{base_url}/app/monthly_account_statement/{name}"
        send_sms_message( to_number, doc_link )



