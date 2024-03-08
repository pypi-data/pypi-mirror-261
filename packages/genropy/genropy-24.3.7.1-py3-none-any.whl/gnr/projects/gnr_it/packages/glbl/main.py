#!/usr/bin/env python
# encoding: utf-8
from gnr.app.gnrdbo import GnrDboTable, GnrDboPackage

class Package(GnrDboPackage):
    def config_attributes(self):
        return dict(sqlschema='glbl',
                    comment='glbl package',
                    name_short='glbl',
                    name_long='Geo Italia',
                    name_full='Geo Italia')
                    
    def config_db(self, pkg):
        pass

  
class Table(GnrDboTable):
    def fillTable(self,records):
        for record in records:
            self.insert(record)

            