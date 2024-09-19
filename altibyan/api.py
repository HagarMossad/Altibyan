import frappe
from frappe import _
from erpnext.stock.utils import scan_barcode
import requests
import json


@frappe.whitelist()
def get_active_domains():
	return frappe.get_active_domains()

@frappe.whitelist()
def scan_batch_barcode(barcode): 
	pass

def send_sms_message(to_number, message):

	doc = frappe.get_doc("Messages Integrations")
	
	username = doc.username
	password = doc.password
	sendername = doc.sendername
	message = message
	if not (username or password or sendername ):
		frappe.throw("Please Enter Configration to send a message")


	url = f"""{doc.sms_url}?username={username}&password={password}&sendername={sendername}&mobiles={to_number}&message={message}"""

	r = requests.get(url)
	if r.status_code == 200:
		print("Message sent successfully!")
		return r
	else:
		print(f"Failed to send message. Status code: {r.status_code}, Response: {r.text}")

def send_whatsapp_message(to_number, message):
	doc = frappe.get_doc("Messages Integrations")
	if not (doc.production_id or doc.phone_id or doc.whatsapp_url ):
		frappe.throw("Please Enter Configration to send a message")
	production_id = doc.production_id
	phone_id = doc.phone_id
	url = f"""{doc.whatsapp_url}/{production_id}/{phone_id}/sendMessage"""
	
	headers = {
		"Content-Type": "application/json",
		"x-maytapi-key": doc.token
	}
	
	payload = {
		"to_number": to_number,
		"type": "text",
		"message": message
	}

	response = requests.post(url, headers=headers, data=json.dumps(payload))
	
	if response.status_code == 200:
		print("Message sent successfully!")
		return response
	else:
		print(f"Failed to send message. Status code: {response.status_code}, Response: {response.text}")
