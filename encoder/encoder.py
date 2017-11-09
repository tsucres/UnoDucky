import sys
import os
import argparse



current_line = 0
ducky_script = ""
ducky_lines = []

# =======================================================
# The following functions handle each a rubber ducky 
# command. They take the eventual parameter as argument.
# =======================================================

def ducky_STRING(text):
    rtn = b''
    for c in text:
        rtn += char_to_byte(c)

    return rtn

def ducky_REM(rem):
    return b''

def ducky_ENTER():
    return char_to_byte('\n')

def ducky_DELAY(delay):
    rtn = b''
    if delay.isdigit():
        rtn = b'\x07' + int(delay).to_bytes(7, byteorder='big')
    else:
        raise Exception("Invalid delay")
    return rtn

def ducky_ALT(control):
    return ducky_MODIFIERS(["ALT"], control)

def ducky_SHIFT(control):
    return ducky_MODIFIERS(["SHIFT"], control)

def ducky_CTRL(control):
    return ducky_MODIFIERS(["CTRL"], control)

def ducky_COMMAND(control):
    return ducky_MODIFIERS(["COMMAND"], control)

def ducky_GUI(control):
    return ducky_MODIFIERS(["GUI"], control)
    
def ducky_ESC(control):
    return ducky_MODIFIERS(["ESC"], control)
    
def ducky_MODIFIERS(modifier_keys, control):
    """ 
        Returns the bytcode corespnding to the association of the 
        modifier key (ALT, CTRL, ...) and another key.

        Parameters
        -----------
        modifier_keys: str
            A string rpreenting a modifier key (defined in lang.modifiers)
            One of those values: ["CTRL", "SHIFT", "ALT", "COMMAND", "GUI"]
        control: str
            A string representing the key. May be empty string, otherwise, 
            must be defined in lang.keys.
    """
    rtn = b''
    modifier_key = bytearray(8)
    for k in modifier_keys:
        
        modifier_key = bytes_or(lang.modifiers[k], modifier_key)
    
    if control != "": # modifier + something
        if control.upper() in lang.keys:
            rtn = bytes_or(modifier_key, lang.keys[control.upper()])
        else:
            raise Exception("Unknown key : \""+control+"\"")

    else: # Just the modifier key
        rtn = lang.keys[modifier_key]

    return rtn



def ducky_REPEAT(nb):
    rtn = b''
    if nb.isdigit():
        print(int(nb))
        print((ducky_to_hex(ducky_lines[current_line-1]))*int(nb))
        if current_line != 0:
            rtn = (ducky_to_hex(ducky_lines[current_line-1]))*int(nb)
        else:
            raise Exception("REPEAT can't be the first instruction of the script.")
            
    else:
        raise Exception("Invalid repeatition")

    return rtn

def ducky_KEY(key):
    rtn = b''
    if key in lang.keys:
        rtn = lang.keys[key]
    else:
        raise Exception("Unknown key : \""+key+"\"")
    return rtn



# =======================================================
# =======================================================
# =======================================================

def bytes_or(a, b):
    """
        Returns
        --------
        bytes
            A bitwise OR operation on the two parameters.
    """
    rtn = bytearray(b'')
    a_b = bytearray(a)
    b_b = bytearray(b)

    if len(a_b) != len(b_b):
        return b''

    i = 0
    while i<len(a_b):
        rtn.append(int(a[i] | b[i]))
        i+=1

    return rtn

# Dictionnary that associates a ducky command with the 
# function that handles its translation to bytecode.
supported_command = {
    "STRING": ducky_STRING,
    "REM": ducky_REM,
    "ENTER": ducky_ENTER,
    "DELAY": ducky_DELAY,
    "ALT": ducky_ALT, 
    "SHIFT": ducky_SHIFT, 
    "CTRL": ducky_CTRL, 
    "CONTROL": ducky_CTRL, 
    "ESC": ducky_ESC, 
    "ESCAPE": ducky_ESC, 
    "COMMAND": ducky_COMMAND, 
    "REPEAT": ducky_REPEAT,
    "GUI": ducky_GUI, 
    "WINDOWS": ducky_GUI, 
    "CTRL-SHIFT": (lambda c: ducky_MODIFIERS(["CTRL", "SHIFT"], c)), 
}

def char_to_byte(c):
    """
        Converts a character to the key combinaison that produces it, expressed in a height bytes long bytecode.
        Parameters
        ----------
        c : str
            A single character, well defined in lang.chars.
    """
    rtn = b''
    if c in lang.chars:
        rtn = lang.chars[c]
    else:
        raise Exception("Unsupported character : '" + str(c) + "'")
    return rtn


def ducky_to_hex(ducky_line):
    """
        Takes a line of ducky script and returns an encoded, equivalent bytecode, for the arduino
    """
    command = ducky_line.split(maxsplit=1)
    rtn = b''
    if len(command) > 0:
        if command[0] in supported_command:
            if len(command) == 1:
                rtn = supported_command[command[0]]()
            else:
                rtn = supported_command[command[0]](command[1])
        elif command[0] in lang.keys:
            rtn = ducky_KEY(command[0])

        else:
            raise Exception("Invalid script: \"" + command[0] + "\" is not a valid command")

    return rtn


def encode_ducky():
    global ducky_lines, current_line

    ducky_lines = ducky_script.split('\n')
    rtn = b''
    while current_line < len(ducky_lines):
        l = ducky_lines[current_line]
        try:
            rtn += ducky_to_hex(l)
        except Exception as e:
            raise Exception("Syntax error at line " + str(current_line+1) + " in the script : \n" + str(e))

        current_line += 1

    return rtn



def generate_output_filename(input_filename):
    """ Returns the input_filename with a new extention """
    return os.path.splitext(input_filename)[0]+'.bin'

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input_file', action='store', help="Input filename", required=True)
parser.add_argument('-o', '--output_file', action='store', help="Output filename", required=False)
parser.add_argument('-l', '--key_layout', action='store', choices=['en_us', 'fr_be'], help="Keyboard layout", required=False, default='en_us')
args = parser.parse_args()

lang = __import__(args.key_layout)

if args.output_file == None:
    args.output_file = generate_output_filename(args.input_file)

f = open(args.input_file, "r")
ducky_script = f.read()
f.close()

compiled = encode_ducky()


fo = open(args.output_file, "wb+")
fo.write(compiled)


