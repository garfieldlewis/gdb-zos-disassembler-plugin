# @file	  common.py
# @author Garfield A. Lewis <garfield.lewis@lzlabs.com>
# @brief  This file contains common routines that will be used in many different
#         areas for convenience sake.
#        
import gdb

# @fn    isSDMEnabled
# @brief Checks to see if the SDM environment is initialized. This is done by
#        verifying that the "sysblk" has been allocated. If the sysblk has not
#        been allocatd then we will raise an exception, otherwise, we will
#        return the address of the sysblk.
#
# @param N/A
# @returns The address of the "sysblk" variable.
def isSDMEnabled( ):
   """Checks to see if the SDM environment is currently enabled.
      
      This is done by checking whether the sysblk variable has been initialized
      in the current envirionment. If it is not we will raise an error
      otherwise the address of the variable will be returned.
   """
   
   sb = gdb.parse_and_eval( "sysblk" )
   
   if sb == 0x0:
      raise gdb.GdbError(  "An SDM environment has not yet been initiated." )
   
   #return( int( str( sb ), 16 ) )
   return sb

# @fn    ebcdic
# @brief Convert the given string into an EBCDIC string.
#
# @param[inout] p   - Pointer to the string to be converted.
# @param[in]    len - The length of the input string.
# @returns An EBCDIC string.
def ebcdic( p, len ):
   """Convert a string of data (p) into ebcdic."""
   
   ptab = "................"  \
          "................"  \
          "................"  \
          "................"  \
          " ...........<(+|"  \
          "&.........!$*);^"  \
          "-/.........,._>?"  \
          ".........`:#@'=\"" \
          ".abcdefghi......"  \
          ".jklmnopqr......"  \
          ".~stuvwxyz......"  \
          "................"  \
          ".ABCDEFGHI......"  \
          ".JKLMNOPQR......"  \
          "..STUVWXYZ......"  \
          "0123456789......"
   rv   = ""
   
   for i in range( len ):
      ix = ord( p[i] ) & 0xff
      rv += ptab[ix]
   
   return rv

# @fn    ascii
# @brief Convert the given string into an ASCII string.
#
# @param[inout] p   - Pointer to the string to be converted.
# @param[in]    len - The length of the input string.
# @returns An ASCII string.
def ascii( p, len ):
   """Convert a string of data (p) into ascii."""
   
   ptab = "................"  \
          "................"  \
          " !\"#$.&'()*+,-./" \
          "0123456789:;<=>?"  \
          "@ABCDEFGHIJKLMNO"  \
          "PQRSTUVWXYZ{\\}^_" \
          "`abcdefghijklmno"  \
          "pqrstuvwxyz{|}~."  \
          "................"  \
          "................"  \
          "................"  \
          "................"  \
          "................"  \
          "................"  \
          "................"  \
          "................"
   rv   = ""
   
   for i in range( len ):
      ix = ord( p[i] ) & 0xff
      rv += ptab[ix]
   
   return rv

def getzthread():
   """Grab the value of the gdb global variable $_zthread.
   
   returns An integer value.  Subtract 1 to use as a sysblk->regs[] index."""
  
   return int( gdb.execute( "p $_zthread", to_string=True ).split( "=" )[1] )
