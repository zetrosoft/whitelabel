import frappe

def run():
    try:
        frappe.db.set_value('Website Settings', 'Website Settings', 'app_logo', '/assets/whitelabel/images/whitelabel_logo.svg')
        frappe.db.commit()
        print("App logo set successfully in Website Settings.")
    except Exception as e:
        print(f"Error setting app logo: {e}")

run()