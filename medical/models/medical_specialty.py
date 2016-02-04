# -*- coding: utf-8 -*-
# © 2015 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.osv import fields, orm


class MedicalSpecialty(orm.Model):
    _name = 'medical.specialty'
    _columns = {
        'code': fields.char(size=256, string='Code'),
        'name': fields.char(size=256, string='Specialty', required=True,
                            translate=True),
    }
    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)', 'Name must be unique!'),
    ]
