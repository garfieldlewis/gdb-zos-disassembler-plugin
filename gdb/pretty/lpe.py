# @file   lpe.py
# @author Peeter Joot <peeter.joot@lzlabs.com>
# @brief  pretty printers for the LPE types.
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

class LPEDDNAMEprinter:
    """Pretty print a 'LPEDDNAME'"""

    def __init__(self, val):
        self.val = val

    def to_string(self):
        s = '{\n'

        s += sprinth16( self.val, 'length' )
        s += sprints( self.val, 'n' )

        s += '}'

        return s

class LPEFCEprinter:
    """Pretty print a 'LPEFCE'"""

    def __init__(self, val):
        self.val = val

    def to_string(self):
        s = '{\n'

        s += sprinth32( self.val, 'totstg' )
        s += sprinth32( self.val, 'acb' )
        s += sprinth32( self.val, 'rd_rpl' )
        s += sprinth32( self.val, 'wr_rpl' )
        s += sprinth32( self.val, 'read' )
        s += sprinth32( self.val, 'write' )
        s += sprinth32( self.val, 'wr_recl' )
        s += sprinth32( self.val, 'rd_recl' )
        s += sprinth32( self.val, 'wr_buf' )
        s += sprinth32( self.val, 'rd_buf' )
        s += sprinth32( self.val, 'wr_arg' )
        s += sprinth32( self.val, 'rd_arg' )
        s += sprinth32( self.val, 'last_op_rba' )
        s += sprinth32( self.val, 'get_len' )
        s += sprinth32( self.val, 'put_len' )
        s += sprinth32( self.val, 'num_recs' )
        s += sprinth32( self.val, 'key_len' )
        s += sprinth32( self.val, 'key_pos' )
        s += sprinth32( self.val, 'fdbk_rsn' )
        s += sprinth32( self.val, 'curr_rba' )
        s += sprinth32( self.val, 'repos_rba' )
        s += sprinth32( self.val, 'srch_key_ptrnum' )
        s += sprinth32( self.val, 'srch_key_len' )
        s += sprinth32( self.val, 'buf_stg' )
        s += sprinth8( self.val, 'vsam_type' )
        s += sprinth8( self.val, 'prev_req' )
        s += sprinth32( self.val, 'flags' )
        s += sprinth32( self.val, 'curr_rrn' )
        s += sprinth32( self.val, 'last_op_key' )
        s += sprinth32( self.val, 'srch_key_rrn' )
        s += sprinth32( self.val, 'num_del' )
        s += sprinth32( self.val, 'num_ins' )
        s += sprinth64( self.val, 'xendrba' )

        s += '}'

        return s


class LPEFCOprinter:
    """Pretty print a 'LPEFCO'"""

    def __init__(self, val):
        self.val = val

    def to_string(self):
        s = '{\n'

        s += sprinthp32( self.val, 'self', "" )
        s += sprinth32( self.val, 'chain' )
        s += sprinth32( self.val, 'ancestor' )
        s += sprinth32( self.val, 'inv_stmt_meth' )
        s += sprinth32( self.val, 'stmt_err_meth' )
        s += sprinth32( self.val, 'diagnose_meth' )
        s += sprinth32( self.val, 'done_meth' )
        s += sprinth32( self.val, 'open_meth' )
        s += sprinth32( self.val, 'close_meth' )
        s += sprinth32( self.val, 'control_meth' )
        s += sprinth32( self.val, 'locate_meth' )
        s += sprinth32( self.val, 'write_meth' )
        s += sprinth32( self.val, 'rewrite_meth' )
        s += sprinth32( self.val, 'delete_meth' )
        s += sprinth32( self.val, 'read_meth' )
        s += sprinth32( self.val, 'unlock_meth' )
        s += sprinth32( self.val, 'wait_meth' )
        s += sprinth32( self.val, 'put_meth' )
        s += sprinth32( self.val, 'get_meth' )
        s += sprinth32( self.val, 'flush_meth' )
        s += sprinth32( self.val, 'finduse_meth' )
        s += sprinth32( self.val, 'settype_meth' )
        s += sprinth32( self.val, 'qrytype_meth' )
        s += sprinth32( self.val, 'pathname' )
        s += sprinth8( self.val, 'ref_count' )
        s += sprinth32( self.val, 'init_pfo' )
        s += sprinth32( self.val, 'init_pfo_anc' )
        s += sprinth32( self.val, 'validity' )
        s += sprinth32( self.val, 'required' )
        s += sprinth32( self.val, 'attrs' )
