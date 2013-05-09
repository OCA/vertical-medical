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


class OeMedicalDiseaseGene(osv.osv):
    _name = 'oemedical.disease.gene'

    _columns = {
        'name': fields.char('Official Symbol', size=256, required=True),
        'gene_id': fields.char('Gene ID', size=256, required=True),
        'long_name': fields.char('Official Long Name', size=256, required=True),
        'location': fields.char('Location', size=256, required=True, help="Locus of the chromosome"),
        'chromosome': fields.char('Affected Chromosome', size=256, required=True),
        'info': fields.text(string='Information'),
        'dominance' : fields.selection([
                    ('d', 'dominant'),
                    ('r', 'recessive'),
                    ], 'Dominance', select=True)

    }

OeMedicalDiseaseGene()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
