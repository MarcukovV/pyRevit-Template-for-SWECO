# -*- coding: utf-8 -*-
"""
Tooltip:
Provide your tooltip here
"""

#__title__ = 'Your pushbutton name'
#__context__ = 'doc-project'	pushbutton only active if it's a project file
#__context__ = 'doc-workshared' pushbutton only active if it's a workshared project file
#__context__ = 'doc-family'		pushbutton only active if it's a family file
#__min_revit_ver__ = 2020		e.g. pushbutton active starting from Revit 2020 and up
#__max_revit_ver__ = 2023		e.g. pushbutton active with Revit version up to 2023

# IMPORTS
# import Revit classes from Autodesk library
from Autodesk.Revit.DB import *

# import standard pyrevit modules from pyrevit library
from pyrevit import revit, forms, script

# VARIABLES
# get current Revit document
doc = __revit__.ActiveUIDocument.Document

# FUNCTIONS

# YOUR SCRIPT
print('Sweco pyRevit Template')