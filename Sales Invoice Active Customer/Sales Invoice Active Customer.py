cust_data = frappe.get_doc("Customer",doc.customer)
if cust_data.get("customer_active_type") != "Active" :
    frappe.throw("Customer Not Active")