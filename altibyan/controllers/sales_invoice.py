import frappe 
from frappe import _
from altibyan.api import send_whatsapp_message , send_sms_message
DOMAINS = frappe.get_active_domains()

@frappe.whitelist()
def validate(self , method):
    if "Tebian" in DOMAINS:
        if frappe.db.get_single_value('Messages Integrations', 'sales_invoice') == 1:
            send_sms(self)

@frappe.whitelist()
def on_submit(self , method):
    if "Tebian" in DOMAINS:
        if frappe.db.get_single_value('Messages Integrations', 'sales_invoice') == 1:
            validate_otp(self)








def validate_otp(self):
    if self.otp != self.verification_otp:
        frappe.throw(_("The OTP don't match!"))

def send_sms(self):
    if not self.send_otp:
        frappe.throw(_("Select OTP Sender!"))


    if self.otp:
        return
    otp = frappe.generate_hash(length=6)
    res = None

    to_number = frappe.get_value("Customer",self.customer,'mobile_no')
    if not to_number:
        frappe.throw(_("This Customer didn't have phone number"))

    message = f"""Welcome to {frappe.defaults.get_user_default("Company")},\nYour OTP code is: {otp} ,\nin {self.doctype} / {self.name}"""
    if self.send_otp == "Whatsapp":
        res = send_whatsapp_message(to_number, message)
    elif self.send_otp == "SMS":
        res = send_sms_message(to_number, message)
    if res.status_code != 200:
        frappe.throw(_("Message didn't sent!"))
    else:
        self.otp = otp