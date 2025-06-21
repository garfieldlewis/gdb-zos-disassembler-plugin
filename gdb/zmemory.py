# @file   zmem.py
# @author Garfield A. Lewis <garfield.lewis@lzlabs.com>
# @brief  Implement a zOS memory dumper plugin for the GDB debugger.
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

class zmemory( gdb.Command ):
   """Display the zOS memory given a VADR. ..."""
   
   def __init__( self ):
      super( zmemory, self ).__init__( "zmemory", gdb.COMMAND_USER )
   
   def invoke( self, arg, from_tty ):
      raise gdb.GdbError( "zmemory -- WIP" )
      
      isSDMEnabled( )
      
      size = 128
      
      if len( arg ) == 0:
         raise gdb.GdbError( "zmemory <address[,size]>" )
      
      args = arg.split( "," )
      iarg = args[0].strip( )
      
      if len( args ) == 2:
         size = int( args[1].strip( ) )
      elif len( args ) != 1:
         raise gdb.GdbError( "zmemory <address[,size]>" )
      
      tgcs  = gdb.target_charset( )
      addr  = gdb.execute( "p/x {}".format( iarg ), to_string=True ) \
                 .split( "=" )[1] \
                 .strip( )
      saddr = int( addr, 16 )
      eaddr = saddr + size
      iaddr = saddr
      w4p   = [ "0", "0", "0", "0", "0" ]
      wc    = 0
      
      print("Dump of zOS memory from {:#x} to {:#x}\n".format( saddr, eaddr ))
      
      try:
         a0 = gdb.execute( "x/1xg {:#x}".format( iaddr ), to_string=True ) \
                 .split( )[1]
         a0 = int( a0, 16 )
         
         while iaddr <= eaddr:
            w4 = gdb.execute( "x/4xw {}".format( a0 ), to_string=True ) \
                    .split( )
            
            if ( ( w4[1] == w4p[1] ) and
                 ( w4[2] == w4p[2] ) and
                 ( w4[3] == w4p[3] ) and
                 ( w4[4] == w4p[4] ) ):
               wc += 1
            else:
               if ( wc > 0 ):
                  print( "---------- {:d} Lines Same As Above ----------".format( wc ) )
               
               wc = 0
               a1 = gdb.execute( "p *(char[16]*){}".format( a0 ), to_string=True ) \
                       .split( "=" )[1] \
                       .split( '"' )[1]
               eb = ebcdic( a1, 16 )
               ac = ascii( a1, 16 )
               
               print( "{:08x}  {:08x} {:08x} {:08x} {:08x}  |{:16s}|{:16s}|".format( iaddr - saddr,
                                                                                     int( w4[1], 16 ),
                                                                                     int( w4[2], 16 ),
                                                                                     int( w4[3], 16 ),
                                                                                     int( w4[4], 16 ),
                                                                                     eb,
                                                                                     ac ) )
            
            w4p    = w4
            iaddr += 16
            a0    += 16
      except gdb.error as e:
         print("*** error ***\n{}".format( e ))
      except gdb.MemoryError as e:
         print("*** Memory Error detected ***\n{}".format( e ))
      
      return
   
zmemory( )
