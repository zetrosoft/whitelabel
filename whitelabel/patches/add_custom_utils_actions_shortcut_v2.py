import frappe

def execute():
    try:
        tools_workspace = frappe.get_doc('Workspace', 'Tools')
        
        # Check if the shortcut already exists to prevent duplicates
        shortcut_exists = False
        for shortcut in tools_workspace.shortcuts:
            if shortcut.label == 'Custom Utils Actions' and shortcut.link_to == 'Custom Utils Actions':
                shortcut_exists = True
                break
        
        if not shortcut_exists:
            tools_workspace.append('shortcuts', {
                'label': 'Custom Utils Actions',
                'type': 'DocType',
                'link_to': 'Custom Utils Actions',
                'doc_type': 'Custom Utils Actions'
            })
            tools_workspace.save()
            frappe.db.commit()
            frappe.msgprint("Shortcut 'Custom Utils Actions' added to 'Tools' workspace.")
        else:
            frappe.msgprint("Shortcut 'Custom Utils Actions' already exists in 'Tools' workspace.")
            
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Failed to add Custom Utils Actions shortcut")
        frappe.msgprint(f"Error adding shortcut: {e}")
