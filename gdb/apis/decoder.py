# @file	  decoder.py
# @author Garfield A. Lewis <garfield.lewis@lzlabs.com>
# @brief  The routines here will be used for the decoding of different zOS
#         innstructions into their basic components parts including all or some
#         of the following:
#         
#         Bx - The register number
#         Dx - The data offset
#         Ix - ???
#         Lx - The length of the data
#         Mx - The mask field.
#         Rx - The register number.
#        
# https://www.ibm.com/support/libraryserver/download/dz9zr006.pdf
#
import gdb

# @class rvalue
# @brief This structure will be used as the return value from these functions.
# 
# @param[in] self - The self pointer to the instantiated structure/class.
# @param[in] _sz  - This number bytes represented by the instruction.
# @param[in] mac  - The machine language representation of the instruction.
# @param[in] asm  - The assembly language representation of the instruction.
# @returns An instance of the structure.
class rvalue:
   def __init__( self, _sz ):
      self._sz  = _sz
      self._mac = ""
      self._asm = ""

# @fn	 RR
# @brief Decode register and register format 1 instructions.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def RR( arg ):
   rv = rvalue( 2 )
   
   ops = gdb.execute( "x/2xb {}".format( arg ), to_string=True ).split( ) 
   
   R1 = int( ops[2], 16 ) >> 4
   R2 = int( ops[2], 16 ) & 0x0f
   
   rv._mac = "{:02X}{:02X}".format( int( ops[1], 16 ), int( ops[2], 16 ) )
   rv._asm = "R{},R{}".format( R1, R2 )
   
   return rv

# @fn	 RR_R
# @brief Decode register and register format 1 instructions.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def RR_R( arg ):
   rv = rvalue( 2 )
   
   ops = gdb.execute( "x/2xb {}".format( arg ), to_string=True ).split( ) 
   
   R1 = int( ops[2], 16 ) >> 4
   
   rv._mac = "{:02X}{:02X}".format( int( ops[1], 16 ), int( ops[2], 16 ) )
   rv._asm = "R{}".format( R1 )
   
   return rv

# @fn	 RRE
# @brief Decode register and register format 2 instructions.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def RRE( arg ):
   rv = rvalue( 4 )
   
   ops = gdb.execute( "x/4xb {}".format( arg ), to_string=True ).split( ) 
   
   R1 = int( ops[4], 16 ) >> 4
   R2 = int( ops[4], 16 ) & 0x0f
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                 int( ops[2], 16 ),
                                                 int( ops[3], 16 ),
                                                 int( ops[4], 16 ) )
   rv._asm = "R{},R{}".format( R1, R2 )
   
   return rv

# @fn	 RRE_R
# @brief Decode register and register format 2 instructions.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def RRE_R( arg ):
   rv = rvalue( 4 )
   
   ops = gdb.execute( "x/4xb {}".format( arg ), to_string=True ).split( ) 
   
   R1 = int( ops[4], 16 ) >> 4
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                 int( ops[2], 16 ),
                                                 int( ops[3], 16 ),
                                                 int( ops[4], 16 ) )
   rv._asm = "R{}".format( R1 )
   
   return rv

# @fn	 RRE_N
# @brief Decode register and register format 2 instructions.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def RRE_N( arg ):
   rv = rvalue( 4 )
   
   ops = gdb.execute( "x/4xb {}".format( arg ), to_string=True ).split( ) 
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                 int( ops[2], 16 ),
                                                 int( ops[3], 16 ),
                                                 int( ops[4], 16 ) )
   rv._asm = ""
   
   return rv

# @fn	 RRR
# @brief Decode register and register format 2 instructions.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def RRR( arg ):
   rv = rvalue( 4 )
   
   ops = gdb.execute( "x/4xb {}".format( arg ), to_string=True ).split( ) 
   
   R1 = int( ops[4], 16 ) >> 4
   R2 = int( ops[4], 16 ) & 0x0f
   R3 = int( ops[3], 16 ) >> 4
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                 int( ops[2], 16 ),
                                                 int( ops[3], 16 ),
                                                 int( ops[4], 16 ) )
   rv._asm = "R{},R{},R{}".format( R1, R2, R3 )
   
   return rv

# @fn	 RRS
# @brief Decode register and register format 2 instructions.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def RRS( arg ):
   rv = rvalue( 6 )
   
   ops = gdb.execute( "x/6xb {}".format( arg ), to_string=True ).split( ) 
   
   R1 = int( ops[2], 16 ) >> 4
   R2 = int( ops[2], 16 ) & 0x0f
   M3 = int( ops[5], 16 ) >> 4
   D4 = ( ( int( ops[3], 16 ) & 0x0f ) << 8 ) | int( ops[4], 16 )
   B4 = int( ops[3], 16 ) >> 4
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                              int( ops[2], 16 ),
                                                              int( ops[3], 16 ),
                                                              int( ops[4], 16 ),
                                                              int( ops[5], 16 ),
                                                              int( ops[6], 16 ) )
   rv._asm = "R{},R{},{},{}({})".format( R1, R2, M3, D4, B4 )
   
   return rv

