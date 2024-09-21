import frappe 
DOMAINS = frappe.get_active_domains()

def validate(self, event):
    if "Tebian" in DOMAINS:
        if self.distribute_charges_based_on == "Percent":
            total_percent = sum(item.percent for item in self.items) or 0
            if total_percent != 100:
                frappe.throw("Total percent must be equal to 100%. Current total is {}%.".format(total_percent))
