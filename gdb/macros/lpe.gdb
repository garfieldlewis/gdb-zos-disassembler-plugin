# @file   lpe.gdb
# @author Peeter Joot <peeter.joot@lzlabs.com>
# @brief  Various macros to manually pretty-print internal SDM structures.
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
#   HWORD, FWORD and other decoding of RDB, LPE and LCE data structures.
#
# @section Source
#
#   Information in this file is original.
#

# refresh manually in debugger with:
#
# source /opt/lzlabs/debug/gdb/macros/lpe.gdb
source /opt/lzlabs/debug/gdb/lpe/lpe.py

# some vim regex's to convert structure field-name pairs into pretty-print lines:
#
# ,/^end/ s/DWORD *\(.*\)/python printh64 ( "   ", "\1", "($arg0)->\1", "," )/
# ,/^end/ s/FWORD *\(.*\)/python printh32 ( "   ", "\1", "($arg0)->\1", "," )/
# ,/^end/ s/HWORD *\(.*\)/python printh16 ( "   ", "\1", "($arg0)->\1", "," )/
# ,/^end/ s/AL3 *\(.*\)/python printh24 ( "   ", "\1", "($arg0)->\1", "," )/
# ,/^end/ s/BYTE *\(.*\)/python printh   ( "   ", "\1", "($arg0)->\1", "," )/

# Then to translate to pretty printer style:
#
# %s/^ *python printh *( *"   ", "\([^"]\+\).*/        s += sprinth8( self.val, '\1' )/
# %s/^ *python printhp32 *( *"   ",.*"..arg0.->\([^"]\+\)", *\("[^"]*"\).*/        s += sprinthp32( self.val, '\1', \2 )/
# %s/^ *python printh\([0-9]*\) *( *"   ", "\([^"]\+\).*/        s += sprinth\1( self.val, '\2' )/

# takes an LPEFOO *
#define pfoo
#   python print    ( "{" )
#   python print    ( "}" )
#end

# takes an LPERCB *
define pRcb
   python print    ( "{" )
   python printh   ( "   ", "length", "($arg0)->length", "," )
   python printh16 ( "   ", "flag1", "($arg0)->flag1", "," )
   python printh16 ( "   ", "flag2", "($arg0)->flag2", "," )
   python printhp32( "   ", "rbd", "($arg0)->rbd", "(LPERBD*)", "," )
   python printhp32( "   ", "kbd", "($arg0)->kbd", "(LPEKBD*)", "," )
   python print    ( "}" )
end

# takes an RPL *
define pRpl
   python print    ( "{" )

   #BYTE resv000[12]
   #python printh32 ( "   ", "fdbk", "($arg0)->fdbk", "," )
   python printh   ( "   ", "fdbk[0]", "($arg0)->fdbk[0]", "," )
   python printh   ( "   ", "fdbk[1]", "($arg0)->fdbk[1]", "," )
   python printh   ( "   ", "fdbk[2]", "($arg0)->fdbk[2]", "," )
   python printh   ( "   ", "fdbk[3]", "($arg0)->fdbk[3]", "," )
   python printh16 ( "   ", "keylen", "($arg0)->keylen", "," )
   #BYTE resv012[6]
   python printh32 ( "   ", "acb", "($arg0)->acb", "," )
   #BYTE resv01c[4]
   python printh32 ( "   ", "area", "($arg0)->area", "," )
   python printh32 ( "   ", "arg", "($arg0)->arg", "," )
   python printh   ( "   ", "optcd1", "($arg0)->optcd1", "," )
   python printh   ( "   ", "optcd2", "($arg0)->optcd2", "," )
   python printh   ( "   ", "optcd3", "($arg0)->optcd3", "," )
   python printh   ( "   ", "optcd4", "($arg0)->optcd4", "," )
   python printh32 ( "   ", "next", "($arg0)->next", "," )
   python printh32 ( "   ", "reclen", "($arg0)->reclen", "," )
   python printh32 ( "   ", "arealen", "($arg0)->arealen", "," )
   #BYTE resv038[14]
   python printh16 ( "   ", "msglen", "($arg0)->msglen", "," )
   python printh32 ( "   ", "msgarea", "($arg0)->msgarea", "," )

   python print    ( "}" )
end

# takes a (lce) KEYAREA *
define pKeyarea
   python print    ( "{" )
   python printh   ( "   ", "flag00", "($arg0)->flag00", "," )
   python printh   ( "   ", "keylen", "($arg0)->keylen", "," )
   python printh32 ( "   ", "keyrcon", "($arg0)->keyrcon", "," )
   python print    ( "}" )
end

define relocRdi
   print (DB2_RDI *)((long)$arg0 + psRegs->mainstor)
   #print (DB2_RDI *)((long)$arg0 + rc_pli_envp->base_mainstor)
end

# takes a DB2_SQLVAR *
define pSqlvar
   python print    ( "{" )

   python printh16 ( "   ", "hDATA_TYPE", "(HWORD *)(&($arg0)->sqlvar.sqlvar_base.hDATA_TYPE)", "," )
   python printh16 ( "   ", "hDATA_LENGTH", "(HWORD *)(&($arg0)->sqlvar.sqlvar_base.hDATA_LENGTH)", "," )
   python printhp32 ( "   ", "VpvDATA_FIELD", "(FWORD *)(&($arg0)->sqlvar.sqlvar_base.VpvDATA_FIELD)", "", "," )
   python printhp32 ( "   ", "VpvNULL_FIELD", "(FWORD *)(&($arg0)->sqlvar.sqlvar_base.VpvNULL_FIELD)", "(short *)", "," )
   python printh16 ( "   ", "hCOL_NAME_LEN", "(HWORD *)(&($arg0)->sqlvar.sqlvar_base.hCOL_NAME_LEN)", "," )
   python prints   ( "   ", "aeCOL_NAME", "($arg0)->sqlvar.sqlvar_base.aeCOL_NAME", "," )

   python print    ( "}" )
