"""
Initialize a KnitNetwork from a set of KnitContours (i.e. isocurves / isolines)
and an optional reference geometry.
---
[NOTE] The ReferenceGeometry is a mesh or surface which is described by the network.
While it is optional, it is **HIGHLY** recommended to provide it, as downstream
methods like meshing or creating a dual might fail without it.
    Inputs:
        Toggle: Set to True to initialize the KnitNetwork.
                {item, bool}
        KnitContours: The contours of the knitting pattern.
                      {list, curve/polyline}
        CourseHeight: The course height of the knitting machine.
                      {item, float}
        ReferenceGeometry: The reference geometry this network is based on.
                           {item, mesh/surface)
    Output:
        KnitNetwork: The initialized KnitNetwork.
                     {item, KnitNetwork}
    Remarks:
        Author: Max Eschenbach
        License: MIT License
        Version: 200801
"""

# PYTHON STANDARD LIBRARY IMPORTS
from __future__ import division

# GPYTHON SDK IMPORTS
from ghpythonlib.componentbase import executingcomponent as component
import Grasshopper, GhPython
import System
import Rhino
import rhinoscriptsyntax as rs

# GHENV COMPONENT SETTINGS
ghenv.Component.Name = "InitializeKnitNetwork"
ghenv.Component.NickName ="IKN"
ghenv.Component.Category = "Cockatoo"
ghenv.Component.SubCategory = "06 KnitNetwork"

# LOCAL MODULE IMPORTS
try:
    import cockatoo
except ImportError:
    errMsg = "The Cockatoo python module seems to be not correctly " + \
             "installed! Please make sure the module is in you search " + \
             "path, see README for instructions!."
    raise ImportError(errMsg)

class InitializeKnitNetwork(component):
    
    def RunScript(self, Toggle, KnitContours, CourseHeight, ReferenceGeometry):
        
        if Toggle and KnitContours and CourseHeight:
            
            # sanitize reference geometry
            if not (isinstance(ReferenceGeometry, Rhino.Geometry.Surface)
            or isinstance(ReferenceGeometry, Rhino.Geometry.NurbsSurface)
            or isinstance(ReferenceGeometry, Rhino.Geometry.Mesh) 
            or isinstance(ReferenceGeometry, Rhino.Geometry.Brep)):
                errMsg = "Input ReferenceGeometry is not a valid Mesh, " + \
                         "Surface or Brep! 'reference_geometry' attribute " + \
                         "will not be set!"
                rml = self.RuntimeMessageLevel.Warning
                self.AddRuntimeMessage(rml, errMsg)
                ReferenceGeometry = None
            
            # create KnitNetwork (inherits from nx.Graph)
            KN = cockatoo.KnitNetwork.create_from_contours(KnitContours,
                                                           CourseHeight,
                                                           ReferenceGeometry)
        elif Toggle and not KnitContours:
            rml = self.RuntimeMessageLevel.Warning
            rMsg = "No KnitContours input!"
            self.AddRuntimeMessage(rml, rMsg)
            return Grasshopper.DataTree[object]()
        elif Toggle and not CourseHeight:
            rml = self.RuntimeMessageLevel.Warning
            rMsg = "No CourseHeight input!"
            self.AddRuntimeMessage(rml, rMsg)
            return Grasshopper.DataTree[object]()
        else:
            return Grasshopper.DataTree[object]()
        
        # return outputs if you have them; here I try it for you:
        return KN