# @fn	 RRF
# @brief Decode register and register format 2 instructions.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def RRF( arg ):
   rv = rvalue( 4 )
   
   ops = gdb.execute( "x/4xb {}".format( arg ), to_string=True ).split( ) 
   
   R1 = int( ops[4], 16 ) >> 4
   M3 = int( ops[3], 16 ) >> 4
   R2 = int( ops[4], 16 ) & 0x0f
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                 int( ops[2], 16 ),
                                                 int( ops[3], 16 ),
                                                 int( ops[4], 16 ) )
   rv._asm = "R{},{},R{}".format( R1, M3, R2 )
   
   return rv

# @fn	 RRF_R
# @brief Decode register and register format 2 instructions.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def RRF_R( arg ):
   rv = rvalue( 4 )
   
   ops = gdb.execute( "x/4xb {}".format( arg ), to_string=True ).split( ) 
   
   R1 = int( ops[3], 16 ) >> 4
   R3 = int( ops[4], 16 ) >> 4
   R2 = int( ops[4], 16 ) & 0x0f
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                 int( ops[2], 16 ),
                                                 int( ops[3], 16 ),
                                                 int( ops[4], 16 ) )
   rv._asm = "R{},R{},R{}".format( R1, R3, R2 )
   
   return rv

# @fn	 RRF_RM
# @brief Decode register and register format 2 instructions.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def RRF_RM( arg ):
   rv = rvalue( 4 )
   
   ops = gdb.execute( "x/4xb {}".format( arg ), to_string=True ).split( ) 
   
   R1 = int( ops[4], 16 ) >> 4
   R3 = int( ops[3], 16 ) >> 4
   R2 = int( ops[4], 16 ) & 0x0f
   M4 = int( ops[3], 16 ) & 0x0f
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                 int( ops[2], 16 ),
                                                 int( ops[3], 16 ),
                                                 int( ops[4], 16 ) )
   rv._asm = "R{},R{},R{},{}".format( R1, R3, R2, M4 )
   
   return rv

# @fn	 RRF_M
# @brief Decode register and register format 2 instructions.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def RRF_M( arg ):
   rv = rvalue( 4 )
   
   ops = gdb.execute( "x/4xb {}".format( arg ), to_string=True ).split( ) 
   
   R1 = int( ops[4], 16 ) >> 4
   R2 = int( ops[4], 16 ) & 0x0f
   M4 = int( ops[3], 16 ) & 0x0f
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                 int( ops[2], 16 ),
                                                 int( ops[3], 16 ),
                                                 int( ops[4], 16 ) )
   rv._asm = "R{},R{},{}".format( R1, R2, M4 )
   
   return rv

# @fn	 RRF_RMRM
# @brief Decode register and register format 2 instructions.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def RRF_RMRM( arg ):
   rv = rvalue( 4 )
   
   ops = gdb.execute( "x/4xb {}".format( arg ), to_string=True ).split( ) 
   
   R1 = int( ops[4], 16 ) >> 4
   M3 = int( ops[3], 16 ) >> 4
   R2 = int( ops[4], 16 ) & 0x0f
   M4 = int( ops[3], 16 ) & 0x0f
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                 int( ops[2], 16 ),
                                                 int( ops[3], 16 ),
                                                 int( ops[4], 16 ) )
   rv._asm = "R{},{},R{},{}".format( R1, M3, R2, M4 )
   
   return rv

# @fn	 RRF_RRM
# @brief Decode register and register format 2 instructions.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def RRF_RRM( arg ):
   rv = rvalue( 4 )
   
   ops = gdb.execute( "x/4xb {}".format( arg ), to_string=True ).split( ) 
   
   R1 = int( ops[4], 16 ) >> 4
   R2 = int( ops[4], 16 ) & 0x0f
   M3 = int( ops[3], 16 ) >> 4
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                 int( ops[2], 16 ),
                                                 int( ops[3], 16 ),
                                                 int( ops[4], 16 ) )
   
   if M3 == 0:
      rv._asm = "R{},R{}".format( R1, R2 )
   else:
      rv._asm = "R{},R{},{}".format( R1, R2, M3 )
   
   return rv

# If both index and base are zero then drop both of them including the parentheses:
# LA  R15,X'0'(X'0',B'0') -> LA R15,0
def formatIndexBasePair( v, w ):
   if v == 0 and w == 0:
      return "";
   elif v == 0:
      return "(,R{})".format( w )
   
   return "({},R{})".format( v, w )

# @fn	 RX
# @brief Decode register and storage format 1 instructions.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def RX( arg ):
   rv = rvalue( 4 )
   
   ops = gdb.execute( "x/4xb {}".format( arg ),
                      to_string=True ).split( )
   
   R1 = int( ops[2], 16 ) >> 4
   X2 = int( ops[2], 16 ) & 0x0f
   B2 = int( ops[3], 16 ) >> 4
   D2 = ( ( int( ops[3], 16 ) & 0x0f ) << 8 ) | int( ops[4], 16 )
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                 int( ops[2], 16 ),
                                                 int( ops[3], 16 ),
                                                 int( ops[4], 16 ) )
   ib = formatIndexBasePair( X2, B2 );
   rv._asm = "R{},{}{}".format( R1, D2, ib )
   
   return rv

