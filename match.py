'''python 3.10.4 introduces  Structural Pattern Matching
this introduces the match and case  statements which can be applied in different areas
      
      Syntax and operation
      
      match subject:
        case <pattern_1>:
            <action_1>
        case <pattern_2>:
            <action_2>
        case <pattern_3>:
            <action_3>
        case _:
            <action_wildcard>
 '''
 #for example
 ## Creating a function that helps user understan python errors
from fileinput import filename
from os import mkdir


def python_errors(error):
    match error:
        case 'KeyError':
            print('The inputted key is not recognised in the dictionary')

        case 'KeyboardInterrupt':
            print('Alert! Experienced Keyboard Interrupt')
        case 'MemoryError':
            print('Alert This operation ran out of memory')
        case 'NameError':
            print('Sorry, Python does not recognize this variable name')
        case 'SyntaxError':
            print('Python does not understand your instruction, you probably made typographical error')
python_errors('KeyError')

python_errors('KeyboardInterrupt')

python_errors('KeyboardInterrupt')

python_errors( 'NameError')
python_errors('SyntaxError')

# Second example
def mac_command(command: str):# you can indicate the datatype to be used
    match command.split():
        case ['touch',filename]: # i'm not a mac book user, so some of commands maybe inaccurate
            print('Creating a new file')
        case ['cp', filename,]:
            print('copying file')
        case ['rm',filename]:
            print('Deleting the file')
        case _:
            print('unknown command')
    
         
mac_command('touch error.py')
mac_command('cp pop.py')
mac_command('rm pop.py',)
mac_command('t pop.py')

