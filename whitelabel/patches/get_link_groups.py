import frappe
import json

@frappe.whitelist()
def get_link_groups_whitelabel(page, is_main_workspace):
    """Returns link groups for a workspace, respecting whitelabel settings."""
    # Get the original link groups
    link_groups = frappe.call('frappe.desk.page.workspace.workspace.get_link_groups', page=page, is_main_workspace=is_main_workspace)

    try:
        hidden_doctypes_str = frappe.db.get_single_value('DocType Settings', 'hidden_doctypes')
        if hidden_doctypes_str:
            hidden_doctypes = json.loads(hidden_doctypes_str)

            # Filter out links to hidden doctypes
            for group in link_groups:
                if group.get('links'):
                    group['links'] = [link for link in group['links'] if link.get('name') not in hidden_doctypes]

            # Remove empty groups
            link_groups = [group for group in link_groups if group.get('links')]

    except (frappe.DoesNotExistError, json.JSONDecodeError):
        # If DocType Settings doesn't exist or the JSON is invalid, return the original list
        pass

    return link_groups
