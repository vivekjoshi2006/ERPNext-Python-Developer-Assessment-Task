import frappe

def execute(filters=None):
    columns = [
        {"label": "Employee", "fieldname": "employee", "fieldtype": "Data", "width": 150},
        {"label": "Total Leaves", "fieldname": "total", "fieldtype": "Int", "width": 120},
        {"label": "Approved", "fieldname": "approved", "fieldtype": "Int", "width": 120},
        {"label": "Pending", "fieldname": "pending", "fieldtype": "Int", "width": 120},
        {"label": "Canceled", "fieldname": "canceled", "fieldtype": "Int", "width": 120},
    ]

    data = frappe.db.sql("""
        SELECT
            employee,
            COUNT(name) as total,
            SUM(status='Approved') as approved,
            SUM(status='Open') as pending,
            SUM(status='Cancelled') as canceled
        FROM `tabLeave Application`
        GROUP BY employee
    """, as_dict=True)

    return columns, data
