import frappe
import json

def get_doctype_list_whitelabel(args=None):
    """Returns a list of DocTypes with read permission, respecting whitelabel settings."""
    # Get the original list of doctypes
    original_doctypes = frappe.call('frappe.desk.reportview.get_doctype_list', args)

    try:
        hidden_doctypes_str = frappe.db.get_single_value('DocType Settings', 'hidden_doctypes')
        if hidden_doctypes_str:
            hidden_doctypes = json.loads(hidden_doctypes_str)
            # Filter out the hidden doctypes
            original_doctypes = [d for d in original_doctypes if d.get('name') not in hidden_doctypes]
    except (frappe.DoesNotExistError, json.JSONDecodeError):
        # If DocType Settings doesn't exist or the JSON is invalid, return the original list
        pass

    return original_doctypes
