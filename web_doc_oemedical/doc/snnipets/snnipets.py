# -*- encoding: utf-8 -*-
class OeMedicalAppointment(orm.Model):

    """
    DocString for a new object.
    Is important say here where will be the menu to test this object.
    Mention the reason whay it was created, if it is necesary link
    some `external <http://externaldoc.com>`_
    especitication about why it was created.

    Probably, there an object on OpenERP base that already comply with your
    needs and in this case it will be easyiest to propose a redisign of the
    feature, or propose a better solution, in other hand it can be used as
    reference for other features if it is documented enought.
    """
    _name = 'oemedical.appointment'
    _description = 'Appointments in OeMedical'
    _columns = {
        'consultations': fields.many2one('product.product',
                                         string='Consultation Services', ),
        'patient': fields.many2one('oemedical.patient', string='Patient',
                                   required=True, index=True),
        'name': fields.char(size=256, string='Appointment ID', readonly=True),
        'appointment_date': fields.datetime(string='Date and Time'),
        'doctor': fields.many2one('oemedical.physician',
                                  string='Physician', index=True),
        'comments': fields.text(string='Comments'),
        'appointment_type': fields.selection([
            ('ambulatory', 'Ambulatory'),
            ('outpatient', 'Outpatient'),
            ('inpatient', 'Inpatient'),
        ], string='Type'),
        'institution': fields.many2one('res.partner',
                                       string='Health Center', ),
        'urgency': fields.selection([
            ('a', 'Normal'),
            ('b', 'Urgent'),
            ('c', 'Medical Emergency'), ],
            string='Urgency Level'),
        'speciality': fields.many2one('oemedical.specialty',
                                      string='Specialty', ),
    }

    _defaults = {
        'name': lambda obj, cr, uid, context:
        obj.pool.get('ir.sequence').get(cr, uid, 'oemedical.appointment'),
    }


def test_method(self, cr, uid, ids, context=None):
    """Something in doc

    :param context['mail']: 'new' to send a new mail or 'reply'
    :type context['mail']: str

    If this values are Ok.

    .. note::
        You must be careful with XX YY

    .. code-block:: python

        obj = self.pool.get('your.object')
        somethingelse

    :returns: list -- list with ids of elements
    """
    return True


def search(self, cr, uid, domain, context=None):
    """
    If you overwrite and orm method is important to say why you did it
    because for the rest of community will be easier understand and create test
    related to your change and consider in the integration with OpenERP API.
    :context['mail']: 'new' to send a new mail or 'reply'
    If some option is true
    :return: True or other thing
    """
    return True


def undocummented_test_method(self, cr, uid, ids, context=None):
    return False