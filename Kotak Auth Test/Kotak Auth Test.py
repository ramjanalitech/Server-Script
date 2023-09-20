api_host_name = frappe.db.get_single_value("Kotak Settings", "api_host_name")
client_code = frappe.db.get_single_value("Kotak Settings", "client_code")
client_id = frappe.db.get_single_value("Kotak Settings", "client_id")
client_secret = frappe.db.get_single_value("Kotak Settings", "client_secret")

try:
    url = "https://apigw.kotak.com:8443/auth/oauth/v2/token"
    payload = f"grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    r = frappe.make_post_request(url, data=payload, headers=headers)
    # r = frappe.make_get_request("https://dummyjson.com/products")
    # frappe.log_error(r)
    # log = frappe.get_doc({
    #     "doctype": "Kotak API Log",
    #     "request_type": "Auth",
    #     "request": "sjdksd",
    #     "response": "sjdhskjdlskdjhsk",
    #     "access_token": "skjdsj dhksjd"
    #     })
    # log.insert(ignore_permissions=True)
    # frappe.db.commit()
    frappe.response["message"] = r
except Exception as e:
    # frappe.log_error(e)
    frappe.response["message"] = e