end

# takes an DB2_SQLDA *
define pSqlda
   python print    ( "{" )

   x/5b ($arg0)->aeEYE_CATCHER
   python printh   ( "   ", "eCCSID_OVERRIDE", "($arg0)->eCCSID_OVERRIDE", "," )
   python printh   ( "   ", "eSQLVAR_COL_NUM", "($arg0)->eSQLVAR_COL_NUM", "," )
   #python printh   ( "   ", "eUNUSED", "($arg0)->eUNUSED", "," )
   python printh32 ( "   ", "iSQLDA_LENGTH", "(FWORD *)(&($arg0)->iSQLDA_LENGTH)", "," )
   python printh16 ( "   ", "hSQLVAR_COUNT", "(HWORD *)(&($arg0)->hSQLVAR_COUNT)", "," )
   python printh16 ( "   ", "hHOST_VARS", "(HWORD *)(&($arg0)->hHOST_VARS)", "," )
   p "asSQLVARS = "
   p /x (DB2_SQLVAR*)(&($arg0)->asSQLVARS[0])

   python print    ( "}" )
end

# takes an DB2_RDI *
define pRdi
   python print    ( "{" )

   python printh16 ( "   ", "hRDI_LENGTH", "(HWORD *)(&($arg0)->hRDI_LENGTH)", "," )
   python printh   ( "   ", "abRDI_FLAG_BYTES[0]", "($arg0)->abRDI_FLAG_BYTES[0]", "," )
   python printh   ( "   ", "abRDI_FLAG_BYTES[1]", "($arg0)->abRDI_FLAG_BYTES[1]", "," )

   python printh16 ( "   ", "hRDI_CURSOR_TYPE", "(HWORD *)(&($arg0)->hRDI_CURSOR_TYPE)", "," )

   #BYTE     aeRDI_PROGRAM_NAME[8]
   p "aeRDI_PROGRAM_NAME = "
   p (char *)($arg0)->aeRDI_PROGRAM_NAME
   x/8b ($arg0)->aeRDI_PROGRAM_NAME

   #BYTE     abRDI_PRECOMP_TIMESTAMP[8]
   p "abRDI_PRECOMP_TIMESTAMP = "
   p (char *)($arg0)->abRDI_PRECOMP_TIMESTAMP
   x/8b ($arg0)->abRDI_PRECOMP_TIMESTAMP

   python printh16 ( "   ", "hRDI_SECTION", "(HWORD *)(&($arg0)->hRDI_SECTION)", "," )
   python printhp32 ( "   ", "VpvRDI_SQLCA", "(FWORD *)(&($arg0)->VpvRDI_SQLCA)", "(DB2_SQLCA*)", "," )
   python printhp32 ( "   ", "VpvRDI_INPUT_HOST_VARS", "(FWORD *)(&($arg0)->VpvRDI_INPUT_HOST_VARS)", "(DB2_SQLDA*)", "," )
   python printhp32 ( "   ", "VpvRDI_OUTPUT_HOST_VARS", "(FWORD *)(&($arg0)->VpvRDI_OUTPUT_HOST_VARS)", "(DB2_SQLDA*)", "," )
   python printh16 ( "   ", "hRDI_CCSID_TO_USE", "(HWORD *)(&($arg0)->hRDI_CCSID_TO_USE)", "," )
   python printh16 ( "   ", "hRDI_STMT_TYPE", "(HWORD *)(&($arg0)->hRDI_STMT_TYPE)", "," )
   python printh32 ( "   ", "iRDI_STMT_NUMBER", "(FWORD *)(&($arg0)->iRDI_STMT_NUMBER)", "," )
   python printh   ( "   ", "bRDI_ONE_LAST_FLAG", "($arg0)->bRDI_ONE_LAST_FLAG", "," )
   #BYTE     acRDI_DONOTCAREABOUTTHIS[19]

   python print    ( "}" )
end

