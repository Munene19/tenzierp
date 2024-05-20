# Copyright (c) 2024, Ltd and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from datetime import datetime


class KRAeTimsRouteTableItem(Document):
    """Route Table doctype child table"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error = None

    def validate(self) -> None:
        """Validation Hook"""
        if self.url_path:
            if not self.url_path.startswith("/"):
                self.url_path = f"/{self.url_path}"

        if not self.last_request_date:
            self.last_request_date = datetime.now()
