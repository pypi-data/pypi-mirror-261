# PyTABS - ETABS .NET API python wrapper
# CaseHyperStatic - cCaseHyperStatic interface
__all__ = ['CaseHyperStatic']

# import ETABS namespace and pyTABS error handler
from pytabs.etabs_config import etabs
from pytabs.error_handle import handle

# import custom enumerations


class CaseHyperStatic:
    """CaseHyperStatic interface"""

    def __init__(self, sap_model: etabs.cSapModel) -> None:
        # link of SapModel interface
        self.sap_model = sap_model
        # create interface for hyperstatic cases
        self.hyerstatic = etabs.cCaseHyperStatic(sap_model.LoadCases.HyperStatic)

        # relate custom enumerations
