# @file   pretty_pli.py
# @author Dirk Amadori <dirk@raincode.com>
# @brief  Byte swapping magic for older gdb versions.
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
#   This file is not required with the SDM gdb customizations for DWARF ENDIANITY
#    (to be contributed to binutils).
#   When that customized debugger is not available, this module can be used to do automatic
#   byte swapping of plirc generated FIXED BIN(15), FIXED BIN(31) types.
#   
# @section Source
#   
#   Information in this file is original.
#
import gdb.printing

# swap16, swap32:
from lpe.lpe import *

class fixedBin16Printer:

    def __init__(self, val):
        self.val = val

    def to_string(self):
        i = int(self.val.cast(gdb.lookup_type('short')))
        s = swap16(i)
        return s

class fixedBin32Printer:

    def __init__(self, val):
        self.val = val

    def to_string(self):
        i = int(self.val.cast(gdb.lookup_type('int')))
        s = swap32(i)
        return s

def build_pretty_printer():
    pp = gdb.printing.RegexpCollectionPrettyPrinter(
        "pretty_pli")
    pp.add_printer('fb16', '^fixed\.bin\.16$', fixedBin16Printer)
    pp.add_printer('fb32', '^fixed\.bin\.32$', fixedBin32Printer)
    return pp

gdb.printing.register_pretty_printer(
    gdb.current_objfile(),
    build_pretty_printer())
