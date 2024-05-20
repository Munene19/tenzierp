const doctypeName = "eTims Branch";

frappe.listview_settings[doctypeName] = {
  onload: function (listview) {
    const companyName = frappe.boot.sysdefaults.company;

    listview.page.add_inner_button(__("Get Branches"), function (listview) {
      frappe.call({
        method:
          "tenzierp.tenzierp.apis.apis.search_branch_request",
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
    });
  },
};
