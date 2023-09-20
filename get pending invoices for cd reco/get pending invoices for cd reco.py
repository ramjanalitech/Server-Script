payload = frappe.form_dict
data = frappe.db.sql("""
    SELECT 
        a.name, a.rounded_total
    FROM
        `tabSales Invoice` a
    LEFT JOIN `tabETPL Cash Discount Reconciliation Details` b on a.name = b.docname AND b.docstatus = 1
    WHERE
        b.clearance_date is null AND 
        a.is_return = 0 AND 
        a.customer = %s AND
        a.docstatus = 1 AND
        a.posting_date BETWEEN %s AND %s
""", (payload.get('customer'), payload.get('from_date'), payload.get('to_date')), as_dict=1)

if data:
    frappe.response['message'] = data
else:
    frappe.response['message'] = []