if doc.bom_no :
    if doc.job_card :
        get_bom = frappe.get_doc("Job Card", doc.job_card)
        if len(get_bom.get("items")) == len(doc.get("items")):
            frappe.log_error("Equal hai")
        else:
            frappe.throw('Material Quantity Issue')