# takes an FIB *
define pfib
   python print    ( "{" )

   python prints   ( "   ", "eyecatch", "($arg0)->eyecatch", "," )
   python printh   ( "   ", "relfib", "($arg0)->relfib", "," )
   python printh   ( "   ", "totfib", "($arg0)->totfib", "," )
   python prints   ( "   ", "ddname", "($arg0)->ddname", "," )
   #python printh   ( "   ", "resv0E", "($arg0)->resv0E", "," )
   python printh   ( "   ", "ftype", "($arg0)->ftype", "," )
   python printh   ( "   ", "access", "($arg0)->access", "," )

   #python a = fibaccess( gdb.parse_and_eval("(unsigned int)(unsigned char)(($arg0)->access)") )
   #python print    ( "   access = " + a + "," )

   #python printh   ( "   ", "resv11", "($arg0)->resv11", "," )
   python printh   ( "   ", "flag12", "($arg0)->flag12", "," )
   python printh   ( "   ", "flag13", "($arg0)->flag13", "," )
   python printh   ( "   ", "flag14", "($arg0)->flag14", "," )
   python printh   ( "   ", "flag15", "($arg0)->flag15", "," )
   python printh   ( "   ", "recfm", "($arg0)->recfm", "," )
   #python printh   ( "   ", "resv17", "($arg0)->resv17", "," )
   python printh32 ( "   ", "blksize", "($arg0)->blksize", "," )
   python printh32 ( "   ", "lrecl", "($arg0)->lrecl", "," )
   #python printh   ( "   ", "resv20", "($arg0)->resv20", "," )
   #python printh   ( "   ", "resv21", "($arg0)->resv21", "," )
   python printh   ( "   ", "bufno", "($arg0)->bufno", "," )
   python printh   ( "   ", "flag23", "($arg0)->flag23", "," )
   python printh   ( "   ", "flag24", "($arg0)->flag24", "," )
   #python printh   ( "   ", "resv25", "($arg0)->resv25", "," )
   #python printh   ( "   ", "resv26", "($arg0)->resv26", "," )
   python printh   ( "   ", "numkey", "($arg0)->numkey", "," )
   #python printh32 ( "   ", "resv28", "($arg0)->resv28", "," )
   #python printh32 ( "   ", "resv2C", "($arg0)->resv2C", "," )
   #python printh   ( "   ", "resv30", "($arg0)->resv30", "," )
   #python printh   ( "   ", "resv31", "($arg0)->resv31", "," )
   #python printh   ( "   ", "resv32", "($arg0)->resv32", "," )
   #python printh   ( "   ", "resv33", "($arg0)->resv33", "," )
   #python printh32 ( "   ", "resv34", "($arg0)->resv34", "," )
   python printh32 ( "   ", "blf", "($arg0)->blf", "," )
   python printh32 ( "   ", "blw", "($arg0)->blw", "," )
   python printh32 ( "   ", "vfs", "($arg0)->vfs", "," )
   python printh32 ( "   ", "lctr", "($arg0)->lctr", "," )
   #python printh32 ( "   ", "resv48", "($arg0)->resv48", "," )
   #python printh32 ( "   ", "resv4C", "($arg0)->resv4C", "," )
   python printhp32 ( "   ", "keyarea", "(FWORD *)(($arg0)->keyarea)", "(KEYAREA *)", "," )
   #python printh32 ( "   ", "resv54", "($arg0)->resv54", "," )
   python printh32 ( "   ", "ldef", "($arg0)->ldef", "," )
   #python printh32 ( "   ", "resv5C", "($arg0)->resv5C", "," )
   #python printh32 ( "   ", "resv60", "($arg0)->resv60", "," )
   #python printh32 ( "   ", "resv64", "($arg0)->resv64", "," )
   #python printh32 ( "   ", "resv68", "($arg0)->resv68", "," )
   #python printh32 ( "   ", "resv6C", "($arg0)->resv6C", "," )
   #python printh32 ( "   ", "resv70", "($arg0)->resv70", "," )
   #python printh32 ( "   ", "resv74", "($arg0)->resv74", "," )
   #python printh32 ( "   ", "resv78", "($arg0)->resv78", "," )
   #python printh32 ( "   ", "resv7C", "($arg0)->resv7C", "," )
   #python printh16 ( "   ", "resv80", "($arg0)->resv80", "," )
   python prints   ( "   ", "fdname", "($arg0)->fdname", "," )

   python print ( "}" )
end

# takes an FCB *
define pfcb
   python print    ( "{" )

   python prints   ( "   ", "eyecatch",   "($arg0)->eyecatch", "," )
   python printh   ( "   ", "relfcb", "($arg0)->relfcb", "," )
   python printh   ( "   ", "totfcb", "($arg0)->totfcb", "," )
#   python printh   ( "   ", "resv06[46]", "($arg0)->resv06[46]", "," )
   python printh   ( "   ", "mode", "($arg0)->mode", "," )
   python printh   ( "   ", "open_flag", "($arg0)->open_flag", "," )
   #python printh   ( "   ", "resv036", "($arg0)->resv036", "," )
   python printh   ( "   ", "close_flag", "($arg0)->close_flag", "," )
   python printh   ( "   ", "mfsw", "($arg0)->mfsw", "," )
   python printh   ( "   ", "keynum", "($arg0)->keynum", "," )
   python printh   ( "   ", "keycmpln", "($arg0)->keycmpln", "," )

   #python printh   ( "   ", "resv03b", "($arg0)->resv03b", "," )
   #
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
#   python printh   ( "   ", "resv58[10]", "($arg0)->resv58[10]", "," )
   python printh   ( "   ", "blfoffid", "($arg0)->blfoffid", "," )
#   python printh   ( "   ", "blfoff[3]", "($arg0)->blfoff[3]", "," )
   python printh32 ( "   ", "blfrcon", "($arg0)->blfrcon", "," )
#   python printh   ( "   ", "resv66[2]", "($arg0)->resv66[2]", "," )
   python printh   ( "   ", "mode_opened", "($arg0)->mode_opened", "," )
#   python printh   ( "   ", "resv69[7]", "($arg0)->resv69[7]", "," )
   python printh   ( "   ", "end_of_page_flag", "($arg0)->end_of_page_flag", "," )
   python printh   ( "   ", "resv71", "($arg0)->resv71", "," )
   python printh   ( "   ", "resv72", "($arg0)->resv72", "," )
   python printh   ( "   ", "flag73", "($arg0)->flag73", "," )
   python printh   ( "   ", "flag74", "($arg0)->flag74", "," )
   python printh   ( "   ", "flag75", "($arg0)->flag75", "," )
   python printh   ( "   ", "flag76", "($arg0)->flag76", "," )
   python printh   ( "   ", "flag77", "($arg0)->flag77", "," )
   python printh32 ( "   ", "dcbrpl", "($arg0)->dcbrpl", "," )
#   python printh   ( "   ", "resv7C[12]", "($arg0)->resv7C[12]", "," )
#
#   Not interesting (always blank):
   #python prints   ( "   ", "progname",   "($arg0)->progname", "," )
   #python prints   ( "   ", "ddname",   "($arg0)->ddname", "," )
   #
   #
