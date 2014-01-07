# coding=utf-8

#    Copyright (C) 2008-2010  Luis Falcon

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.



from osv import fields, osv


class surgery (osv.osv):
	_name = "medical.surgery"
	_description = "Surgery"
	_columns = {
		'name' : fields.many2one ('medical.procedure','Code', help="Procedure Code, for example ICD-10-PCS Code 7-character string"),
		'pathology' : fields.many2one ('medical.pathology','Base condition', help="Base Condition / Reason"),
		'classification' : fields.selection ([
				('o','Optional'),
				('r','Required'),
				('u','Urgent'),
                                ], 'Surgery Classification', select=True),
		'surgeon' : fields.many2one('medical.physician','Surgeon', help="Surgeon who did the procedure"),
		'date': fields.datetime ('Date of the surgery'),
		'age': fields.char ('Patient age',size=3,help='Patient age at the moment of the surgery. Can be estimative'),
		'description' : fields.char ('Description', size=128),
		'extra_info' : fields.text ('Extra Info'),
		}

surgery ()


# Add to the Medical patient_data class (medical.patient) the surgery field.

class medical_patient (osv.osv):
	_name = "medical.patient"
	_inherit = "medical.patient"
	_columns = {
		'surgery' : fields.many2many ('medical.surgery', 'patient_surgery_rel','patient_id','surgery_id', 'Surgeries'),
		
	}

medical_patient ()




