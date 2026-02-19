# ERPNext Python Developer Assessment Task

This repository contains a custom Frappe application developed for the Python Developer Assessment. The project focuses on Employee Management and Leave Request workflows, featuring backend validations and automated data fetching.

## 🚀 Project Implementation Proof

All functional requirements, including backend validations (Red Error Popups), auto-fetching logic, and CSV export features, are documented in the PDF below:

👉 **[View Implementation Screenshots (PDF)](https://www.google.com/search?q=./Task_Validation_Screenshots.pdf)**

---

## 🛠️ Setup & Installation

Follow these steps to install the app on your local Frappe/ERPNext bench:

1. **Get the app from GitHub:**
```bash
bench get-app erpnext_assessment https://github.com/vivekjoshi2006/ERPNext-Python-Developer-Assessment-Task.git

```


2. **Install the app on your site:**
*(Replace `[your-site-name]` with your actual site name, e.g., site1.local)*
```bash
bench --site [your-site-name] install-app erpnext_assessment

```


3. **Build and Migrate:**
```bash
bench build
bench --site [your-site-name] migrate

```



---

## 🔐 Test Credentials

For evaluation, you may use the default administrator credentials or the following test setup:

| Role | Username | Password |
| --- | --- | --- |
| **Administrator** | `administrator` | `admin` |

---

## 📡 API Endpoints (REST)

The system exposes standard Frappe REST API endpoints for integration:

* **Employee Data:** `GET /api/resource/Employee Management`
* **Leave Requests:** `POST /api/resource/Leave Request`
* **Export Service:** `GET /api/method/frappe.desk.reportview.export_query`

---

## 🛑 Key Features & Validations

### 1. Backend Validation (Python)

* **Date Integrity:** A `before_save` controller in Python ensures that the `To Date` cannot be earlier than the `From Date`. It triggers a `frappe.throw` error, preventing invalid data from reaching the database.

### 2. Automated Logic (JavaScript)

* **Dynamic Fetching:** Used `frm.add_fetch` and Client Scripts to automatically populate the Employee Name when an Employee ID is selected, improving UX and data accuracy.

### 3. Data Export

* **CSV Utility:** Configured Role Permissions to allow the export of Leave Request data directly from the List View.

### 4. Search & Pagination

* **Standard UI:** Leverages Frappe’s built-in search filters and pagination for handling large datasets efficiently.