#   python printh   ( "   ", "resv98[8]", "($arg0)->resv98[8]", "," )
   python printh32 ( "   ", "rerun_counter", "($arg0)->rerun_counter", "," )
   python printhp32 ( "   ", "fib", "(FWORD *)(($arg0)->fib)", "(FIB *)", "," )
   python printh32 ( "   ", "nrecarea", "($arg0)->nrecarea", "," )
   #python printh32 ( "   ", "resvAC", "($arg0)->resvAC", "," )
   python printh   ( "   ", "flagB0", "($arg0)->flagB0", "," )
   python printh   ( "   ", "flagB1", "($arg0)->flagB1", "," )
   python printh   ( "   ", "flagB2", "($arg0)->flagB2", "," )
   python printh   ( "   ", "reason", "($arg0)->reason", "," )
   #python printh32 ( "   ", "resvB4", "($arg0)->resvB4", "," )
   #python printh32 ( "   ", "resvB8", "($arg0)->resvB8", "," )
   #python printh32 ( "   ", "resvBC", "($arg0)->resvBC", "," )
   #python printh32 ( "   ", "resvC0", "($arg0)->resvC0", "," )
   #python printh32 ( "   ", "resvC4", "($arg0)->resvC4", "," )
   python printh   ( "   ", "byte1", "($arg0)->byte1", "," )
   python printh   ( "   ", "rc", "($arg0)->rc", "," )
   python printh   ( "   ", "byteCA", "($arg0)->byteCA", "," )
   python printh   ( "   ", "errmgsw", "($arg0)->errmgsw", "," )
   #python printh32 ( "   ", "resvCC", "($arg0)->resvCC", "," )
   #python printh32 ( "   ", "resvD0", "($arg0)->resvD0", "," )
   #python printh32 ( "   ", "resvD4", "($arg0)->resvD4", "," )
   python printh32 ( "   ", "count", "($arg0)->count", "," )
   python printh32 ( "   ", "advance", "($arg0)->advance", "," )
   python printh32 ( "   ", "linage_is", "($arg0)->linage_is", "," )
   python printh32 ( "   ", "footing_at", "($arg0)->footing_at", "," )
   python printh32 ( "   ", "top_lines", "($arg0)->top_lines", "," )
   python printh32 ( "   ", "bottom_lines", "($arg0)->bottom_lines", "," )
   #python printh32 ( "   ", "resvF0", "($arg0)->resvF0", "," )
   #python printh32 ( "   ", "resvF4", "($arg0)->resvF4", "," )
   python printh   ( "   ", "advopt", "($arg0)->advopt", "," )
   python printh   ( "   ", "byteF9", "($arg0)->advchan", "," )
   #python printh   ( "   ", "resvFA", "($arg0)->resvFA", "," )
   #python printh   ( "   ", "resvFB", "($arg0)->resvFB", "," )
   python printh32 ( "   ", "mrecarea", "($arg0)->mrecarea", "," )
   #python printh32 ( "   ", "resv100", "($arg0)->resv100", "," )
   #python printh32 ( "   ", "resv104", "($arg0)->resv104", "," )
   #python printh32 ( "   ", "resv108", "($arg0)->resv108", "," )
   #python printh32 ( "   ", "resv10C", "($arg0)->resv10C", "," )
   #python printh32 ( "   ", "resv110", "($arg0)->resv110", "," )

   python print ( "}" )
end

# takes an IGZXDSP_PARM *
define pdispparm
   python print    ( "{" )
   python printh32 ( "   ", "numitem", "($arg0)->numitem", "," )
   python printh   ( "   ", "upon", "($arg0)->upon", "," )
   python printh   ( "   ", "flags", "($arg0)->flags", "," )
   python printh16 ( "   ", "codepage", "($arg0)->codepage", "," )
   python print    ( "}" )
end

# takes an IGZXDSP_PARG *
define pdispparg
   python print    ( "{" )
   python printh32 ( "   ", "item_adr", "($arg0)->item_adr", "," )
   python printh32 ( "   ", "item_type", "($arg0)->item_type", "," )
   python printh32 ( "   ", "item_len", "($arg0)->item_len", "," )
   python printh32 ( "   ", "item_digits", "($arg0)->item_digits", "," )
   python print    ( "}" )
end

# takes a DCB *
define pdcb
   python print    ( "{" )
   python printh32 ( "   ", "dcbe", "($arg0)->dcbe", "," )
   python printh   ( "   ", "kl", "($arg0)->kl", "," )
   python printh   ( "   ", "devt", "($arg0)->devt", "," )
   python printh16 ( "   ", "trbal", "($arg0)->trbal", "," )
   python printh32 ( "   ", "bufcb", "($arg0)->bufcb", "," )
   python printh   ( "   ", "bufno", "($arg0)->bufno", "," )
   python printh24 ( "   ", "bufca", "($arg0)->bufca", "," )
   python printh16 ( "   ", "bufl", "($arg0)->bufl", "," )
   python printh16 ( "   ", "dsorg", "($arg0)->dsorg", "," )
   python printh   ( "   ", "dsorg1", "($arg0)->dsorg1", "," )
   python printh   ( "   ", "dsorg2", "($arg0)->dsorg2", "," )
   python printh32 ( "   ", "iob", "($arg0)->iob", "," )
   python printh   ( "   ", "bftek", "($arg0)->bftek", "," )
   python printh24 ( "   ", "eoda", "($arg0)->eoda", "," )
   python printh32 ( "   ", "eod", "($arg0)->eod", "," )
   python printh   ( "   ", "recfm", "($arg0)->recfm", "," )
   python printh24 ( "   ", "exlsta", "($arg0)->exlsta", "," )
   python printh32 ( "   ", "exlst", "($arg0)->exlst", "," )
