import frappe

def execute():
    custom_workspaces = {
        "Buying": {"label": "Purchasing", "sequence_id": 1},
        "Selling": {"label": "Sales & Marketing", "sequence_id": 2},
        "Accounts": {"label": "Finance", "sequence_id": 3},
        "Stock": {"label": "Inventory Management", "sequence_id": 4},
    }

    for original_label, details in custom_workspaces.items():
        # Check if a workspace with the original label exists
        if frappe.db.exists("Workspace", original_label):
            # If it exists, update its properties
            workspace = frappe.get_doc("Workspace", original_label)
            workspace.label = details["label"]
            workspace.title = details["label"] # Assuming title should also be translated
            workspace.sequence_id = details["sequence_id"]
            workspace.is_hidden = 0 # Ensure it's not hidden
            workspace.save()
            frappe.db.commit()
        else:
            # If it doesn't exist, create a new one
            workspace = frappe.new_doc("Workspace")
            workspace.label = details["label"]
            workspace.title = details["label"]
            workspace.sequence_id = details["sequence_id"]
            workspace.is_hidden = 0
            workspace.for_user = None # Make it public
            workspace.module = "Whitelabel" # Assign to your custom app module
            workspace.save()
            frappe.db.commit()
