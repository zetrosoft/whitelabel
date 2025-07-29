import frappe

def execute():
    translations = {
        "Buying": "Purchasing",
        "Selling": "Sales & Marketing",
        "Accounts": "Finance",
        "Stock": "Inventory Management",
    }

    for english_label, indonesian_label in translations.items():
        if frappe.db.exists("Workspace", english_label):
            workspace = frappe.get_doc("Workspace", english_label)
            workspace.label = indonesian_label
            workspace.title = indonesian_label
            workspace.save()
            frappe.db.commit()