#   python printh   ( "   ", "ddname[8]", "($arg0)->ddname[8]", "," )
   python printh16 ( "   ", "tiotoff", "($arg0)->tiotoff", "," )
   python printh16 ( "   ", "macrf", "($arg0)->macrf", "," )
   python printh   ( "   ", "iflgs", "($arg0)->iflgs", "," )
   python printh24 ( "   ", "deba", "($arg0)->deba", "," )
   python printh32 ( "   ", "deb", "($arg0)->deb", "," )
   python printh   ( "   ", "oflg", "($arg0)->oflg", "," )
   python printh   ( "   ", "iflg", "($arg0)->iflg", "," )
   python printh16 ( "   ", "macr", "($arg0)->macr", "," )
   python printh   ( "   ", "macr1", "($arg0)->macr1", "," )
   python printh   ( "   ", "macr2", "($arg0)->macr2", "," )
   python printh   ( "   ", "oflgs", "($arg0)->oflgs", "," )
   python printh24 ( "   ", "iortna", "($arg0)->iortna", "," )
   python printh32 ( "   ", "iortn", "($arg0)->iortn", "," )
   python printh   ( "   ", "optcd", "($arg0)->optcd", "," )
   python printh24 ( "   ", "checka", "($arg0)->checka", "," )
   python printh32 ( "   ", "check", "($arg0)->check", "," )
   python printh   ( "   ", "iobl", "($arg0)->iobl", "," )
   python printh24 ( "   ", "syna", "($arg0)->syna", "," )
   python printh16 ( "   ", "blksi", "($arg0)->blksi", "," )
   python printh32 ( "   ", "recad", "($arg0)->recad", "," )
   python printh   ( "   ", "bufoff", "($arg0)->bufoff", "," )
   python printh16 ( "   ", "lrecl", "($arg0)->lrecl", "," )
   python printh   ( "   ", "eropt", "($arg0)->eropt", "," )
   python printh24 ( "   ", "notea", "($arg0)->notea", "," )
   python printh16 ( "   ", "precl", "($arg0)->precl", "," )
   python printh32 ( "   ", "eob", "($arg0)->eob", "," )
   python printh32 ( "   ", "note", "($arg0)->note", "," )
   python print ( "}" )
end

# takes an LPEDSC *
define pdsc
   python print    ( "{" )

   python printh   ( "   ", "type", "($arg0)->type", "," )
   python printh   ( "   ", "datatype", "($arg0)->datatype", "," )
   python printh   ( "   ", "codepage", "($arg0)->codepage", "," )
   python printh   ( "   ", "flags", "($arg0)->flags", "," )
   python printh32 ( "   ", "length", "($arg0)->length", "," )
   python printh32 ( "   ", "rank", "($arg0)->rank", "," )
   python printh32 ( "   ", "rvo", "($arg0)->rvo", "," )

   python print    ( "}" )
end

# takes an LPEDED *
define pded
   python print    ( "{" )

   python printh   ( "   ", "type", "($arg0)->type", "," )
   python printh   ( "   ", "flags", "($arg0)->flags", "," )
   python printh   ( "   ", "p", "($arg0)->pic.p", "," )
   python printh   ( "   ", "s", "($arg0)->pic.s", "," )
   python printh   ( "   ", "pic.plen", "($arg0)->pic.plen", "," )
   python printh   ( "   ", "pic.dlen", "($arg0)->pic.dlen", "," )
   python printh16 ( "   ", "pic.flags", "($arg0)->pic.flags", "," )
   python printh   ( "   ", "pic.ctlstr[0]", "($arg0)->pic.ctlstr[0]", "," )

   python print    ( "}" )
end


# takes a LPEOCB *
define pocb
   python print    ( "{" )

   python a = fop( i32r("($arg0)->attrs") )
   python print    ( "   attrs = " + a + "," )

   python a = fop( i32r("($arg0)->invalids") )
   python print    ( "   invalids = " + a + "," )

   python printh32 ( "   ", "linesize", "($arg0)->linesize", "," )
   python printh32 ( "   ", "pagesize", "($arg0)->pagesize", "," )
   python printh32 ( "   ", "title", "($arg0)->title", "," )
   python printh32 ( "   ", "titledsc", "($arg0)->titledsc", "," )
   python printh32 ( "   ", "reserved", "($arg0)->reserved", "," )
   python print    ( "}" )
end

