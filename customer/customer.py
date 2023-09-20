# if doc.workflow_state !='Approved':
#     doc.disabled=1
    
# if doc.workflow_state =='Approved':
#     if len(doc.accounts) < 1 :
#         frappe.throw("Please Add Accounts Details")
        
# if doc.workflow_state =='Approved':
#     if doc.disabled==1 :
#         frappe.msgprint("Kindly Remove Disabled")
cust_exits = frappe.db.exists("Customer", doc.name)
if cust_exits :
    cust_data = frappe.get_doc("Customer",doc.name)
    if cust_data :
        if cust_data.get("customer_active_type") == "Legal" :
            user = frappe.get_doc("User", frappe.session.user)
            m = 0
            l = 0
            for role in user.roles:
                if role.role == 'Accounts Manager' :
                    m=1
            if m == 0 :
                frappe.throw("Do not have a permission to change customer active type")
                
        if doc.customer_active_type == "Legal" :
            user = frappe.get_doc("User", frappe.session.user)
            for role in user.roles:
                if role.role == 'Customer creation Approver' :
                    l=1
            if l == 0 :
                frappe.throw("Do not have a permission to change customer active type")