# @fn	 RX_M
# @brief Decode register and storage format 1 instructions.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def RX_M( arg ):
   rv = rvalue( 4 )
   
   ops = gdb.execute( "x/4xb {}".format( arg ), to_string=True ).split( ) 
   
   M1 = int( ops[2], 16 ) >> 4
   D2 = ( ( int( ops[3], 16 ) & 0x0f ) << 8 ) | int( ops[4], 16 )
   X2 = int( ops[2], 16 ) & 0x0f
   B2 = int( ops[3], 16 ) >> 4
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                 int( ops[2], 16 ),
                                                 int( ops[3], 16 ),
                                                 int( ops[4], 16 ) )
   ib = formatIndexBasePair( X2, B2 );
   rv._asm = "{},{}{}".format( M1, D2, ib )
   
   return rv

# @fn	 RXE
# @brief Decode register and storage format 1 instructions.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def RXE( arg ):
   rv = rvalue( 6 )
   
   ops = gdb.execute( "x/6xb {}".format( arg ), to_string=True ).split( ) 
   
   R1 = int( ops[2], 16 ) >> 4
   D2 = ( ( int( ops[3], 16 ) & 0x0f ) << 12 ) | int( ops[4], 16 )
   X2 = int( ops[2], 16 ) & 0x0f
   B2 = int( ops[3], 16 ) >> 4
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                              int( ops[2], 16 ),
                                                              int( ops[3], 16 ),
                                                              int( ops[4], 16 ),
                                                              int( ops[5], 16 ),
                                                              int( ops[6], 16 ) )
   ib = formatIndexBasePair( X2, B2 );
   rv._asm = "R{},{}{}".format( R1, D2, ib )
   
   return rv

# @fn	 RXF
# @brief Decode register and storage format 1 instructions.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def RXF( arg ):
   rv = rvalue( 6 )
   
   ops = gdb.execute( "x/6xb {}".format( arg ), to_string=True ).split( ) 
   
   R1 = int( ops[5], 16 ) >> 4
   R3 = int( ops[2], 16 ) >> 4
   D2 = ( ( int( ops[3], 16 ) & 0x0f ) << 8 ) | int( ops[4], 16 )
   X2 = int( ops[2], 16 ) & 0x0f
   B2 = int( ops[3], 16 ) >> 4
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                              int( ops[2], 16 ),
                                                              int( ops[3], 16 ),
                                                              int( ops[4], 16 ),
                                                              int( ops[5], 16 ),
                                                              int( ops[6], 16 ) )
   ib = formatIndexBasePair( X1, B2 );
   rv._asm = "R{},R{},{}{}".format( R1, R3, D2, ib )
   
   return rv

# @fn	 RXY
# @brief Decode register and storage format 2 instructions.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def RXY( arg ):
   rv = rvalue( 6 )
   
   ops = gdb.execute( "x/6xb {}".format( arg ), to_string=True ).split( ) 
   
   R1 = int( ops[2], 16 ) >> 4
   X2 = int( ops[2], 16 ) & 0x0f
   B2 = int( ops[3], 16 ) >> 4
   D2 = ( ( int( ops[5], 16 ) << 12 ) |
          ( ( int( ops[3], 16 ) & 0x0f ) << 8 ) |
          ( int( ops[4], 16 ) ) )
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                              int( ops[2], 16 ),
                                                              int( ops[3], 16 ),
                                                              int( ops[4], 16 ),
                                                              int( ops[5], 16 ),
                                                              int( ops[6], 16 ) )
   ib = formatIndexBasePair( B2, D2 );
   rv._asm = "R{},{}{}".format( R1, X2, ib )
   
   return rv

# @fn	 RXY_M
# @brief Decode register and storage format 2 instructions.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def RXY_M( arg ):
   rv = rvalue( 6 )
   
   ops = gdb.execute( "x/6xb {}".format( arg ), to_string=True ).split( ) 
   
   M1 = int( ops[2], 16 ) >> 4
   X2 = int( ops[2], 16 ) & 0x0f
   B2 = int( ops[3], 16 ) >> 4
   D2 = ( ( int( ops[5], 16 ) << 12 ) |
          ( ( int( ops[3], 16 ) & 0x0f ) << 8 ) |
          ( int( ops[4], 16 ) ) )
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                              int( ops[2], 16 ),
                                                              int( ops[3], 16 ),
                                                              int( ops[4], 16 ),
                                                              int( ops[5], 16 ),
                                                              int( ops[6], 16 ) )
   ib = formatIndexBasePair( B2, D2 );
   rv._asm = "R{},{}{}".format( R1, X2, ib )
   
   return rv

# @fn	 RS
# @brief Decode ??? format 1 instructions.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def RS( arg ):
   rv = rvalue( 4 )
   
   ops = gdb.execute( "x/4xb {}".format( arg ), to_string=True ).split( ) 
   
   R1 = int( ops[2], 16 ) >> 4
   R3 = int( ops[2], 16 ) & 0x0f
   D2 = ( ( int( ops[3], 16 ) & 0x0f ) << 8 ) | int( ops[4], 16 )
   B2 = int( ops[3], 16 ) >> 4
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                 int( ops[2], 16 ),
                                                 int( ops[3], 16 ),
                                                 int( ops[4], 16 ) )
   rv._asm = "R{},R{},{}({})".format( R1, R3, D2, B2 )
   
   return rv

