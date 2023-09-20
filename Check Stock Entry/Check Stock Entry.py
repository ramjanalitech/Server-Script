jc = frappe.form_dict.doc
jc = json.loads(jc)
ae = frappe.db.count("Stock Entry",{'job_card': jc.get("name")})
if ae > 0:
    frappe.response["message"] = True
else :
    frappe.response["message"] = False
