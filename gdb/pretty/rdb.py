# @file   rdb.py
# @author Peeter Joot <peeter.joot@lzlabs.com>
# @brief  pretty printers for the RDB types.
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


class DB2_SQLVARprinter:
    """Pretty print a 'DB2_SQLVAR'.  This is a pretty printer reimplementation of the lpe.gdb macro pSqlvar"""

    def __init__(self, val):
        self.val = val

    def to_string(self):
        s = '{\n'

        s += sprinth16( self.val, 'hDATA_TYPE' )
        s += sprinth16( self.val, 'hDATA_LENGTH' )
        s += sprinthp32( self.val, 'VpvDATA_FIELD', '(void *)' )
        s += sprinthp32( self.val, 'VpvNULL_FIELD', '(short *)' )
        s += sprinth16( self.val, 'hCOL_NAME_LEN' )
        s += sprints( self.val, 'aeCOL_NAME' )

        s += '}'

        return s


class DB2_SQLDAprinter:
    """Pretty print a 'DB2_SQLDA'.  This is a pretty printer reimplementation of the lpe.gdb macro pSqlda"""

    def __init__(self, val):
        self.val = val

    def to_string(self):
        s = '{\n'

        s += sprints( self.val, 'aeEYE_CATCHER' )
        s += sprinth8( self.val, 'eCCSID_OVERRIDE' )
        s += sprinth8( self.val, 'eSQLVAR_COL_NUM' )
        s += sprinth32( self.val, 'iSQLDA_LENGTH' )
        s += sprinth16( self.val, 'hSQLVAR_COUNT' )
        s += sprinth16( self.val, 'hHOST_VARS' )
        s += sprinthp32( self.val, 'asSQLVARS', '(DB2_SQLVAR *)' )

        s += '}'

        return s


class DB2_RDIprinter:
    """Pretty print a 'DB2_RDI'.  This is a pretty printer reimplementation of the lpe.gdb macro pRdi"""

    def __init__(self, val):
        self.val = val

    def to_string(self):
        s = '{\n'

        s += sprinth16( self.val, 'hRDI_LENGTH' )
        s += sprinth8( self.val, 'abRDI_FLAG_BYTES[0]' )
        s += sprinth8( self.val, 'abRDI_FLAG_BYTES[1]' )

        s += sprinth16( self.val, 'hRDI_CURSOR_TYPE' )

        s += sprinth16( self.val, 'aeRDI_PROGRAM_NAME' )
        s += sprinth16( self.val, 'abRDI_PRECOMP_TIMESTAMP' )

        s += sprinth16( self.val, 'hRDI_SECTION' )
        s += sprinthp32( self.val, 'VpvRDI_SQLCA', '(DB2_SQLCA*)' )
        s += sprinthp32( self.val, 'VpvRDI_INPUT_HOST_VARS', '(DB2_SQLDA*)' )
        s += sprinthp32( self.val, 'VpvRDI_OUTPUT_HOST_VARS', '(DB2_SQLDA*)' )
        s += sprinth16( self.val, 'hRDI_CCSID_TO_USE' )
        s += sprinth16( self.val, 'hRDI_STMT_TYPE' )
        s += sprinth32( self.val, 'iRDI_STMT_NUMBER' )
        s += sprinth8( self.val, 'bRDI_ONE_LAST_FLAG' )

        s += '}'

        return s

