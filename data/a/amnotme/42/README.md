
# Libft

### libft  
My implementation of the standard library as a project for 42. 

### libft-unit-test  
A testing script built by 42 students to test the libft  
project.



------------------------------------------------------------------  

# Summer In San Francisco  

A dash project where students are given 42 minutes to complete.  

-----------------------------------------------------------------
# Fillit  

fillit is program which seeks to find the smallest space possible to fit 
valid tetramino pieces. (Pieces which are composed of 4 hash marks.


-----------------------------------------------------------------
# Get Next Line

Get next line is a function that allows the user to obtain the next line
from stdin or from a file without the need of knowing how long the file
or line is to begin with.

-----------------------------------------------------------------  
# FDF

Fdf is an implemenation of a basic wireframe using the minilibx library.
 
----------------------------------------------------------------- 

# Ft_Latin

----------------------------------------------------------------- 

# Init

----------------------------------------------------------------- 

# Piscine PHP

## Ongoing right now  

----------------------------------------------------------------
	 
# PHP 

## Day 00

![Day 00 Score](Day00/Score_Day00.png)




*ex00* -> Basic or home ->		basics.html  
*ex01* -> Mendeleiev ->			mendeleiev.html  
*ex02* -> Day of the 43 ->		doft.html doft.css resources/  
*ex03* -> The shrunk agent ->	responsive.html responsive.css  
*ex04* -> SNCF Sandwich ->		menu.html menu.css  
*ex05* -> SCUMM	->				-n/a-  



![Periodic Table](Day00/Periodic_Table.gif)

## Day01

-----------------------------------------------------------------------------
##	libft Unit tests

libft-unit-test is a complete testing suite for 42's libft project, allowing you to test your lib, track your progress and benchmarking your lib (with system's libc or with another lib)

# Installation
You must have the following file structure:
```
.
|- libft/
|- libft-unit-tests/
```
Whereas:
	`libft` is your project folder.
	`libft-unit-tests` is the folder containing this repository.

Afterwards, you can just `make`.

(NOTE: Before running `make`, you can edit the `LIBFTDIR` variable containing the path to your libft folder.)

# Usage

Run `make f` or `./run_test` when inside the repo's directory. `./run_test -b` to use the Benchmark mode. (`-b` option to compare with system's libc and `-v <libft file>` option to compare with another libft file (should be `libft.so`).

the `-nospeed` option is available if you're mad enough at your optimization. :)

# Linux

To get it work on linux:

+ Install this two packages libbsd-dev and libncurses-dev
+ Add a rule called 'so' in your Makefile to compile your libft in dynamic library instead of static (must be called "libft.so").

# Screenshots

