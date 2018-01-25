/* Copyright 2016 LasLabs Inc.
 * License GPL-3.0 or later (http://www.gnu.org/licenses/gpl). */

odoo.define("medical.tour", function (require) {
    "use strict";
    
    var core = require('web.core');
    var tour = require('web_tour.tour');
    
    var _t = core._t;
    
    tour.STEPS.MEDICAL = [
        tour.STEPS.MENU_MORE,
        {
            trigger: '.o_app[data-menu-xmlid="medical.medical_root"], .oe_menu_toggler[data-menu-xmlid="medical.medical_root"]',
            content: _t('Manage electronic medical records using the <b>Medical</b> app.'),
            position: 'bottom',
        },
    ];
    
    tour.register('medical_tour', {
        url: "/web",
    },
        tour.STEPS.MEDICAL
    );

});
