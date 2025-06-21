# @file   lce.py
# @author Peeter Joot <peeter.joot@lzlabs.com>
# @brief  pretty printers for LCE types.
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
#    Fixme: description todo.
#
# @section Source
#
#   Information in this file is original.
#
import sys

if sys.path[0] != '/opt/lzlabs/debug/gdb':
    sys.path.insert( 0, '/opt/lzlabs/debug/gdb' )

from pretty.helper import *

class FIBprinter:
    """Pretty print a 'struct FIB'"""

    def __init__(self, val):
        self.val = val

    def to_string(self):
        s = '{\n'

        s += sprints( self.val, 'eyecatch' )
        s += sprinth8( self.val, 'relfib' )
        s += sprinth8( self.val, 'totfib' )
        s += sprints( self.val, 'ddname' )
        s += sprinth8( self.val, 'ftype' )
        s += sprinth8( self.val, 'access' )
        s += sprinth8( self.val, 'flag12' )
        s += sprinth8( self.val, 'flag13' )
        s += sprinth8( self.val, 'flag14' )
        s += sprinth8( self.val, 'flag15' )
        s += sprinth8( self.val, 'recfm' )
        s += sprinth32( self.val, 'blksize' )
        s += sprinth32( self.val, 'lrecl' )
        s += sprinth8( self.val, 'bufno' )
        s += sprinth8( self.val, 'flag23' )
        s += sprinth8( self.val, 'flag24' )
        s += sprinth8( self.val, 'numkey' )

        s += sprinthp32( self.val, 'blf', '(void *)' )
        s += sprinthp32( self.val, 'blw', '(unsigned short *)' )
        # pointer to 6 bytes:
        s += sprinthp32( self.val, 'vfs', '(char *)' )
        # pointer to 1 byte followed by 2 bytes:
        s += sprinthp32( self.val, 'lctr', '(void *)' )
        s += sprinthp32( self.val, 'keyarea', '(KEYAREA *)' )
        # pointer to 4 bytes followed by 1 byte:
        s += sprinthp32( self.val, 'ldef', '(void *)' )

        s += sprints( self.val, 'fdname' )

        s += '}'

        return s


class IGZXDSP_PARMprinter:
    """Pretty print a 'IGZXDSP_PARM'.  This is a pretty printer reimplementation of the lpe.gdb macro pdispparm"""

    def __init__(self, val):
        self.val = val

    def to_string(self):
        s = '{\n'

        s += sprinth32( self.val, 'numitem' )
        s += sprinth8( self.val, 'upon' )
        s += sprinth8( self.val, 'flags' )
        s += sprinth16( self.val, 'codepage' )

        s += '}'

        return s


class IGZXDSP_PARGprinter:
    """Pretty print a 'IGZXDSP_PARG'.  This is a pretty printer reimplementation of the lpe.gdb macro pdispparg"""

    def __init__(self, val):
        self.val = val

    def to_string(self):
        s = '{\n'

        s += sprinth32( self.val, 'item_adr' )
        s += sprinth32( self.val, 'item_type' )
        s += sprinth32( self.val, 'item_len' )
        s += sprinth32( self.val, 'item_digits' )

        s += '}'

        return s


class FCBprinter:
    """Pretty print a 'FCB'.  This is a pretty printer reimplementation of the lpe.gdb macro pfcb"""

    def __init__(self, val):
        self.val = val

    def to_string(self):
        s = '{\n'

        s += sprints( self.val, 'eyecatch' )
        s += sprinth8( self.val, 'relfcb' )
        s += sprinth8( self.val, 'totfcb' )
        s += sprinth8( self.val, 'mode' )
        s += sprinth8( self.val, 'open_flag' )
        s += sprinth8( self.val, 'close_flag' )
        s += sprinth8( self.val, 'mfsw' )
        s += sprinth8( self.val, 'keynum' )
        s += sprinth8( self.val, 'keycmpln' )

        # not interesting:
        #
        #python printh32 ( "   ", "ioread", "($arg0)->ioread", "," )
        #python printh32 ( "   ", "iowrite", "($arg0)->iowrite", "," )
        #python printh32 ( "   ", "iowrewrite", "($arg0)->iowrewrite", "," )
        #python printh32 ( "   ", "iomrewrite", "($arg0)->iomrewrite", "," )
        #python printh32 ( "   ", "iostart", "($arg0)->iostart", "," )
        #python printh32 ( "   ", "iodelete", "($arg0)->iodelete", "," )
        #python printh32 ( "   ", "iowriterr", "($arg0)->iowriterr", "," )
        #
        s += sprinth8( self.val, 'blfoffid' )
        s += sprints( self.val, 'blfoff' )
        s += sprinth32( self.val, 'blfrcon' )
        s += sprinth8( self.val, 'mode_opened' )
        s += sprinth8( self.val, 'end_of_page_flag' )
        s += sprinth8( self.val, 'resv71' )
        s += sprinth8( self.val, 'resv72' )
        s += sprinth8( self.val, 'flag73' )
        s += sprinth8( self.val, 'flag74' )
        s += sprinth8( self.val, 'flag75' )
        s += sprinth8( self.val, 'flag76' )
        s += sprinth8( self.val, 'flag77' )
        s += sprinth32( self.val, 'dcbrpl' )
        s += sprinthp32( self.val, 'dcbrpl', '(DCB *)' )
        s += sprints( self.val, 'progname' )
        s += sprints( self.val, 'ddname' )
        s += sprinth32( self.val, 'rerun_counter' )
        s += sprinthp32 ( self.val, 'fib', '(FIB *)' )
        s += sprinth32( self.val, 'nrecarea' )
        s += sprinth8( self.val, 'flagB0' )
        s += sprinth8( self.val, 'flagB1' )
        s += sprinth8( self.val, 'flagB2' )
        s += sprinth8( self.val, 'reason' )
        s += sprinth8( self.val, 'byte1' )
        s += sprinth8( self.val, 'rc' )
        s += sprinth8( self.val, 'byteCA' )
        s += sprinth8( self.val, 'errmgsw' )
        s += sprinth32( self.val, 'count' )
        s += sprinth32( self.val, 'advance' )
        s += sprinth32( self.val, 'linage_is' )
        s += sprinth32( self.val, 'footing_at' )
        s += sprinth32( self.val, 'top_lines' )
        s += sprinth32( self.val, 'bottom_lines' )
        s += sprinth8( self.val, 'advopt' )
        s += sprinth8( self.val, 'advchan' )
        s += sprinth32( self.val, 'mrecarea' )

        s += '}'

        return s


class KEYAREAprinter:
    """Pretty print a 'KEYAREA'.  This is a pretty printer reimplementation of the lpe.gdb macro pKeyarea"""

    def __init__(self, val):
        self.val = val

    def to_string(self):
        s = '{\n'

        s += sprinth8( self.val, 'flag00' )
        s += sprinth8( self.val, 'keylen' )
        s += sprinth32( self.val, 'keyrcon' )

        s += '}'

        return s

