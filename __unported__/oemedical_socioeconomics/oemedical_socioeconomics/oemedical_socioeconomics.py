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
from openerp.tools.translate import _
from dateutil.relativedelta import relativedelta
from datetime import datetime


class OeMedicalSocioeconomics(orm.Model):

    _inherit='oemedical.patient'

    _columns={
            'ses' : fields.selection([
                (None, ''),
                ('0', 'Lower'),
                ('1', 'Lower-middle'),
                ('2', 'Middle'),
                ('3', 'Middle-upper'),
                ('4', 'Higher'),
                ], 'Socioeconomics', help="SES - Socioeconomic Status", sort=False),
            'housing' : fields.selection([
                (None, ''),
                ('0', 'Shanty, deficient sanitary conditions'),
                ('1', 'Small, crowded but with good sanitary conditions'),
                ('2', 'Comfortable and good sanitary conditions'),
                ('3', 'Roomy and excellent sanitary conditions'),
                ('4', 'Luxury and excellent sanitary conditions'),
                ], 'Housing conditions', help="Housing and sanitary living conditions", sort=False),
            'hostile_area' : fields.boolean('Hostile Area', help="Check if patient lives in a zone of high hostility (eg, war)"),
            'sewers' : fields.boolean('Sanitary Sewers'),
            'water' : fields.boolean('Running Water'),
            'trash' : fields.boolean('Trash recollection'),
            'electricity' : fields.boolean('Electrical supply'),
            'gas' : fields.boolean('Gas supply'),
            'telephone' : fields.boolean('Telephone'),
            'television' : fields.boolean('Television'),
            'internet' : fields.boolean('Internet'),
            'single_parent' : fields.boolean('Single parent family'),
            'domestic_violence' : fields.boolean('Domestic violence'),
            'working_children' : fields.boolean('Working children'),
            'teenage_pregnancy' : fields.boolean('Teenage pregnancy'),
            'sexual_abuse' : fields.boolean('Sexual abuse'),
            'drug_addiction' : fields.boolean('Drug addiction'),
            'school_withdrawal' : fields.boolean('School withdrawal'),
            'prison_past' : fields.boolean('Has been in prison'),
            'prison_current' : fields.boolean('Is currently in prison'),
            'relative_in_prison' : fields.boolean('Relative in prison', help="Check if someone from the nuclear family - parents sibblings  is or has been in prison"),
            'ses_notes' : fields.text('Extra info'),
            'fam_apgar_help' : fields.selection([
                (None, ''),
                ('0', 'None'),
                ('1', 'Moderately'),
                ('2', 'Very much'),
                ], 'Help from family',
                help="Is the patient satisfied with the level of help coming from the family when there is a problem ?", sort=False),
            'fam_apgar_discussion' : fields.selection([
                (None, ''),
                ('0', 'None'),
                ('1', 'Moderately'),
                ('2', 'Very much'),
                ], 'Problems discussion',
                help="Is the patient satisfied with the level talking over the problems as family ?", sort=False),
            'fam_apgar_decisions' : fields.selection([
                (None, ''),
                ('0', 'None'),
                ('1', 'Moderately'),
                ('2', 'Very much'),
                ], 'Decision making',
                help="Is the patient satisfied with the level of making important decisions as a group ?", sort=False),
            'fam_apgar_timesharing' : fields.selection([
                (None, ''),
                ('0', 'None'),
                ('1', 'Moderately'),
                ('2', 'Very much'),
                ], 'Time sharing',
                help="Is the patient satisfied with the level of time that they spend together ?", sort=False),
            'fam_apgar_affection' : fields.selection([
                (None, ''),
                ('0', 'None'),
                ('1', 'Moderately'),
                ('2', 'Very much'),
                ], 'Family affection',
                help="Is the patient satisfied with the level of affection coming from the family ?", sort=False),
            'fam_apgar_score' : fields.integer('Score', help="Total Family APGAR 7 - 10 : Functional Family 4 - 6  : Some level of disfunction \n" \
                "0 - 3  : Severe disfunctional family \n"), 
            'income' : fields.selection([
                (None, ''),
                ('h', 'High'),
                ('m', 'Medium / Average'),
                ('l', 'Low'),
                ], 'Income', sort=False),
            'education' : fields.selection([
                (None, ''),
                ('0', 'None'),
                ('1', 'Incomplete Primary School'),
                ('2', 'Primary School'),
                ('3', 'Incomplete Secondary School'),
                ('4', 'Secondary School'),
                ('5', 'University'),
                ], 'Education Level', help="Education Level", sort=False),
            'works_at_home' : fields.boolean('Works at home', help="Check if the patient works at his / her house"),
            'hours_outside' : fields.integer('Hours outside home', help="Number of hours a day the patient spend outside the house"),

                }


OeMedicalSocioeconomics()