# @fn	 RS_M
# @brief Decode ??? format 1 instructions.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def RS_M( arg ):
   rv = rvalue( 4 )
   
   ops = gdb.execute( "x/4xb {}".format( arg ), to_string=True ).split( ) 
   
   R1 = int( ops[2], 16 ) >> 4
   M3 = int( ops[2], 16 ) & 0x0f
   D2 = ( ( int( ops[3], 16 ) & 0x0f ) << 8 ) | int( ops[4], 16 )
   B2 = int( ops[3], 16 ) >> 4
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                 int( ops[2], 16 ),
                                                 int( ops[3], 16 ),
                                                 int( ops[4], 16 ) )
   rv._asm = "R{},{},{}(R{})".format( R1, M3, D2, B2 )
   
   return rv

# @fn	 RS_D
# @brief Decode ??? format 1 instructions.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def RS_D( arg ):
   rv = rvalue( 4 )
   
   ops = gdb.execute( "x/4xb {}".format( arg ), to_string=True ).split( ) 
   
   R1 = int( ops[2], 16 ) >> 4
   D2 = ( ( int( ops[3], 16 ) & 0x0f ) << 8 ) | int( ops[4], 16 )
   B2 = int( ops[3], 16 ) >> 4
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                 int( ops[2], 16 ),
                                                 int( ops[3], 16 ),
                                                 int( ops[4], 16 ) )
   rv._asm = "R{},{}({})".format( R1, D2, B2 )
   
   return rv

# @fn	 RSY
# @brief Decode ??? format ? instructions.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def RSY( arg ):
   rv = rvalue( 6 )
   
   ops = gdb.execute( "x/6xb {}".format( arg ), to_string=True ).split( ) 
   
   R1 = int( ops[2], 16 ) >> 4
   R3 = int( ops[2], 16 ) & 0x0f
   D2 = ( int( ops[6], 16 ) << 12 )           | \
        ( ( int( ops[3], 16 ) & 0x0f ) << 8 ) | \
        int( ops[4], 16 )
   B2 = int( ops[3], 16 ) >> 4
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                              int( ops[2], 16 ),
                                                              int( ops[3], 16 ),
                                                              int( ops[4], 16 ),
                                                              int( ops[5], 16 ),
                                                              int( ops[6], 16 ) )
   rv._asm = "R{},R{},{}({})".format( R1, R3, D2, B2 )
   
   return rv

# @fn	 RSY_M
# @brief Decode ??? format ? instructions.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def RSY_M( arg ):
   rv = rvalue( 6 )
   
   ops = gdb.execute( "x/6xb {}".format( arg ), to_string=True ).split( ) 
   
   R1 = int( ops[2], 16 ) >> 4
   M3 = int( ops[2], 16 ) & 0x0f
   D2 = ( int( ops[6], 16 ) << 12 )           | \
        ( ( int( ops[3], 16 ) & 0x0f ) << 8 ) | \
        int( ops[4], 16 )
   B2 = int( ops[3], 16 ) >> 4
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                              int( ops[2], 16 ),
                                                              int( ops[3], 16 ),
                                                              int( ops[4], 16 ),
                                                              int( ops[5], 16 ),
                                                              int( ops[6], 16 ) )
   rv._asm = "R{},{},{}({})".format( R1, M3, D2, B2 )
   
   return rv

# @fn	 RSI
# @brief Decode ??? format ? instructions.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def RSI( arg ):
   rv = rvalue( 4 )
   
   ops = gdb.execute( "x/4xb {}".format( arg ), to_string=True ).split( ) 
   
   R1 = int( ops[2], 16 ) >> 4
   R3 = int( ops[2], 16 ) & 0x0f
   I2 = ( int( ops[3], 16 ) << 8 ) | int( ops[4], 16 )
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                 int( ops[2], 16 ),
                                                 int( ops[3], 16 ),
                                                 int( ops[4], 16 ) )
   rv._asm = "R{},R{},{}".format( R1, R3, I2 )
   
   return rv

# @fn	 RSL
# @brief Decode ??? format ? instructions.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def RSL( arg ):
   rv = rvalue( 6 )
   
   ops = gdb.execute( "x/6xb {}".format( arg ), to_string=True ).split( ) 
   
   D1 = ( int( ops[3], 16 ) << 8 ) | int( ops[4], 16 )
   L1 = int( ops[2], 16 ) >> 4
   B1 = int( ops[3], 16 ) >> 4
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                              int( ops[2], 16 ),
                                                              int( ops[3], 16 ),
                                                              int( ops[4], 16 ),
                                                              int( ops[5], 16 ),
                                                              int( ops[6], 16 ) )
   rv._asm = "{}(L{},{})".format( D1, L1, B1 )
   
   return rv

# @fn	 RI
# @brief Decode register and immediate format 1 instructions.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def RI( arg ):
   rv = rvalue( 4 )
   
   ops = gdb.execute( "x/4xb {}".format( arg ), to_string=True ).split( ) 
   
   R1 = int( ops[2], 16 ) >> 4
   I2 = ( int( ops[3], 16 ) << 8 ) | ( int( ops[4], 16 ) )
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                 int( ops[2], 16 ),
                                                 int( ops[3], 16 ),
                                                 int( ops[4], 16 ) )
   rv._asm = "R{},{}".format( R1, I2 )
   
   return rv

