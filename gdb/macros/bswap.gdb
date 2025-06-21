# @file   bswap.gdb
# @author Peeter Joot <peeter.joot@lzlabs.com>
# @brief  Byte swapping macros that call some underlying python functions.
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
#   Byte swapping, and mainstor relocation stuff.
#   
# @section Source
#   
#   Information in this file is original.
#
define bswap16
   python print swap16( gdb.parse_and_eval( "$arg0" ) )
end

define bswap32
   python print swap32( gdb.parse_and_eval( "$arg0" ) )
end

define bswap64
   python print swap64( gdb.parse_and_eval( "$arg0" ) )
end

define bswap16x
   python print "0x%02X" % swap16( gdb.parse_and_eval( "$arg0" ) )
end

define bswap32x
   python print "0x%04X" % swap32( gdb.parse_and_eval( "$arg0" ) )
end

define bswap64x
   python print "0x%016X" % swap64( gdb.parse_and_eval( "$arg0" ) )
end


#define ptr32
#  if $argc == 1
#    print /x (((((unsigned)($arg0) & 0xff000000) >> 24) | (((unsigned)($arg0) & 0x00ff0000) >>  8) | (((unsigned)($arg0) & 0x0000ff00) <<  8) | (((unsigned)($arg0) & 0x000000ff) << 24)) & 0x7fffffff) + (unsigned long)regs->mainstor
#  end
#  if $argc == 2
#    print /x (((((unsigned)($arg0) & 0xff000000) >> 24) | (((unsigned)($arg0) & 0x00ff0000) >>  8) | (((unsigned)($arg0) & 0x0000ff00) <<  8) | (((unsigned)($arg0) & 0x000000ff) << 24)) & 0x7fffffff) + (unsigned long)($arg1)
#  end
#end

define ptr32
   #if $argc == 1
      python print VadrToPtr($arg0)
   #end
   #if $argc == 2
   #   python print "(" + $arg1 + " *)" + VadrToPtr($arg0)
   #end
end