# takes a ACB *
define pacb
   python print    ( "{" )
   python printh32 ( "   ", "ambl", "($arg0)->ambl", "," )
   python printh32 ( "   ", "rpl", "($arg0)->rpl", "," )
   python printh   ( "   ", "macr1", "($arg0)->macr1", "," )
   python printh   ( "   ", "macr2", "($arg0)->macr2", "," )
   python printh   ( "   ", "bstrno", "($arg0)->bstrno", "," )
   python printh   ( "   ", "strno", "($arg0)->strno", "," )
   python printh16 ( "   ", "bufnd", "($arg0)->bufnd", "," )
   python printh16 ( "   ", "bufni", "($arg0)->bufni", "," )
   python printh   ( "   ", "macr3", "($arg0)->macr3", "," )
   python printh   ( "   ", "shrp", "($arg0)->shrp", "," )
   python printh   ( "   ", "macr4", "($arg0)->macr4", "," )
   python printh   ( "   ", "recfm", "($arg0)->recfm", "," )
   python printh   ( "   ", "cctyp", "($arg0)->cctyp", "," )
   python printh   ( "   ", "rls", "($arg0)->rls", "," )
   python printh   ( "   ", "dsorg1", "($arg0)->dsorg1", "," )
   python printh   ( "   ", "dsorg2", "($arg0)->dsorg2", "," )
   python printh32 ( "   ", "passwd", "($arg0)->passwd", "," )
   python printh32 ( "   ", "exlst", "($arg0)->exlst", "," )
   #python printh   ( "   ", "ddname[8]", "($arg0)->ddname[8]", "," )
   python printh16 ( "   ", "tiotoff", "($arg0)->tiotoff", "," )
   python printh16 ( "   ", "infl", "($arg0)->infl", "," )
   python printh   ( "   ", "iflgs", "($arg0)->iflgs", "," )
   python printh24 ( "   ", "deba", "($arg0)->deba", "," )
   python printh32 ( "   ", "deb", "($arg0)->deb", "," )
   python printh   ( "   ", "oflgs", "($arg0)->oflgs", "," )
   python printh   ( "   ", "erflg", "($arg0)->erflg", "," )
   python printh16 ( "   ", "inflg", "($arg0)->inflg", "," )
   python printh32 ( "   ", "bufsp", "($arg0)->bufsp", "," )
   python printh16 ( "   ", "blksi", "($arg0)->blksi", "," )
   python printh16 ( "   ", "recsiz", "($arg0)->recsiz", "," )
   python printh32 ( "   ", "uwork", "($arg0)->uwork", "," )
   python printh32 ( "   ", "cbwork", "($arg0)->cbwork", "," )
   python printh32 ( "   ", "appladdr", "($arg0)->appladdr", "," )
   python print    ( "}" )
end

# takes a LPESCB *
define pscb
   python print    ( "{" )
   python printh32 ( "   ", "skipline", "($arg0)->skipline", "," )
   python printhp32 ( "   ", "src", "($arg0)->src", "", "," )
   python printhp32( "   ", "srcded", "($arg0)->srcded", "(LPEDED*)" , "," )
   python printhp32( "   ", "srcdsc", "($arg0)->srcdsc", "(LPEDSC*)" , "," )
   python printh16 ( "   ", "cmd", "($arg0)->cmd", "," )
   python printh16 ( "   ", "fmtctl", "($arg0)->fmtctl", "," )
   python printhp32( "   ", "fco", "($arg0)->fco", "(LPEFCO*)", "," )
   python printhp32 ( "   ", "efse_tab", "($arg0)->efse_tab", "", "," )
   python printhp32 ( "   ", "efse_use", "($arg0)->efse_use", "", "," )
   python printhp32( "   ", "fmttab", "($arg0)->fmttab", "(LPEFMTTAB*)", "," )
   python print    ( "}" )
end

# takes a LPEFED *
define pfed
   python print   ( "{" )

   python printh16( "   ", "length", "($arg0)->length", "," )
   python printh  ( "   ", "type", "($arg0)->type", "," )
   python printh  ( "   ", "flags", "($arg0)->flags", "," )
   python printh  ( "   ", "AB.format", "($arg0)->AB.format", "," )
   python printh  ( "   ", "AB.flags", "($arg0)->AB.flags", "," )
   python printh16( "   ", "AB.length", "($arg0)->AB.length", "," )

   python printh   ( "   ", "X.format", "($arg0)->X.format", "," )
   python printh   ( "   ", "X.flags", "($arg0)->X.flags", "," )
   python printh16 ( "   ", "X.count", "($arg0)->X.count", "," )

   python printh   ( "   ", "EF.format", "($arg0)->EF.format", "," )
   python printh   ( "   ", "EF.flags", "($arg0)->EF.flags", "," )
   python printh16 ( "   ", "EF.width", "($arg0)->EF.width", "," )
   python printh   ( "   ", "EF.precision", "($arg0)->EF.precision", "," )
   python printh   ( "   ", "EF.scale", "($arg0)->EF.scale", "," )

   python printh   ( "   ", "COL.format", "($arg0)->COL.format", "," )
   python printh   ( "   ", "COL.flags", "($arg0)->COL.flags", "," )
   python printh16 ( "   ", "COL.position", "($arg0)->COL.position", "," )

   python print   ( "}" )
end

# takes a LPEPFO *
define ppfo
   python print    ( "{" )
   python printhp32 ( "   ", "anchor", "($arg0)->anchor", "", "," )
   python a = fop( i32r("($arg0)->declared") )
   python print    ( "   declared = " + a + "," )
   python a = fop( i32r("($arg0)->invalids") )
   python print    ( "   invalids = " + a + "," )
   python printhp32( "   ", "nameptr", "($arg0)->nameptr", "(LPEDDNAME*)" , "," )
   python printhp32( "   ", "envptr", "($arg0)->envptr", "(LPEENV*)" , "," )
   python print    ( "}" )
end

# takes a LPEENV *
define penv
   python print   ( "{" )
   python printh32( "   ", "flags1", "($arg0)->flags1", "," )
   python printh  ( "   ", "spare0", "($arg0)->spare0", "," )
   python printh  ( "   ", "recfm", "($arg0)->recfm", "," )
   python printh16( "   ", "spare2", "($arg0)->spare2", "," )
   python printh16( "   ", "flags2", "($arg0)->flags2", "," )
   python printh32( "   ", "count", "($arg0)->count", "," )
   python print   ( "}" )
end

