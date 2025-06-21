# @file   helper.py
# @author Peeter Joot <peeter.joot@lzlabs.com>
# @brief  pretty printer helper functions for internal SDM types
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
#   Fixme: describe.
#
# @section Source
#
#   Information in this file is original.
#
import sys
import gdb.printing

if sys.path[0] != '/opt/lzlabs/debug/gdb':
    sys.path.insert( 0, '/opt/lzlabs/debug/gdb' )

# swap32, VadrToPtr, ...
from apis.bswapreloc import *

def sprints(val, n, prefix = '   ', suffix = ',\n' ):
    """ gdb.Value based interface that takes an EBCDIC string and displays it in ASCII."""
    e = val[n]

    #if length == 0:
    #    sc = e.string('cp1140', 'strict', length)
    #else:
    sc = e.string('cp1140')

    s = ''
    if len(sc) != 0:
        s = prefix + n + ' = "' + sc + '" [ibm1140]' + suffix
    #else:
    #    s = prefix + n + ' = "' + sc + suffix

    return s


def sprinth8(val, n):
    """ gdb.Value based interface that takes a BYTE value and displays it in hexadecimal."""

    prefix = '   '
    suffix = ",\n"
    e = val[n]

    v = int(e.cast(gdb.lookup_type('char')))

    s = ''
    if v != 0:
        s = "%s%s = 0x%X%s" % (prefix, n, v & 0xFF, suffix)
    return s

def sprinth16(val, n):
    """ gdb.Value based interface that takes a HWORD value and displays it in hexadecimal."""
    prefix = '   '
    suffix = ",\n"
    e = val[n]

    pushort = gdb.lookup_type('unsigned short').pointer()
    v2 = gdb.Value(e).cast(pushort).dereference()
    sw = swap16(v2)

    s = ''
    if sw != 0:
        s = "%s%s = 0x%04hX%s" % (prefix, n, sw & 0xFFFF, suffix)
    return s

def sprinth24(val, n):
    """ gdb.Value based interface that takes a AL3 value and displays it in hexadecimal."""
    prefix = '   '
    suffix = ",\n"
    e = val[n]

    puint = gdb.lookup_type('unsigned').pointer()
    v2 = gdb.Value(e).cast(puint).dereference()
    sw = swap32(v2)
    sw &= 0xFFFFFF;

    s = ''
    if sw != 0:
        s = "%s%s = 0x%06hX%s" % (prefix, n, sw, suffix)
    return s

def sprinth32(val, n):
    """ gdb.Value based interface that takes a FWORD value and displays it in hexadecimal."""
    prefix = '   '
    suffix = ",\n"
    e = val[n]

    puint = gdb.lookup_type('unsigned').pointer()
    #print type(puint)
    #print type(e)
    #v = gdb.Value(e).cast(puint)
    #print type(v)
    v2 = gdb.Value(e).cast(puint).dereference()
    #print type(v2)
    sw = swap32(v2)
    #print sw
    #print v2.to_string() # bombs

    s = ''
    if sw != 0:
        s = "%s%s = 0x%08X%s" % (prefix, n, sw & 0xFFFFFFFF, suffix)
    return s

def sprinthp32(val, n, ptr):
    """ gdb.Value based interface that takes a FWORD value and displays it in hexadecimal, and shows it's relocation value and underlying type."""
    prefix = '   '
    suffix = ",\n"
    e = val[n]

    puint = gdb.lookup_type('unsigned').pointer()
    v2 = gdb.Value(e).cast(puint).dereference()
    sw = swap32(v2) & 0xFFFFFFFF

    s = ''
    if sw != 0:
        reloc = VadrToPtr(sw)
        s = "%s%s = mainstor(0x%08X) = %s0x%016X%s" % (prefix, n, sw, ptr, reloc, suffix)
    return s

