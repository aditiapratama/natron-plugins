# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named Ls_Contacts_GLExt.py
# See http://natron.readthedocs.org/en/master/devel/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from Ls_Contacts_GLExt import *
except ImportError:
    pass

def getPluginID():
    return "natron.community.plugins.Ls_Contacts_GL"

def getLabel():
    return "Ls_Contacts_GL"

def getVersion():
    return 1.0

def getIconPath():
    return "Ls_Contacts_GL.png"

def getGrouping():
    return "Community/GLSL/Merge"

def getPluginDescription():
    return "Tile inputs into a grid for impressing clients, choosing versions or checking continuity."

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group
    lastNode.setColor(0.2941, 0.3686, 0.7765)

    # Create the user parameters
    lastNode.Controls = lastNode.createPageParam("Controls", "Controls")
    param = lastNode.createStringParam("sep01", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep01 = param
    del param

    param = lastNode.createStringParam("sep02", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep02 = param
    del param

    param = lastNode.createIntParam("Shadertoy2paramValueInt2", "Use inputs up to : ")
    param.setMinimum(1, 0)
    param.setMaximum(4, 0)
    param.setDisplayMinimum(1, 0)
    param.setDisplayMaximum(4, 0)
    param.setDefaultValue(4, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy2paramValueInt2 = param
    del param

    param = lastNode.createStringParam("sep03", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep03 = param
    del param

    param = lastNode.createSeparatorParam("ROWS_COLUMNS", "Rows / Columns")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.ROWS_COLUMNS = param
    del param

    param = lastNode.createStringParam("sep04", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep04 = param
    del param

    param = lastNode.createStringParam("sep05", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep05 = param
    del param

    param = lastNode.createIntParam("Shadertoy2paramValueInt0", "Rows : ")
    param.setMinimum(1, 0)
    param.setMaximum(4096, 0)
    param.setDisplayMinimum(1, 0)
    param.setDisplayMaximum(4096, 0)
    param.setDefaultValue(2, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy2paramValueInt0 = param
    del param

    param = lastNode.createStringParam("sep06", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep06 = param
    del param

    param = lastNode.createIntParam("Shadertoy2paramValueInt1", "Columns : ")
    param.setMinimum(1, 0)
    param.setMaximum(4096, 0)
    param.setDisplayMinimum(1, 0)
    param.setDisplayMaximum(4096, 0)
    param.setDefaultValue(2, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy2paramValueInt1 = param
    del param

    param = lastNode.createStringParam("sep07", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep07 = param
    del param

    param = lastNode.createStringParam("sep08", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep08 = param
    del param

    param = lastNode.createSeparatorParam("TRANSFORM", "Transform : ")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.TRANSFORM = param
    del param

    param = lastNode.createStringParam("sep09", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep09 = param
    del param

    param = lastNode.createStringParam("sep10", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep10 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy2paramValueFloat7", "Scale : ")
    param.setMinimum(0.01, 0)
    param.setMaximum(3000, 0)
    param.setDisplayMinimum(0.01, 0)
    param.setDisplayMaximum(3000, 0)
    param.setDefaultValue(99.99999999999999, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy2paramValueFloat7 = param
    del param

    param = lastNode.createStringParam("sep11", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep11 = param
    del param

    param = lastNode.createIntParam("Shadertoy2paramValueInt3", "Seed : ")
    param.setMinimum(1, 0)
    param.setMaximum(4096, 0)
    param.setDisplayMinimum(1, 0)
    param.setDisplayMaximum(4096, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy2paramValueInt3 = param
    del param

    param = lastNode.createStringParam("sep12", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep12 = param
    del param

    param = lastNode.createStringParam("sep13", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep13 = param
    del param

    param = lastNode.createSeparatorParam("OPTIONS", "Options")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.OPTIONS = param
    del param

    param = lastNode.createStringParam("sep14", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep14 = param
    del param

    param = lastNode.createStringParam("sep15", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep15 = param
    del param

    param = lastNode.createBooleanParam("Shadertoy2paramValueBool4", "Random : ")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy2paramValueBool4 = param
    del param

    param = lastNode.createStringParam("sep16", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep16 = param
    del param

    param = lastNode.createBooleanParam("Shadertoy2paramValueBool5", "New pattern per frame : ")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy2paramValueBool5 = param
    del param

    param = lastNode.createStringParam("sep17", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep17 = param
    del param

    param = lastNode.createBooleanParam("Shadertoy2paramValueBool6", "Crop edges : ")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy2paramValueBool6 = param
    del param

    param = lastNode.createStringParam("sep18", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep18 = param
    del param

    param = lastNode.createStringParam("sep19", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep19 = param
    del param

    lastNode.Credits = lastNode.createPageParam("Credits", "Credits")
    param = lastNode.createStringParam("sep101", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep101 = param
    del param

    param = lastNode.createStringParam("sep102", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep102 = param
    del param

    param = lastNode.createSeparatorParam("NAME", "Ls_Contacts_GL v1.0")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.NAME = param
    del param

    param = lastNode.createStringParam("sep103", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep103 = param
    del param

    param = lastNode.createStringParam("sep104", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep104 = param
    del param

    param = lastNode.createSeparatorParam("LINE01", "")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.LINE01 = param
    del param

    param = lastNode.createStringParam("sep105", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep105 = param
    del param

    param = lastNode.createStringParam("sep106", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep106 = param
    del param

    param = lastNode.createSeparatorParam("FR", "ShaderToy 0.8.8")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.FR = param
    del param

    param = lastNode.createStringParam("sep107", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep107 = param
    del param

    param = lastNode.createStringParam("sep108", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep108 = param
    del param

    param = lastNode.createSeparatorParam("CONVERSION", " (Fabrice Fernandez - 2018)")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.CONVERSION = param
    del param

    param = lastNode.createStringParam("sep109", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep109 = param
    del param

    param = lastNode.createStringParam("sep110", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep110 = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['Controls', 'Credits', 'Node', 'Settings'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "Output2"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output2")
    lastNode.setPosition(4139, 4048)
    lastNode.setSize(80, 43)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput2 = lastNode

    del lastNode
    # End of node "Output2"

    # Start of node "Source1"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Source1")
    lastNode.setLabel("Source1")
    lastNode.setPosition(3939, 3668)
    lastNode.setSize(80, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupSource1 = lastNode

    del lastNode
    # End of node "Source1"

    # Start of node "Shadertoy2"
    lastNode = app.createNode("net.sf.openfx.Shadertoy", 1, group)
    lastNode.setScriptName("Shadertoy2")
    lastNode.setLabel("Shadertoy2")
    lastNode.setPosition(4139, 3838)
    lastNode.setSize(80, 48)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupShadertoy2 = lastNode

    param = lastNode.getParam("paramValueInt0")
    if param is not None:
        param.setValue(2, 0)
        del param

    param = lastNode.getParam("paramValueInt1")
    if param is not None:
        param.setValue(2, 0)
        del param

    param = lastNode.getParam("paramValueInt2")
    if param is not None:
        param.setValue(4, 0)
        del param

    param = lastNode.getParam("paramValueInt3")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramValueBool4")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("paramValueBool5")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("paramValueBool6")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("paramValueFloat7")
    if param is not None:
        param.setValue(99.99999999999999, 0)
        del param

    param = lastNode.getParam("imageShaderSource")
    if param is not None:
        param.setValue("//\n//\n//                          MMMMMMMMMMMMMMMMMMMMMMMMMMMM\n//                        MM.                          .MM\n//                       MM.  .MMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                      MM.  .MMMMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                     MM.  .MMMM        MMMMMMM    MMM.  .MM\n//                    MM.  .MMM           MMMMMM     MMM.  .MM\n//                   MM.  .MmM              MMMM      MMM.  .MM\n//                  MM.  .MMM                 MM       MMM.  .MM\n//                 MM.  .MMM                   M        MMM.  .MM\n//                MM.  .MMM                              MMM.  .MM\n//                 MM.  .MMM                            MMM.  .MM\n//                  MM.  .MMM       M                  MMM.  .MM\n//                   MM.  .MMM      MM                MMM.  .MM\n//                    MM.  .MMM     MMM              MMM.  .MM\n//                     MM.  .MMM    MMMM            MMM.  .MM\n//                      MM.  .MMMMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                       MM.  .MMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                        MM.                          .MM\n//                          MMMMMMMMMMMMMMMMMMMMMMMMMMMM\n//\n//\n//\n//\n// Adaptation pour Natron par F. Fernandez\n// Code original : LS_Contacts pour Autodesk Flame\n//\n// Adapted to Natron by F.Fernandez\n// Original code : LS_Contacts Matchbox for Autodesk Flame\n//\n// Tiles the inputs into a grid for impressing clients\n// lewis@lewissaunders.com\n// TODO:\n//  o Nonsquare pixels support... eek\n//  o Variable width borders look gross, how can we get a nice even spacing?\n\n// iChannel0: Source1, filter = linear\n// iChannel1: Source2, filter = linear\n// iChannel2: Source3, filter = linear\n// iChannel3: Source4, filter = linear\n// BBox: iChannel0\n\n\n\nuniform int rows = 2; // Rows : (rows), min=1, max=4096\nuniform int cols = 2; // Columns : (columns), min=1, max=4096\nuniform int randomcount = 4; // Use inputs up to : (max used inputs), min=1, max=4\nuniform int seed = 1; // Seed : (seed), min=1, max=4096\n\n\nuniform bool random = false; // Random : \nuniform bool perframe = false; // New pattern per frame : \nuniform bool filltiles = false; // Crop edges : \n\nuniform float scale = 100; // Scale : (scale), min=0.01, max=3000\n\n\n\n\n// Mysterious dirty random number generator\nfloat rand(vec2 co){\n\treturn fract(sin(dot(co.xy ,vec2(12.9898,78.233))) * 43758.5453);\n}\n\nvoid mainImage( out vec4 fragColor, in vec2 fragCoord )\n{\n\tvec2 coords = fragCoord.xy / vec2(iResolution.x, iResolution.y);\n\tvec2 tilecoords = vec2(0.0, 0.0);\n\tvec4 o = vec4(0.0);\n\tfloat aspectdiff, tilew, tileh;\n\tint tilex, tiley, tileidx;\n\n\t// Figure out how big each tile will be, and which tile we\'re in\n\ttilew = iResolution.x / float(cols);\n\ttileh = iResolution.y / float(rows);\n\ttilex = int(fragCoord.x / tilew);\n\ttiley = int((iResolution.y - fragCoord.y) / tileh);\n\ttileidx = tiley * cols + tilex;\n\t\n\t// Randomize the tile index\n\tif(random) {\n\t\tif(perframe) {\n\t\t\ttileidx = int(rand(vec2(float(tilex - seed), float(tiley) + 1234.0 * iTime)) * float(randomcount));\n\t\t} else {\n\t\t\ttileidx = int(rand(vec2(float(tilex - seed), float(tiley))) * float(randomcount));\n\t\t}\n\t}\n\n\t// Get current coordinates within this tile\n\ttilecoords.x = mod(fragCoord.x, tilew) / tilew;\n\ttilecoords.y = mod(fragCoord.y, tileh) / tileh;\n\t\n\t// Scale coordinates about the centre of each tile to maintain proportions and do fit/fill\n\ttilecoords -= vec2(0.5);\n\ttilecoords *= 100.0 / scale;\n\taspectdiff = (tilew / tileh) / (iResolution.x / iResolution.y);\n\tif(aspectdiff > 1.0) {\n\t\ttilecoords.x *= aspectdiff;\n\t\tif(filltiles) {\n\t\t\ttilecoords /= aspectdiff;\n\t\t}\n\t} else {\n\t\ttilecoords.y /= aspectdiff;\n\t\tif(filltiles) {\n\t\t\ttilecoords *= aspectdiff;\n\t\t}\n\t}\n\ttilecoords += vec2(0.5);\n\t\n\t// Finally grab input for the tile we\'re in\n\tif(tileidx == 0) {\n\t\to = texture2D(iChannel0, tilecoords);\n\t} else if(tileidx == 1) {\n\t\to = texture2D(iChannel1, tilecoords);\n\t} else if(tileidx == 2) {\n\t\to = texture2D(iChannel2, tilecoords);\n\t} else if(tileidx == 3) {\n\t\to = texture2D(iChannel3, tilecoords);\n\t}\n\t\n\t// Draw black if we\'re in a border area\n\tif((tilecoords.x <= 0.0) || (tilecoords.x > 1.0)) {\n\t\t\to = vec4(0.0);\n\t}\n\tif((tilecoords.y <= 0.0) || (tilecoords.y > 1.0)) {\n\t\t\to = vec4(0.0);\n\t}\n\t\n\tfragColor = o;\n}\n")
        del param

    param = lastNode.getParam("mipmap0")
    if param is not None:
        param.set("linear")
        del param

    param = lastNode.getParam("inputLabel0")
    if param is not None:
        param.setValue("Source1")
        del param

    param = lastNode.getParam("mipmap1")
    if param is not None:
        param.set("linear")
        del param

    param = lastNode.getParam("inputLabel1")
    if param is not None:
        param.setValue("Source2")
        del param

    param = lastNode.getParam("mipmap2")
    if param is not None:
        param.set("linear")
        del param

    param = lastNode.getParam("inputLabel2")
    if param is not None:
        param.setValue("Source3")
        del param

    param = lastNode.getParam("mipmap3")
    if param is not None:
        param.set("linear")
        del param

    param = lastNode.getParam("inputLabel3")
    if param is not None:
        param.setValue("Source4")
        del param

    param = lastNode.getParam("bbox")
    if param is not None:
        param.set("iChannel0")
        del param

    param = lastNode.getParam("NatronParamFormatChoice")
    if param is not None:
        param.set("PC_Video")
        del param

    param = lastNode.getParam("mouseParams")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("paramCount")
    if param is not None:
        param.setValue(8, 0)
        del param

    param = lastNode.getParam("paramType0")
    if param is not None:
        param.set("int")
        del param

    param = lastNode.getParam("paramName0")
    if param is not None:
        param.setValue("rows")
        del param

    param = lastNode.getParam("paramLabel0")
    if param is not None:
        param.setValue("Rows :")
        del param

    param = lastNode.getParam("paramHint0")
    if param is not None:
        param.setValue("rows")
        del param

    param = lastNode.getParam("paramDefaultInt0")
    if param is not None:
        param.setValue(2, 0)
        del param

    param = lastNode.getParam("paramMinInt0")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramMaxInt0")
    if param is not None:
        param.setValue(4096, 0)
        del param

    param = lastNode.getParam("paramType1")
    if param is not None:
        param.set("int")
        del param

    param = lastNode.getParam("paramName1")
    if param is not None:
        param.setValue("cols")
        del param

    param = lastNode.getParam("paramLabel1")
    if param is not None:
        param.setValue("Columns :")
        del param

    param = lastNode.getParam("paramHint1")
    if param is not None:
        param.setValue("columns")
        del param

    param = lastNode.getParam("paramDefaultInt1")
    if param is not None:
        param.setValue(2, 0)
        del param

    param = lastNode.getParam("paramMinInt1")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramMaxInt1")
    if param is not None:
        param.setValue(4096, 0)
        del param

    param = lastNode.getParam("paramType2")
    if param is not None:
        param.set("int")
        del param

    param = lastNode.getParam("paramName2")
    if param is not None:
        param.setValue("randomcount")
        del param

    param = lastNode.getParam("paramLabel2")
    if param is not None:
        param.setValue("Use inputs up to :")
        del param

    param = lastNode.getParam("paramHint2")
    if param is not None:
        param.setValue("max used inputs")
        del param

    param = lastNode.getParam("paramDefaultInt2")
    if param is not None:
        param.setValue(4, 0)
        del param

    param = lastNode.getParam("paramMinInt2")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramMaxInt2")
    if param is not None:
        param.setValue(4, 0)
        del param

    param = lastNode.getParam("paramType3")
    if param is not None:
        param.set("int")
        del param

    param = lastNode.getParam("paramName3")
    if param is not None:
        param.setValue("seed")
        del param

    param = lastNode.getParam("paramLabel3")
    if param is not None:
        param.setValue("Seed :")
        del param

    param = lastNode.getParam("paramHint3")
    if param is not None:
        param.setValue("seed")
        del param

    param = lastNode.getParam("paramDefaultInt3")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramMinInt3")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramMaxInt3")
    if param is not None:
        param.setValue(4096, 0)
        del param

    param = lastNode.getParam("paramType4")
    if param is not None:
        param.set("bool")
        del param

    param = lastNode.getParam("paramName4")
    if param is not None:
        param.setValue("random")
        del param

    param = lastNode.getParam("paramLabel4")
    if param is not None:
        param.setValue("Random :")
        del param

    param = lastNode.getParam("paramType5")
    if param is not None:
        param.set("bool")
        del param

    param = lastNode.getParam("paramName5")
    if param is not None:
        param.setValue("perframe")
        del param

    param = lastNode.getParam("paramLabel5")
    if param is not None:
        param.setValue("New pattern per frame :")
        del param

    param = lastNode.getParam("paramType6")
    if param is not None:
        param.set("bool")
        del param

    param = lastNode.getParam("paramName6")
    if param is not None:
        param.setValue("filltiles")
        del param

    param = lastNode.getParam("paramLabel6")
    if param is not None:
        param.setValue("Crop edges :")
        del param

    param = lastNode.getParam("paramType7")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName7")
    if param is not None:
        param.setValue("scale")
        del param

    param = lastNode.getParam("paramLabel7")
    if param is not None:
        param.setValue("Scale :")
        del param

    param = lastNode.getParam("paramHint7")
    if param is not None:
        param.setValue("scale")
        del param

    param = lastNode.getParam("paramDefaultFloat7")
    if param is not None:
        param.setValue(99.99999999999999, 0)
        del param

    param = lastNode.getParam("paramMinFloat7")
    if param is not None:
        param.setValue(0.01, 0)
        del param

    param = lastNode.getParam("paramMaxFloat7")
    if param is not None:
        param.setValue(3000, 0)
        del param

    del lastNode
    # End of node "Shadertoy2"

    # Start of node "Source2"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Source2")
    lastNode.setLabel("Source2")
    lastNode.setPosition(4078, 3667)
    lastNode.setSize(80, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupSource2 = lastNode

    del lastNode
    # End of node "Source2"

    # Start of node "Source3"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Source3")
    lastNode.setLabel("Source3")
    lastNode.setPosition(4205, 3674)
    lastNode.setSize(80, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupSource3 = lastNode

    del lastNode
    # End of node "Source3"

    # Start of node "Source4"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Source4")
    lastNode.setLabel("Source4")
    lastNode.setPosition(4333, 3669)
    lastNode.setSize(80, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupSource4 = lastNode

    del lastNode
    # End of node "Source4"

    # Now that all nodes are created we can connect them together, restore expressions
    groupOutput2.connectInput(0, groupShadertoy2)
    groupShadertoy2.connectInput(0, groupSource1)
    groupShadertoy2.connectInput(1, groupSource2)
    groupShadertoy2.connectInput(2, groupSource3)
    groupShadertoy2.connectInput(3, groupSource4)

    param = groupShadertoy2.getParam("paramValueInt0")
    group.getParam("Shadertoy2paramValueInt0").setAsAlias(param)
    del param
    param = groupShadertoy2.getParam("paramValueInt1")
    group.getParam("Shadertoy2paramValueInt1").setAsAlias(param)
    del param
    param = groupShadertoy2.getParam("paramValueInt2")
    group.getParam("Shadertoy2paramValueInt2").setAsAlias(param)
    del param
    param = groupShadertoy2.getParam("paramValueInt3")
    group.getParam("Shadertoy2paramValueInt3").setAsAlias(param)
    del param
    param = groupShadertoy2.getParam("paramValueBool4")
    group.getParam("Shadertoy2paramValueBool4").setAsAlias(param)
    del param
    param = groupShadertoy2.getParam("paramValueBool5")
    group.getParam("Shadertoy2paramValueBool5").setAsAlias(param)
    del param
    param = groupShadertoy2.getParam("paramValueBool6")
    group.getParam("Shadertoy2paramValueBool6").setAsAlias(param)
    del param
    param = groupShadertoy2.getParam("paramValueFloat7")
    group.getParam("Shadertoy2paramValueFloat7").setAsAlias(param)
    del param

    try:
        extModule = sys.modules["Ls_Contacts_GLExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)