# takes a LPEFCO *
define pfco
   python print   ( "{" )
   python printhp32( "   ", "self",  "($arg0)->self", "", "," )
   python printh32( "   ", "chain", "($arg0)->chain", "," )
   python printh32( "   ", "ancestor", "($arg0)->ancestor", "," )
   python printh32( "   ", "inv_stmt_meth", "($arg0)->inv_stmt_meth", "," )
   python printh32( "   ", "stmt_err_meth", "($arg0)->stmt_err_meth", "," )
   python printh32( "   ", "diagnose_meth", "($arg0)->diagnose_meth", "," )
   python printh32( "   ", "done_meth", "($arg0)->done_meth", "," )
   python printh32( "   ", "open_meth", "($arg0)->open_meth", "," )
   python printh32( "   ", "close_meth", "($arg0)->close_meth", "," )
   python printh32( "   ", "control_meth", "($arg0)->control_meth", "," )
   python printh32( "   ", "locate_meth", "($arg0)->locate_meth", "," )
   python printh32( "   ", "write_meth", "($arg0)->write_meth", "," )
   python printh32( "   ", "rewrite_meth", "($arg0)->rewrite_meth", "," )
   python printh32( "   ", "delete_meth", "($arg0)->delete_meth", "," )
   python printh32( "   ", "read_meth", "($arg0)->read_meth", "," )
   python printh32( "   ", "unlock_meth", "($arg0)->unlock_meth", "," )
   python printh32( "   ", "wait_meth", "($arg0)->wait_meth", "," )
   python printh32( "   ", "put_meth", "($arg0)->put_meth", "," )
   python printh32( "   ", "get_meth", "($arg0)->get_meth", "," )
   python printh32( "   ", "flush_meth", "($arg0)->flush_meth", "," )
   python printh32( "   ", "finduse_meth", "($arg0)->finduse_meth", "," )
   python printh32( "   ", "settype_meth", "($arg0)->settype_meth", "," )
   python printh32( "   ", "qrytype_meth", "($arg0)->qrytype_meth", "," )
   python printh32( "   ", "pathname", "($arg0)->pathname", "," )
   python printh  ( "   ", "ref_count", "($arg0)->ref_count", "," )
   python printh32( "   ", "init_pfo", "($arg0)->init_pfo", "," )
   python printh32( "   ", "init_pfo_anc", "($arg0)->init_pfo_anc", "," )
   python printh32( "   ", "validity", "($arg0)->validity", "," )
   python printh32( "   ", "required", "($arg0)->required", "," )
   python a = fop( i32r("($arg0)->attrs") )
   python print   ( "   attrs = " + a + "," )
   python printhp32( "   ", "pfo", "($arg0)->pfo", "(LPEPFO*)" , "," )
   python printh32( "   ", "ehb", "($arg0)->ehb", "," )
   python printh32( "   ", "length", "($arg0)->length", "," )
   python printhp32( "   ", "dcb_acb", "($arg0)->dcb_acb", "", "," )
   python printh32( "   ", "io_buf", "($arg0)->io_buf", "," )
   python printh32( "   ", "blksize", "($arg0)->blksize", "," )
   python printh32( "   ", "blkxfer", "($arg0)->blkxfer", "," )
   python printh32( "   ", "buf_obj", "($arg0)->buf_obj", "," )
   python printh32( "   ", "buf_left", "($arg0)->buf_left", "," )
   python printh32( "   ", "prior_rec_l", "($arg0)->prior_rec_l", "," )
   python printh32( "   ", "recsize", "($arg0)->recsize", "," )
   python printh32( "   ", "bufsize", "($arg0)->bufsize", "," )
   python printh32( "   ", "big_io_buf", "($arg0)->big_io_buf", "," )
   python printh32( "   ", "dcbe", "($arg0)->dcbe", "," )
   python printh  ( "   ", "err_type", "($arg0)->err_type", "," )
   python printh  ( "   ", "err_code", "($arg0)->err_code", "," )
   python printh32( "   ", "environ", "($arg0)->environ", "," )
   python printh32( "   ", "platform", "($arg0)->platform", "," )
   python printh32( "   ", "flags", "($arg0)->flags", "," )
   python printh32( "   ", "retry", "($arg0)->retry", "," )
   python printh32( "   ", "delay", "($arg0)->delay", "," )
   python printh32( "   ", "norm_buf", "($arg0)->norm_buf", "," )
   python printh32( "   ", "plwa", "($arg0)->plwa", "," )
   python printh32( "   ", "xmit", "($arg0)->xmit", "," )
   python printh32( "   ", "next_byte", "($arg0)->next_byte", "," )
   python printh32( "   ", "copy_byte", "($arg0)->copy_byte", "," )
   python printh32( "   ", "copy_pfo", "($arg0)->copy_pfo", "," )
   python printh32( "   ", "scb", "($arg0)->scb", "," )
   python printh32( "   ", "tabtab", "($arg0)->tabtab", "," )
   python printh32( "   ", "reccnt", "($arg0)->reccnt", "," )
   python printh32( "   ", "bytesinto", "($arg0)->bytesinto", "," )
   python printh32( "   ", "bufleftnorm", "($arg0)->bufleftnorm", "," )
   python printh32( "   ", "bytesintonorm", "($arg0)->bytesintonorm", "," )
   python printh32( "   ", "pagenobif", "($arg0)->pagenobif", "," )
   python printh32( "   ", "countbif", "($arg0)->countbif", "," )
   python printh32( "   ", "linenobif", "($arg0)->linenobif", "," )
   python printh32( "   ", "pagesize", "($arg0)->pagesize", "," )
   python printh32( "   ", "linesize", "($arg0)->linesize", "," )
   python printh32( "   ", "sioflags", "($arg0)->sioflags", "," )
   python printh32( "   ", "normareasize", "($arg0)->normareasize", "," )
   python printh32( "   ", "tsonextbyte", "($arg0)->tsonextbyte", "," )
   python printh32( "   ", "qsa", "($arg0)->qsa", "," )
   python printh32( "   ", "dcb_len", "($arg0)->dcb_len", "," )
   python printh32( "   ", "dcbe_len", "($arg0)->dcbe_len", "," )
   python printh32( "   ", "dd_access", "($arg0)->dd_access", "," )
   python printh32( "   ", "dd_blksize", "($arg0)->dd_blksize", "," )
   python printh16( "   ", "dd_lrecl", "($arg0)->dd_lrecl", "," )
   python printh16( "   ", "dd_retcode", "($arg0)->dd_retcode", "," )
   p "dd_ddname = "
   p (char *)($arg0)->dd_ddname
   python printh  ( "   ", "dd_recfm", "($arg0)->dd_recfm", "," )
   python printh16( "   ", "dd_disp", "($arg0)->dd_disp", "," )
   python printh  ( "   ", "dd_flags", "($arg0)->dd_flags", "," )
