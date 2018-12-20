# @class_declaration interna_articulosagen #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactalma import models as modelos


class interna_articulosagen(modelos.mtd_articulosagen, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactalma_articulosagen #
class flfactalma_articulosagen(interna_articulosagen, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration articulosagen #
class articulosagen(flfactalma_articulosagen, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactalma.articulosagen_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
