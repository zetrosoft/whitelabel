from frappe import _

def get_workspace_label_overrides():
    return {
        "Buying": _("Purchasing"),
        "Selling": _("Sales & Marketing"),
        "Accounts": _("Finance"),
        "Stock": _("Inventory Management"),
    }