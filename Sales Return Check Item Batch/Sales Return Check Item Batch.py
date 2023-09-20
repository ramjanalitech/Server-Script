if doc.is_return :
    if doc.items :
        x=0
        for itm in doc.items:
           if itm.item_code :
                x=x+1
                d = frappe.db.get_list("Batch",doc.batch_no , filters={'name':itm.batch_no, 'item':itm.item_code} )
                if not d :
                    frappe.throw(f"Row # {x},  {itm.item_code} : Item batch number invalid.")