# @fn	 RI_M
# @brief Decode register and immediate format 1 instructions.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def RI_M( arg ):
   rv = rvalue( 4 )
   
   ops = gdb.execute( "x/4xb {}".format( arg ), to_string=True ).split( ) 
   
   M1 = int( ops[2], 16 ) >> 4
   I2 = ( int( ops[3], 16 ) << 8 ) | ( int( ops[4], 16 ) )
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                 int( ops[2], 16 ),
                                                 int( ops[3], 16 ),
                                                 int( ops[4], 16 ) )
   rv._asm = "{},{}".format( M1, I2 )
   
   return rv

# @fn	 RIL
# @brief Decode register and immediate format 2 instructions.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def RIL( arg ):
   rv = rvalue( 6 )
   
   ops = gdb.execute( "x/6xb {}".format( arg ), to_string=True ).split( ) 
   
   R1 = int( ops[2], 16 ) >> 4
   I2 = ( int( ops[3], 16 ) << 12 ) | \
        ( int( ops[4], 16 ) << 8  ) | \
        int( ops[5], 16 )
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                              int( ops[2], 16 ),
                                                              int( ops[3], 16 ),
                                                              int( ops[4], 16 ),
                                                              int( ops[5], 16 ),
                                                              int( ops[6], 16 ) )
   rv._asm = "R{},{}".format( R1, I2 )
   
   return rv

# @fn	 RIL_M
# @brief Decode register and immediate format 2 instructions.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def RIL_M( arg ):
   rv = rvalue( 6 )
   
   ops = gdb.execute( "x/6xb {}".format( arg ), to_string=True ).split( ) 
   
   M1 = int( ops[2], 16 ) >> 4
   I2 = ( int( ops[3], 16 ) << 12 ) | \
        ( int( ops[4], 16 ) << 8  ) | \
        ( int( ops[5], 16 ) << 4  ) | \
        int( ops[6], 16 )
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                              int( ops[2], 16 ),
                                                              int( ops[3], 16 ),
                                                              int( ops[4], 16 ),
                                                              int( ops[5], 16 ),
                                                              int( ops[6], 16 ) )
   rv._asm = "R{},{}".format( R1, I2 )
   
   return rv

# @fn	 RIE
# @brief Decode register and immediate format 3 instructions.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def RIE( arg ):
   rv = rvalue( 6 )
   
   ops = gdb.execute( "x/6xb {}".format( arg ), to_string=True ).split( ) 
   
   R1 = int( ops[2], 16 ) >> 4
   R3 = int( ops[2], 16 ) & 0x0f
   I2 = ( int( ops[3], 16 ) << 8 ) | int( ops[4], 16 )
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                              int( ops[2], 16 ),
                                                              int( ops[3], 16 ),
                                                              int( ops[4], 16 ),
                                                              int( ops[5], 16 ),
                                                              int( ops[6], 16 ) )
   rv._asm = "R{},R{},{}".format( R1, R3, I2 )
   
   return rv

# @fn	 RIE_M
# @brief Decode register and immediate format 3 instructions.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def RIE_M( arg ):
   rv = rvalue( 6 )
   
   ops = gdb.execute( "x/6xb {}".format( arg ), to_string=True ).split( ) 
   
   R1 = int( ops[2], 16 ) >> 4
   R2 = int( ops[2], 16 ) & 0x0f
   M3 = int( ops[5], 16 ) >> 4
   I4 = ( int( ops[3], 16 ) << 8 ) | int( ops[4], 16 )
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                              int( ops[2], 16 ),
                                                              int( ops[3], 16 ),
                                                              int( ops[4], 16 ),
                                                              int( ops[5], 16 ),
                                                              int( ops[6], 16 ) )
   rv._asm = "R{},R{},{},{}".format( R1, R2, M3, I4 )
   
   return rv

# @fn	 RIE_IM
# @brief Decode register and immediate format 3 instructions.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def RIE_IM( arg ):
   rv = rvalue( 6 )
   
   ops = gdb.execute( "x/6xb {}".format( arg ), to_string=True ).split( ) 
   
   R1 = int( ops[2], 16 ) >> 4
   I2 = ( int( ops[3], 16 ) << 8 ) | int( ops[4], 16 )
   M3 = int( ops[5], 16 ) >> 4
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                              int( ops[2], 16 ),
                                                              int( ops[3], 16 ),
                                                              int( ops[4], 16 ),
                                                              int( ops[5], 16 ),
                                                              int( ops[6], 16 ) )
   rv._asm = "R{},{},{}".format( R1, I2, M3 )
   
   return rv

# @fn	 RIE_MI
# @brief Decode register and immediate format 3 instructions.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def RIE_MI( arg ):
   rv = rvalue( 6 )
   
   ops = gdb.execute( "x/6xb {}".format( arg ), to_string=True ).split( ) 
   
   R1 = int( ops[2], 16 ) >> 4
   I2 = int( ops[5], 16 )
   M3 = int( ops[2], 16 ) & 0x0f
   I4 = ( int( ops[3], 16 ) << 8 ) | int( ops[4], 16 )
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                              int( ops[2], 16 ),
                                                              int( ops[3], 16 ),
                                                              int( ops[4], 16 ),
                                                              int( ops[5], 16 ),
                                                              int( ops[6], 16 ) )
   rv._asm = "R{},{},{},{}".format( R1, I2, M3, I4 )
   
   return rv

