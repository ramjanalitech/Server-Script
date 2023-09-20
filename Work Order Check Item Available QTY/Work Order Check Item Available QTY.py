if doc.stock_entry_type == "Material Consumption for Manufacture" :
    bom = frappe.get_doc("BOM", doc.bom_no)
    if bom :
        for item in bom.get("items") :
            pr_qty = item.qty/bom.quantity

            for itm in doc.items :
                if itm.item_code==item.item_code :
                    m_qty = pr_qty*doc.fg_completed_qty
                    if itm.qty < m_qty :
                        frappe.throw("Please Check %s You Have Item Quantity %s Required Item Quantity %s" % (itm.item_code,itm.qty, m_qty))
                        
if doc.stock_entry_type == "Material Consumption for Manufacture":
    bom = frappe.get_doc("BOM", doc.bom_no)
    if bom:
        for item in bom.get("items"):
            pr_qty = item.qty / bom.quantity

            for itm in doc.items:
                if itm.item_code == item.item_code:
                    m_qty = pr_qty * doc.fg_completed_qty
                    if itm.qty < m_qty:
                        frappe.throw("Please Check %s You Have Item Quantity %s Required Item Quantity %s" % (itm.item_code, itm.qty, m_qty))
