# Get the 'customer' and 'company' values from the form dictionary
customer = frappe.form_dict.customer
company = frappe.form_dict.company

# Retrieve the 'customer_group' for the specified customer from the database
customer_group = frappe.db.get_value("Customer", customer, "customer_group")

# Check if the customer belongs to "Amazon" or "Branch Debtors" group
if "Amazon" in customer_group or "Branch Debtors" in customer_group:
    # Set an empty dictionary as the response message
    frappe.response["message"] = {}
else:
    # Execute an SQL query to fetch outstanding invoice data
    outstanding = frappe.db.sql("""
        SELECT
            customer as party,
            posting_date,
            name as voucher_no,
            SUM(outstanding_amount) as closing,
            SUM(outstanding_amount) as overdue,
            DATEDIFF(CURDATE(), DATE_ADD(posting_date, INTERVAL 150 DAY)) due_days,
            status,
            (SELECT SUM(debit - credit)
             FROM `tabGL Entry`
             WHERE party = customer AND is_cancelled = 0 AND docstatus = 1) AS total_outstanding
        FROM `tabSales Invoice`
        WHERE
            customer = %s AND
            company = %s AND
            status <> 'Paid' AND
            is_return = 0 AND
            docstatus = 1 AND
            DATE_ADD(posting_date, INTERVAL 150 DAY) < CURDATE()
        HAVING overdue > 0
    """, (customer, company), as_dict=1)

    # Set the response message to the result of the SQL query
    frappe.response["message"] = outstanding
