# @class_declaration interna_lineastransstock #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactalma import models as modelos


class interna_lineastransstock(modelos.mtd_lineastransstock, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactalma_lineastransstock #
class flfactalma_lineastransstock(interna_lineastransstock, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration lineastransstock #
class lineastransstock(flfactalma_lineastransstock, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactalma.lineastransstock_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
