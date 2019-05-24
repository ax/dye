=== 
dye
===

Lightweight module with ANSI control codes to dye python scripts.

This package contains just one module,
it consist only on some declaration,
something like:

``RED = \x1b[31m``

The module has the trivial task of extend the namespace of your application to include
terms you can use to color and format terminal output using ANSI control codes.

Usage
-----

.. code:: python

	from dye import *

	print fg.BLUE+"colorz"+fg.RESET
	print fg.LBLUE+"colorz"+fg.RESET

	print style.BOLD + fg.GREEN + bg.YELLOW + "colorz" + style.RESET_ALL

The strings contained in the colorz variables are ANSI control codes.

In this set there are:

- the basic 8 colors

.. code:: python

	BLACK
	RED
	GREEN 
	YELLOW
	BLUE
	MAGENTA
	CYAN
	WHITE

- their high intensity versions

.. code:: python

	HBLACK
	HRED
	HGREEN 
	HYELLOW
	HBLUE
	HMAGENTA
	HCYAN
	HWHITE

- The following styles are supported:

.. code:: python

	BOLD
	DIM
	UNDERL
	BLINK
	REVERSE
	HIDDEN

- reset sequences

.. code:: python

	RESET_ALL
	RESET_BOLD
	RESET_DIM
	RESET_UNDERL
	RESET_BLINK
	RESET_REVERSE
	RESET_HIDDEN

You can set text color using ``fg`` codes: ``fg.RED``

You can set background color using ``bg`` codes: ``bg.RED``

You can set styles using ``style`` codes: ``style.BOLD``

