# PyTABS - ETABS .NET API python wrapper
# PropTendon - cPropTendon interface
__all__ = ['PropTendon']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import etabs
from pytabs.error_handle import handle

# import custom enumerations


# import typing


class PropTendon:
    """PropTendon interface"""

    def __init__(self, sap_model: etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create PropTendon interface
        self.prop_tendon = etabs.cPropTendon(sap_model.PropTendon)

        # relate custom enumerations
