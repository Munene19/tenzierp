const doctypeName = "eTims Registered Stock Movement";

frappe.listview_settings[doctypeName] = {
  onload: function (listview) {
    const companyName = frappe.boot.sysdefaults.company;

    listview.page.add_inner_button(
      __("Get Stock Movements"),
      function (listview) {
        frappe.call({
          method:
            "tenzierp.tenzierp.apis.apis.perform_stock_movement_search",
          args: {
            request_data: {
              company_name: companyName,
            },
          },
          callback: (response) => {},
          error: (error) => {
            // Error Handling is Defered to the Server
          },
        });
      }
    );
  },
};