#   python a = fop( i32r("($arg0)->attrs") )
#   python print   ( "   attrs = " + a + "," )
        s += sprinthp32( self.val, 'pfo', "(LPEPFO*)" )
        s += sprinth32( self.val, 'ehb' )
        s += sprinth32( self.val, 'length' )
        s += sprinthp32( self.val, 'dcb_acb', "" )
        s += sprinth32( self.val, 'io_buf' )
        s += sprinth32( self.val, 'blksize' )
        s += sprinth32( self.val, 'blkxfer' )
        s += sprinth32( self.val, 'buf_obj' )
        s += sprinth32( self.val, 'buf_left' )
        s += sprinth32( self.val, 'prior_rec_l' )
        s += sprinth32( self.val, 'recsize' )
        s += sprinth32( self.val, 'bufsize' )
        s += sprinth32( self.val, 'big_io_buf' )
        s += sprinth32( self.val, 'dcbe' )
        s += sprinth8( self.val, 'err_type' )
        s += sprinth8( self.val, 'err_code' )
        s += sprinth32( self.val, 'environ' )
        s += sprinth32( self.val, 'platform' )
        s += sprinth32( self.val, 'flags' )
        s += sprinth32( self.val, 'retry' )
        s += sprinth32( self.val, 'delay' )
        s += sprinth32( self.val, 'norm_buf' )
        s += sprinth32( self.val, 'plwa' )
        s += sprinth32( self.val, 'xmit' )
        s += sprinth32( self.val, 'next_byte' )
        s += sprinth32( self.val, 'copy_byte' )
        s += sprinth32( self.val, 'copy_pfo' )
        s += sprinth32( self.val, 'scb' )
        s += sprinth32( self.val, 'tabtab' )
        s += sprinth32( self.val, 'reccnt' )
        s += sprinth32( self.val, 'bytesinto' )
        s += sprinth32( self.val, 'bufleftnorm' )
        s += sprinth32( self.val, 'bytesintonorm' )
        s += sprinth32( self.val, 'pagenobif' )
        s += sprinth32( self.val, 'countbif' )
        s += sprinth32( self.val, 'linenobif' )
        s += sprinth32( self.val, 'pagesize' )
        s += sprinth32( self.val, 'linesize' )
        s += sprinth32( self.val, 'sioflags' )
        s += sprinth32( self.val, 'normareasize' )
        s += sprinth32( self.val, 'tsonextbyte' )
        s += sprinth32( self.val, 'qsa' )
        s += sprinth32( self.val, 'dcb_len' )
        s += sprinth32( self.val, 'dcbe_len' )
        s += sprinth32( self.val, 'dd_access' )
        s += sprinth32( self.val, 'dd_blksize' )
        s += sprinth16( self.val, 'dd_lrecl' )
        s += sprinth16( self.val, 'dd_retcode' )
        s += sprints( self.val, 'dd_ddname' )
        s += sprinth8( self.val, 'dd_recfm' )
        s += sprinth16( self.val, 'dd_disp' )
        s += sprinth8( self.val, 'dd_flags' )
        s += sprints( self.val, 'dd_dsname' )
        s += sprints( self.val, 'dd_elname' )
        s += sprinth16( self.val, 'ds_blksize' )
        s += sprinth16( self.val, 'ds_lrecl' )
        s += sprinth16( self.val, 'ds_retcode' )
        s += sprinth8( self.val, 'ds_refcm' )

        s += '}'

        return s


class LPEDSCprinter:
    """Pretty print a 'LPEDSC'.  This is a pretty printer reimplementation of the lpe.gdb macro pdsc"""

    def __init__(self, val):
        self.val = val

    def to_string(self):
        s = '{\n'

        s += sprinth8( self.val, 'type' )
        s += sprinth8( self.val, 'datatype' )
        s += sprinth8( self.val, 'codepage' )
        s += sprinth8( self.val, 'flags' )
        s += sprinth32( self.val, 'length' )
        s += sprinth32( self.val, 'rank' )
        s += sprinth32( self.val, 'rvo' )

        s += '}'

        return s



## takes an LPEDED *
#define pded
#
#
#        s += sprinth8( self.val, 'type' )
#        s += sprinth8( self.val, 'flags' )
#        s += sprinth8( self.val, 'p' )
#        s += sprinth8( self.val, 's' )
#        s += sprinth8( self.val, 'pic' )
#        #s += sprinth8( self.val, 'pic.plen' )
#        #s += sprinth8( self.val, 'pic.dlen' )
#        #s += sprinth16( self.val, 'pic.flags' )
#        #s += sprints( self.val, 'pic.ctlstr' )
#

# Fixme: unlike pocb, this doesn't do the attrs/invalids decoding.
class LPEOCBprinter:
    """Pretty print a 'LPEOCB'.  This is a pretty printer reimplementation of the lpe.gdb macro pocb"""

    def __init__(self, val):
        self.val = val

    def to_string(self):
        s = '{\n'

        s += sprinth32( self.val, 'attrs' )
        #python a = fop( i32r("($arg0)->attrs") )
        #python print    ( "   attrs = " + a + "," )
        s += sprinth32( self.val, 'invalids' )
        #python a = fop( i32r("($arg0)->invalids") )
        #python print    ( "   invalids = " + a + "," )
        s += sprinth32( self.val, 'linesize' )
        s += sprinth32( self.val, 'pagesize' )
        s += sprinth32( self.val, 'title' )
        s += sprinth32( self.val, 'titledsc' )
        s += sprinth32( self.val, 'reserved' )

        s += '}'

        return s


