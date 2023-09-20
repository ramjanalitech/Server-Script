if doc.stock_entry_type == "Manufacture":

    if doc.geo_item_group == "SEMI FINISH" :
        l=0
        user = frappe.get_doc("User", frappe.session.user)
        for role in user.roles:
            if role.role == 'Manufacturing User' :
                l=1
            if role.role == "Manufacturing Manager":
                l=1
            if role.role == 'Manufacture Entry Submitter' :
                frappe.throw("Do not have a permission ")
        if l == 0 :
            frappe.throw("Do not have a permission ")
    
    
    if doc.geo_item_group != "SEMI FINISH" :
        l=0
        user = frappe.get_doc("User", frappe.session.user)
        for role in user.roles:
            if role.role == 'Manufacture Entry Submitter' :
                l=1
            
        if l != 1 :
            frappe.throw("Do not have a permission")
