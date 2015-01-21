# -*- coding: utf-8 -*-
import os
import web


def read_base_doc(name):
    '''
    Method that will be sure to convert path of index in absolute path.
    TODO: It is not finished yet
    '''
    os.path.dirname(os.path.realpath(__file__))

    return ''


class OeMedicalDoc(web.http.Controller):
    _cp_path = '/oemedicaldoc'

    @web.http.httprequest
    def index(self, req, s_action=None, **kw):
#        html = read_template("index.html") XXX failed on pep8 check
        html = read_base_doc("index.html")
        return html
