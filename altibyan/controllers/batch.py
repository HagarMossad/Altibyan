import frappe 
DOMAINS = frappe.get_active_domains()


def fetch_barcode(self , event):
    if "Tebian" in DOMAINS:
        self.barcode = self.batch_id
        sql = f'''select 
                    b.barcode 
                from 
                    `tabItem Barcode` b
                inner join 
                    `tabItem` i
                on 
                    i.name = b.parent
                where 
                    i.name = '{self.item}'
                '''
        data = frappe.db.sql(sql , as_dict = 1)
        if data :
            self.item_barcode = data[0]["barcode"]

