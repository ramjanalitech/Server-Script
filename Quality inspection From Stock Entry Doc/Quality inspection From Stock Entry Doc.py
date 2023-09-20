if doc.stock_entry_type == "Manufacture" :
    if doc.geo_item_group=="SEMI FINISH":
        # doc.inspection_required=1
        check_quality_ins=frappe.get_list("Quality Inspection",filters={'reference_name':doc.name}, fields=["*"])
        if not check_quality_ins:
            if doc.inspection_required:
                # frappe.frappe.msgprint('inspection_required_for_semi_finish')
                work_order= frappe.get_doc("Work Order", doc.work_order)
                Item = frappe.get_doc("Item", work_order.production_item)
                if Item.inspection_required_before_delivery:
                    # frappe.msgprint('inspection_required_before_delivery')
                    frappe.get_doc({'doctype':'Quality Inspection',
                        'inspection_type':"Incoming",
                        'manual_inspection': 1,
                        'reference_name':doc.name,
                        'reference_type':"Stock Entry",
                        'status':"For checking purpose",
                        'item_code': work_order.production_item,
                        'inspected_by':doc.modified_by,
                        'sample_size':doc.fg_completed_qty
                    }).insert()
                    frappe.msgprint('Quality Inspection Created')
            # doc.save()