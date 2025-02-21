# Copyright (c) 2024, Ltd and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class eTimsRoutes(Document):
    """Routes Table Doctype"""

    def validate(self) -> None:
        """Validation Hook"""

        # Call validations in child tables
        for child in self.routes_table:
            child.validate()
