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
        let formatted_from_date = moment(from_date).format('YYYY-MM-DD');

        console.log(frm.doc.customer)

        frappe.set_route('query-report', 'Customer Ledger Summary', {
            "party": frm.doc.customer,
            "to_date": formatted_today,
            "from_date": formatted_from_date,
        });
    },
    sms_btn: function(frm) {
        frappe.call({
            method: "altibyan.controllers.monthly_account_statement.send_sms",
            args:{
                "name": frm.docname,
                "customer": frm.doc.customer
            }, 
            callback: function (r) {
                if (r.message && r.message.length) {
                    
                }
            }
        })
        
    },
    whats_btn: function(frm) {
        frappe.call({
            method: "altibyan.controllers.monthly_account_statement.send_whattsapp",
            args:{
                "name": frm.docname,
                "customer": frm.doc.customer
            }, 
            callback: function (r) {
                if (r.message && r.message.length) {
                    
                }
            }
        })
        
    },
    accepted: function(frm) {
        if (frm.doc.accepted) {
            frm.set_value('refused', 0); 
        }
    },

    refused: function(frm) {
        if (frm.doc.refused) {
            frm.set_value('accepted', 0); 
        }
    }

});
