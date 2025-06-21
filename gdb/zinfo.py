# @file	  zinfo.py
# @author Garfield A. Lewis <garfield.lewis@lzlabs.com>
# @brief  Implement zOS versions of certain info commands for the GDB debugger.
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
#   Implementation of some SDM flavoured INFO commands for the GDB debugger.
#   
# @section Source
#   
#   Information in this file is original.
#
import sys
import os
import gdb

from apis.common import *

# Add the current path to the system path so that the subsequent import will
# find my external libraries.
if sys.path[0] != '/opt/lzlabs/debug/gdb':
   sys.path.insert( 0, '/opt/lzlabs/debug/gdb' )

# @classs infosdm
# @brief  Gives a high level of the current SDM. This is basically a view of
#         information that can be found in the global sysblk structure.
class infosdm( gdb.Command ):
   """Display the overall SDM status.
  
   Usage:

   (gdb) info sdm
   """
   
   def __init__( self ):
      super( infosdm, self ).__init__( "info sdm", gdb.COMMAND_STATUS )
   
   def invoke( self, arg, from_tty ):
      sb = isSDMEnabled( )
      
      ty = gdb.lookup_type( "SYSBLK" )
      
      sdmMsg  = "{:*^80s}\n".format( " SDM Information " )
      
      #for k,v in gdb.types.deep_items( tt ):
      for f in ty.keys( ):
         if ( sb[f].type.code == gdb.TYPE_CODE_STRUCT ) or \
            ( sb[f].type.code == gdb.TYPE_CODE_UNION ):
            ttp = gdb.types.get_basic_type( sb[f].type )
            
            sdmMsg += "{:18} : {}\n".format( f, sb[f].address )
         elif ( sb[f].type.code == gdb.TYPE_CODE_PTR ):
            ttp = gdb.types.get_basic_type( sb[f].type )
            
            sdmMsg += "{:18} : {}\n".format( f, sb[f].address )
         elif ( sb[f].type.code == gdb.TYPE_CODE_TYPEDEF ):
            ttp = gdb.types.get_basic_type( sb[f].type )
            
            if ( ttp.code == gdb.TYPE_CODE_STRUCT ) or \
               ( ttp.code == gdb.TYPE_CODE_UNION ):
               sdmMsg += "{:18} : {}\n".format( f, sb[f].address )
            else:
               sdmMsg += "{:18} : {}\n".format( f, sb[f] )
         else:
            sdmMsg += "{:18} : {}\n".format( f, sb[f] )
      
      sdmMsg += "{:*^80s}".format( " SDM Information End " )
      
      print(sdmMsg)
      
      # @question Is there a single SYSBLK for the SDM job or is there one per
      #           thread?
      # @question Are the SYSBLK.REGS for each thread. The comment in the lhe.h
      #           file says "Registers for each CPU". What does that mean?

infosdm( )

# @classs infozthreads
# @brief  Display of the current SMD threads.
class infozthreads( gdb.Command ):
   """Display all current SDM threads.
   
   Usage:

   (gdb) info zthreads
   """
   
   def __init__( self ):
      super( infozthreads, self ).__init__( "info zthreads", gdb.COMMAND_STATUS )
   
   def invoke( self, arg, from_tty ):
      isSDMEnabled( )
      
      mcpus = gdb.parse_and_eval( "sysblk->max_cpu_threads" )
      
      sdmMsg  = "{:*^80s}\n".format( " SDM Threads " )
      sdmMsg += "Max Threads = {}\n".format( mcpus )
      sdmMsg += " {:3} {:21} Frame\n".format( "Id", "Target Id" )
      
      tid = 1
      
      for cpu in range( 0, int( mcpus ) ):
         caddr = int( gdb.parse_and_eval( "sysblk->regs[{}].psw.ia.F".format( cpu ) ) )
         
         if caddr != 0x0:
            maddr   = gdb.execute( "p/x sysblk->regs[{}].mainstor".format( cpu ), to_string=True ) \
                                                                  .split( "=" )[1]                 \
                                                                  .strip( )
            prog    = gdb.execute( "p sysblk->regs[{}].taskinfo.progname".format( cpu ), to_string=True ) \
                                                                         .split( "=" )[1]                 \
                                                                         .strip( '" \n' )                 \
                                                                         .split( "\\" )[0]
            prog    = '"' + prog + '"';
            sdmMsg += "{:3} Thread {} {:10} {:#016x} in XXXX( ) from YYY\n".format( tid,
                                                                                    maddr,
                                                                                    prog,
                                                                                    int( maddr, 16 ) + caddr )
            tid    += 1
      
      sdmMsg += "{:*^80s}".format( " SDM Threads End " )
      
      print(sdmMsg)