class LPESCBprinter:
    """Pretty print a 'LPESCB'.  This is a pretty printer reimplementation of the lpe.gdb macro pscb"""

    def __init__(self, val):
        self.val = val

    def to_string(self):
        s = '{\n'

        s += sprinth32( self.val, 'skipline' )
        s += sprinthp32( self.val, 'src', "" )
        s += sprinthp32( self.val, 'srcded', "(LPEDED*)" )
        s += sprinthp32( self.val, 'srcdsc', "(LPEDSC*)" )
        s += sprinth16( self.val, 'cmd' )
        s += sprinth16( self.val, 'fmtctl' )
        s += sprinthp32( self.val, 'fco', "(LPEFCO*)" )
        s += sprinthp32( self.val, 'efse_tab', "" )
        s += sprinthp32( self.val, 'efse_use', "" )
        s += sprinthp32( self.val, 'fmttab', "(LPEFMTTAB*)" )

        s += '}'

        return s


# takes a LPEFED *
#define pfed
#
#
#        s += sprinth16( self.val, 'length' )
#        s += sprinth8( self.val, 'type' )
#        s += sprinth8( self.val, 'flags' )
#        s += sprinth8( self.val, 'AB.format' )
#        s += sprinth8( self.val, 'AB.flags' )
#        s += sprinth16( self.val, 'AB.length' )
#
#        s += sprinth8( self.val, 'X.format' )
#        s += sprinth8( self.val, 'X.flags' )
#        s += sprinth16( self.val, 'X.count' )
#
#        s += sprinth8( self.val, 'EF.format' )
#        s += sprinth8( self.val, 'EF.flags' )
#        s += sprinth16( self.val, 'EF.width' )
#        s += sprinth8( self.val, 'EF.precision' )
#        s += sprinth8( self.val, 'EF.scale' )
#
#        s += sprinth8( self.val, 'COL.format' )
#        s += sprinth8( self.val, 'COL.flags' )
#        s += sprinth16( self.val, 'COL.position' )


# Fixme: implement the declared, invalids decoding that the macro had.
class LPEPFOprinter:
    """Pretty print a 'LPEPFO'.  This is a pretty printer reimplementation of the lpe.gdb macro ppfo"""

    def __init__(self, val):
        self.val = val

    def to_string(self):
        s = '{\n'

        s += sprinthp32( self.val, 'anchor', "" )

        s += sprinth32( self.val, 'declared' )
        #python a = fop( i32r("($arg0)->declared") )
        #python print    ( "   declared = " + a + "," )

        s += sprinth32( self.val, 'invalids' )
        #python a = fop( i32r("($arg0)->invalids") )
        #python print    ( "   invalids = " + a + "," )

        s += sprinthp32( self.val, 'nameptr', "(LPEDDNAME*)" )
        s += sprinthp32( self.val, 'envptr', "(LPEENV*)" )

        s += '}'

        return s



class LPEENVprinter:
    """Pretty print a 'LPEENV'.  This is a pretty printer reimplementation of the lpe.gdb macro penv"""

    def __init__(self, val):
        self.val = val

    def to_string(self):
        s = '{\n'

        s += sprinth32( self.val, 'flags1' )
        #s += sprinth8( self.val, 'spare0' )
        s += sprinth8( self.val, 'recfm' )
        #s += sprinth16( self.val, 'spare2' )
        s += sprinth16( self.val, 'flags2' )
        s += sprinth32( self.val, 'count' )

        s += '}'

        return s



class LPERCBprinter:
    """Pretty print a 'LPERCB'.  This is a pretty printer reimplementation of the lpe.gdb macro pRcb"""

    def __init__(self, val):
        self.val = val

    def to_string(self):
        s = '{\n'

        s += sprinth8( self.val, 'length' )
        s += sprinth16( self.val, 'flag1' )
        s += sprinth16( self.val, 'flag2' )
        s += sprinthp32( self.val, 'rbd', "(LPERBD*)" )
        s += sprinthp32( self.val, 'kbd', "(LPEKBD*)" )

        s += '}'

        return s



class LPERBDprinter:
    """Pretty print a 'LPERBD'.  This is a pretty printer reimplementation of the lpe.gdb macro prbd"""

    def __init__(self, val):
        self.val = val

    def to_string(self):
        s = '{\n'

        s += sprinthp32( self.val, 'buf', "(char *)" )
        s += sprinth8( self.val, 'type' )
        s += sprinth8( self.val, 'flags' )
        s += sprinth16( self.val, 'fill' )
        s += sprinth32( self.val, 'length' )

        s += '}'

        return s


class LPEKBDprinter:
    """Pretty print a 'LPEKBD'.  This is a pretty printer reimplementation of the lpe.gdb macro pkbd"""

    def __init__(self, val):
        self.val = val

    def to_string(self):
        s = '{\n'

        s += sprinthp32( self.val, 'key', "(char *)" )
        s += sprinth8( self.val, 'flags' )
        s += sprinth8( self.val, 'codepage' )
        s += sprinth16( self.val, 'length' )

        s += '}'

        return s

