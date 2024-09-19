import frappe
from erpnext.stock.utils import scan_barcode


@frappe.whitelist()
def get_active_domains():
	return frappe.get_active_domains()

		