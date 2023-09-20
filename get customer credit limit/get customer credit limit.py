# Get the 'customer' and 'company' values from the form dictionary
customer = frappe.form_dict.customer
company = frappe.form_dict.company

# Create a dictionary with customer and company values for SQL queries
values = {"customer": customer, "company": company}

# Query to fetch credit limit for the customer
credit_limit = frappe.db.sql("""
    SELECT credit_limit
    FROM `tabCustomer Credit Limit`
    WHERE parent = %(customer)s
    AND parenttype = "Customer"
    AND company = %(company)s
""", values=values, as_dict=1)

# Query to fetch outstanding sales invoices for the customer
outstanding_sales_invoices = frappe.db.sql("""
    SELECT SUM(rounded_total) as total
    FROM `tabSales Invoice`
    WHERE company = %(company)s
    AND customer = %(customer)s
    AND status IN ('Unpaid', 'Overdue')
""", values=values, as_dict=1)

# Query to calculate the total credit balance for the customer
outstanding_gl_entries = frappe.db.sql("""
    SELECT (SUM(debit) - SUM(credit)) as total
    FROM `tabGL Entry`
    WHERE is_cancelled = 0
    AND party = %(customer)s
    AND company = %(company)s
""", values=values, as_dict=1)

# Initialize the credit limit as 0
cl = 0

# Check if credit_limit has a value, and if so, assign it to cl
if credit_limit:
    cl = credit_limit[0].credit_limit

# Log an error message (optional)
frappe.log_error('customer error', f"{outstanding_gl_entries}, {credit_limit}")

# Create an HTML message with credit information
html = f'Limit: {cl}, Due: {outstanding_sales_invoices[0].total if outstanding_sales_invoices[0].total else 0}, Credit Bal: {cl - (outstanding_sales_invoices[0].total if outstanding_sales_invoices[0].total else 0)}'

# Set the response message to the HTML message
frappe.response["message"] = html