### Default mode
![Unit Testing](https://camo.githubusercontent.com/d48094cc4a8bccb4610a3990794916ee74be9614/687474703a2f2f696d6167652e6e6f656c736861636b2e636f6d2f66696368696572732f323031362f33352f313437323932333734302d636170747572652d642d656372616e2d323031362d30392d30332d612d31392d32362d33322e706e67)

### Benchmark mode
![Benchmarking](https://camo.githubusercontent.com/89f54b0ab69793e585c503ac2d35ac73f09d053a/687474703a2f2f696d6167652e6e6f656c736861636b2e636f6d2f66696368696572732f323031362f33352f313437323932333734392d636170747572652d642d656372616e2d323031362d30392d30332d612d31392d32372d30392e706e67)
#
#
#  14/10/2015
#  ol@staff.42.fr
#

MinilibX

Interface simplifiee de programmation graphique pour debutant
#

Cette minilibX est la version native pour MacOSX.
[ Elle n'utilise plus les librairies graphiques X11, ni XQuartz le serveur X pour MacOSX. ]
L'interface / l'API, reste identique a la version precedente. Les man presents dans la minilibX
d'origine sont toujours valides.

Le fichier mlx.h a inclure dans vos programmes rapelle les petites differences de comportement
entre les 2 versions, dues a la gestion graphique differente selon les systemes d'exploitation.

#

Cette version utilise le systeme de fenetrage Cocoa de MacOSX ( AppKit ), et les primitives
graphiques OpenGL moderne.

#

License: la MinilibX macos est fournie sous license BSD: Copyright Olivier Crouzet - 2014-2015
         la MinilibX est fournie sous license BSD:  Copyright Olivier Crouzet - 1999-2015
#
# filllit  

  fillit project done in collaboration with gmalpart for 42 school
# INIT

-------------------------------------------------
## Goals

This first project, init, will give you the opportunity to discover system and network basic commands,   
many of the services used on a server machine, as well as a few ideas of scripts that can be useful   
for SysAdmins on a daily basis.

### Network

-------------------------------------------------


### System
-------------------------------------------------
### Scripts . 
-------------------------------------------------
# FT_RETRO

###  Subject and Goals

	The goal of this project is to implement a simplistic shoot-em-up-style game in your
	terminal. For those of you who don’t know what that kind of game is (shame on you, by
	the way), have a look at Gradius, R-Type, etc...

	You will use a ’screen’ made up of a grid of ’squares’, that you can equate to the
	characters on your terminal, so that the entities of your game are each represented by a
	character on screen.

###### Basic Requirements

- [x] Single-player
- [x] Display using the ```ncurses```  library
- [x] Horizontal or vertical scrolling (The screen area moves through the world, very
	much like in R-Type for example)
- [ ] Random enemies
- [x] The player can shoot at enemies
- [ ] Basic collision handling (If an enemy touches you, you die)
- [ ] Game entities occupy one ’square’ of the map only.
- [x] Frame-based timing

###### Game Dynamics

- [x] Acquire input (Player controls, network, etc ...)
- [ ] Update game entities
- [x] Render display
- [ ] Repeat until game ends !


###### Essential Features Before Bonus Implementation

- [x] Displaying score, time, number of lives, etc... on screen
- [x] Clock-based timing (Use whichever system facility or library you like)
- [x] Entities that can occupy multiple squares
- [ ] Enemies can also shoot
- [x] Scenery (Collidable objects or simple background)

###### Bonus Suggestions

- [ ] Large and hard-to-beat boss enemies
- [ ] Enemies have a scripted behaviour
- [ ] Multiplayer, either on the same keyboard or through the network if you’re feeling cocky
- [ ] Scripted game worlds, with pre-determined batches of enemies

### Architecture of the classes

			UML DIAGRAMS OF CLASSES
```
		------------------------------------
				Entity
		------------------------------------
		# _hp				Int
		# _lives			Int
		# _posX				Int
		# _posY 			Int
		# _speed			Int
		# _name				String
		# _sprite			String
		------------------------------------
		+ getHp( void )			Int
		+ getLives( void )		Int
		+ getPosX( void ) 		Int
		+ getPoxY( void )		Int
		+ getSpeed( void )		Int
		+ getName( void )		String
		+ getSprite( void )		String
		+ setHp( const int )		Void
		+ setLives( const int )		Void
		+ setPosX( const int ) 		Void
		+ setPosY( const int )		Void
		+ setSpeed( const int ) 	Void
		+ setName( const string)	Void
		------------------------------------
```
```
		------------------------------------
				Enemy : Entity
		------------------------------------
		------------------------------------
		------------------------------------
```
```
		------------------------------------
				Player : Entity
		------------------------------------
		------------------------------------
		------------------------------------
```
```
		------------------------------------
				Rock : Entity
		------------------------------------
		------------------------------------
		------------------------------------
```
```
		------------------------------------
				Weapon : Entity
		------------------------------------
		------------------------------------
		------------------------------------
```

# Abstract VM

*Summary: The purpose of this project is to create a simple virtual machine 
that can interpret programs written in a basic assembly language.*

## The Project

AbstractVM is a machine that uses a stack to compute simple arithmetic expressions.
These arithmetic expressions are provided to the machine as basic assembly programs.

### The Assembly Language

this is an example of the assembly program.

```
1 ; -------------
2 ; exemple.avm -
3 ; -------------
4
5 push int32(42)
6 push int32(33)
7
8 add
9
10 push float(44.55)
11
12 mul
13
14 push double(42.42)
15 push int32(42)
16
17 dump
18
19 pop
20
21 assert double(42.42)
22
23 exit
```
#### Description of the assembly language


AbstractVM is composed of a series of instructions, with one instruction per
line.  **However**, AbstractVM's language has limited type system, which
is a **major** difference from other real world assembly languages.

- **Comments**:  Comments start with a ’;’ and finish with a newline. 
A comment can be either at the start of a line, or after an instruction.

- **push _v_:** Pushes the value v at the top of the stack. 
The value v must have one ofthe following form:
  - **int8(n):** Creates an 8-bit integer with value n.
  - **int16(n):** Creates a 16-bit integer with value n
  - **int32(n):** Creates a 32-bit integer with value n.
  - **float(z):** Creates a float with value z.
  - **double(z):** Creates a double with value z.

- **pop:**  Unstacks the value from the top of the stack. 
If the stack is empty, theprogram execution must stop with an error.

- **dump:**  Displays each value of the stack, from the most recent one to the 
oldest one **WITHOUT CHANGING** the stack. Each value is separated from the 
next one by a newline.

- **assert: _v_** Asserts that the value at the top of the stack is equal to the
one passed as parameter for this instruction. If it is not the case, the program
execution must stop with an error. The value _v_ has the same form that those 
passed as parameters to the instruction **push**.

- **add:**  Unstacks the first two values on the stack, adds them together and 
stacks the result. _If_ the number of values on the stack is strictly inferior 
to 2, the program execution **must** stop with an error.

- **sub:** Unstacks the first two values on the stack, subtracts them, then 
stacks the result. _If_ the number of values on the stack is strictly inferior 
to 2, the program execution **must** stop with an error.

- **mul:** Unstacks the first two values on the stack, multiplies them, 
then stacks the result. _If_ the number of values on the stack is strictly 
inferior to 2, the program execution **must** stop with an error.

- **div:**  Unstacks the first two values on the stack, divides them, then 
stacks the result. _If_ the number of values on the stack is strictly inferior 
to 2, the program execution **must** stop with an error. Moreover, _if_ the 
divisor is equal to 0, the program execution **must** stop with an error too. 
Chatting about floating point values is relevant a this point. If you don’t 
understand why, some will understand. The linked question is an open one, 
there’s no definitive answer.

- **mod:** Unstacks the first two values on the stack, calculates the modulus, 
then stacks the result. _If_ the number of values on the stack is strictly 
inferior to 2, the program execution **must** stop with an error. Moreover, _if_
the divisor is equal to 0, the program execution **must** stop with an error 
too. Same note as above about _fp values_.

- **print:** Asserts that the value at the top of the stack is an **8-bit** 
integer. (_If_ not, see the instruction assert), then interprets it as an ASCII
value and displays the corresponding character on the standard output.

- **exit:** Terminate the execution of the current program. _If_ this 
instruction does not appear after all other instructions have been processed, 
the execution **must** stop with an error

```
For non commutative operations, consider the stack v1 on v2 on
stack_tail, the calculation in infix notation v2 op v1.
```

When a computation involves two operands of different types, the value returned
has the type of the more precise operand. Please do note that because of the 
extensibility of the machine, the precision question is not a trivial one. 
This is covered more in details later in this document.

### Grammar

The assembly language of AbstractVM is generated from the following grammar 
(**#** corresponds to the end of the input, not to the character ’#’):

```
1 S := INSTR [SEP INSTR]* #
2
3 INSTR :=
4 push VALUE
5 | pop
6 | dump
7 | assert VALUE
8 | add
9 | sub
10 | mul
11 | div
12 | mod
13 | print
14 | exit
15
16 VALUE :=
17 int8(N)
18 | int16(N)
19 | int32(N)
20 | float(Z)
21 | double(Z)
22
23 N := [-]?[0..9]+
24
25 Z := [-]?[0..9]+.[0..9]+
26
27 SEP := '\n'+
```

### Errors

When one of the following cases is encountered, AbstractVM must raise an 
exception and stop the execution of the program cleanly. It is forbidden to 
raise **scalar exceptions**. Moreover your exception classes must inherit 
from ``` std::exception ```.

- The assembly program includes one or several lexical errors or syntactic errors.
- An instruction is unknown
- Overflow on a value
- Underflow on a value
- Instruction pop on an empty stack
- Division/modulo by 0
- The program doesn’t have an exit instruction
- An assert instruction is not true
- The stack is composed of strictly less that two values when an arithmetic 
instruction is executed.

### Execution

Your machine must be able to run programs from a file passed as a parameter 
and from the standard input. When reading from the standard input, the end of 
the program is indicated by the special symbol ";;" otherwise absent.

examples:

```
1 $>./avm
2 push int32(2)
3 push int32(3)
4 add
5 assert int32(5)
6 dump
7 exit
8 ;;
9 5
10 $>
```
```
1 $>cat sample.avm
2 ; -------------
3 ; sample.avm -
4 ; -------------
5
6 push int32(42)
7 push int32(33)
8 add
9 push float(44.55)
10 mul
11 push double(42.42)
12 push int32(42)
13 dump
14 pop
15 assert double(42.42)
16 exit
17 $>./avm ./sample.avm
18 42
19 42.42
20 3341.25
21 $>
```
```
1 $>./avm
2 pop
3 ;;
4 Line : Error : Pop on empty stack
5 $>
```
## Mandatory Part

### Generic Instructions

- You are free to use any compiler you like.
- Your code must compile with: -Wall -Wextra -Werror.
- You are free to use any C++ version you like.
- You are free to use any library you like.
- You must provide a Makefile with the usual rules.
- Any class that declares at least one attribute must be written in canonical 
form. Inheriting from a class that declares attributes does not count as 
declaring attributes.
- It’s forbidden to implement any function in a header file, except for 
templates and the virtual destructor of a base class.
- The “keyword” "using namespace" is forbidden.

### The IOperand interface

- Int8 : Representation of a signed integer coded on 8bits.
- Int16 : Representation of a signed integer coded on 16bits.
- Int32 : Representation of a signed integer coded on 32bits.
- Float : Representation of a float.
- Double : Representation of a double.

Each one of these operand classes **MUST** implement the following 
IOperand interface:

```
class IOperand {
public:
	virtual int getPrecision( void ) const = 0; // Precision of the type of the instance
	virtual eOperandType getType( void ) const = 0; // Type of the instance
	virtual IOperand const * operator+( IOperand const & rhs ) const = 0; // Sum
	virtual IOperand const * operator-( IOperand const & rhs ) const = 0; // Difference
	virtual IOperand const * operator*( IOperand const & rhs ) const = 0; // Product
	virtual IOperand const * operator/( IOperand const & rhs ) const = 0; // Quotient
	virtual IOperand const * operator%( IOperand const & rhs ) const = 0; // Modulo

	virtual std::string const & toString( void ) const = 0; // String representation of the instance
	virtual ~IOperand( void ) {}
};
```

### Creation of new Operand

New operands **MUST** be created via a "factory method". 
The member function must have this prototype:

```
IOperand const * createOperand( eOperandType type, std::string const & value ) const;
```

The ```eOperandType type``` is an enum defining the following values:
``` Int8, Int16, Int32, Float, Double```

Depending on the _enum_ value passed as a parameter, the member function 
createOperand creates a new IOperand by calling one of the following private 
member functions:

```
IOperand const * createInt8( std::string const & value ) const;
IOperand const * createInt16( std::string const & value ) const;
IOperand const * createInt32( std::string const & value ) const;
IOperand const * createFloat( std::string const & value ) const;
IOperand const * createDouble( std::string const & value ) const;
```

In order to choose the right member function for the creation of the new 
IOperand, you **MUST** create and use an array (here, a vector shows little 
interest) of pointers on member functions with enum values as index
###Version 0.1 :

- Builtin commands
	- Builtin exit
	- Builtin cd
	- Builtin echo
	- Builtin export
	- Builtin alias
	- Builtin unalias
- Parser 
	- Lexer ✅
	- type AST ✅
	- Parser ✅

- Execution
	- Operators (">" ">>" "<" "|" "||" "&&" ";")
	- Simple commands

- Errors Handling 

- Version 0.2 :
	- Builtin continue
	- Builtin history  
	- Builtin break
	- Builtin source
	- Builtin shopt

- Version 1.0
	- No leaks
	- No segs faults
	- No fd leaks
	- Norme

-changed builtin prototypes to return ints, so they can be used with logic operators

the convention is to return 0 on success or different code on failure;

-echo will always return 0, always success
-exit will not return? but will use sh->exit_code variable for exiting, or if argument given and argument is numeric it will use that as its exit code; for example "exit 123" will exit with code 123
-help builtin will always return 0, we need to change the help message to describe the shell and display builtin info
feature suggestion? maybe have help builtin describe each builtin separately, ie if user types "help cd" then display detailed information about cd and its options/functionality

-env builtin will always return 0, always successful because it only display environment variables and it does not fail
-setenv will return 0 if it succeeds, or 1 if variable name is not alphanumeric, also 1 if variable's first character is not alpha
 --setenv without parameters calls env() builtin (always returns 0)
-usetenv will return 0 if it succeeds, or 1 if given too few arguments, for ex "unsetenv" without a parameter will fail, return 1

the basics of a shell

	The shell runs in three different steps
	1. ) Read: read the commnad from standard input
	2. ) Parse: Separate the command string into a program and arguments.
3. ) Execute: Run the parsed command.
# Ft_bistromatic

### Goals

The goal of the porject is to write a program able to display the result of the  
of an arithmetic expression composed of numbers with infinite size expressed in  
any base, if GNU's bc can handle the size, the program should too.  

### Check of List
*Makefile  
*authorfile  
*parser  

# Ft_script

-----------------

This is a project which seeks to recode the script command

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    README.md                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: leopoldohernandez <Leo@42.us.org>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/05/01 11:32:33 by leopoldoh         #+#    #+#              #
#    Updated: 2018/05/01 11:32:35 by leopoldoh        ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


#
#
#  14/10/2015
#  ol@staff.42.fr
#

MinilibX

Interface simplifiee de programmation graphique pour debutant
#

Cette minilibX est la version native pour MacOSX.
[ Elle n'utilise plus les librairies graphiques X11, ni XQuartz le serveur X pour MacOSX. ]
L'interface / l'API, reste identique a la version precedente. Les man presents dans la minilibX
d'origine sont toujours valides.

Le fichier mlx.h a inclure dans vos programmes rapelle les petites differences de comportement
entre les 2 versions, dues a la gestion graphique differente selon les systemes d'exploitation.

#

Cette version utilise le systeme de fenetrage Cocoa de MacOSX ( AppKit ), et les primitives
graphiques OpenGL moderne.

#

License: la MinilibX macos est fournie sous license BSD: Copyright Olivier Crouzet - 2014-2015
         la MinilibX est fournie sous license BSD:  Copyright Olivier Crouzet - 1999-2015
#
#
#
#  14/10/2015
#  ol@staff.42.fr
#

MinilibX

Interface simplifiee de programmation graphique pour debutant
#

Cette minilibX est la version native pour MacOSX.
[ Elle n'utilise plus les librairies graphiques X11, ni XQuartz le serveur X pour MacOSX. ]
L'interface / l'API, reste identique a la version precedente. Les man presents dans la minilibX
d'origine sont toujours valides.

Le fichier mlx.h a inclure dans vos programmes rapelle les petites differences de comportement
entre les 2 versions, dues a la gestion graphique differente selon les systemes d'exploitation.

#

Cette version utilise le systeme de fenetrage Cocoa de MacOSX ( AppKit ), et les primitives
graphiques OpenGL moderne.

#

License: la MinilibX macos est fournie sous license BSD: Copyright Olivier Crouzet - 2014-2015
         la MinilibX est fournie sous license BSD:  Copyright Olivier Crouzet - 1999-2015
#
