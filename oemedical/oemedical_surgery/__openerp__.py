# -*- encoding: utf-8 -*-
{

	'name' : 'Medical : Surgery module',  
	'version' : '1.0',
	'author' : 'Thymbra',
	'category' : 'Generic Modules/Others',
	'depends' : ['medical'],
	'description' : """

Surgery Module for Medical.

If you want to include standard procedures, please install the correspondant procedure module (such as medical_icd10)
""",
	"website" : "http://medical.sourceforge.net",
	"init_xml" : [],
	"update_xml" : ["medical_surgery_view.xml","security/ir.model.access.csv"],
	"active": False 
}
