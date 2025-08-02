frappe.ui.form.on('DocType Settings', {
	refresh: function(frm) {
		// Wrapper for the custom UI
		let wrapper = frm.get_field('doctype_cards').$wrapper;
		wrapper.html(`
			<div class="doctype-settings-container">
				<div class="doctype-settings-toolbar">
					<div class="form-group">
						<div class="checkbox">
							<label>
								<input type="checkbox" class="show-hidden-only">
								${__('Show only hidden doctypes')}
							</label>
						</div>
					</div>
				</div>
				<div class="doctype-cards-container"></div>
			</div>
		`);

		let container = wrapper.find('.doctype-cards-container');
		let show_hidden_only_cb = wrapper.find('.show-hidden-only');

		let hidden_doctypes = JSON.parse(frm.doc.hidden_doctypes || '[]');

		frappe.call({
			method: 'whitelabel.api.get_all_doctypes_for_settings',
			callback: function(r) {
				let doctypes_by_module = {};

				// Group doctypes by module
				r.message.forEach(d => {
					if (!doctypes_by_module[d.module]) {
						doctypes_by_module[d.module] = [];
					}
					doctypes_by_module[d.module].push(d.name);
				});

				// Render cards for each module
				for (let module in doctypes_by_module) {
					let doctypes = doctypes_by_module[module];
					doctypes.sort();

					let card_html = `
						<div class="frappe-card doctype-module-card" data-module="${module}">
							<div class="frappe-card-head">
								<div class="card-title">
									<h5>${__(module)}</h5>
								</div>
							</div>
							<div class="frappe-card-body">
								<div class="doctype-list">
									${doctypes.map(dt => `
										<div class="doctype-checkbox" data-doctype="${dt}">
											<div class="checkbox">
												<label>
													<input type="checkbox" data-doctype-name="${dt}" ${hidden_doctypes.includes(dt) ? 'checked' : ''}>
													${__(dt)}
												</label>
											</div>
										</div>
									`).join('')}
								</div>
							</div>
						</div>
					`;
					container.append(card_html);
				}

				// Handle checkbox changes
				wrapper.on('change', 'input[type="checkbox"][data-doctype-name]', function() {
					let doctype = $(this).data('doctype-name');
					if (this.checked) {
						if (!hidden_doctypes.includes(doctype)) {
							hidden_doctypes.push(doctype);
						}
					} else {
						hidden_doctypes = hidden_doctypes.filter(d => d !== doctype);
					}
					frm.set_value('hidden_doctypes', JSON.stringify(hidden_doctypes, null, 2));
				});

				// Handle filter
				show_hidden_only_cb.on('change', function() {
					let show_hidden = this.checked;
					wrapper.find('.doctype-module-card').each(function() {
						let module_card = $(this);
						let has_visible_doctype = false;

						module_card.find('.doctype-checkbox').each(function() {
							let dt_checkbox = $(this);
							let doctype_name = dt_checkbox.data('doctype');
							let is_hidden = hidden_doctypes.includes(doctype_name);

							if (show_hidden) {
								dt_checkbox.toggle(is_hidden);
							} else {
								dt_checkbox.show();
							}

							if (dt_checkbox.is(':visible')) {
								has_visible_doctype = true;
							}
						});

						module_card.toggle(has_visible_doctype);
					});
				});
			}
		});
	},
	after_save: function() {
		frappe.ui.toolbar.clear_cache();
		frappe.show_alert({message: __("DocType settings saved. Please refresh to see changes."), indicator: "green"});
	}
});