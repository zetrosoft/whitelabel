import frappe

def execute():
    workspaces_to_hide = ["Buying", "Selling", "Accounts", "Stock"]

    for workspace_name in workspaces_to_hide:
        if frappe.db.exists("Workspace", workspace_name):
            workspace = frappe.get_doc("Workspace", workspace_name)
            workspace.is_hidden = 1
            workspace.save()
            frappe.db.commit()