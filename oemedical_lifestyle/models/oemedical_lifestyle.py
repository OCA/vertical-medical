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


class DrugsRecreational(orm.Model):
    
    _name = 'oemedical.drugs_recreational'
    _description = 'Recreational Drug'
    _columns = {


    'name' : fields.char('Name', translate=True, help="Name of the drug"),
    'street_name' : fields.char('Street names',
        help="Common name of the drug in street jargon"),

    'toxicity' : fields.selection([
        ('0', 'None'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Extreme'),
        ], 'Toxicity', sort=False),

    'addiction_level' : fields.selection([
        ('0', 'None'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Extreme'),
        ], 'Dependence', sort=False),

    'legal_status' : fields.selection([
        ('0', 'Legal'),
        ('1', 'Illegal'),
        ], 'Legal Status', sort=False),

    'category' : fields.selection([
        ('cannabinoid', 'Cannabinoids'),
        ('depressant', 'Depressants'),
        ('dissociative', 'Dissociative Anesthetics'),
        ('hallucinogen', 'Hallucinogens'),
        ('opioid', 'Opioids'),
        ('stimulant', 'Stimulants'),
        ('other', 'Others'),
        ], 'Category', sort=False),

    'withdrawal_level' : fields.integer('Withdrawal',
        help="Presence and severity of characteristic withdrawal "
        "symptoms.\nUsing Henningfield rating. 1=highest and 6=lowest"),

    'reinforcement_level' : fields.integer('Reinforcement',
        help="A measure of the substance's ability to get users to take it "
        " again and again, and in preference to other substances.\nUsing "
        " Henningfield rating. 1=highest and 6=lowest"),

    'tolerance_level' : fields.integer('Tolerance',
        help="How much of the substance is needed to satisfy increasing "
        "cravings for it, and the level of stable need that is eventually "
        "reached.\nUsing Henningfield rating. 1=highest and 6=lowest"),

    'dependence_level' : fields.integer('Dependence',
        help="How difficult it is for the user to quit, the relapse rate, "
        "the percentage of people who eventually become dependent, the "
        "rating users give their own need for the substance and the "
        "degree to which the substance will be used in the face of "
        "evidence that it causes harm.\nUsing Henningfield rating. "
        "1=highest and 6=lowest"),

    'intoxication_level' : fields.integer('Intoxication',
        help="the level of intoxication is associated with addiction and "
        "increases the personal and social damage a substance may do. \n"
        "Using Henningfield rating. 1=highest and 6=lowest"),

    'route_oral' : fields.boolean('Oral'),

    'route_popping' : fields.boolean('Skin Popping',
        help="Subcutaneous or Intradermical administration"),

    'route_inhaling' : fields.boolean('Smoke / Inhale',
        help="Insufflation, excluding nasal"),

    'route_sniffing' : fields.boolean('Sniffing',
        help="Also called snorting - inhaling through the nares  "),

    'route_injection' : fields.boolean('Injection',
        help="Injection - Intravenous, Intramuscular..."),

    'dea_schedule_i' : fields.boolean('DEA schedule I',
        help="Schedule I and II drugs have a high potential for abuse. "
        "They require greater storage security and have a quota on "
        "manufacturing, among other restrictions. Schedule I drugs are "
        "available for research only and have no approved medical use; "
        "Schedule II drugs are available only by prescription "
        "(unrefillable) and require a form for ordering. Schedule III "
        "and IV drugs are available by prescription, may have five "
        "refills in 6 months, and may be ordered orally. "
        "Some Schedule V drugs are available over the counter"),

    'dea_schedule_ii' : fields.boolean('II',
        help="Schedule I and II drugs have a high potential for abuse."
        "They require greater storage security and have a quota on"
        "manufacturing, among other restrictions. Schedule I drugs are"
        "available for research only and have no approved medical use; "
        "Schedule II drugs are available only by prescription "
        "(unrefillable) and require a form for ordering. Schedule III "
        "and IV drugs are available by prescription, may have five"
        "refills in 6 months, and may be ordered orally. "
        "Some Schedule V drugs are available over the counter"),

    'dea_schedule_iii' : fields.boolean('III',
        help="Schedule I and II drugs have a high potential for abuse. "
        "They require greater storage security and have a quota on "
        "manufacturing, among other restrictions. Schedule I drugs are "
        "available for research only and have no approved medical use; "
        "Schedule II drugs are available only by prescription "
        "(unrefillable) and require a form for ordering. Schedule III "
        "and IV drugs are available by prescription, may have five "
        "refills in 6 months, and may be ordered orally. "
        "Some Schedule V drugs are available over the counter"),

    'dea_schedule_iv' : fields.boolean('IV',
        help="Schedule I and II drugs have a high potential for abuse. "
        "They require greater storage security and have a quota on "
        "manufacturing, among other restrictions. Schedule I drugs are "
        "available for research only and have no approved medical use; "
        "Schedule II drugs are available only by prescription "
        "(unrefillable) and require a form for ordering. Schedule III "
        "and IV drugs are available by prescription, may have five "
        "refills in 6 months, and may be ordered orally. "
        "Some Schedule V drugs are available over the counter"),

    'dea_schedule_v' : fields.boolean('V',
        help="Schedule I and II drugs have a high potential for abuse. "
        "They require greater storage security and have a quota on "
        "manufacturing, among other restrictions. Schedule I drugs are "
        "available for research only and have no approved medical use; "
        "Schedule II drugs are available only by prescription "
        "(unrefillable) and require a form for ordering. Schedule III "
        "and IV drugs are available by prescription, may have five "
        "refills in 6 months, and may be ordered orally. "
        "Some Schedule V drugs are available over the counter"),

    'info' : fields.text('Extra Info'),


}

DrugsRecreational()

class PatientRecreationalDrugs(orm.Model):
# TODO:  If no more fields are needed, should be moved as one2many inside of oemedical_patient... 
    _name = 'oemedical.patient.recreational_drugs'
    _description = 'Patient use of Recreational Drugs'

    _columns = {
            'patient_id' : fields.many2one('medical.patient', 'Patient'),
            'recreational_drug' : fields.many2one('oemedical.drugs_recreational', 'Recreational Drug'),
                }

''' CAGE questionnaire to assess patient dependency to alcohol '''
PatientRecreationalDrugs()

class PatientCAGE(orm.Model):

    _name = 'oemedical.patient.cage'
    _description =  'Patient CAGE Questionnaire'
    _columns = {

    'name' : fields.many2one('medical.patient', 'Patient', required=True),
    'evaluation_date' : fields.datetime('Date'),
    'cage_c' : fields.boolean('Hard to Cut down', help='Have you ever felt you needed to Cut down on your drinking ?'),
    'cage_a' : fields.boolean('Angry with Critics', help='Have people Annoyed you by criticizing your drinking ?'),
    'cage_g' : fields.boolean('Guilt', help='Have you ever felt Guilty about drinking ?'),
    'cage_e' : fields.boolean('Eye-opener', help='Have you ever felt you needed a drink first thing in the morning (Eye-opener) to steady your nerves or to get rid of a hangover?'),
    'cage_score' : fields.integer('CAGE Score'),

}

PatientCAGE()

class MedicalPatient(orm.Model):

    _inherit='medical.patient'

    _columns = {

    'exercise' : fields.boolean('Exercise'),
    'exercise_minutes_day' : fields.integer('Minutes / day', help="How many minutes a day the patient exercises"),
    'sleep_hours' : fields.integer('Hours of sleep', help="Average hours of sleep per day"),
    'sleep_during_daytime' : fields.boolean('Sleeps at daytime', help="Check if the patient sleep hours are during daylight rather than at night"),
    'number_of_meals' : fields.integer('Meals per day'),
    'eats_alone' : fields.boolean('Eats alone', help="Check this box if the patient eats by him / herself."),
    'salt' : fields.boolean('Salt',  help="Check if patient consumes salt with the food"),
    'coffee' : fields.boolean('Coffee'),
    'coffee_cups' : fields.integer('Cups per day', help="Number of cup of coffee a day"),
    'soft_drinks' : fields.boolean('Soft drinks (sugar)', help="Check if the patient consumes soft drinks with sugar"),
    'diet' : fields.boolean('Currently on a diet', help="Check if the patient is currently on a diet"),
    'diet_info' : fields.char('Diet info', help="Short description on the diet"),
    'smoking' : fields.boolean('Smokes'),
    'smoking_number' : fields.integer('Cigarretes a day'),
    'ex_smoker' : fields.boolean('Ex-smoker'),
    'second_hand_smoker' : fields.boolean('Passive smoker', help="Check it the patient is a passive / second-hand smoker"),
    'age_start_smoking' : fields.integer('Age started to smoke'),
    'age_quit_smoking' : fields.integer('Age of quitting', help="Age of quitting smoking"),
    'alcohol' : fields.boolean('Drinks Alcohol'),
    'age_start_drinking' : fields.integer('Age started to drink ', help="Date to start drinking"),
    'age_quit_drinking' : fields.integer('Age quit drinking ', help="Date to stop drinking"),
    'ex_alcoholic' : fields.boolean('Ex alcoholic'),
    'alcohol_beer_number' : fields.integer('Beer / day'),
    'alcohol_wine_number' : fields.integer('Wine / day'),
    'alcohol_liquor_number' : fields.integer('Liquor / day'),
    'drug_usage' : fields.boolean('Drug Habits'),
    'ex_drug_addict' : fields.boolean('Ex drug addict'),
    'drug_iv' : fields.boolean('IV drug user', help="Check this option if the patient injects drugs"),
    'age_start_drugs' : fields.integer('Age started drugs ', help="Age of start drugs"),
    'age_quit_drugs' : fields.integer('Age quit drugs ', help="Date of quitting drugs"),
    'recreational_drugs' : fields.one2many( 'oemedical.patient.recreational_drugs', 'patient_id', 'Drugs'),
    'traffic_laws' : fields.boolean('Obeys Traffic Laws', help="Check if the patient is a safe driver"),
    'car_revision' : fields.boolean('Car Revision', help="Maintain the vehicle. Do periodical checks - tires,breaks ..."),
    'car_seat_belt' : fields.boolean('Seat belt', help="Safety measures when driving : safety belt"),
    'car_child_safety' : fields.boolean('Car Child Safety', help="Safety measures when driving : child seats, proper seat belting, not seating on the front seat, ...."),
    'home_safety' : fields.boolean('Home safety',  help="Keep safety measures for kids in the kitchen, correct storage of chemicals, ..."),
    'motorcycle_rider' : fields.boolean('Motorcycle Rider', help="The patient rides motorcycles"),
    'helmet' : fields.boolean('Uses helmet',  help="The patient uses the proper motorcycle helmet"),
    'lifestyle_info' : fields.text('Extra Information'),
    'sexual_preferences' : fields.selection([
        ('h', 'Heterosexual'),
        ('g', 'Homosexual'),
        ('b', 'Bisexual'),
        ('t', 'Transexual'),
        ], 'Sexual Preferences', sort=False),

    'sexual_practices' : fields.selection([
        ('s', 'Safe / Protected sex'),
        ('r', 'Risky / Unprotected sex'),
        ], 'Sexual Practices', sort=False),

    'sexual_partners' : fields.selection([
        ('m', 'Monogamous'),
        ('t', 'Polygamous'),
        ], 'Sexual Partners', sort=False),

    'sexual_partners_number' : fields.integer('Number of sexual partners'),

    'first_sexual_encounter' : fields.integer('Age first sexual encounter'),

    'anticonceptive' : fields.selection([
        ('0', 'None'),
        ('1', 'Pill / Minipill'),
        ('2', 'Male condom'),
        ('3', 'Vasectomy'),
        ('4', 'Female sterilisation'),
        ('5', 'Intra-uterine device'),
        ('6', 'Withdrawal method'),
        ('7', 'Fertility cycle awareness'),
        ('8', 'Contraceptive injection'),
        ('9', 'Skin Patch'),
        ('10', 'Female condom'),
        ], 'Anticonceptive Method', sort=False),

    'sex_oral' : fields.selection([
        ('0', 'None'),
        ('1', 'Active'),
        ('2', 'Passive'),
        ('3', 'Both'),
        ], 'Oral Sex', sort=False),

    'sex_anal' : fields.selection([
        ('0', 'None'),
        ('1', 'Active'),
        ('2', 'Passive'),
        ('3', 'Both'),
        ], 'Anal Sex', sort=False),

    'prostitute' : fields.boolean('Prostitute', help="Check if the patient (he or she) is a prostitute"),
    'sex_with_prostitutes' : fields.boolean('Sex with prostitutes', help="Check if the patient (he or she) has sex with prostitutes"),

    'sexuality_info' : fields.text('Extra Information'),

    'cage' : fields.one2many('oemedical.patient.cage', 'name', 'CAGE'),
            }

MedicalPatient()


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
