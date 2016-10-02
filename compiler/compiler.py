import sys
import os
import argparse

import keyboard
#import en_en
#import fr_be


current_line = 0
ducky_script = ""
ducky_lines = []


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

"""
def ducky_ALT(control):
    rtn = b''
    if control != "": # ALT + something
        if control in en_en.keys:
            rtn = bytes_or(en_en.modifiers["ALT"], en_en.keys[control])
        else:
            raise Exception("Unknown key : \""+control+"\"")
    else: # Just ALT
        rtn = en_en.keys["ALT"]
    return rtn

def ducky_SHIFT(control):
    rtn = b''
    if control != "": # SHIFT + something
        if control in en_en.keys:
            rtn = bytes_or(en_en.modifiers["SHIFT"], en_en.keys[control])
        else:
            raise Exception("Unknown key : \""+control+"\"")
    else: # Just SHIFT
        rtn = en_en.keys["SHIFT"]
    return rtn

def ducky_CTRL(control):
    rtn = b''
    if control != "": # CTRL + something
        if control in en_en.keys:
            rtn = bytes_or(en_en.modifiers["CTRL"], en_en.keys[control])
        else:
            raise Exception("Unknown key : \""+control+"\"")
    else: # Just CTRL
        rtn = en_en.keys["CTRL"]
    return rtn

def ducky_COMMAND(control):
    rtn = b''
    if control != "": # COMMAND + something
        if control in en_en.keys:
            rtn = bytes_or(en_en.modifiers["COMMAND"], en_en.keys[control])
        else:
            raise Exception("Unknown key : \""+control+"\"")
    else: # Just COMMAND
        rtn = en_en.keys["COMMAND"]
    return rtn


def ducky_GUI(control):
    rtn = b''
    if control != "": # GUI + something
        if control in en_en.keys:
            rtn = bytes_or(en_en.modifiers["GUI"], en_en.keys[control])
        else:
            raise Exception("Unknown key : \""+control+"\"")
    else: # Just GUI
        rtn = en_en.keys["GUI"]
    return rtn

"""

def ducky_MODIFIERS(modifier_keys, control):
    """ 
        used for ALT, CTRL, SHIFT, COMMAND, GUI, 
    """
    rtn = b''
    modifier_key = 0
    for k in modifier_keys:
        modifier_key = bytes_and(lang.modifiers[k], modifier_key)

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



def bytes_and(a, b):
    """ TODO: how to make an OR operation on bytes otherwise?"""
    rtn = bytearray(b'')
    a_b = bytearray(a)
    b_b = bytearray(b)

    if len(a_b) != len(b_b):
        return b''

    i = 0
    while i<len(a_b):
        rtn.append(int(a[i] & b[i]))
        i+=1

    return rtn


def bytes_or(a, b):
    """ TODO: how to make an OR operation on bytes otherwise?"""
    
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

supported_command = {
    "STRING": ducky_STRING,
    "REM": ducky_REM,
    "ENTER": ducky_ENTER,
    "DELAY": ducky_DELAY,
    "ALT": (lambda c: ducky_MODIFIERS(["ALT"], c)), 
    "SHIFT": (lambda c: ducky_MODIFIERS(["SHIFT"], c)), 
    "CTRL": (lambda c: ducky_MODIFIERS(["CTRL"], c)), 
    "CONTROL": (lambda c: ducky_MODIFIERS(["CTRL"], c)), 
    "ESC": (lambda c: ducky_MODIFIERS(["ESC"], c)), 
    "ESCAPE": (lambda c: ducky_MODIFIERS(["ESC"], c)), 
    "COMMAND": (lambda c: ducky_MODIFIERS(["COMMAND"], c)), 
    "REPEAT": ducky_REPEAT,
    "GUI": (lambda c: ducky_MODIFIERS("GUI", c)), 
    "WINDOWS": (lambda c: ducky_MODIFIERS("GUI", c)), 
    "CTRL-SHIFT": (lambda c: ducky_MODIFIERS(["CTRL", "SHIFT"], c)), 
}

def char_to_byte(c):
    """
        convert a character to the key combinaison that produces it, expressed in a row of height bytes
    """
    rtn = b''
    if c in lang.chars:
        rtn = lang.chars[c]
    else:
        raise Exception("Unsupported character : '" + str(c) + "'")
    return rtn


def ducky_to_hex(ducky_line):
    """
        take a line of duccky script and return an encoded equivalent for the arduino
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


def compile_ducky():
    global ducky_lines, current_line

    ducky_lines = ducky_script.split('\n')
    print(ducky_lines)
    rtn = b''
    while current_line < len(ducky_lines):
        l = ducky_lines[current_line]
        try:
            print(l)
            rtn += ducky_to_hex(l)
        except Exception as e:
            raise Exception("Syntax error at line " + str(current_line) + " in the script : \n" + str(e))

        current_line += 1

    return rtn



def generate_output_filename(input_filename):
    return os.path.splitext(input_filename)[0]+'.bin'

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input_file', action='store', help="Input file", required=True)
parser.add_argument('-o', '--output_file', action='store', help="Output filename", required=False)
parser.add_argument('-l', '--key_layout', action='store', choices=['en_en', 'fr_be'], help="Keyboard layout", required=False, default='en_en')
args = parser.parse_args()

lang = __import__(args.key_layout)

if args.output_file == None:
    args.output_file = generate_output_filename(args.input_file)

f = open(args.input_file, "r")
ducky_script = f.read()
f.close()

compiled = compile_ducky()

#print(compiled)

fo = open(args.output_file, "wb+")
fo.write(compiled)


