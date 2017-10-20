# author: ax
'''
 dye.py
 -
 ANSI control codes to print colorz in terminals
 -------------------------------------------
  - Basic 8 colorz and 8 high intensity version
  - Some styles
'''

_ESC = '\x1b'
_CSI = _ESC+'[' # Control Sequence Initiator

# ANSI Select Graphic Rendition (SGR) control code = CSI+SGRparameters+m
# parameters are separated with ;

# Some styles
class style:
	RESET_ALL		= _CSI+'0m'
	BOLD 			= _CSI+'1m'
	DIM 			= _CSI+'2m'
	UNDERL 			= _CSI+'4m'
	BLINK 			= _CSI+'5m'


	RESET_BOLD 		= _CSI+'21m'
	RESET_DIM 		= _CSI+'22m'
	RESET_UNDERL	= _CSI+'24m'
	RESET_BLINK 	= _CSI+'25m'

	REVERSE			= _CSI+'7m'
	RESET_REVERSE	= _CSI+'27m'
	HIDDEN			= _CSI+'8m'
	RESET_HIDDEN	= _CSI+'28m'

# 8 colors SGR parameters 40-47 select the background color
class bg:
	RESET_ALL	= _CSI+'0m'
	RESET 		= _CSI+'49m'
	BLACK		= _CSI+'40m'
	RED			= _CSI+'41m'
	GREEN		= _CSI+'42m'
	YELLOW		= _CSI+'43m'
	BLUE		= _CSI+'44m'
	MAGENTA		= _CSI+'45m'
	CYAN		= _CSI+'46m'
	WHITE		= _CSI+'47m'
# 8 colors SGR parameters 100-107 select the
# background high intensity color
	HBLACK		= _CSI+'100m'
	HRED		= _CSI+'101m'
	HGREEN		= _CSI+'102m'
	HYELLOW		= _CSI+'103m'
	HBLUE		= _CSI+'104m'
	HMAGENTA	= _CSI+'105m'
	HCYAN		= _CSI+'106m'
	HWHITE		= _CSI+'107m'

# 8 colors SGR parameters 30-37 select the foreground color
class fg:
	RESET_ALL	= _CSI+'0m'
	RESET 		= _CSI+'39m'
	BLACK		= _CSI+'30m'
	RED			= _CSI+'31m'
	GREEN		= _CSI+'32m'
	YELLOW		= _CSI+'33m'
	BLUE		= _CSI+'34m'
	MAGENTA		= _CSI+'35m'
	CYAN		= _CSI+'36m'
	WHITE		= _CSI+'37m'
# 8 colors SGR parameters 90-97 select the
# foreground high intensity color
	HBLACK		= _CSI+'90m'
	HRED		= _CSI+'91m'
	HGREEN		= _CSI+'92m'
	HYELLOW		= _CSI+'93m'
	HBLUE		= _CSI+'94m'
	HMAGENTA	= _CSI+'95m'
	HCYAN		= _CSI+'96m'
	HWHITE		= _CSI+'97m'