#   python printh  ( "   ", "dd_dsname[44]", "($arg0)->dd_dsname[44]", "," )
#   python printh  ( "   ", "dd_elname[8]", "($arg0)->dd_elname[8]", "," )
   python printh16( "   ", "ds_blksize", "($arg0)->ds_blksize", "," )
   python printh16( "   ", "ds_lrecl", "($arg0)->ds_lrecl", "," )
   python printh16( "   ", "ds_retcode", "($arg0)->ds_retcode", "," )
   python printh  ( "   ", "ds_refcm", "($arg0)->ds_refcm", "," )
   python print   ( "}" )
end

define prbd
   python print     ( "{" )
   python printhp32 ( "   ", "buf", "($arg0)->buf", "(char *)", "," )
   python printh    ( "   ", "type",   "($arg0)->type",   "," )
   python printh    ( "   ", "flags",  "($arg0)->flags",  "," )
   python printh16  ( "   ", "fill",   "($arg0)->fill",   "," )
   python printh32  ( "   ", "length", "($arg0)->length", "," )
   python print     ( "}" )
end

define pkbd
   python print     ( "{" )
   python printhp32 ( "   ", "key", "($arg0)->key", "(char *)", "," )
   python printh    ( "   ", "flags", "($arg0)->flags", "," )
   python printh    ( "   ", "codepage", "($arg0)->codepage", "," )
   python printh16  ( "   ", "length", "($arg0)->length", "," )
   python print     ( "}" )
end

# LPEFCE
define pfce
   python printh32 ( "   ", "totstg", "($arg0)->totstg", "," )
   python printh32 ( "   ", "acb", "($arg0)->acb", "," )
   python printh32 ( "   ", "rd_rpl", "($arg0)->rd_rpl", "," )
   python printh32 ( "   ", "wr_rpl", "($arg0)->wr_rpl", "," )
   python printh32 ( "   ", "read", "($arg0)->read", "," )
   python printh32 ( "   ", "write", "($arg0)->write", "," )
   python printh32 ( "   ", "wr_recl", "($arg0)->wr_recl", "," )
   python printh32 ( "   ", "rd_recl", "($arg0)->rd_recl", "," )
   python printh32 ( "   ", "wr_buf", "($arg0)->wr_buf", "," )
   python printh32 ( "   ", "rd_buf", "($arg0)->rd_buf", "," )
   python printh32 ( "   ", "wr_arg", "($arg0)->wr_arg", "," )
   python printh32 ( "   ", "rd_arg", "($arg0)->rd_arg", "," )
   python printh32 ( "   ", "last_op_rba", "($arg0)->last_op_rba", "," )
   python printh32 ( "   ", "get_len", "($arg0)->get_len", "," )
   python printh32 ( "   ", "put_len", "($arg0)->put_len", "," )
   python printh32 ( "   ", "num_recs", "($arg0)->num_recs", "," )
   python printh32 ( "   ", "key_len", "($arg0)->key_len", "," )
   python printh32 ( "   ", "key_pos", "($arg0)->key_pos", "," )
   python printh32 ( "   ", "fdbk_rsn", "($arg0)->fdbk_rsn", "," )
   python printh32 ( "   ", "curr_rba", "($arg0)->curr_rba", "," )
   python printh32 ( "   ", "repos_rba", "($arg0)->repos_rba", "," )
   python printh32 ( "   ", "srch_key_ptrnum", "($arg0)->srch_key_ptrnum", "," )
   python printh32 ( "   ", "srch_key_len", "($arg0)->srch_key_len", "," )
   python printh32 ( "   ", "buf_stg", "($arg0)->buf_stg", "," )
   python printh   ( "   ", "vsam_type", "($arg0)->vsam_type", "," )
   python printh   ( "   ", "prev_req", "($arg0)->prev_req", "," )
   python printh32 ( "   ", "flags", "($arg0)->flags", "," )
   python printh32 ( "   ", "curr_rrn", "($arg0)->curr_rrn", "," )
   python printh32 ( "   ", "last_op_key", "($arg0)->last_op_key", "," )
   python printh32 ( "   ", "srch_key_rrn", "($arg0)->srch_key_rrn", "," )
   python printh32 ( "   ", "num_del", "($arg0)->num_del", "," )
   python printh32 ( "   ", "num_ins", "($arg0)->num_ins", "," )
   python printh64 ( "   ", "xendrba", "($arg0)->xendrba", "," )
end

# takes an LPEDDNAME *
define pddn
   python print    ( "{" )
   python printh16 ( "   ", "len", "($arg0)->length", "," )
   python prints   ( "   ", "n",   "($arg0)->n", "," )
   python print    ( "}" )
end

