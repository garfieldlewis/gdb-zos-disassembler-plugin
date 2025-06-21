# @file   sdmpretty.py
# @author Peeter Joot <peeter.joot@lzlabs.com>
# @brief  pretty printer for internal SDM types
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
#   Load with:
#
#   (gdb) source /opt/lzlabs/debug/gdb/sdmpretty.py
#
#   Once done, any defined pretty printers will be loaded (currently only FIB is supported)
#
# @section Source
#
#   Information in this file is original.
#
import sys
import gdb.printing

if sys.path[0] != '/opt/lzlabs/debug/gdb':
    sys.path.insert( 0, '/opt/lzlabs/debug/gdb' )

from pretty.helper import *
from pretty.lce import *
from pretty.lpe import *
from pretty.rdb import *
from pretty.zccb import *

def SDMbuild_pretty_printer():
    pp = gdb.printing.RegexpCollectionPrettyPrinter(
        "SDM")
    # Note: it appears the the regex pattern must be lower case.

    # lz_lce:
    pp.add_printer('FIB', '^fib$', FIBprinter)
    pp.add_printer('IGZXDSP_PARM', '^igzxdsp_parm$', IGZXDSP_PARMprinter)
    pp.add_printer('IGZXDSP_PARG', '^igzxdsp_parg$', IGZXDSP_PARGprinter)
    pp.add_printer('FCB', '^fcb$', FCBprinter)
    pp.add_printer('KEYAREA', '^keyarea$', KEYAREAprinter)

    # lz_lpe:
    pp.add_printer('LPEDDNAME', '^lpeddname$', LPEDDNAMEprinter)
    pp.add_printer('LPEFCE', '^lpefce$', LPEFCEprinter)
    pp.add_printer('LPEFCO', '^lpefco$', LPEFCOprinter)
    pp.add_printer('LPEDSC', '^lpedsc$', LPEDSCprinter)
    pp.add_printer('LPEOCB', '^lpeocb$', LPEOCBprinter)
    pp.add_printer('LPESCB', '^lpescb$', LPESCBprinter)
    pp.add_printer('LPEPFO', '^lpepfo$', LPEPFOprinter)
    pp.add_printer('LPEENV', '^lpeenv$', LPEENVprinter)
    pp.add_printer('LPERCB', '^lpercb$', LPERCBprinter)
    pp.add_printer('LPERBD', '^lperbd$', LPERBDprinter)
    pp.add_printer('LPEKBD', '^lpekbd$', LPEKBDprinter)

    # zccb.h:
    pp.add_printer('RPL', '^rpl$', RPLprinter)
    pp.add_printer('DCB', '^DCB$', DCBprinter)
    pp.add_printer('ACB', '^acb$', ACBprinter)

    # lz_rdb
    pp.add_printer('DB2_SQLVAR', '^db2_sqlvar$', DB2_SQLVARprinter)
    pp.add_printer('DB2_SQLDA', '^db2_sqlda$', DB2_SQLDAprinter)
    pp.add_printer('DB2_RDI', '^db2_rdi$', DB2_RDIprinter)

    return pp

gdb.printing.register_pretty_printer(
    gdb.current_objfile(),
    SDMbuild_pretty_printer())
