# @file	  sdm.py
# @author Garfield A. Lewis <garfield.lewis@lzlabs.com>
# @brief  SDM environment for the GDB debugger.
#
# @section Copyright
#   
#   Copyright Notice:
#   
#   Copyright (C) 2019 LzLabs GmbH
#   All Rights Reserved.
#   
#   This product and associated documentation includes confidential,
#   proprietary and trade secret information and code.  No part of
#   this product or associated documentation may be modified,
#   distributed, or copied in any form except as expressly permitted
#   by the license agreement pertaining to this product.
#   
# @section License
#   
#   This file is Object Code Only and is NOT to be distributed in source form.
#   
# @section Description
#   
#   Implementation of some SDM environment for the GDB debugger. This can be
#   used to debug problems associated with the LzLabs SDM.
#   
# @section Source
#   
#   Information in this file is original.
#
import sys
#import os

# Add the current path to the system path so that the subsequent import will
# find my external libraries.
if sys.path[0] != '/opt/lzlabs/debug/gdb':
   sys.path.insert( 0, '/opt/lzlabs/debug/gdb' )

_zthread      = 1
_zbreakpoints = []

from zdisass import *
from zinfo import * 
from zfuncs import *
from zmemory import *
from sdmpretty import *
