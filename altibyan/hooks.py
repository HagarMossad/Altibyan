app_name = "altibyan"
app_title = "Altibyan"
app_publisher = "Hagar Mossad"
app_description = "Altibyan"
app_email = "hagermossad80@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "altibyan",
# 		"logo": "/assets/altibyan/logo.png",
# 		"title": "Altibyan",
# 		"route": "/altibyan",
# 		"has_permission": "altibyan.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/altibyan/css/altibyan.css"
# app_include_js = "/assets/altibyan/js/altibyan.js"

# include js, css files in header of web template
# web_include_css = "/assets/altibyan/css/altibyan.css"
# web_include_js = "/assets/altibyan/js/altibyan.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "altibyan/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"Sales Order" : "public/js/sales_order.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "altibyan/public/icons.svg"

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
# 	"methods": "altibyan.utils.jinja_methods",
# 	"filters": "altibyan.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "altibyan.install.before_install"
# after_install = "altibyan.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "altibyan.uninstall.before_uninstall"
# after_uninstall = "altibyan.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "altibyan.utils.before_app_install"
# after_app_install = "altibyan.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "altibyan.utils.before_app_uninstall"
# after_app_uninstall = "altibyan.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "altibyan.notifications.get_notification_config"

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
	"Batch": {
		"before_save": "altibyan.controllers.batch.fetch_barcode",
	},
    "Item" : {
        "before_insert": "altibyan.controllers.item.calculate_total",
    },
    "Sales Order":{
        "on_submit":"altibyan.controllers.sales_order.on_submit"
    },
    "Customer":{
        "before_insert":"altibyan.controllers.customer.before_insert"
    },
    "Supplier":{
        "before_insert":"altibyan.controllers.supplier.before_insert"
    },
    "Landed Cost Voucher":{
        "validate": "altibyan.controllers.landed_cost.validate"
    },
    "Delivery Note":{
        "validate": "altibyan.controllers.delivery_note.validate",
        "on_submit":"altibyan.controllers.delivery_note.on_submit"
    },
    "Sales Invoice":{
        "validate": "altibyan.controllers.sales_invoice.validate",
        "on_submit":"altibyan.controllers.sales_invoice.on_submit"
    },
}
after_install = [
    "altibyan.install.after_install",
    ]

after_migrate = [
    "altibyan.install.after_install",
]

domains = {
    "Tebian" : "altibyan.domains.tebian",
}

# Scheduled Tasks
# ---------------

scheduler_events = {
# 	"all": [
# 		"altibyan.tasks.all"
# 	],
# 	"daily": [
# 		"altibyan.tasks.daily"
# 	],
# 	"hourly": [
# 		"altibyan.tasks.hourly"
# 	],
# 	"weekly": [
# 		"altibyan.tasks.weekly"
# 	],
	"monthly": [
		"altibyan.controllers.customer.class_classification"
	],
}

# Testing
# -------

# before_tests = "altibyan.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "altibyan.event.get_events"
# }
override_whitelisted_methods = {
	# "erpnext.stock.utils.scan_barcode": "altibyan.api.scan_batch_barcode"
}
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "altibyan.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["altibyan.utils.before_request"]
# after_request = ["altibyan.utils.after_request"]

# Job Events
# ----------
# before_job = ["altibyan.utils.before_job"]
# after_job = ["altibyan.utils.after_job"]

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
# 	"altibyan.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

