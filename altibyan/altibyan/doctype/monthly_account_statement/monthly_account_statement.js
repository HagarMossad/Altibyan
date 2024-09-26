// Copyright (c) 2024, Hagar Mossad and contributors
// For license information, please see license.txt

frappe.ui.form.on("Monthly Account Statement", {
	refresh:function(frm) {
       console.log("hhhhh");
	},
    gl_btn: function(frm) {

        let today = new Date();
        let from_date = new Date();
        from_date.setDate(today.getDate() - 30);
        
        let formatted_today = frappe.datetime.get_today();
        let formatted_from_date = frappe.datetime.strftime(from_date, '%Y-%m-%d');
        console.log(today)
        frappe.set_route('query-report', 'General Ledger', {
            "customer": frm.doc.customer,  
            "to_date": formatted_today,
            "from_date": formatted_from_date,
            "party_type": "Customer" ,

            // "account":,
        });
    }
});