# @fn	 RIE_RI
# @brief Decode register and immediate format 3 instructions.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def RIE_RI( arg ):
   rv = rvalue( 6 )
   
   ops = gdb.execute( "x/6xb {}".format( arg ), to_string=True ).split( ) 
   
   R1 = int( ops[2], 16 ) >> 4
   R2 = int( ops[2], 16 ) & 0x0f
   I3 = int( ops[3], 16 )
   I4 = int( ops[4], 16 )
   I5 = int( ops[5], 16 )
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                              int( ops[2], 16 ),
                                                              int( ops[3], 16 ),
                                                              int( ops[4], 16 ),
                                                              int( ops[5], 16 ),
                                                              int( ops[6], 16 ) )
   
   if I5 == 0:
      rv._asm = "R{},R{},{},{}".format( R1, R2, I3, I4 )
   else:
      rv._asm = "R{},R{},{},{},{}".format( R1, R2, I3, I4, I5 )
   
   return rv

# @fn	 RIS
# @brief Decode register and immediate format 3 instructions.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def RIS( arg ):
   rv = rvalue( 6 )
   
   ops = gdb.execute( "x/6xb {}".format( arg ), to_string=True ).split( ) 
   
   R1 = int( ops[2], 16 ) >> 4
   I2 = int( ops[5], 16 )
   M3 = int( ops[2], 16 ) & 0x0f
   D4 = ( ( int( ops[3], 16 ) & 0x0f ) << 8 ) | int( ops[4], 16 )
   B4 = int( ops[3], 16 ) >>4
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                              int( ops[2], 16 ),
                                                              int( ops[3], 16 ),
                                                              int( ops[4], 16 ),
                                                              int( ops[5], 16 ),
                                                              int( ops[6], 16 ) )
   rv._asm = "R{},{},{},{}({})".format( R1, I2, M3, D4, B4 )
   
   return rv

# @fn	 S
# @brief Decode ???.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def S( arg ):
   rv = rvalue( 4 )
   
   ops = gdb.execute( "x/4xb {}".format( arg ), to_string=True ).split( ) 
   
   D2 = int( ops[3], 16 ) >> 4
   B2 = ( ( int( ops[3], 16 ) & 0x0f ) << 8 ) | int( ops[4], 16 )
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                 int( ops[2], 16 ),
                                                 int( ops[3], 16 ),
                                                 int( ops[4], 16 ) )
   rv._asm = "{}({})".format( D2, B2 )
   
   return rv

# @fn	 S_I
# @brief Decode ???.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def S_I( arg ):
   rv = rvalue( 4 )
   
   ops = gdb.execute( "x/4xb {}".format( arg ), to_string=True ).split( ) 
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                 int( ops[2], 16 ),
                                                 int( ops[3], 16 ),
                                                 int( ops[4], 16 ) )
   rv._asm = ""
   
   return rv

# @fn	 SI
# @brief Decode storage and immediate format instructions.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def SI( arg ):
   rv = rvalue( 4 )
   
   ops = gdb.execute( "x/4xb {}".format( arg ), to_string=True ).split( ) 
   
   D1 = ( ( int( ops[3], 16 ) & 0x0f ) << 8 ) | int( ops[4], 16 ) 
   B1 = int( ops[3], 16 ) >> 4
   I2 = int( ops[2], 16 )
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                 int( ops[2], 16 ),
                                                 int( ops[3], 16 ),
                                                 int( ops[4], 16 ) )
   rv._asm = "{}({}),{}".format( D1, B1, I2 )
   
   return rv

# @fn	 SIY
# @brief Decode storage and immediate format instructions.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def SIY( arg ):
   rv = rvalue( 6 )
   
   ops = gdb.execute( "x/6xb {}".format( arg ), to_string=True ).split( ) 
   
   I2 = int( ops[2], 16 )
   B1 = int( ops[3], 16 ) >> 4
   D1 = ( ( int( ops[5], 16 ) << 12 ) |
          ( ( int( ops[3], 16 ) & 0x0f ) << 8 ) |
          ( int( ops[4], 16 ) ) )
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                              int( ops[2], 16 ),
                                                              int( ops[3], 16 ),
                                                              int( ops[4], 16 ),
                                                              int( ops[5], 16 ),
                                                              int( ops[6], 16 ) )
   rv._asm = "{}({}),{}".format( D1, B1, I2 )
   
   return rv

# @fn	 SIL
# @brief Decode storage and immediate format instructions.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def SIL( arg ):
   rv = rvalue( 6 )
   
   ops = gdb.execute( "x/6xb {}".format( arg ), to_string=True ).split( ) 
   
   D1 = ( ( int( ops[3], 16 ) & 0x0f ) << 16 ) | int( ops[4], 16 )
   B1 = int( ops[3], 16 ) >> 4
   I2 = ( int( ops[5], 16 ) << 16 ) | int( ops[6], 16 )
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                              int( ops[2], 16 ),
                                                              int( ops[3], 16 ),
                                                              int( ops[4], 16 ),
                                                              int( ops[5], 16 ),
                                                              int( ops[6], 16 ) )
   rv._asm = "{}({}),{}".format( D1, B1, I2 )
   
   return rv

