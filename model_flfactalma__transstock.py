# @class_declaration interna_transstock #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactalma import models as modelos


class interna_transstock(modelos.mtd_transstock, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactalma_transstock #
class flfactalma_transstock(interna_transstock, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def initValidation(name, data=None):
        return form.iface.initValidation(name, data)

    def iniciaValoresLabel(self, template=None, cursor=None, data=None):
        return form.iface.iniciaValoresLabel(self, template, cursor)

    def bChLabel(fN=None, cursor=None):
        return form.iface.bChLabel(fN, cursor)

    def getFilters(self, name, template=None):
        return form.iface.getFilters(self, name, template)

    def getForeignFields(self, template=None):
        return form.iface.getForeignFields(self, template)

    def getDesc():
        return form.iface.getDesc()


# @class_declaration transstock #
class transstock(flfactalma_transstock, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


definitions = importlib.import_module("models.flfactalma.transstock_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
