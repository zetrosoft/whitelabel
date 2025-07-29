
frappe.ready(function() {
    // Function to apply translations
    function applyMenuTranslations() {
        const translations = {
            "Buying": "Purchasing",
            "Selling": "Sales & Marketing",
            "Accounts": "Finance",
            "Stock": "Inventory Management"
        };

        // Target elements that might contain the menu labels
        // This includes sidebar links and potentially workspace cards
        for (const [original, translated] of Object.entries(translations)) {
            // Select elements by their text content, which is less brittle than title attributes
            // and more likely to catch various representations of the menu item.
            // We look for elements that are part of the navigation or workspace structure.
            document.querySelectorAll(
                `.sidebar-item-label:not([data-translated="true"]):contains("${original}")` +
                `, .workspace-card-label:not([data-translated="true"]):contains("${original}")`
            ).forEach(element => {
                if (element.textContent.trim() === original) {
                    element.textContent = translated;
                    element.setAttribute("data-translated", "true"); // Mark as translated
                }
            });
        }
    }

    // Apply translations when the desk is ready and on route changes
    frappe.router.on('change', () => {
        // Use a longer delay to ensure all dynamic content is loaded
        setTimeout(applyMenuTranslations, 1000);
    });

    // Also apply on initial load
    setTimeout(applyMenuTranslations, 1000);

    // Observe DOM changes for dynamically loaded content (e.g., after app updates)
    const observer = new MutationObserver((mutations) => {
        mutations.forEach((mutation) => {
            if (mutation.addedNodes.length) {
                applyMenuTranslations();
            }
        });
    });

    // Start observing the body for child list changes and subtree modifications
    observer.observe(document.body, { childList: true, subtree: true });
});