infozthreads( )

# @classs infozregisters
# @brief  ???
class infozregisters( gdb.Command ):
   """Display SDM registers for the current zOS thread, as set by zthread (or implicitly for single threaded batch)
  
   Usage:

   (gdb) info zregisters
   """
   
   def __init__( self ):
      super( infozregisters, self ).__init__( "info zregisters", gdb.COMMAND_STATUS )
   
   def invoke( self, arg, from_tty ):
      isSDMEnabled( )
      
      rIx = getzthread() - 1
      m2  = gdb.execute( "printf \"%ld %ld\","       \
                         "sysblk->regs[{}].cpultid," \
                         "sysblk->regs[{}].cputid".format( rIx, rIx ), \
                         to_string=True ) \
               .split( ) 
      
      # Start building the output string.
      sdmMsg  = "{:*^80s}\n".format( " SDM Registers " )
      sdmMsg += "CPU{:04X}\tThread ID: {:016x}\n".format( int( m2[0] ), \
                                                          int( m2[1] ) )
      sdmMsg += "\nGeneral Registers:\n\n"
      
      for ix in range( 0, 16, 4 ):
         r4      = gdb.execute( "printf \"%ld %ld %ld %ld\","   \
                                "sysblk->regs[{}].x_gpr[{}].D," \
                                "sysblk->regs[{}].x_gpr[{}].D," \
                                "sysblk->regs[{}].x_gpr[{}].D," \
                                "sysblk->regs[{}].x_gpr[{}].D".format( rIx, ix,       \
                                                                       rIx, ix + 1,   \
                                                                       rIx, ix + 2,   \
                                                                       rIx, ix + 3 ), \
                                to_string=True ) \
                      .split( )
         sdmMsg += "    gr{:<2} : {:08x}" \
                   "    gr{:<2} : {:08x}" \
                   "    gr{:<2} : {:08x}" \
                   "    gr{:<2} : {:08x}\n".format( ix    , int( r4[0] ), \
                                                    ix + 1, int( r4[1] ), \
                                                    ix + 2, int( r4[2] ), \
                                                    ix + 3, int( r4[3] ) )
      
      sdmMsg += "\nControl Registers:\n\n"
      
      for ix in range( 0, 16, 4 ):
         r4      = gdb.execute( "printf \"%ld %ld %ld %ld\","  \
                                "sysblk->regs[{}].x_cr[{}].D," \
                                "sysblk->regs[{}].x_cr[{}].D," \
                                "sysblk->regs[{}].x_cr[{}].D," \
                                "sysblk->regs[{}].x_cr[{}].D".format( rIx, ix,       \
                                                                      rIx, ix + 1,   \
                                                                      rIx, ix + 2,   \
                                                                      rIx, ix + 3 ), \
                                to_string=True ) \
                      .split( )
         sdmMsg += "    cr{:<2} : {:08x}" \
                   "    cr{:<2} : {:08x}" \
                   "    cr{:<2} : {:08x}" \
                   "    cr{:<2} : {:08x}\n".format( ix   ,  int( r4[0] ), \
                                                    ix + 1, int( r4[1] ), \
                                                    ix + 2, int( r4[2] ), \
                                                    ix + 3, int( r4[3] ) )
      
      sdmMsg += "\nAccess Registers:\n\n"
      
      for ix in range( 0, 16, 4 ):
         r4      = gdb.execute( "printf \"%ld %ld %ld %ld\","  \
                                "sysblk->regs[{}].x_ar[{}].F," \
                                "sysblk->regs[{}].x_ar[{}].F," \
                                "sysblk->regs[{}].x_ar[{}].F," \
                                "sysblk->regs[{}].x_ar[{}].F".format( rIx, ix,       \
                                                                      rIx, ix + 1,   \
                                                                      rIx, ix + 2,   \
                                                                      rIx, ix + 3 ), \
                                to_string=True ) \
                      .split( )
         sdmMsg += "    ar{:<2} : {:08x}" \
                   "    ar{:<2} : {:08x}" \
                   "    ar{:<2} : {:08x}" \
                   "    ar{:<2} : {:08x}\n".format( ix   ,  int( r4[0] ), \
                                                    ix + 1, int( r4[1] ), \
                                                    ix + 2, int( r4[2] ), \
                                                    ix + 3, int( r4[3] ) )
      
      sdmMsg += "\nFloating Point Registers:\n\n"
      
      for ix in range( 0, 16, 2 ):
         r4      = gdb.execute( "printf \"%ld %ld %ld %ld\"," \
                                "sysblk->regs[{}].fpr[{}],"   \
                                "sysblk->regs[{}].fpr[{}],"   \
                                "sysblk->regs[{}].fpr[{}],"   \
                                "sysblk->regs[{}].fpr[{}]".format( rIx, 2 * ix,             \
                                                                   rIx, 2 * ix + 1,         \
                                                                   rIx, 2 * (ix + 1),       \
                                                                   rIx, 2 * (ix + 1) + 1),  \
                                to_string=True ) \
                      .split( )
         sdmMsg += "    fpr{:<2} : {:08x} {:08x}" \
                   "    fpr{:<2} : {:08x} {:08x}\n".format( ix,     int( r4[0] ), \
                                                                    int( r4[1] ), \
                                                            ix + 1, int( r4[2] ), \
                                                                    int( r4[3] ) )

      # Floating Point Control register
      fpc = gdb.execute( "p sysblk->regs[{}].fpc".format( rIx ), to_string=True ) \
               .split( "=" )[1]
      # Prefix register
      pxr = gdb.execute( "p sysblk->regs[{}].x_pxr.F".format( rIx ), to_string=True ) \
               .split( "=" )[1]
      # Program Status word
      #psa = gdb.execute( "p sysblk->regs[{}].psa".format( rIx ), to_string=True ) \
      #         .split( 1 )
      
      sdmMsg += "\nFloating Point Control Register: {:08x}\n".format( int( fpc ) )
      sdmMsg += "\nPrefix Register: {:08x}\n".format( int( pxr ) )
      sdmMsg += "{:*^80s}".format( " SDM Registers End " )
      
      print(sdmMsg)

