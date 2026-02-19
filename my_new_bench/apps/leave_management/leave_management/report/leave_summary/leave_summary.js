frappe.query_reports["Leave Summary"] = {
    filters: [

    ],
    formatter: function(value, row, column, data, default_formatter) {
        return default_formatter(value, row, column, data);
    }
};
