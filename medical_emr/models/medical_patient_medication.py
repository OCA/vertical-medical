# -*- coding: utf-8 -*-
###############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2004-TODAY Tech-Receptives(<http://www.techreceptives.com>)
#    Special Credit and Thanks to Thymbra Latinoamericana S.A.
#    Ported to 8.0 by Dave Lasley - LasLabs (https://laslabs.com)
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
###############################################################################

from openerp.osv import fields, orm


class MedicalPatientMedication(orm.Model):
    _name = 'medical.patient.medication'

    _columns = {
        'patient_id': fields.many2one('medical.patient', string='Patient',),
        #        'name': fields.many2one('medical.patient', string='Patient',
        #                                readonly=True ),
        'doctor': fields.many2one('medical.physician', string='Physician',
                                  help='Physician who prescribed the medicament'),
        'adverse_reaction': fields.text(string='Adverse Reactions',
                                        help='Side effects or adverse reactions that the patient experienced'),
        'notes': fields.text(string='Extra Info'),
        'is_active': fields.boolean(string='Active',
                                    help='Check if the patient is currently taking the medication'),
        'course_completed': fields.boolean(string='Course Completed'),
        'template': fields.many2one('medical.medication.template',
                                    string='Medication Template', ),
        'discontinued_reason': fields.char(size=256,
                                           string='Reason for discontinuation',
                                           help='Short description for discontinuing the treatment'),
        'discontinued': fields.boolean(string='Discontinued'),
    }


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
