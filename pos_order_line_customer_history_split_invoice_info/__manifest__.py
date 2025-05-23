{
    "name": "Point of Sale - Customer history split invoice info",
    "summary": "Customer history split invoice info",
    "version": "17.0.1.0.0",
    "category": "Point of sale",
    "website": "https://github.com/OCA/vertical-medical",
    "author": "Serpent Consulting Services Pvt. Ltd., Odoo Community Association (OCA)",
    "maintainers": ["Serpent Consulting Services Pvt. Ltd."],
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "point_of_sale",
        "pos_order_line_customer_history",
        "pos_order_split_invoice",
    ],
    "assets": {
        "point_of_sale._assets_pos": [
            "pos_order_line_customer_history_split_invoice_info/static/src/Screens/CustomerHistoryScreen.xml"
        ]
    },
}
