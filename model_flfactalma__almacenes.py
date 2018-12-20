# @class_declaration interna_almacenes #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactalma import models as modelos


class interna_almacenes(modelos.mtd_almacenes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactalma_almacenes #
class flfactalma_almacenes(interna_almacenes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration almacenes #
class almacenes(flfactalma_almacenes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactalma.almacenes_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
