"""
Remeshes the input mesh using the new QuadRemesh functionality.
    Inputs:
        Geometry: The original input mesh or brep to quad-remesh. {item, mesh/brep}
        TargetQuadCount: The number of quads to try to achieve in the final remeshed object. {item, integer}
        AdaptiveQuadCount: Respect the original Target Quad Count value as much as possible. True returns more quads than TargetQuadCount depending on amount of high-curvature areas {item, boolean}
        AdaptiveSize: Larger values results in for quad sizes that adjust to match input curvature. Smaller values results in more uniform quad sizes at the risk of less feature preservation. Range [0 - 100] {item, float}
        DetectHardEdges: When enabled the hard edges in models will be retained. {item, boolean}
        GuideCurves: GuideCurves for the remeshing process {list, curve}
        GuideCurveInfluence: 0 = Approximate 1 = Interpolate Edge Ring 2 = Interpolate Edge Loop This value is ignored if Guide Curves are not supplied {item, number}
        SymmetryAxis: Symmetry axis to use for symmetric remeshing. [0 = No Symmetry, 1 = X, 2 = Y, 4 = Z] {item, integer}
        PreserveMeshArrayEdgesMode: 0=off, 1=On(Smart), 2=On(Strict) : Mesh array's created from Breps will have their brep face edge boundaries retained. Smart - Small or insignificant input faces are ignored. Strict - All input faces are factored in remeshed result. {item, integer}
    Output:
        QuadMesh: The remeshed result {item/list, Mesh}
    Remarks:
        Author: Max Eschenbach
        License: Apache License 2.0
        Version: 200324
"""

from __future__ import division
from ghpythonlib.componentbase import executingcomponent as component
import Grasshopper, GhPython
import System
import Rhino
import rhinoscriptsyntax as rs

ghenv.Component.Name = "QuadReMesh"
ghenv.Component.NickName = "QRM"
ghenv.Component.Category = "COCKATOO"
ghenv.Component.SubCategory = "3 Remeshing"

class QuadReMesh(component):
    
    def checkInputData(self, geo, tqc, aqc, aqs, dhe, gci, sa, pmaem):
        # check Geometry input
        if not geo or geo == None or geo == []:
            return None
        
        # check TargetQuadCount input
        if ((not tqc) or 
            (tqc == None) or 
            (tqc == [])):
            return None
        
        # check AdaptiveQuadCount input
        if aqc == None or aqc == []:
            aqc = False
        
        # check AdaptiveSize input
        if not aqs or aqs == None or aqs == []:
            aqs = 0
        elif aqs > 100:
            aqs = 100
        
        # check DetectHardEdges input
        if dhe == None or dhe == []:
            dhe = False
        
        # check GuideCurveInfluence input
        if ((not gci) or
            (gci == None) or 
            (gci == [])):
            gci = 0
        elif gci > 2:
            gci = 2
       
       # check SymmetryAxis input
        if ((not sa) or 
            (sa == None) or 
            (sa == []) or 
            (sa == 0) or 
            (sa > 4)):
                sa = Rhino.Geometry.QuadRemeshSymmetryAxis.None
        elif sa == 1:
            sa = Rhino.Geometry.QuadRemeshSymmetryAxis.X
        elif sa == 2 or sa == 3:
            sa = Rhino.Geometry.QuadRemeshSymmetryAxis.Y
        elif sa == 4:
            sa = Rhino.Geometry.QuadRemeshSymmetryAxis.Z
        
        # check PreserveMeshArrayEdgesMode input
        if ((not pmaem) or 
            (pmaem == None) or
            (pmaem == []) or
            (pmaem < 0)):
                pmaem = 0
        elif pmaem > 2:
            pmaem = 2
        
        return (geo, tqc, aqc, aqs, dhe, gci, sa, pmaem)
    
    def createRemeshParameters(self, tqc, aqc, aqs, dhe, gci, sa, pmaem):
        # create quad remesh parameters instance
        qrp = Rhino.Geometry.QuadRemeshParameters()
        
        # fill instance with the parameters
        qrp.TargetQuadCount = tqc
        qrp.AdaptiveQuadCount = aqc
        qrp.AdaptiveSize = aqs
        qrp.DetectHardEdges = dhe
        qrp.GuideCurveInfluence = gci
        qrp.SymmetryAxis = sa
        qrp.PreserveMeshArrayEdgesMode = pmaem
        
        # return the quad remesh parameters
        return qrp
    
    def RunScript(self, Geometry, TargetQuadCount, AdaptiveQuadCount, AdaptiveSize, DetectHardEdges, GuideCurves, GuideCurveInfluence, SymmetryAxis, PreserveMeshArrayEdgesMode):
        
        # define outputs so that they are never empty
        QuadMesh = []
        
        # CHECK INPUTS ---------------------------------------------------------
        
        result = self.checkInputData(Geometry,
                                     TargetQuadCount,
                                     AdaptiveQuadCount,
                                     AdaptiveSize,
                                     DetectHardEdges,
                                     GuideCurveInfluence,
                                     SymmetryAxis,
                                     PreserveMeshArrayEdgesMode)
        if not result:
            # return if the check fails
            return None
        else:
            # unpack the result of the check
            Geometry,\
            TargetQuadCount,\
            AdaptiveQuadCount,\
            AdaptiveSize, DetectHardEdges,\
            GuideCurveInfluence,\
            SymmetryAxis,\
            PreserveMeshArrayEdgesMode = result
        
        # CREATE PARAMETERS ----------------------------------------------------
        
        # create QuadRemeshing Parameters based on input values
        ReParams = self.createRemeshParameters(TargetQuadCount,
                                               AdaptiveQuadCount,
                                               AdaptiveSize,
                                               DetectHardEdges,
                                               GuideCurveInfluence,
                                               SymmetryAxis,
                                               PreserveMeshArrayEdgesMode)
        
        # TRIGGER REMESHING ----------------------------------------------------
        
        # if guidecurves are supplied, supply them to the remesh routine
        if GuideCurves and GuideCurves != None and GuideCurves != []:
            # if a mesh is supplied as geometry, remesh this mesh
            if type(Geometry) == Rhino.Geometry.Mesh:
                QuadMesh = Geometry.QuadRemesh(ReParams,
                                               GuideCurves)
            
            # if a brep is supplied, create a new quadmesh from this brep
            elif type(Geometry) == Rhino.Geometry.Brep:
                QuadMesh = Rhino.Geometry.Mesh.QuadRemeshBrep(Geometry,
                                                              ReParams,
                                                              GuideCurves)
        
        # if no guidecurves are supplied, don't add them to the routine
        else:
            # if a mesh is supplied as geometry, remesh this mesh
            if type(Geometry) == Rhino.Geometry.Mesh:
                QuadMesh = Geometry.QuadRemesh(ReParams)
                
            # if a brep is supplied, create a new quadmesh from this brep
            elif type(Geometry) == Rhino.Geometry.Brep:
                QuadMesh = Rhino.Geometry.Mesh.QuadRemeshBrep(Geometry,
                                                              ReParams)
        # return remeshed result
        return QuadMesh
