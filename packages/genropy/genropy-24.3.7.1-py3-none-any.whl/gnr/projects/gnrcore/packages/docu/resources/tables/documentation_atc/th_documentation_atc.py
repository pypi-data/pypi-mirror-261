#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('_row_count')
        r.fieldcell('filepath')
        r.fieldcell('external_url')
        r.fieldcell('description')
        r.fieldcell('mimetype')
        r.fieldcell('text_content')
        r.fieldcell('info')
        r.fieldcell('is_foreign_document')
        r.fieldcell('maintable_id')
        r.fieldcell('atc_download')

    def th_order(self):
        return '_row_count'

    def th_query(self):
        return dict(column='_row_count', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('_row_count')
        fb.field('filepath')
        fb.field('external_url')
        fb.field('description')
        fb.field('mimetype')
        fb.field('text_content')
        fb.field('info')
        fb.field('is_foreign_document')
        fb.field('maintable_id')
        fb.field('atc_download')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