# @fn    SS
# @brief Decode storage and storage format instructions.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def SS( arg ):
   rv = rvalue( 6 )
   
   ops = gdb.execute( "x/6xb {}".format( arg ), to_string=True ).split( ) 
   
   D1 = ( int( ops[3], 16 ) & 0x0f ) << 16 | int( ops[4], 16 )
   L  = int( ops[2], 16 )
   B1 = int( ops[3], 16 ) >> 4
   D2 = ( int( ops[5], 16 ) & 0x0f ) << 16 | int( ops[6], 16 )
   B2 = int( ops[4], 16 ) >> 4
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                              int( ops[2], 16 ),
                                                              int( ops[3], 16 ),
                                                              int( ops[4], 16 ),
                                                              int( ops[5], 16 ),
                                                              int( ops[6], 16 ) )
   rv._asm = "{}({},{}),{}({})".format( D1, L, B1, D2, B2 )
   
   return rv

# @fn    SS_R
# @brief Decode storage and storage format instructions.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def SS_R( arg ):
   rv = rvalue( 6 )
   
   ops = gdb.execute( "x/6xb {}".format( arg ), to_string=True ).split( ) 
    
   R1 = int( ops[2], 16 ) >> 4
   R3 = int( ops[2], 16 ) & 0x0f
   D2 = ( ( int( ops[3], 16 ) & 0x0f ) << 8 ) | int( ops[4], 16 )
   B2 = int( ops[3], 16 ) >> 4
   D4 = ( ( int( ops[5], 16 ) & 0x0f ) << 8 ) | int( ops[6], 16 )
   B4 = int( ops[5], 16 ) >> 4
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                              int( ops[2], 16 ),
                                                              int( ops[3], 16 ),
                                                              int( ops[4], 16 ),
                                                              int( ops[5], 16 ),
                                                              int( ops[6], 16 ) )
   rv._asm = "R{},R{},{}({}),{}({})".format( R1, R3, D2,
                                                         B2, D4, B4 )
   
   return rv

# @fn    SS_L
# @brief Decode storage and storage format instructions.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def SS_L( arg ):
   rv = rvalue( 6 )
   
   ops = gdb.execute( "x/6xb {}".format( arg ), to_string=True ).split( ) 
    
   D1 = ( ( int( ops[3], 16 ) & 0x0f ) << 8 ) | int( ops[4], 16 )
   L1 = int( ops[2], 16 ) >> 4
   B1 = int( ops[3], 16 ) >> 4
   D2 = ( ( int( ops[5], 16 ) & 0x0f ) << 8 ) | int( ops[6], 16 )
   L2 = int( ops[2], 16 ) & 0x0f
   B2 = int( ops[5], 16 ) >> 4
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                              int( ops[2], 16 ),
                                                              int( ops[3], 16 ),
                                                              int( ops[4], 16 ),
                                                              int( ops[5], 16 ),
                                                              int( ops[6], 16 ) )
   rv._asm = "{}(L{},{}),{}(L{},{})".format( D1, L1, B1,
                                                         D2, L2, B2 )
   
   return rv

# @fn    SS_D
# @brief Decode storage and storage format instructions.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def SS_D( arg ):
   rv = rvalue( 6 )
   
   ops = gdb.execute( "x/6xb {}".format( arg ), to_string=True ).split( ) 
    
   D1 = ( ( int( ops[3], 16 ) & 0x0f ) << 8 ) | int( ops[4], 16 )
   B1 = int( ops[3], 16 ) >> 4
   D2 = ( ( int( ops[5], 16 ) & 0x0f ) << 8 ) | int( ops[6], 16 )
   L2 = int( ops[2], 16 )
   B2 = int( ops[5], 16 ) >> 4
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                              int( ops[2], 16 ),
                                                              int( ops[3], 16 ),
                                                              int( ops[4], 16 ),
                                                              int( ops[5], 16 ),
                                                              int( ops[6], 16 ) )
   rv._asm = "{}({}),{}(L{},{})".format( D1, B1, D2, L2, B2 )
   
   return rv

# @fn    SS_RR
# @brief Decode storage and storage format instructions.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def SS_RR( arg ):
   rv = rvalue( 6 )
   
   ops = gdb.execute( "x/6xb {}".format( arg ), to_string=True ).split( ) 
    
   R1 = int( ops[2], 16 ) >> 4
   D2 = ( ( int( ops[3], 16 ) & 0x0f ) << 8 ) | int( ops[4], 16 )
   B2 = int( ops[3], 16 ) >> 4
   R3 = int( ops[2], 16 ) & 0x0f
   D4 = ( ( int( ops[5], 16 ) & 0x0f ) << 8 ) | int( ops[6], 16 )
   B4 = int( ops[5], 16 ) >> 4
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                              int( ops[2], 16 ),
                                                              int( ops[3], 16 ),
                                                              int( ops[4], 16 ),
                                                              int( ops[5], 16 ),
                                                              int( ops[6], 16 ) )
   rv._asm = "R{},{}({}),R{},{}({})".format( R1, D2, B2,
                                                         R3, D4, B4 )
   
   return rv

# @fn    SS_I
# @brief Decode storage and storage format instructions.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def SS_I( arg ):
   rv = rvalue( 6 )
   
   ops = gdb.execute( "x/6xb {}".format( arg ), to_string=True ).split( ) 
    
   D1 = ( ( int( ops[3], 16 ) & 0x0f ) << 8 ) | int( ops[4], 16 )
   L1 = int( ops[2], 16 ) >> 4
   B1 = int( ops[3], 16 ) >> 4
   D2 = ( ( int( ops[5], 16 ) & 0x0f ) << 8 ) | int( ops[6], 16 )
   B2 = int( ops[5], 16 ) >> 4
   I3 = int( ops[2], 16 ) & 0x0f
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                              int( ops[2], 16 ),
                                                              int( ops[3], 16 ),
                                                              int( ops[4], 16 ),
                                                              int( ops[5], 16 ),
                                                              int( ops[6], 16 ) )
   rv._asm = "{}(L{},{}),{}({}),{}".format( D1, L1, B1,
                                                         D2, B2, I3 )
   
   return rv

