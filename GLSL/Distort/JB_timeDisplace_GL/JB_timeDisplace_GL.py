# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named JB_timeDisplace_GLExt.py
# See http://natron.readthedocs.org/en/master/devel/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from JB_timeDisplace_GLExt import *
except ImportError:
    pass

def getPluginID():
    return "natron.community.plugins.JB_timeDisplace_GL"

def getLabel():
    return "JB_timeDisplace_GL"

def getVersion():
    return 1.0

def getIconPath():
    return "JB_timeDisplace_GL.png"

def getGrouping():
    return "Community/GLSL/Distort"

def getPluginDescription():
    return "Tries to emulate the Sapphire s_TimeDisplace node."

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group
    lastNode.setColor(0.07451, 0.5686, 0.4863)

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

    param = lastNode.createSeparatorParam("SETUP", "Setup")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.SETUP = param
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

    param = lastNode.createDoubleParam("Shadertoy1_2paramValueFloat0", "Red timeshift : ")
    param.setMinimum(0, 0)
    param.setMaximum(10000, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(10, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueFloat0 = param
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

    param = lastNode.createDoubleParam("Shadertoy1_2paramValueFloat1", "Green timeshift : ")
    param.setMinimum(0, 0)
    param.setMaximum(10000, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(10, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueFloat1 = param
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

    param = lastNode.createDoubleParam("Shadertoy1_2paramValueFloat2", "Blue timeshift : ")
    param.setMinimum(0, 0)
    param.setMaximum(10000, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(10, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueFloat2 = param
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

    param = lastNode.createIntParam("Shadertoy1_2paramValueInt3", "Iterations : ")
    param.setMinimum(0, 0)
    param.setMaximum(10000, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(25, 0)
    param.setDefaultValue(2, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueInt3 = param
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

    param = lastNode.createSeparatorParam("TIMING", "Timing")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.TIMING = param
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

    param = lastNode.createIntParam("previous_frametimeOffset", "Frame offset : ")
    param.setMinimum(-1000, 0)
    param.setMaximum(1000, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(25, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(False)
    param.setValue(1, 0)
    lastNode.previous_frametimeOffset = param
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

    param = lastNode.createSeparatorParam("OPTION", "Option")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.OPTION = param
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

    param = lastNode.createBooleanParam("Shadertoy1_2paramValueBool4", "Interpolate : ")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("interpolate")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueBool4 = param
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

    param = lastNode.createSeparatorParam("NAME", "JB_timeDisplace_GL v1.0")

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
    lastNode.setPosition(4139, 4769)
    lastNode.setSize(80, 32)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput2 = lastNode

    del lastNode
    # End of node "Output2"

    # Start of node "Source"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Source")
    lastNode.setLabel("Source")
    lastNode.setPosition(4134, 3645)
    lastNode.setSize(80, 32)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupSource = lastNode

    del lastNode
    # End of node "Source"

    # Start of node "Shadertoy1_2"
    lastNode = app.createNode("net.sf.openfx.Shadertoy", 1, group)
    lastNode.setScriptName("Shadertoy1_2")
    lastNode.setLabel("Shadertoy1_2")
    lastNode.setPosition(4134, 4310)
    lastNode.setSize(80, 34)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupShadertoy1_2 = lastNode

    param = lastNode.getParam("paramValueFloat0")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramValueFloat1")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramValueFloat2")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramValueInt3")
    if param is not None:
        param.setValue(2, 0)
        del param

    param = lastNode.getParam("paramValueBool4")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("imageShaderSource")
    if param is not None:
        param.setValue("//\n//\n//                          MMMMMMMMMMMMMMMMMMMMMMMMMMMM\n//                        MM.                          .MM\n//                       MM.  .MMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                      MM.  .MMMMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                     MM.  .MMMM        MMMMMMM    MMM.  .MM\n//                    MM.  .MMM           MMMMMM     MMM.  .MM\n//                   MM.  .MmM              MMMM      MMM.  .MM\n//                  MM.  .MMM                 MM       MMM.  .MM\n//                 MM.  .MMM                   M        MMM.  .MM\n//                MM.  .MMM                              MMM.  .MM\n//                 MM.  .MMM                            MMM.  .MM\n//                  MM.  .MMM       M                  MMM.  .MM\n//                   MM.  .MMM      MM                MMM.  .MM\n//                    MM.  .MMM     MMM              MMM.  .MM\n//                     MM.  .MMM    MMMM            MMM.  .MM\n//                      MM.  .MMMMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                       MM.  .MMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                        MM.                          .MM\n//                          MMMMMMMMMMMMMMMMMMMMMMMMMMMM\n//\n//\n//\n//\n// Adaptation pour Natron par F. Fernandez\n// Code original : JB_timeDisplace Matchbox pour Autodesk Flame\n\n// Adapted to Natron by F.Fernandez\n// Original code : JB_timeDisplace Matchbox for Autodesk Flame\n\n\n// iChannel0: Input 1, filter=linear, wrap=clamp\n// iChannel1: Input 2, filter=linear, wrap=clamp\n// iChannel2: previous frame, filter=linear, wrap=clamp\n// iChannel3: next frame, filter=linear, wrap=clamp\n// BBox: iChannel0\n\n\n\n\nuniform float redTS = 1.0; // Red timeshift : \nuniform float greenTS = 1.0; // Green timeshift : \nuniform float blueTS = 1.0; // Blue timeshift : \n\nuniform int iterations = 2; // Iterations : \nuniform bool interpolate = false; // Interpolate\n\n\n\n\nvoid mainImage( out vec4 fragColor, in vec2 fragCoord )\n{\n\tvec2 st0;\n\tst0.x = fragCoord.x / iResolution.x;\n\tst0.y = fragCoord.y / iResolution.y;\n\t\n\tvec4 getColPixel0;\n\tgetColPixel0 = texture2D(iChannel0, st0);\n\t\n\tvec3 color;\n\tvec2 st1;\n\tvec2 st2;\n\tvec2 st3;\n\tvec4 getColPixel1;\t\t\n\t\t\n   \tvec3 prev = texture2D( iChannel2, st0 ).rgb;\n  \tvec3 next = texture2D( iChannel3, st0 ).rgb;\n   \tvec3 curr = texture2D( iChannel0, st0 ).rgb;\n\t\t\n\t\t\n\t\t\n\tcolor = getColPixel0.rgb;\n\tfloat colorBuffer;\n\tint count=0;\n\tfor (int x = 0; x <=iterations; x++)\n\t{\n\t\tfor (int y = 1; y<= iterations; y++)\n\t\t{\n\t\tst1.x = (fragCoord.x+x) / iResolution.x;\n\t\tst1.y = (fragCoord.y+y) / iResolution.y;\n\t\tif ( (fragCoord.x+x) >=0 && (fragCoord.x+x) <= iResolution.x){getColPixel1 = texture2D(iChannel1, st1);}\n\t\tif ( (fragCoord.y+y) >=0 && (fragCoord.y+y) <= iResolution.y){getColPixel1 = texture2D(iChannel1, st1);}\t\t\n\t\tcolor += getColPixel1.rgb;count++;\n\t\t}\n\tcount++;\n\t}\n\t\n\tfor (int x = 0; x <=iterations; x++)\n\t{\n\t\tfor (int y = 1; y<= iterations; y++)\n\t\t{\n\t\tst1.x = (fragCoord.x-x) / iResolution.x;\n\t\tst1.y = (fragCoord.y+y) / iResolution.y;\n\t\tif ( (fragCoord.x-x) >=0 && (fragCoord.x-x) <= iResolution.x){getColPixel1 = texture2D(iChannel1, st1);}\n\t\tif ( (fragCoord.y+y) >=0 && (fragCoord.y+y) <= iResolution.y){getColPixel1 = texture2D(iChannel1, st1);}\t\t\n\t\tcolor += getColPixel1.rgb;count++;\n\t\t}\n\tcount++;\n\t}\n\t\n\tfor (int x = 0; x <=iterations; x++)\n\t{\n\t\tfor (int y = 1; y<= iterations; y++)\n\t\t{\n\t\tst1.x = (fragCoord.x+x) / iResolution.x;\n\t\tst1.y = (fragCoord.y-y) / iResolution.y;\n\t\tif ( (fragCoord.x+x) >=0 && (fragCoord.x+x) <= iResolution.x){getColPixel1 = texture2D(iChannel1, st1);}\n\t\tif ( (fragCoord.y-y) >=0 && (fragCoord.y-y) <= iResolution.y){getColPixel1 = texture2D(iChannel1, st1);}\t\t\n\t\tcolor += getColPixel1.rgb;count++;\n\t\t}\n\tcount++;\n\t}\n\tfor (int x = 0; x <=iterations; x++)\n\t{\n\t\tfor (int y = 1; y<= iterations; y++)\n\t\t{\n\t\tst1.x = (fragCoord.x-x) / iResolution.x;\n\t\tst1.y = (fragCoord.y-y) / iResolution.y;\n\t\tif ( (fragCoord.x-x) >=0 && (fragCoord.x-x) <= iResolution.x){getColPixel1 = texture2D(iChannel1, st1);}\n\t\tif ( (fragCoord.y-y) >=0 && (fragCoord.y-y) <= iResolution.y){getColPixel1 = texture2D(iChannel1, st1);}\t\t\n\t\tcolor += getColPixel1.rgb;count++;\n\t\t}\n\tcount++;\n\t}\n\tcolor/=count;\n\tfloat buffer = 1;\n\tvec3 outcolor = curr;\n\tif ((color.r*redTS)>=(color.b*blueTS) && (color.r*redTS)>=(color.g*greenTS) ){outcolor = next;if (interpolate == true){outcolor = (next+curr)*0.5;}}\n\tif ((color.g*greenTS)>=(color.r*redTS) && (color.g*greenTS)>=(color.b*blueTS) ){outcolor = curr;}\n\tif ((color.b*blueTS)>=(color.r*redTS) && (color.b*blueTS)>=(color.g*greenTS) ){outcolor = prev;if (interpolate == true){outcolor = (next+prev)*0.5;}}\n\n\tvec4 outColor;\n\tfragColor =  vec4(outcolor,1.0);\n}\n")
        del param

    param = lastNode.getParam("mipmap0")
    if param is not None:
        param.set("linear")
        del param

    param = lastNode.getParam("wrap0")
    if param is not None:
        param.set("clamp")
        del param

    param = lastNode.getParam("inputLabel0")
    if param is not None:
        param.setValue("Input 1")
        del param

    param = lastNode.getParam("mipmap1")
    if param is not None:
        param.set("linear")
        del param

    param = lastNode.getParam("wrap1")
    if param is not None:
        param.set("clamp")
        del param

    param = lastNode.getParam("inputLabel1")
    if param is not None:
        param.setValue("Input 2")
        del param

    param = lastNode.getParam("mipmap2")
    if param is not None:
        param.set("linear")
        del param

    param = lastNode.getParam("wrap2")
    if param is not None:
        param.set("clamp")
        del param

    param = lastNode.getParam("inputLabel2")
    if param is not None:
        param.setValue("previous frame")
        del param

    param = lastNode.getParam("mipmap3")
    if param is not None:
        param.set("linear")
        del param

    param = lastNode.getParam("wrap3")
    if param is not None:
        param.set("clamp")
        del param

    param = lastNode.getParam("inputLabel3")
    if param is not None:
        param.setValue("next frame")
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
        param.setValue(5, 0)
        del param

    param = lastNode.getParam("paramType0")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName0")
    if param is not None:
        param.setValue("redTS")
        del param

    param = lastNode.getParam("paramLabel0")
    if param is not None:
        param.setValue("Red timeshift :")
        del param

    param = lastNode.getParam("paramDefaultFloat0")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramType1")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName1")
    if param is not None:
        param.setValue("greenTS")
        del param

    param = lastNode.getParam("paramLabel1")
    if param is not None:
        param.setValue("Green timeshift :")
        del param

    param = lastNode.getParam("paramDefaultFloat1")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramType2")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName2")
    if param is not None:
        param.setValue("blueTS")
        del param

    param = lastNode.getParam("paramLabel2")
    if param is not None:
        param.setValue("Blue timeshift :")
        del param

    param = lastNode.getParam("paramDefaultFloat2")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramType3")
    if param is not None:
        param.set("int")
        del param

    param = lastNode.getParam("paramName3")
    if param is not None:
        param.setValue("iterations")
        del param

    param = lastNode.getParam("paramLabel3")
    if param is not None:
        param.setValue("Iterations :")
        del param

    param = lastNode.getParam("paramDefaultInt3")
    if param is not None:
        param.setValue(2, 0)
        del param

    param = lastNode.getParam("paramType4")
    if param is not None:
        param.set("bool")
        del param

    param = lastNode.getParam("paramName4")
    if param is not None:
        param.setValue("interpolate")
        del param

    param = lastNode.getParam("paramLabel4")
    if param is not None:
        param.setValue("Interpolate")
        del param

    del lastNode
    # End of node "Shadertoy1_2"

    # Start of node "Dot1"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot1")
    lastNode.setLabel("Dot1")
    lastNode.setPosition(4167, 4017)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot1 = lastNode

    del lastNode
    # End of node "Dot1"

    # Start of node "next_frame"
    lastNode = app.createNode("net.sf.openfx.timeOffset", 1, group)
    lastNode.setScriptName("next_frame")
    lastNode.setLabel("next_frame")
    lastNode.setPosition(4022, 4128)
    lastNode.setSize(80, 34)
    lastNode.setColor(0.7, 0.65, 0.35)
    groupnext_frame = lastNode

    param = lastNode.getParam("timeOffset")
    if param is not None:
        param.setValue(-1, 0)
        del param

    del lastNode
    # End of node "next_frame"

    # Start of node "previous_frame"
    lastNode = app.createNode("net.sf.openfx.timeOffset", 1, group)
    lastNode.setScriptName("previous_frame")
    lastNode.setLabel("previous_frame")
    lastNode.setPosition(3864, 4125)
    lastNode.setSize(80, 34)
    lastNode.setColor(0.7, 0.65, 0.35)
    groupprevious_frame = lastNode

    param = lastNode.getParam("timeOffset")
    if param is not None:
        param.setValue(1, 0)
        del param

    del lastNode
    # End of node "previous_frame"

    # Start of node "Dot2"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot2")
    lastNode.setLabel("Dot2")
    lastNode.setPosition(4358, 4320)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot2 = lastNode

    del lastNode
    # End of node "Dot2"

    # Start of node "Dot3"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot3")
    lastNode.setLabel("Dot3")
    lastNode.setPosition(4055, 4017)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot3 = lastNode

    del lastNode
    # End of node "Dot3"

    # Start of node "Dot4"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot4")
    lastNode.setLabel("Dot4")
    lastNode.setPosition(3897, 4017)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot4 = lastNode

    del lastNode
    # End of node "Dot4"

    # Start of node "Displace_matte"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Displace_matte")
    lastNode.setLabel("Displace_matte")
    lastNode.setPosition(4317, 3638)
    lastNode.setSize(80, 32)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupDisplace_matte = lastNode

    del lastNode
    # End of node "Displace_matte"

    # Now that all nodes are created we can connect them together, restore expressions
    groupOutput2.connectInput(0, groupShadertoy1_2)
    groupShadertoy1_2.connectInput(0, groupDot1)
    groupShadertoy1_2.connectInput(1, groupDot2)
    groupShadertoy1_2.connectInput(2, groupprevious_frame)
    groupShadertoy1_2.connectInput(3, groupnext_frame)
    groupDot1.connectInput(0, groupSource)
    groupnext_frame.connectInput(0, groupDot3)
    groupprevious_frame.connectInput(0, groupDot4)
    groupDot2.connectInput(0, groupDisplace_matte)
    groupDot3.connectInput(0, groupDot1)
    groupDot4.connectInput(0, groupDot3)

    param = groupShadertoy1_2.getParam("paramValueFloat0")
    group.getParam("Shadertoy1_2paramValueFloat0").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueFloat1")
    group.getParam("Shadertoy1_2paramValueFloat1").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueFloat2")
    group.getParam("Shadertoy1_2paramValueFloat2").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueInt3")
    group.getParam("Shadertoy1_2paramValueInt3").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueBool4")
    group.getParam("Shadertoy1_2paramValueBool4").setAsAlias(param)
    del param
    param = groupnext_frame.getParam("timeOffset")
    param.setExpression("ret = (thisGroup.previous_frame.timeOffset.get())*-1", False, 0)
    del param
    param = groupprevious_frame.getParam("timeOffset")
    group.getParam("previous_frametimeOffset").setAsAlias(param)
    del param

    try:
        extModule = sys.modules["JB_timeDisplace_GLExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)