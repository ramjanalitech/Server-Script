if doc.party_type == 'Customer' :
    cust = frappe.get_doc("Customer", doc.party)
    if cust :
        if cust.sales_team:
            doc.geo_sales_person = cust.sales_team[0].sales_person
            doc.geo_territory = cust.territory
            doc.save()