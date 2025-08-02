import frappe
import json

@frappe.whitelist()
def get_doctypes_whitelabel():
    """Returns a list of DocTypes for the Role Permission Manager, respecting whitelabel settings."""
    # Get the original list of doctypes
    doctypes = frappe.call('frappe.core.doctype.role_permission_manager.role_permission_manager.get_doctypes')

    try:
        hidden_doctypes_str = frappe.db.get_single_value('DocType Settings', 'hidden_doctypes')
        if hidden_doctypes_str:
            hidden_doctypes = json.loads(hidden_doctypes_str)
            # Filter out the hidden doctypes
            doctypes = [dt for dt in doctypes if dt not in hidden_doctypes]

    except (frappe.DoesNotExistError, json.JSONDecodeError):
        # If DocType Settings doesn't exist or the JSON is invalid, return the original list
        pass

    return doctypes
