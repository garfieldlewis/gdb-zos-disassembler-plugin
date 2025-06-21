# @file   lpe.py
# @author Peeter Joot <peeter.joot@lzlabs.com>
# @brief  LPE FIB,FCO and byteswaping methods for SDM debugging.
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
#   LPE related FOP constants, FIB related stuff, 
#   and various print macros that can be used
#   in gdb scripts (lpe.gdb)
#   
# @section Source
#   
#   Information in this file is original.
#
import sys
import gdb.printing

if sys.path[0] != '/opt/lzlabs/debug/gdb':
    sys.path.insert( 0, '/opt/lzlabs/debug/gdb' )

from apis.bswapreloc import *

LPEFOP_LINESIZE      = 0x08000000
LPEFOP_PAGESIZE      = 0x04000000
LPEFOP_TITLE         = 0x02000000
LPEFOP_FILE          = 0x01000000
LPEFOP_KEYED         = 0x00800000
LPEFOP_PRINT         = 0x00400000
LPEFOP_SYSPRINTE     = 0x00200000
LPEFOP_EXTERNAL      = 0x00040000
LPEFOP_UNBUFFERED    = 0x00020000
LPEFOP_BUFFERED      = 0x00010000
LPEFOP_INPUT         = 0x00008000
LPEFOP_OUTPUT        = 0x00004000
LPEFOP_UPDATE        = 0x00002000
LPEFOP_SEQUENTIAL    = 0x00000800
LPEFOP_DIRECT        = 0x00000400
LPEFOP_STRING        = 0x00000200
LPEFOP_SYSPRINT      = 0x00000040
LPEFOP_STREAM        = 0x00000002
LPEFOP_RECORD        = 0x00000001

def fop(v):
    """ Translate (PL/I runtime) LPEFOP values to named constants. """
    o = v
    ret = ""
    sep = ""
 
    if v & LPEFOP_LINESIZE:
        ret = ret + sep + "LINESIZE";
        sep = " | "
        v = v & ~LPEFOP_LINESIZE
    if v & LPEFOP_PAGESIZE:
        ret = ret + sep + "PAGESIZE";
        sep = " | "
        v = v & ~LPEFOP_PAGESIZE
    if v & LPEFOP_TITLE:
        ret = ret + sep + "TITLE";
        sep = " | "
        v = v & ~LPEFOP_TITLE
    if v & LPEFOP_FILE:
        ret = ret + sep + "FILE";
        sep = " | "
        v = v & ~LPEFOP_FILE
    if v & LPEFOP_KEYED:
        ret = ret + sep + "KEYED";
        sep = " | "
        v = v & ~LPEFOP_KEYED
    if v & LPEFOP_PRINT:
        ret = ret + sep + "PRINT";
        sep = " | "
        v = v & ~LPEFOP_PRINT
    if v & LPEFOP_SYSPRINTE:
        ret = ret + sep + "SYSPRINTE";
        sep = " | "
        v = v & ~LPEFOP_SYSPRINTE
    if v & LPEFOP_EXTERNAL:
        ret = ret + sep + "EXTERNAL";
        sep = " | "
        v = v & ~LPEFOP_EXTERNAL
    if v & LPEFOP_UNBUFFERED:
        ret = ret + sep + "UNBUFFERED";
        sep = " | "
        v = v & ~LPEFOP_UNBUFFERED
    if v & LPEFOP_BUFFERED:
        ret = ret + sep + "BUFFERED";
        sep = " | "
        v = v & ~LPEFOP_BUFFERED
    if v & LPEFOP_INPUT:
        ret = ret + sep + "INPUT";
        sep = " | "
        v = v & ~LPEFOP_INPUT
    if v & LPEFOP_OUTPUT:
        ret = ret + sep + "OUTPUT";
        sep = " | "
        v = v & ~LPEFOP_OUTPUT
    if v & LPEFOP_UPDATE:
        ret = ret + sep + "UPDATE";
        sep = " | "
        v = v & ~LPEFOP_UPDATE
    if v & LPEFOP_SEQUENTIAL:
        ret = ret + sep + "SEQUENTIAL";
        sep = " | "
        v = v & ~LPEFOP_SEQUENTIAL
    if v & LPEFOP_DIRECT:
        ret = ret + sep + "DIRECT";
        sep = " | "
        v = v & ~LPEFOP_DIRECT
    if v & LPEFOP_STRING:
        ret = ret + sep + "STRING";
        sep = " | "
        v = v & ~LPEFOP_STRING
    if v & LPEFOP_SYSPRINT:
        ret = ret + sep + "SYSPRINT";
        sep = " | "
        v = v & ~LPEFOP_SYSPRINT
    if v & LPEFOP_STREAM:
        ret = ret + sep + "STREAM";
        sep = " | "
        v = v & ~LPEFOP_STREAM
    if v & LPEFOP_RECORD:
        ret = ret + sep + "RECORD";
        sep = " | "
        v = v & ~LPEFOP_RECORD

    if v:
        ret = hex(v) + "| " + ret;

    return hex(o) + " ( " + ret + " )"


