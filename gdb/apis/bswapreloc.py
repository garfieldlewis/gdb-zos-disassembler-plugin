# @file   bswapreloc.py
# @author Peeter Joot <peeter.joot@lzlabs.com>
# @brief  byteswaping and mainstor relocation methods for SDM debugging.
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
#   Examples: Fixme.
#
# @section Source
#
#   Information in this file is original.
#

import gdb
import struct
import string
import codecs
import sys
import ctypes

if sys.path[0] != '/opt/lzlabs/debug/gdb':
    sys.path.insert( 0, '/opt/lzlabs/debug/gdb' )

from apis.common import *

def swap16(h):
    """byteswap a 16-bit value."""
    return struct.unpack("<H", struct.pack(">H", h))[0]

def swap32(i):
    """byteswap a 32-bit value"""
    return struct.unpack("<I", struct.pack(">I", i))[0]

def swap64(l):
    """byteswap a 64-bit value"""
    return struct.unpack("<L", struct.pack(">L", l))[0]

def MainstorValue():
    """Lookup mainstor value from CPU[0].  In a single threaded application (like batch), this is equivalent to regs->mainstor.
   
    Example:

    (gdb) python print "0x%016X" % (MainstorValue())
    0x00007FFBC1A45000
    """
    sb = gdb.lookup_type( "SYSBLK" )
    if sb == 0x0:
        raise gdb.GdbError(  "An SDM environment has not yet been initialized." )

    tid = getzthread() - 1
    mainstor = int(gdb.parse_and_eval( "sysblk->regs[{}].mainstor".format(tid) ).cast(gdb.lookup_type('long')))

    return mainstor

def VadrToPtr(p32):
    """Use the mainstor value from CPU[0] to compute the runtime relocation of a VADR pointer.

    Example:

    (gdb) python print "0x%016X" % (VadrToPtr(1))
    0x00007FFBC1A45001
    """
    p32m = p32 & 0x7FFFFFFF
    if p32m == 0:
        return p32
    else:
        return p32m + MainstorValue()

def wordtobytes(word, b):
    """An internal helper function to unpack an FWORD into 4 integer byte values, and append them to an array"""
    w = word >> 24
    b.append(w)
    w = (word >> 16) & 0xFF
    b.append(w)
    w = (word >> 8) & 0xFF
    b.append(w)
    w = word & 0xFF
    b.append(w)

printable = string.ascii_letters + string.digits + string.punctuation + ' '

def asciiBytesToPrintable(astr):
    """An internal function for VadrDumpF to convert an array of ASCII byte values to a string, substituting '.' for unprintable characters"""
    return ''.join(chr(c) if (chr(c) in printable) else '.' for c in astr)

def ebcdicBytesToPrintable(estr):
    """An internal function for VadrDumpF to convert an array of EBCDIC byte values to ASCII, substituting '.' for unprintable characters"""
    s = ''
    for x in estr:
        # doesn't work with python3: get error like: bytes type required, not 'str' (once c is passed down to decode.)
        #c = chr(x)
        c = bytes( ctypes.c_char(x) )
        e = codecs.decode(c, 'cp1140')
        if e in printable:
            s += e
        else:
            s += '.'

    return s

def VadrDumpF(a, n = 4):
    """Dump of n FWORDs (rounded up to a multiple of 4) from a legacy or native address, with EBCDIC and ASCII columns.
   
    Example:

    (gdb) python VadrDumpF(16951668)
    0102A974  C6C9C200 0104C3D6 C2D7D9C9 D5E30084  |FIB...COBPRINT.d|................|

    (gdb) python VadrDumpF(16951668, 5)
    0102A974  C6C9C200 0104C3D6 C2D7D9C9 D5E30084  |FIB...COBPRINT.d|................|
    0102A984  80802410 00008400 00000079 00000079  |......d....`...`|..$........y...y|

    (gdb) python VadrDumpF(0x7fffc3fb0240,12)
    00007FFFC3FB0240  00000000 00000000 002301BC FF7F0000  |............."..|.........#......|
    00007FFFC3FB0250  7002FBC3 FF7F0000 EBCC32D8 FF7F0000  |...C.".....Q."..|p.........2.....|
    00007FFFC3FB0260  484000BD FB7F0000 00000000 01000000  |. ..."..........|H@..............|
    """

    if ( a < 0x7FFFFFFF ):
        p = VadrToPtr(a)
    else:
        p = a
    #print "a = %04X" % (a)
    #print "n = %d" % (n)

    r = n % 4
    if ( r != 0 ):
        n += 4 - r

    #print "rounded(n) = %d" % (n)
    words = []
    asbytes = []
    i = 0
    while i < n:
        thisaddr = p + 4*i
        deref = gdb.execute( "x/4xw {}".format( thisaddr ), to_string=True ).split( )
        #print deref
        j = 1
        while j <= 4:
            word = swap32( int(deref[j], 16) )
            #print "%016X %08X" % (thisaddr + 4*(j-1), word)
            words.append(word)
            wordtobytes(word, asbytes)
            j += 1
        i += 4

    #print asbytes

    i = 0
    while i < n:
        thesebytes = asbytes[i*4:i*4+16]
        if ( a < 0x7FFFFFFF ):
            print("%08X  %08X %08X %08X %08X  |%s|%s|" % (a + 4*i, words[i], words[i+1], words[i+2], words[i+3],
                    ebcdicBytesToPrintable(thesebytes),
                    asciiBytesToPrintable(thesebytes)))
        else:
            print("%016X  %08X %08X %08X %08X  |%s|%s|" % (a + 4*i, words[i], words[i+1], words[i+2], words[i+3],
                    ebcdicBytesToPrintable(thesebytes),
                    asciiBytesToPrintable(thesebytes)))
        i += 4

def PtrDumpF(p, n = 4):
    """Dump of n FWORDs (rounded up to a multiple of 4) from an address in legacy storage, with EBCDIC and ASCII columns.
   
    Example:
    (gdb) p fib
    $4 = (FIB *) 0x7ffbc2a6f974
    (gdb) python PtrDumpF(0x7ffbc2a6f974, 8)
    0x00007FFBC2A6F974 = mainstor(0x0102A974):
    0102A974  C6C9C200 0104C3D6 C2D7D9C9 D5E30084  |FIB...COBPRINT.d|................|
    0102A984  80802410 00008400 00000079 00000079  |......d....`...`|..$........y...y|
    """
    a = p - MainstorValue()

    print("0x%016X = mainstor(0x%08X):" % (p, a))
    VadrDumpF(a, n)
