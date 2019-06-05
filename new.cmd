@ECHO OFF
SETLOCAL

SET "PYTHON_TEMPLATE=bin\default_template.py"
SET "PYTHON_PARSE_SINGLE=bin\parse_single_problem.py"


REM This gets the datetime format for the header info
SET X=
FOR /F "skip=1 delims=" %%x in ('wmic os get localdatetime') do IF NOT DEFINED X SET X=%%x
SET DATE.YEAR=%X:~0,4%
SET DATE.MONTH=%X:~4,2%
SET DATE.DAY=%X:~6,2%
SET DATE.HOUR=%X:~8,2%
SET DATE.MINUTE=%X:~10,2%
SET DATE.SECOND=%X:~12,2%
SET DATE.FRACTIONS=%X:~15,6%
SET DATE.OFFSET=%X:~21,4%

REM Use these as you like
SET "YYYYMMDD=%DATE.YEAR%.%DATE.MONTH%.%DATE.DAY%"
SET "YYYYMMDD_HHMMSS=%DATE.YEAR%%DATE.MONTH%%DATE.DAY%_%DATE.HOUR%%DATE.MINUTE%%DATE.SECOND%"

REM Prepend some common header information
ECHO # Problem #    : %1%2 > %1%2.py
ECHO # Created on   : %YYYYMMDD% >> %1%2.py

REM Copy our template to a new file and name it the problem id
IF EXIST %PYTHON_TEMPLATE% (
    TYPE %PYTHON_TEMPLATE% >> %1%2.py
)

REM TODO: cleanup old files here

REM Parse the html of the target URL on codeforces and create in/out files for each test case
call .env\Scripts\python %PYTHON_PARSE_SINGLE% %1 %2

REM End of normal execution
GOTO :DONE

REM For script-execution errors, e.g. missing argument
:SYNTAX
ECHO Invalid syntax. Usage: "%~nx0"

REM Done
:DONE
ENDLOCAL