#x = fop( 0x00864801 | 0x10000000)
#print "x = " + x

FIB_ACCESS_SEQUENTIAL = 0x80
FIB_ACCESS_RANDOM     = 0x40
FIB_ACCESS_DYNAMIC    = 0x20

def fibaccess(v):
    o = v
    ret = ""
    if v & FIB_ACCESS_SEQUENTIAL:
        ret = "FIB_ACCESS_SEQUENTIAL";
    if v & FIB_ACCESS_RANDOM:
        ret = "FIB_ACCESS_RANDOM";
    if v & FIB_ACCESS_DYNAMIC:
        ret = "FIB_ACCESS_DYNAMIC";

    return hex(o) + " ( " + ret + " )"
 

# Second generation debug helper methods to be phased out (implement python gdb pretty printerrs instead):
def i16r(v):
    return swap16( gdb.parse_and_eval( "*(unsigned short*)(" + v + ")" ) )

def i24r(v):
    tmp1 = int;
    tmp2 = int;
    tmp1 = swap16( gdb.parse_and_eval( "*(unsigned short*)(" + v + ")" ) )
    tmp2 = gdb.parse_and_eval( "*((unsigned char*)(" + v + ") + 2)" )
    return (tmp1 << 8) | (tmp2 << 16)

def i32r(v):
    return swap32( gdb.parse_and_eval( "*(unsigned int*)(" + v + ")" ) )

def i64r(v):
    return swap64( gdb.parse_and_eval( "*(unsigned long*)(" + v + ")" ) )

def printh(prefix, n, e, suffix):
    v = gdb.parse_and_eval( e )
    if v != 0:
        print("%s%s = 0x%X%s" % (prefix, n, v, suffix))

def prints(prefix, n, e, suffix):
    s = gdb.parse_and_eval( e )
    print("%s%s = %s%s" % (prefix, n, s, suffix))

def printh16(prefix, n, e, suffix):
    sw = i16r(e)
    if sw != 0:
        print("%s%s = 0x%04hX%s" % (prefix, n, sw, suffix))

def printh24(prefix, n, e, suffix):
    sw = i24r(e)
    if sw != 0:
        print("%s%s = 0x%06hX%s" % (prefix, n, sw, suffix))

def printh32(prefix, n, e, suffix):
    sw = i32r(e)
    if sw != 0:
        print("%s%s = 0x%08X%s" % (prefix, n, sw, suffix))

def printh64(prefix, n, e, suffix):
    sw = i64r(e)
    if sw != 0:
        print("%s%s = 0x%016X%s" % (prefix, n, sw, suffix))

#   python printhp32 ( "   ", "srcded", "($arg0)->srcded", "", ",", "regs" )
# prefix: "    "
# n: "srcded"
# e: "($arg0)->srcded"
# t: "(LPEDED*)"
# suffix: -- unused.
def printhp32(prefix, n, e, t, suffix):
    sw = i32r(e)
    if sw != 0:
        print("%s%s = 0x%08X (%s0x%016lX)," % (prefix, n, sw, t, VadrToPtr(sw)))


