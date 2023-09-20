if doc.geo_item_group == "SEMI FINISH":
    if doc.inspection_required:
        work_order= frappe.get_doc("Work Order", doc.work_order)
        Item = frappe.get_doc("Item", work_order.production_item)
        if Item.inspection_required_before_delivery:
            check_quality_inspection = frappe.db.exists("Quality Inspection",{'reference_name':doc.name,'status':"Accepted","docstatus":1})
            if not check_quality_inspection:
                frappe.throw("Quality Inspection Required")