frappe.ui.form.on("Sales Order", {
    scan_batch_barcode(frm) {
        console.log("ggggggggggg");
        if(frm.doc.scan_batch_barcode){
            console.log(frm.doc.scan_batch_barcode)
            frappe.call({
                method: "altibyan.api.get_active_domains",
                callback: function (r) {
                    if (r.message && r.message.length) {
                        if (r.message.includes("Tebian")) {
                            frappe.call(
                                {
                                    "method" :"altibyan.api.scan_batch_barcode" , 
                                    args :{
                                        "barcode" : frm.doc.scan_batch_barcode
                                    }
                                }
                            )
                        }
                    }
                }
            })
        }
        
    },

})