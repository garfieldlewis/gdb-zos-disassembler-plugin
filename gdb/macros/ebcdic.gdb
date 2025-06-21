# @file   ebcdic.gdb
# @author Peeter Joot <peeter.joot@lzlabs.com>
# @brief  EBCDIC and ASCII charset switching macros
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
#   Load this file with:
#
#   (gdb) source /opt/lzlabs/debug/gdb/macros/ebcdic.gdb
#
#   To switch to EBCDIC char display use:
#
#   (gdb) ebc
#   (gdb) p '\xF0'
#
#   and to switch back to ASCII use:
#
#   (gdb) asc
#   (gdb) p '\x61'
#
# @section Source
#
#   Information in this file is original.
#

define ascii
   set target-charset ASCII
end

define ebc
   set target-charset EBCDIC-US
end
