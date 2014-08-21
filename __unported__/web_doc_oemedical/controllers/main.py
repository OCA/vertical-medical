# -*- coding: utf-8 -*-
import ast
import base64
import csv
import glob
import itertools
import logging
import operator
import datetime
import hashlib
import os
import re
import simplejson
import time
import urllib2
import xmlrpclib
import zlib
from xml.etree import ElementTree
from cStringIO import StringIO
import babel.messages.pofile
import werkzeug.utils
import werkzeug.wrappers
import openerp
import web

def read_base_doc(name):
    '''
    Method that will be sure to convert path of index in absolute path.
    TODO: It is not finished yet
    '''
    whereami=os.path.dirname(os.path.realpath(__file__))
    
    return ''


class OeMedicalDoc(web.http.Controller):
    _cp_path='/oemedicaldoc'

    @web.http.httprequest
    def index(self, req, s_action=None, **kw):
        html = read_template("index.html")
        return html
