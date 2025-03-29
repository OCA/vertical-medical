/** @odoo-module **/
import {PartnerDetailsEdit} from "@point_of_sale/app/screens/partner_list/partner_editor/partner_editor";
import {patch} from "@web/core/utils/patch";

patch(PartnerDetailsEdit.prototype, {
    setup() {
        super.setup(...arguments);
        this.changes.weight = this.props.partner.weight || null;
        this.changes.weight_uom = this.props.partner.weight_uom || null;
    },
});
