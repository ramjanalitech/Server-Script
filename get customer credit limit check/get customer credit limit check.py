if doc.is_return == 0:
    
    customer = doc.customer
    company = doc.company

    values = {"customer": customer, "company": company}

    credit_limit = frappe.db.sql("""
        SELECT credit_limit FROM `tabCustomer Credit Limit`WHERE parent = %(customer)s AND parenttype = "Customer" AND company = %(company)s""", values=values, as_dict=1)
    
    outstanding = frappe.db.sql("""
        SELECT SUM(rounded_total) AS total FROM `tabSales Invoice` WHERE company = %(company)s AND customer = %(customer)s AND status IN ('Unpaid', 'Overdue')""", values=values, as_dict=1)

    gl_entries = frappe.db.sql("""
        SELECT (SUM(debit) - SUM(credit)) AS total FROM `tabGL Entry` WHERE is_cancelled = 0 AND party = %(customer)s AND company = %(company)s""", values=values, as_dict=1)

    cl = 0
    html = ""

    if credit_limit:
        cl = credit_limit[0].credit_limit
        html = f'Limit: {cl}, Due: {outstanding[0].total or 0}, Credit Bal: {cl - outstanding[0].total or 0}'

    mcl = cl - (outstanding[0].total if outstanding and outstanding[0].total else 0)

    frappe.log_error('error', f"{customer}, {mcl}")

    if doc.total > mcl:
        frappe.throw('Please Check Customer Credit Limit')

    frappe.response["message"] = html
