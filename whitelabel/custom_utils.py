import frappe

@frappe.whitelist()
def get_public_workspaces():
    workspaces = frappe.get_all('Workspace', filters={'public': 1}, fields=['name', 'sequence_id'], order_by='sequence_id asc')
    return workspaces

@frappe.whitelist()
def update_workspace_order(workspace_names):
    for i, name in enumerate(workspace_names):
        frappe.db.set_value('Workspace', name, 'sequence_id', i + 1)
    frappe.db.commit()
    return {"status": "success", "message": "Workspace order updated."}

@frappe.whitelist()
def get_workspace_doc(workspace_name):
    doc = frappe.get_doc('Workspace', workspace_name)
    return doc.as_dict()

@frappe.whitelist()
def add_shortcut_to_workspace(workspace_name, shortcut_label, shortcut_type, link_to, doc_type=None):
    doc = frappe.get_doc('Workspace', workspace_name)
    
    new_shortcut = {
        "label": shortcut_label,
        "type": shortcut_type,
        "link_to": link_to,
        "doc_type": doc_type,
        "parentfield": "shortcuts",
        "parenttype": "Workspace",
        "parent": workspace_name
    }
    doc.append("shortcuts", new_shortcut)
    doc.save()
    frappe.db.commit()
    return {"status": "success", "message": f"Shortcut '{shortcut_label}' added to '{workspace_name}' workspace."}

@frappe.whitelist()
def check_doctype_exists(doctype_name):
    return frappe.db.exists('DocType', doctype_name)