# @fn    SS_DD
# @brief Decode storage and storage format instructions.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def SS_DD( arg ):
   rv = rvalue( 6 )
   
   ops = gdb.execute( "x/6xb {}".format( arg ), to_string=True ).split( ) 
    
   D1 = ( ( int( ops[3], 16 ) & 0x0f ) << 8 ) | int( ops[4], 16 )
   R1 = int( ops[2], 16 ) >> 4
   B1 = int( ops[3], 16 ) >> 4
   D2 = ( ( int( ops[5], 16 ) & 0x0f ) << 8 ) | int( ops[6], 16 )
   B2 = int( ops[5], 16 ) >> 4
   R3 = int( ops[2], 16 ) & 0x0f
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                              int( ops[2], 16 ),
                                                              int( ops[3], 16 ),
                                                              int( ops[4], 16 ),
                                                              int( ops[5], 16 ),
                                                              int( ops[6], 16 ) )
   rv._asm = "{}(R{},{}),{}({}),R{}".format( D1, R1, B1,
                                                         D2, B2, R3 )
   
   return rv

# @fn    SSE
# @brief Decode
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def SSE( arg ):
   rv = rvalue( 6 )
   
   ops = gdb.execute( "x/6xb {}".format( arg ), to_string=True ).split( ) 
   
   D1 = ( ( int( ops[3], 16 ) & 0x0f ) << 8 ) | int( ops[4], 16 )
   B1 = int( ops[3], 16 ) >> 4
   D2 = ( ( int( ops[5], 16 ) & 0x0f ) << 8 ) | int( ops[6], 16 )
   B2 = int( ops[5], 16 ) >> 4
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                              int( ops[2], 16 ),
                                                              int( ops[3], 16 ),
                                                              int( ops[4], 16 ),
                                                              int( ops[5], 16 ),
                                                              int( ops[6], 16 ) )
   rv._asm = "{}({}),{}({})".format( D1, B1, D2, B2 )
   
   return rv

# @fn    SSF
# @brief Decode
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def SSF( arg ):
   rv = rvalue( 6 )
   
   ops = gdb.execute( "x/6xb {}".format( arg ), to_string=True ).split( ) 
   
   D1 = ( int( ops[3], 16 ) & 0x0f ) << 8 | int( ops[4], 16 )
   B1 = int( ops[3], 16 ) >> 4
   D2 = ( int( ops[5], 16 ) & 0x0f ) << 8 | int( ops[6], 16 )
   B2 = int( ops[5], 16 ) >> 4
   R3 = int( ops[2], 16 ) >> 4
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                              int( ops[2], 16 ),
                                                              int( ops[3], 16 ),
                                                              int( ops[4], 16 ),
                                                              int( ops[5], 16 ),
                                                              int( ops[6], 16 ) )
   rv._asm = "{}({{}),{}({}),{}".format( D1, B1, D2, B2, R3 )
   
   return rv

# @fn    E
# @brief Decode
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def E( arg ):
   rv = rvalue( 2 )
   
   ops = gdb.execute( "x/2xb {}".format( arg ), to_string=True ).split( ) 
   
   rv._mac = "{:02X}{:02X}".format( int( ops[1], 16 ), int( ops[2], 16 ) )
   rv._asm = ""
   
   return rv

# @fn    Dd
# @brief Decode the DIAGNOSE instruction.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def Dd( arg ):
   rv = rvalue( 4 )
   
   ops = gdb.execute( "x/4xb {}".format( arg ), to_string=True ).split( ) 
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                 int( ops[2], 16 ),
                                                 int( ops[3], 16 ),
                                                 int( ops[4], 16 ) )
   rv._asm = ""
   
   return rv

# @fn    I
# @brief Decode
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def I( arg ):
   rv = rvalue( 2 )
   
   ops = gdb.execute( "x/2xb {}".format( arg ), to_string=True ).split( ) 
   
   I = int( ops[2], 16 )
   
   rv._mac = "{:02X}{:02X}".format( int( ops[1], 16 ), int( ops[2], 16 ) )
   rv._asm = "{}".format( I )
   
   return rv

# @fn    NYI
# @brief Place holder for not yet implemented functionality.
#
# @param[in] arg - The address of the instruction to decode.
# @return rv - A rvalue structure.
def NYI( arg ):
   rv = rvalue( 6 )
   
   ops = gdb.execute( "x/6xb {}".format( arg ), to_string=True ).split( ) 
   
   rv._mac = "{:02X}{:02X} {:02X}{:02X} {:02X}{:02X}".format( int( ops[1], 16 ),
                                                              int( ops[2], 16 ),
                                                              int( ops[3], 16 ),
                                                              int( ops[4], 16 ),
                                                              int( ops[5], 16 ),
                                                              int( ops[6], 16 ) )
   rv._asm = "?NYI?"
   
   return rv
