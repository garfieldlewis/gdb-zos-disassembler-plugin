# The main SDM modules that will load all the other required modules
1. source <plugin-dir>/sdm.py

# The top level commands are found in these modules
1. source <plugin-dir>/zdisass.py
  * zdisass
2. source <plugin-dir>/zinfo.py
  * infosdm
  * infozthreads
  * infozbreakpoints
3. source <plugin-dir>/zmem.py
  * zmemory
4. source <plugin-dir>/zfuncs.py
  * zthreads

# Auxilary commands found in these modules modules
## These are internal commands that are used by the top level commands
1. source <plugin-dir>/apis/instructions.py
  * getInst
  * zos_2byte_mnemonics
  * zos_3byte_mnemonics
  * zos_4byte_mnemonics
2. source <plugin-dir>/apis/decoder.py
  * rvalue
  * RR
  * RR_R
  * RRE
  * RRE_R
  * RRE_N
  * RRR
  * RRS
  * RRF
  * RRF_R
  * RRF_RM
  * RRF_M
  * RRF_RMRM
  * RRF_RRM
  * RX
  * RX_M
  * RXE
  * RXF
  * RXY
  * RXY_M
  * RS
  * RS_M
  * RS_D
  * RSY
  * RSY_M
  * RSI
  * RSL
  * RI
  * RI_M
  * RIL
  * RIL_M
  * RIE
  * RIE_M
  * RIE_IM
  * RIE_MI
  * RIE_RI
  * RIE
  * S
  * S_I
  * SI
  * SIY
  * SIL
  * SS
  * SS_R
  * SS_L
  * SS_D
  * SS_RR
  * SS_I
  * SS_DD
  * SSE
  * SSF
  * E
  * Dd
  * I
  * NYI
3. source <plugin-dir>/apis/common.py
  * isSDMEnabled
  * ebcdic

# Testing considerations
1. info sdm
2. info zthreads
3. info zbreakpoints
4. zdisass regs->mainstor+regs->psw.ia.F
5. zdisass 0x7ffb40a2b41c,+150
