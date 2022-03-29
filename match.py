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

python_errors('KeyError')

python_errors('KeyboardInterrupt')

python_errors('KeyboardInterrupt')

python_errors( 'NameError')