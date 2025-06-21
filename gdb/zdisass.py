# @file	  zdisass.py
# @author Garfield A. Lewis <garfield.lewis@lzlabs.com>
# @brief  Implement a zOS disassembler plugin for the GDB debugger.
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
#   The documention for the instructions implemented in this code can all be
#   found publicly at the following location:
#
#   https://www.ibm.com/support/libraryserver/download/dz9zr006.pdf
#
# @section Source
#
#   Information in this file is original.
#
import sys
import os

# Add the current path to the system path so that the subsequent import will
# find my external libraries.
if sys.path[0] != '/opt/lzlabs/debug/gdb':
   sys.path.insert( 0, '/opt/lzlabs/debug/gdb' )

from apis.common import *
from apis.decoder import *
from apis.instructions import *
from apis.bswapreloc import *

class zdisass( gdb.Command ):
   """Disassemble a zOS instruction stream similar to the normal disass command.

   Examples:
   (gdb) zdisass regs->mainstor+regs->psw.ia.F
   (gdb) zdisass 0x7ffb40a2b41c,+150
   """

   def __init__( self ):
      super( zdisass, self ).__init__( "zdisass", gdb.COMMAND_USER )

   def invoke( self, arg, from_tty ):
      isSDMEnabled( )

      size = 64

      if len( arg ) == 0:
         raise gdb.GdbError( "zdisass <symbol|address[,size]]>" )

      args = arg.split( "," )
      iarg = args[0].strip( )

      if len( args ) == 2:
         size = int( args[1].strip( ) )
      elif len( args ) != 1:
         raise gdb.GdbError( "zdisass <symbol|address[,size]]>" )

      addr  = gdb.execute( "p/x {}".format( iarg ), to_string=True ) \
                 .split( "=" )[1] \
                 .strip( )
      saddr = int( addr, 16 )
      eaddr = saddr + size
      iaddr = saddr

      print("Dump of zOS assembler code from {:#x} to {:#x}".format( saddr, eaddr ))

      ms = MainstorValue();
      zaddr = saddr - ms;

      try:
         while iaddr < eaddr:
            # Most of the instruction Mnemonics are 2 bytes. However, there are
            # others that are 3 and 4 bytes as well. Based on what again is
            # documented in Appendix B of the document mentioned above, the
            # following instructions beginning whith these 2 bytes are 3 and 4
            # byte Mnemonics. All others are 2 bytes.
            #
            # 3 bytes: 0xa5, 0xa7, 0xc0, 0xc2, 0xc4, 0xc6, 0xc8
            # 4 bytes: 0xb2, 0xb3, 0xb9, 0xe3, 0xe5, 0xeb, 0xec, 0xed
            #
            inst = gdb.execute( "x/6xb {}".format( iaddr ), to_string=True ) \
                      .split( )

            # This is the base instruction Mnemonic
            im = int( inst[1], 16 )

            if ( im == 0xa5 ) or \
               ( im == 0xa7 ) or \
               ( im == 0xc0 ) or \
               ( im == 0xc2 ) or \
               ( im == 0xc4 ) or \
               ( im == 0xc6 ) or \
               ( im == 0xc8 ):
               im = ( ( im << 4 ) | ( int( inst[2], 16 ) & 0x0f ) )
            elif ( im == 0x01 ) or \
                 ( im == 0xb2 ) or \
                 ( im == 0xb3 ) or \
                 ( im == 0xb9 ) or \
                 ( im == 0xe5 ):
               im = ( ( im << 8 ) | int( inst[2], 16 ) )
            elif ( im == 0xe3 ) or \
                 ( im == 0xeb ) or \
                 ( im == 0xec ) or \
                 ( im == 0xed ):
               im = ( ( im << 8 ) | int( inst[5], 16 ) )

            ii = getInst( im )
            #print "ii: {}, im: {}".format(ii, im)

            func = ii["func"]
            if ( func == None ):
               break
            else:
               rv = func( iaddr )

            off = iaddr - saddr;

            res = "{:#x} {:08X} <{:=+04X}>: {:14} {:6} {}".format( iaddr,
                                                                   zaddr + off,
                                                                   off,
                                                                   rv._mac,
                                                                   ii["name"],
                                                                   rv._asm );

            print(res)

            iaddr += rv._sz;
      except gdb.error:
         print("*** error ***")
      except gdb.MemoryError:
         print("*** Memory Error detected ***")

      return

zdisass( )
