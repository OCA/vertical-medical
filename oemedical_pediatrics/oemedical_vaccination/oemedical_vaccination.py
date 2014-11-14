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

from openerp.osv import fields, orm


class OeMedicalVaccination(orm.Model):
    _name = 'oemedical.vaccination'

    _columns = {
        'name': fields.char(size=256, string='Name'),
        'vaccine_lot': fields.char(size=256, string='Lot Number',
                                   help='Please check on the vaccine (product) production lot numberand'
                                   ' tracking number when available !'),
        'patient_id': fields.many2one('oemedical.patient', string='Patient',
                                      readonly=True),
        'vaccine': fields.many2one('product.product', string='Vaccine',
                                   required=True,
                                   help='Vaccine Name. Make sure that the vaccine (product) has all the'
                                   ' proper information at product level. Information such as provider,'
                                   ' supplier code, tracking number, etc.. This  information must always'
                                   ' be present. If available, please copy / scan the vaccine leaflet'
                                   ' and attach it to this record'),
        'dose': fields.integer(string='Dose #'),
        'observations': fields.char(size=256, string='Observations',
                                    required=True),
        'date': fields.datetime(string='Date'),
        'institution': fields.many2one('res.partner', string='Institution',
                                       help='Medical Center where the patient is being or was vaccinated'),
        'next_dose_date': fields.datetime(string='Next Dose'),
    }

OeMedicalVaccination()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
