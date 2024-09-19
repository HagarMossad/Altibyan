frappe.ui.form.on("Sales Order", {
    scan_batch_barcode(frm) {
        frappe.call({
            method: "dynamic.api.get_active_domains",
            callback: function (r) {
                if (r.message && r.message.length) {
                    if (r.message.includes("Tebian")) {
                        
                    }
                }
            }
        })
    },

})