infozregisters( )

# @classs infozmodules
# @brief  ???
class infozmodules( gdb.Command ):
   """Display SDM loaded modules.
  
   Usage:

   (gdb) info zmodules
   """
   
   def __init__( self ):
      super( infozmodules, self ).__init__( "info zmodules", gdb.COMMAND_STATUS )
   
   def invoke( self, arg, from_tty ):
      isSDMEnabled( )
      
      off = gdb.parse_and_eval( "regs->mainstor+regs->tcb+0x144" )
      
      sdmMsg  = "{:*^80s}\n".format( " SDM Loaded Modules List " )
      sdmMsg += "{:*^80s}".format( " SDM Loaded Modules List End " )
      
      print(sdmMsg)

infozmodules( )

# @classs infozbreakpoints
# @brief  ???
class infozbreakpoints( gdb.Command ):
   """Display SDM breakpoints.
  
   Usage:

   (gdb) info zbreakpoints
   """
   
   def __init__( self ):
      super( infozbreakpoints, self ).__init__( "info zbreakpoints", gdb.COMMAND_STATUS )
   
   def invoke( self, arg, from_tty ):
      isSDMEnabled( )
      
      ty = gdb.lookup_type( "SYSBLK" )
      
      sdmMsg  = "{:*^80s}\n".format( " SDM Breakpoints " )
      sdmMsg += "{:*^80s}".format( " SDM Breakpoints End " )
      
      #print(sdmMsg)
      print("???NYI???")

infozbreakpoints( )
