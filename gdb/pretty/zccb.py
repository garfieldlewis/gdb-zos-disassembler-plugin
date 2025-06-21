# @file   zccb.py
# @author Peeter Joot <peeter.joot@lzlabs.com>
# @brief  pretty printers for misc zccb.h types.
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


class RPLprinter:
    """Pretty print a 'RPL'.  This is a pretty printer reimplementation of the lpe.gdb macro pRpl"""

    def __init__(self, val):
        self.val = val

    def to_string(self):
        s = '{\n'

        s += sprinth8( self.val, 'fdbk' )
        s += sprinth16( self.val, 'keylen' )
        s += sprinth32( self.val, 'acb' )
        s += sprinth32( self.val, 'area' )
        s += sprinth32( self.val, 'arg' )
        s += sprinth8( self.val, 'optcd1' )
        s += sprinth8( self.val, 'optcd2' )
        s += sprinth8( self.val, 'optcd3' )
        s += sprinth8( self.val, 'optcd4' )
        s += sprinth32( self.val, 'next' )
        s += sprinth32( self.val, 'reclen' )
        s += sprinth32( self.val, 'arealen' )
        s += sprinth16( self.val, 'msglen' )
        s += sprinth32( self.val, 'msgarea' )

        s += '}'

        return s


class DCBprinter:
    """Pretty print a 'DCB'.  This is a pretty printer reimplementation of the lpe.gdb macro pdcb"""

    def __init__(self, val):
        self.val = val

    def to_string(self):
        s = '{\n'

        s += sprinth32( self.val, 'dcbe' )
        s += sprinth8( self.val, 'kl' )
        s += sprinth8( self.val, 'devt' )
        s += sprinth16( self.val, 'trbal' )
        s += sprinth32( self.val, 'bufcb' )
        s += sprinth8( self.val, 'bufno' )
        s += sprinth24( self.val, 'bufca' )
        s += sprinth16( self.val, 'bufl' )
        s += sprinth16( self.val, 'dsorg' )
        s += sprinth8( self.val, 'dsorg1' )
        s += sprinth8( self.val, 'dsorg2' )
        s += sprinth32( self.val, 'iob' )
        s += sprinth8( self.val, 'bftek' )
        s += sprinth24( self.val, 'eoda' )
        s += sprinth32( self.val, 'eod' )
        s += sprinth8( self.val, 'recfm' )
        s += sprinth24( self.val, 'exlsta' )
        s += sprinth32( self.val, 'exlst' )
        s += sprints( self.val, 'ddname' )
        s += sprinth16( self.val, 'tiotoff' )
        s += sprinth16( self.val, 'macrf' )
        s += sprinth8( self.val, 'iflgs' )
        s += sprinth24( self.val, 'deba' )
        s += sprinth32( self.val, 'deb' )
        s += sprinth8( self.val, 'oflg' )
        s += sprinth8( self.val, 'iflg' )
        s += sprinth16( self.val, 'macr' )
        s += sprinth8( self.val, 'macr1' )
        s += sprinth8( self.val, 'macr2' )
        s += sprinth8( self.val, 'oflgs' )
        s += sprinth24( self.val, 'iortna' )
        s += sprinth32( self.val, 'iortn' )
        s += sprinth8( self.val, 'optcd' )
        s += sprinth24( self.val, 'checka' )
        s += sprinth32( self.val, 'check' )
        s += sprinth8( self.val, 'iobl' )
        s += sprinth24( self.val, 'syna' )
        s += sprinth16( self.val, 'blksi' )
        s += sprinth32( self.val, 'recad' )
        s += sprinth8( self.val, 'bufoff' )
        s += sprinth16( self.val, 'lrecl' )
        s += sprinth8( self.val, 'eropt' )
        s += sprinth24( self.val, 'notea' )
        s += sprinth16( self.val, 'precl' )
        s += sprinth32( self.val, 'eob' )
        s += sprinth32( self.val, 'note' )

        s += '}'

        return s


class ACBprinter:
    """Pretty print a 'ACB'.  This is a pretty printer reimplementation of the lpe.gdb macro pacb"""

    def __init__(self, val):
        self.val = val

    def to_string(self):
        s = '{\n'

        s += sprinth32( self.val, 'ambl' )
        s += sprinth32( self.val, 'rpl' )
        s += sprinth8( self.val, 'macr1' )
        s += sprinth8( self.val, 'macr2' )
        s += sprinth8( self.val, 'bstrno' )
        s += sprinth8( self.val, 'strno' )
        s += sprinth16( self.val, 'bufnd' )
        s += sprinth16( self.val, 'bufni' )
        s += sprinth8( self.val, 'macr3' )
        s += sprinth8( self.val, 'shrp' )
        s += sprinth8( self.val, 'macr4' )
        s += sprinth8( self.val, 'recfm' )
        s += sprinth8( self.val, 'cctyp' )
        s += sprinth8( self.val, 'rls' )
        s += sprinth8( self.val, 'dsorg1' )
        s += sprinth8( self.val, 'dsorg2' )
        s += sprinth32( self.val, 'passwd' )
        s += sprinth32( self.val, 'exlst' )
        s += sprints( self.val, 'ddname' )
        s += sprinth16( self.val, 'tiotoff' )
        s += sprinth16( self.val, 'infl' )
        s += sprinth8( self.val, 'iflgs' )
        s += sprinth24( self.val, 'deba' )
        s += sprinth32( self.val, 'deb' )
        s += sprinth8( self.val, 'oflgs' )
        s += sprinth8( self.val, 'erflg' )
        s += sprinth16( self.val, 'inflg' )
        s += sprinth32( self.val, 'bufsp' )
        s += sprinth16( self.val, 'blksi' )
        s += sprinth16( self.val, 'recsiz' )
        s += sprinth32( self.val, 'uwork' )
        s += sprinth32( self.val, 'cbwork' )
        s += sprinth32( self.val, 'appladdr' )

        s += '}'

        return s
