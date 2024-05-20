from .tenzierp.doctype.doctype_names_mapping import (
    COUNTRIES_DOCTYPE_NAME,
    IMPORTED_ITEMS_STATUS_DOCTYPE_NAME,
    ITEM_CLASSIFICATIONS_DOCTYPE_NAME,
    PACKAGING_UNIT_DOCTYPE_NAME,
    PAYMENT_TYPE_DOCTYPE_NAME,
    PRODUCT_TYPE_DOCTYPE_NAME,
    PURCHASE_RECEIPT_DOCTYPE_NAME,
    ROUTES_TABLE_DOCTYPE_NAME,
    STOCK_MOVEMENT_TYPE_DOCTYPE_NAME,
    TAXATION_TYPE_DOCTYPE_NAME,
    TRANSACTION_PROGRESS_DOCTYPE_NAME,
    TRANSACTION_TYPE_DOCTYPE_NAME,
    UNIT_OF_QUANTITY_DOCTYPE_NAME,
)

app_name = "tenzierp"
app_title = "Tenzierp"
app_publisher = "Ltd"
app_description = "KRA Etims Integration for ERPNext based applications"
app_email = "solutions@.co.ke"
app_license = "gpl-3.0"
required_apps = ["frappe/erpnext"]


# Fixtures
# --------
fixtures = [
    {
        "doctype": "Custom Field",
        "filters": [
            [
                "dt",
                "in",
                (
                    "Item",
                    "Sales Invoice",
                    "Sales Invoice Item",
                    "POS Invoice",
                    "POS Invoice Item",
                    "Purchase Invoice",
                    "Purchase Invoice Item",
                    "Customer",
                    "Customer",
                    "Customer Group",
                    "Stock Ledger Entry",
                    "BOM",
                    "Warehouse",
                    "Item Tax Template",
                ),
            ]
        ],
    },
    {"dt": TRANSACTION_TYPE_DOCTYPE_NAME},
    {"dt": PURCHASE_RECEIPT_DOCTYPE_NAME},
    {"dt": UNIT_OF_QUANTITY_DOCTYPE_NAME},
    {"dt": IMPORTED_ITEMS_STATUS_DOCTYPE_NAME},
    {"dt": ROUTES_TABLE_DOCTYPE_NAME},
    {"dt": COUNTRIES_DOCTYPE_NAME},
    {"dt": ITEM_CLASSIFICATIONS_DOCTYPE_NAME},
    {
        "dt": TAXATION_TYPE_DOCTYPE_NAME,
        "filters": [["name", "in", ("A", "B", "C", "D", "E")]],
    },
    {
        "dt": PRODUCT_TYPE_DOCTYPE_NAME,
        "filters": [["name", "in", (1, 2, 3)]],
    },
    {"dt": PACKAGING_UNIT_DOCTYPE_NAME},
    {"dt": STOCK_MOVEMENT_TYPE_DOCTYPE_NAME},
    {
        "dt": PAYMENT_TYPE_DOCTYPE_NAME,
        "filters": [
            [
                "name",
                "in",
                (
                    "CASH",
                    "CREDIT",
                    "CASH/CREDIT",
                    "BANK CHECK",
                    "DEBIT&CREDIT CARD",
                    "MOBILE MONEY",
                    "OTHER",
                ),
            ]
        ],
    },
    {
        "dt": TRANSACTION_PROGRESS_DOCTYPE_NAME,
        "filters": [
            [
                "name",
                "in",
                (
                    "Wait for Approval",
                    "Approved",
                    "Cancel Requested",
                    "Canceled",
                    "Credit Note Generated",
                    "Transferred",
                ),
            ]
        ],
    },
]
# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/tenzierp/css/tenzierp.css"
# app_include_js = "/assets/tenzierp/js/tenzierp.js"

# include js, css files in header of web template
# web_include_css = "/assets/tenzierp/css/tenzierp.css"
# web_include_js = "/assets/tenzierp/js/tenzierp.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "tenzierp/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "Sales Invoice": "tenzierp/overrides/client/sales_invoice.js",
    "POS Invoice": "tenzierp/overrides/client/pos_invoice.js",
    "Customer": "tenzierp/overrides/client/customer.js",
    "Item": "tenzierp/overrides/client/items.js",
    "BOM": "tenzierp/overrides/client/bom.js",
}

doctype_list_js = {
    "Item": "tenzierp/overrides/client/items_list.js",
    "Sales Invoice": "tenzierp/overrides/client/sales_invoice_list.js",
    "POS Invoice": "tenzierp/overrides/client/pos_invoice_list.js",
}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "tenzierp/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "tenzierp.utils.jinja_methods",
# 	"filters": "tenzierp.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "tenzierp.install.before_install"
# after_install = "tenzierp.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "tenzierp.uninstall.before_uninstall"
# after_uninstall = "tenzierp.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "tenzierp.utils.before_app_install"
# after_app_install = "tenzierp.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "tenzierp.utils.before_app_uninstall"
# after_app_uninstall = "tenzierp.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "tenzierp.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
    # 	"*": {
    # 		"on_update": "method",
    # 		"on_cancel": "method",
    # 		"on_trash": "method"
    # 	}
    "Sales Invoice": {
        "on_submit": [
            "tenzierp.tenzierp.overrides.server.sales_invoice.on_submit"
        ],
        "on_update": [
            "tenzierp.tenzierp.overrides.server.sales_invoice.on_update"
        ],
    },
    "POS Invoice": {
        "on_submit": [
            "tenzierp.tenzierp.overrides.server.pos_invoice.on_submit"
        ],
        "on_update": [
            "tenzierp.tenzierp.overrides.server.pos_invoice.pos_on_update"
        ],
    },
    "Stock Ledger Entry": {
        "on_update": [
            "tenzierp.tenzierp.overrides.server.stock_ledger_entry.on_update"
        ]
    },
    "Purchase Invoice": {
        "on_submit": [
            "tenzierp.tenzierp.overrides.server.purchase_invoice.on_submit"
        ],
    },
    "Item": {
        "validate": [
            "tenzierp.tenzierp.overrides.server.item.validate"
        ],
    },
}

# Scheduled Tasks
# ---------------

scheduler_events = {
    # 	"all": [
    # 		"tenzierp.tasks.all"
    # 	],
    # 	"daily": [
    # 		"tenzierp.tasks.daily"
    # 	],
    "hourly": [
        "tenzierp.tenzierp.background_tasks.tasks.send_sales_invoices_information",
        "tenzierp.tenzierp.background_tasks.tasks.send_pos_invoices_information",
        "tenzierp.tenzierp.background_tasks.tasks.send_stock_information",
        "tenzierp.tenzierp.background_tasks.tasks.send_purchase_information",
        "tenzierp.tenzierp.background_tasks.tasks.send_item_inventory_information",
    ],
    # 	"weekly": [
    # 		"tenzierp.tasks.weekly"
    # 	],
    "monthly": [
        "tenzierp.tenzierp.background_tasks.tasks.refresh_code_lists"
    ],
}

# Testing
# -------

# before_tests = "tenzierp.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "tenzierp.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "tenzierp.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["tenzierp.utils.before_request"]
# after_request = ["tenzierp.utils.after_request"]

# Job Events
# ----------
# before_job = ["tenzierp.utils.before_job"]
# after_job = ["tenzierp.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"tenzierp.auth.validate"
# ]
