pp = frappe.form_dict.doc
pp = json.loads(pp)
ae = frappe.db.count("Work Order",{'production_plan': pp.get("name")})
order_count =0
if ae > 0:
    if len(pp.get('po_items')) == ae :
        frappe.response["message"] = False
    else :
        for itm in pp.get('po_items'):
            e = frappe.db.get_list("Work Order",filters={'production_plan': pp.get("name"),"production_item":itm.get('item_code'),"production_plan_item":itm.get('name')}, fields=["*"])
            if e :
                e=[{},{}]
            else :
                wo = frappe.get_doc({
                "doctype": "Work Order",
                "production_item": itm.get("item_code"),
                "qty": itm.get("planned_qty"),
                "production_plan": pp.get("name"),
                "bom_no": itm.get("bom_no"),
                "branch":pp.get("branch"),
                "production_plan_item":itm.get("name"),
                "transfer_material_against":"Job Card",
                "planned_start_date":itm.get("planned_start_date"),
                "fg_warehouse":itm.get("warehouse")
                
                })
                order_count = order_count+1
                wo.insert( ignore_mandatory=True )
                bom = frappe.get_doc("BOM",itm.get("bom_no"))
                if bom :
                    for b in bom.operations :
                        wo.append('operations',{
                            'bom':itm.get("bom_no"),
                            "description": b.get('description'),
                            "operation": b.get('operation'),
                            "workstation": b.get('workstation'),
                            "time_in_mins":0.3
                        })
                wo.save()
        frappe.msgprint(f"{order_count} Work Order Created")
        frappe.response["message"] = "ok"        
else:
    for itm in pp.get("po_items"):
                
        wo = frappe.get_doc({
                "doctype": "Work Order",
                "production_item": itm.get("item_code"),
                "qty": itm.get("planned_qty"),
                "production_plan": pp.get("name"),
                "bom_no": itm.get("bom_no"),
                "branch":pp.get("branch"),
                "planned_start_date":itm.get("planned_start_date"),
                "fg_warehouse":itm.get("warehouse"),
                "production_plan_item":itm.get("name"),
                "transfer_material_against":"Job Card"
                
                })
        order_count = order_count+1
        wo.insert( ignore_mandatory=True )
        bom = frappe.get_doc("BOM",itm.get("bom_no"))
        if bom :
            for b in bom.operations :
                wo.append('operations',{
                    'bom':itm.get("bom_no"),
                    "description": b.get('description'),
                    "operation": b.get('operation'),
                    "workstation": b.get('workstation'),
                    "time_in_mins":0.3
                })
        wo.save()
    frappe.msgprint(f"{order_count} Work Order Created")
    frappe.response["message"] = "ok"