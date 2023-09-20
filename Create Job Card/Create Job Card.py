pp = frappe.form_dict.doc
pp = json.loads(pp)
ae = frappe.db.count("Job Card",{'work_order': pp.get("name")})
if ae > 0:
    frappe.response["message"] = False
else:
    frappe.response["message"] = "ok"