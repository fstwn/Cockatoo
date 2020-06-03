"""
Cockatoo module for automatic generation of knitting patterns based on
mesh or NURBS surface reference geometry.

Author: Max Eschenbach
License: Apache License 2.0
Version: 200603
"""

# PYTHON STANDARD LIBRARY IMPORTS ----------------------------------------------
from __future__ import absolute_import

# LOCAL MODULE IMPORTS ---------------------------------------------------------
from cockatoo import environment
from cockatoo import exception
from cockatoo._knitconstraint import KnitConstraint
from cockatoo._knitnetworkbase import KnitNetworkBase
from cockatoo._knitnetwork import KnitNetwork
from cockatoo._knitdinetwork import KnitDiNetwork
from cockatoo._knitmappingnetwork import KnitMappingNetwork

# AUTHORSHIP -------------------------------------------------------------------

__author__ = """Max Eschenbach (post@maxeschenbach.com)"""

# ALL LIST ---------------------------------------------------------------------
__all__ = [
    "environment",
    "exception",
    "KnitNetworkBase",
    "KnitNetwork",
    "KnitDiNetwork",
    "KnitMappingNetwork",
]

# MAIN -------------------------------------------------------------------------
if __name__ == '__main__':
    pass