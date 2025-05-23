from odoo import models


class PosOrderLine(models.Model):
    _inherit = "pos.order.line"

    def _export_for_ui(self, orderline):
        result = super()._export_for_ui(orderline)
        result["is_splitting_invoice_unpaid"] = orderline._is_splitting_invoice_unpaid()
        result["is_splitted_move_line"] = orderline._is_splitted_move_line()
        return result

    def _is_splitting_invoice_unpaid(self):
        move = self.order_id.splitting_move_id
        return bool(move and move.payment_state != "paid")

    def _is_splitted_move_line(self):
        move = self.order_id.splitting_move_id
        if not move:
            return False
        return any(line.product_id == self.product_id for line in move.invoice_line_ids)
