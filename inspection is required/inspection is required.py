if doc.stock_entry_type =="Manufacture" :
    if doc.geo_item_group=="SEMI FINISH":
        work_order = frappe.get_doc("Work Order",doc.work_order)
        if work_order:
            Item = frappe.get_doc("Item", work_order.production_item)
            doc.inspection_required=Item.inspection_required_before_delivery
        