# -*- coding: utf-8 -*-
#/#############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2004-TODAY Tech-Receptives(<http://www.techreceptives.com>)
#    Special Credit and Thanks to Thymbra Latinoamericana S.A.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#/#############################################################################
from osv import osv
from osv import fields


class OeMedicalMedicationTemplate(osv.osv):
    _name = 'oemedical.medication.template'

    _columns = {
        'name': fields.char(size=256, string='Name'),     
        'start_treatment': fields.datetime(string='Start'),
        'form': fields.many2one('oemedical.drug.form', string='Form', ),
        'route': fields.many2one('oemedical.drug.route',
                                 string='Administration Route', ),
        #'duration_period': fields.selection([], string='Treatment period'),
        'qty': fields.integer(string='x'),
        #'frequency_unit': fields.selection([], string='unit'),
        'dose': fields.float(string='Dose'),
        'duration': fields.integer(string='Treatment duration'),
        'frequency_prn': fields.boolean(string='PRN'),
        'frequency': fields.integer(string='Frequency'),
        'indication': fields.many2one('oemedical.pathology',
                                      string='Indication', ),
        'medicament': fields.many2one('oemedical.medicament',
                                      string='Medicament', ),
        'common_dosage': fields.many2one('oemedical.medication.dosage',
                                         string='Frequency', ),
        'admin_times': fields.char(size=256, string='Admin hours',
                                   required=True),
        'end_treatment': fields.datetime(string='End'),
        'dose_unit': fields.many2one('oemedical.dose.unit',
                                     string='dose unit', ),
    }

OeMedicalMedicationTemplate()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
