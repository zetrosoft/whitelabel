
frappe.ui.form.on('Custom Utils Actions', {
    refresh: function(frm) {
        frm.add_custom_button(__('Get Public Workspaces'), function() {
            frappe.call({
                method: "whitelabel.custom_utils.get_public_workspaces",
                callback: function(r) {
                    if (r.message) {
                        frm.set_value('workspaces_json', JSON.stringify(r.message, null, 2));
                    }
                }
            });
        }, __('Actions'));

        frm.add_custom_button(__('Update Workspace Order'), function() {
            let new_order_str = frm.doc.new_workspace_order;
            if (new_order_str) {
                let workspace_names = new_order_str.split(',').map(item => item.trim());
                frappe.call({
                    method: "whitelabel.custom_utils.update_workspace_order",
                    args: {
                        workspace_names: workspace_names
                    },
                    callback: function(r) {
                        if (r.message) {
                            frappe.msgprint(r.message.message);
                            frm.set_value('workspaces_json', ''); // Clear the JSON after update
                            frm.set_value('new_workspace_order', ''); // Clear the input
                        }
                    }
                });
            } else {
                frappe.msgprint(__('Please enter the new workspace order.'));
            }
        }, __('Actions'));
    }
});
