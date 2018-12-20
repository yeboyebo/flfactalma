# @class_declaration interna_articuloscli #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactalma import models as modelos


class interna_articuloscli(modelos.mtd_articuloscli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactalma_articuloscli #
class flfactalma_articuloscli(interna_articuloscli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration articuloscli #
class articuloscli(flfactalma_articuloscli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactalma.articuloscli_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
