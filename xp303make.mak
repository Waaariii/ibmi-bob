### Custom object definitions for XP303MAKE
### Included by the QSYSmake generic Makefile.

.PHONY: all
all: PFs LFs DSPFs MODULEs SRVPGMs PGMs make_post

### Group objects by type so they're compiled in the correct order.
PFs: FLDREF.FILE SO1SCP.FILE SYSOPT.FILE

LFs:

DSPFs: SO1001D.FILE

MODULEs: JSB067.MODULE

SRVPGMs:

PGMs: SO1001.PGM

### Rules
FLDREF.FILE: FLDREF.PF 
PGMSTS.FILE: PGMSTS.PF

SO1SCP.FILE: SO1SCP.PF FLDREF.FILE
SYSOPT.FILE: SYSOPT.PF FLDREF.FILE

SO1001D.FILE: SO1001D.DSPF FLDREF.FILE  # Eventually add message file here.

SO1001.MODULE: SO1001.RPGLE SO1001D.FILE SYSOPT.FILE SO1SCP.FILE PGMOPT.FILE PGMSTS.FILE
JSB067.MODULE: JSB067.C

SO1001.PGM: SO1001.MODULE
JSB067.PGM: JSB067.MODULE
JSB010.MODULE: JSB010.SQLRPGLE