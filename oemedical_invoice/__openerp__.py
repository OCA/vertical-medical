# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2010  Adrián Bernardi, Mario Puntin
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name" : "Medical Invoice",
    "version" : "0.1",
    "author" : "Silix",
    "description" : """ 
        This module add functionality to create invoices for doctor's consulting charge.

        Features:
        -Invoice of multiple appointments at a time.
        """,
    "website" : "http://www.silix.com.ar",
    "depends" : ["medical","medical_lab"],
    "category" : "Generic Modules/Others",
    "init_xml" : [],
    "demo_xml" : [],
    "update_xml" : [
        "views/medical_invoice_view.xml",
        "views/appointment_invoice.xml",
        "views/prescription_invoice.xml",
        "views/create_lab_invoice.xml"           
    ],
    'installable': False,
    'active': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
