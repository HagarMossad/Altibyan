import frappe 
DOMAINS = frappe.get_active_domains()

def calculate_total(self , event):
    if "Tebian" in DOMAINS:
        if self.variant_of != None:
            for variant in self.attributes :
                if variant.attribute == "length" :
                    self.length = variant.attribute_value
                elif variant.attribute == "width" :
                    self.width = variant.attribute_value
                elif variant.attribute == "height" :
                    self.height = variant.attribute_value

            self.total =float(self.length) * float(self.width) * float(self.height)
            default_uom  = frappe.db.get_single_value('Stock Settings','default_uom')
            self.append("uoms" , {"uom" : default_uom , "conversion_factor" : self.total})
