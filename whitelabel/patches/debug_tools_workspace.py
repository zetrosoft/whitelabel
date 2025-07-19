import frappe

def execute():
    try:
        tools_workspace = frappe.get_doc('Workspace', 'Tools')
        frappe.msgprint(f"Tools Workspace Shortcuts: {tools_workspace.shortcuts}")
            
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Failed to debug Tools workspace")
        frappe.msgprint(f"Error debugging Tools workspace: {e}")
