# @file	  funcs.py
# @author Garfield A. Lewis <garfield.lewis@lzlabs.com>
# @brief  SDM environment for the GDB debugger.
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
#   Implementation of some SDM environment for the GDB debugger. This can be
#   used to debug problems associated with the LzLabs SDM.
#   
# @section Source
#   
#   Information in this file is original.
#
import sys
import os
import gdb

# Add the current path to the system path so that the subsequent import will
# find my external libraries.
if sys.path[0] != '/opt/lzlabs/debug/gdb':
   sys.path.insert( 0, '/opt/lzlabs/debug/gdb' )

from apis.common import *

# @classs zthread
# @brief  
class zthread( gdb.Command ):
   """zOS thread functions.
  
   Switch to a specific SDM thread.

   Example:

   (gdb) zthread 1
   (gdb) info zregisters

   (gdb) zthread
   [Current zOS thread is 1 (Thread 0x7ffbc4000000)]
   """
   
   def __init__( self, arg ):
      super( zthread, self ).__init__( "zthread", gdb.COMMAND_USER )
      
      gdb.execute( "set $_zthread={}".format( arg ) )
   
   def invoke( self, arg, from_tty ):
      sb = isSDMEnabled()
      
      args  = gdb.string_to_argv( arg )
      tid   = getzthread()
      maddr = gdb.execute( "p/x sysblk->regs[{}].mainstor".format( tid - 1 ),
                           to_string=True )                                \
                                                          .split( "=" )[1] \
                                                          .strip( )
      
      if len( args ) == 0:
         print("[Current zOS thread is {} (Thread {})]".format( tid, maddr ))
      elif len( args ) == 1:
         print("[Switching to zOS thread {} (Thread {})]".format( args[0], maddr ))
         
         gdb.execute( "set $_zthread={}".format( args[0] ) )
      else:
         raise gdb.GdbError( "Invalid argument '{}' specified.".format( args[0] ) )
      
zthread( 1 )
