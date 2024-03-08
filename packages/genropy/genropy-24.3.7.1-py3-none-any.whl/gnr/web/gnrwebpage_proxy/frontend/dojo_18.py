#!/usr/bin/env pythonw
# -*- coding: utf-8 -*-
#
#  dojo_16.py
#
#  Created by Giovanni Porcari on 2007-03-24.
#  Copyright (c) 2007 Softwell. All rights reserved.

# --------------------------- GnrWebPage subclass ---------------------------
from gnr.web.gnrwebpage_proxy.frontend.dojo_base import GnrBaseDojoFrontend
from gnr.web.gnrwebstruct import  GnrDomSrc_dojo_18

class GnrWebFrontend(GnrBaseDojoFrontend):
    version = 'd18'
    domSrcFactory = GnrDomSrc_dojo_18

    def css_frontend(self, theme=None):
        theme = theme or self.theme
        return ['dojo/resources/dojo.css',
                'dijit/themes/dijit.css',
                'dijit/themes/%s/%s.css' % (theme, theme),
                'dojox/grid/_grid/Grid.css',
                'dojox/grid/_grid/%sGrid.css' % theme
        ]

    def gnrjs_frontend(self):
        return ['gnrbag','gnrdomsource','gnrlang', 'gnrstores', 
                'genro','genro_patch','genro_rpc','genro_wdg', 'genro_src',
                'genro_widgets','genro_components','genro_frm',
                'genro_dev', 'genro_dlg', 'genro_dom','genro_extra']

    def css_genro_frontend(self):
        return {'all': ['gnrbase'], 'print': ['gnrprint']}


