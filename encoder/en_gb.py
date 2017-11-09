import keyboard

KEY_BACKSLASH=64
KEY_ASH=100

# Association of characters to the key combinaion that produce it
chars = {

	"a": bytes([0, 0, keyboard.KEY_A, 0, 0, 0, 0, 0]),
	"b": bytes([0, 0, keyboard.KEY_B, 0, 0, 0, 0, 0]),
	"c": bytes([0, 0, keyboard.KEY_C, 0, 0, 0, 0, 0]),
	"d": bytes([0, 0, keyboard.KEY_D, 0, 0, 0, 0, 0]),
	"e": bytes([0, 0, keyboard.KEY_E, 0, 0, 0, 0, 0]),
	"f": bytes([0, 0, keyboard.KEY_F, 0, 0, 0, 0, 0]),
	"g": bytes([0, 0, keyboard.KEY_G, 0, 0, 0, 0, 0]),
	"h": bytes([0, 0, keyboard.KEY_H, 0, 0, 0, 0, 0]),
	"i": bytes([0, 0, keyboard.KEY_I, 0, 0, 0, 0, 0]),
	"j": bytes([0, 0, keyboard.KEY_J, 0, 0, 0, 0, 0]),
	"k": bytes([0, 0, keyboard.KEY_K, 0, 0, 0, 0, 0]),
	"l": bytes([0, 0, keyboard.KEY_L, 0, 0, 0, 0, 0]),
	"m": bytes([0, 0, keyboard.KEY_M, 0, 0, 0, 0, 0]),
	"n": bytes([0, 0, keyboard.KEY_N, 0, 0, 0, 0, 0]),
	"o": bytes([0, 0, keyboard.KEY_O, 0, 0, 0, 0, 0]),
	"p": bytes([0, 0, keyboard.KEY_P, 0, 0, 0, 0, 0]),
	"q": bytes([0, 0, keyboard.KEY_Q, 0, 0, 0, 0, 0]),
	"r": bytes([0, 0, keyboard.KEY_R, 0, 0, 0, 0, 0]),
	"s": bytes([0, 0, keyboard.KEY_S, 0, 0, 0, 0, 0]),
	"t": bytes([0, 0, keyboard.KEY_T, 0, 0, 0, 0, 0]),
	"u": bytes([0, 0, keyboard.KEY_U, 0, 0, 0, 0, 0]),
	"v": bytes([0, 0, keyboard.KEY_V, 0, 0, 0, 0, 0]),
	"w": bytes([0, 0, keyboard.KEY_W, 0, 0, 0, 0, 0]),
	"x": bytes([0, 0, keyboard.KEY_X, 0, 0, 0, 0, 0]),
	"y": bytes([0, 0, keyboard.KEY_Y, 0, 0, 0, 0, 0]),
	"z": bytes([0, 0, keyboard.KEY_Z, 0, 0, 0, 0, 0]),

	"A": bytes([keyboard.MODIFIERKEY_LEFT_SHIFT, 0, keyboard.KEY_A, 0, 0, 0, 0, 0]),
	"B": bytes([keyboard.MODIFIERKEY_LEFT_SHIFT, 0, keyboard.KEY_B, 0, 0, 0, 0, 0]),
	"C": bytes([keyboard.MODIFIERKEY_LEFT_SHIFT, 0, keyboard.KEY_C, 0, 0, 0, 0, 0]),
	"D": bytes([keyboard.MODIFIERKEY_LEFT_SHIFT, 0, keyboard.KEY_D, 0, 0, 0, 0, 0]),
	"E": bytes([keyboard.MODIFIERKEY_LEFT_SHIFT, 0, keyboard.KEY_E, 0, 0, 0, 0, 0]),
	"F": bytes([keyboard.MODIFIERKEY_LEFT_SHIFT, 0, keyboard.KEY_F, 0, 0, 0, 0, 0]),
	"G": bytes([keyboard.MODIFIERKEY_LEFT_SHIFT, 0, keyboard.KEY_G, 0, 0, 0, 0, 0]),
	"H": bytes([keyboard.MODIFIERKEY_LEFT_SHIFT, 0, keyboard.KEY_H, 0, 0, 0, 0, 0]),
	"I": bytes([keyboard.MODIFIERKEY_LEFT_SHIFT, 0, keyboard.KEY_I, 0, 0, 0, 0, 0]),
	"J": bytes([keyboard.MODIFIERKEY_LEFT_SHIFT, 0, keyboard.KEY_J, 0, 0, 0, 0, 0]),
	"K": bytes([keyboard.MODIFIERKEY_LEFT_SHIFT, 0, keyboard.KEY_K, 0, 0, 0, 0, 0]),
	"L": bytes([keyboard.MODIFIERKEY_LEFT_SHIFT, 0, keyboard.KEY_L, 0, 0, 0, 0, 0]),
	"M": bytes([keyboard.MODIFIERKEY_LEFT_SHIFT, 0, keyboard.KEY_M, 0, 0, 0, 0, 0]),
	"N": bytes([keyboard.MODIFIERKEY_LEFT_SHIFT, 0, keyboard.KEY_N, 0, 0, 0, 0, 0]),
	"O": bytes([keyboard.MODIFIERKEY_LEFT_SHIFT, 0, keyboard.KEY_O, 0, 0, 0, 0, 0]),
	"P": bytes([keyboard.MODIFIERKEY_LEFT_SHIFT, 0, keyboard.KEY_P, 0, 0, 0, 0, 0]),
	"Q": bytes([keyboard.MODIFIERKEY_LEFT_SHIFT, 0, keyboard.KEY_Q, 0, 0, 0, 0, 0]),
	"R": bytes([keyboard.MODIFIERKEY_LEFT_SHIFT, 0, keyboard.KEY_R, 0, 0, 0, 0, 0]),
	"S": bytes([keyboard.MODIFIERKEY_LEFT_SHIFT, 0, keyboard.KEY_S, 0, 0, 0, 0, 0]),
	"T": bytes([keyboard.MODIFIERKEY_LEFT_SHIFT, 0, keyboard.KEY_T, 0, 0, 0, 0, 0]),
	"U": bytes([keyboard.MODIFIERKEY_LEFT_SHIFT, 0, keyboard.KEY_U, 0, 0, 0, 0, 0]),
	"V": bytes([keyboard.MODIFIERKEY_LEFT_SHIFT, 0, keyboard.KEY_V, 0, 0, 0, 0, 0]),
	"W": bytes([keyboard.MODIFIERKEY_LEFT_SHIFT, 0, keyboard.KEY_W, 0, 0, 0, 0, 0]),
	"X": bytes([keyboard.MODIFIERKEY_LEFT_SHIFT, 0, keyboard.KEY_X, 0, 0, 0, 0, 0]),
	"Y": bytes([keyboard.MODIFIERKEY_LEFT_SHIFT, 0, keyboard.KEY_Y, 0, 0, 0, 0, 0]),
	"Z": bytes([keyboard.MODIFIERKEY_LEFT_SHIFT, 0, keyboard.KEY_Z, 0, 0, 0, 0, 0]),

	"1": bytes([0, 0, keyboard.KEY_1, 0, 0, 0, 0, 0]),
	"2": bytes([0, 0, keyboard.KEY_2, 0, 0, 0, 0, 0]),
	"3": bytes([0, 0, keyboard.KEY_3, 0, 0, 0, 0, 0]),
	"4": bytes([0, 0, keyboard.KEY_4, 0, 0, 0, 0, 0]),
	"5": bytes([0, 0, keyboard.KEY_5, 0, 0, 0, 0, 0]),
	"6": bytes([0, 0, keyboard.KEY_6, 0, 0, 0, 0, 0]),
	"7": bytes([0, 0, keyboard.KEY_7, 0, 0, 0, 0, 0]),
	"8": bytes([0, 0, keyboard.KEY_8, 0, 0, 0, 0, 0]),
	"9": bytes([0, 0, keyboard.KEY_9, 0, 0, 0, 0, 0]),
	"0": bytes([0, 0, keyboard.KEY_0, 0, 0, 0, 0, 0]),


	"-": bytes([0, 0, keyboard.KEY_MINUS, 0, 0, 0, 0, 0]),
	"=": bytes([0, 0, keyboard.KEY_EQUAL, 0, 0, 0, 0, 0]),
	"[": bytes([0, 0, keyboard.KEY_LEFT_BRACE, 0, 0, 0, 0, 0]),
	"]": bytes([0, 0, keyboard.KEY_RIGHT_BRACE, 0, 0, 0, 0, 0]),
	";": bytes([0, 0, keyboard.KEY_SEMICOLON, 0, 0, 0, 0, 0]),
	"'": bytes([0, 0, keyboard.KEY_QUOTE, 0, 0, 0, 0, 0]),
	"\\": bytes([0, 0, KEY_BACKSLASH, 0, 0, 0, 0, 0]),
	",": bytes([0, 0, keyboard.KEY_COMMA, 0, 0, 0, 0, 0]),
	".": bytes([0, 0, keyboard.KEY_PERIOD, 0, 0, 0, 0, 0]),
	"/": bytes([0, 0, keyboard.KEY_SLASH, 0, 0, 0, 0, 0]),



	"!": bytes([keyboard.MODIFIERKEY_SHIFT, 0, keyboard.KEY_1, 0, 0, 0, 0, 0]),
	"\"": bytes([keyboard.MODIFIERKEY_SHIFT, 0, keyboard.KEY_2, 0, 0, 0, 0, 0]),
	"#": bytes([0, 0, KEY_ASH, 0, 0, 0, 0, 0]),
	"$": bytes([keyboard.MODIFIERKEY_SHIFT, 0, keyboard.KEY_4, 0, 0, 0, 0, 0]),
	"%": bytes([keyboard.MODIFIERKEY_SHIFT, 0, keyboard.KEY_5, 0, 0, 0, 0, 0]),
	"&": bytes([keyboard.MODIFIERKEY_SHIFT, 0, keyboard.KEY_7, 0, 0, 0, 0, 0]),
	"(": bytes([keyboard.MODIFIERKEY_SHIFT, 0, keyboard.KEY_9, 0, 0, 0, 0, 0]),
	")": bytes([keyboard.MODIFIERKEY_SHIFT, 0, keyboard.KEY_0, 0, 0, 0, 0, 0]),
	"*": bytes([keyboard.MODIFIERKEY_SHIFT, 0, keyboard.KEY_8, 0, 0, 0, 0, 0]),
	"+": bytes([keyboard.MODIFIERKEY_SHIFT, 0, keyboard.KEY_EQUAL, 0, 0, 0, 0, 0]),
	":": bytes([keyboard.MODIFIERKEY_SHIFT, 0, keyboard.KEY_SEMICOLON, 0, 0, 0, 0, 0]),

	"<": bytes([keyboard.MODIFIERKEY_SHIFT, 0, KEY_COMMA, 0, 0, 0, 0, 0]),
	"=": bytes([0, 0, keyboard.KEY_EQUAL, 0, 0, 0, 0, 0]),
	">": bytes([keyboard.MODIFIERKEY_SHIFT, 0, KEY_PERIOD, 0, 0, 0, 0, 0]),
	"?": bytes([keyboard.MODIFIERKEY_SHIFT, 0, keyboard.KEY_SLASH, 0, 0, 0, 0, 0]),
	"@": bytes([keyboard.MODIFIERKEY_RIGHT_ALT, 0, keyboard.KEY_QUOTE, 0, 0, 0, 0, 0]),

	"^": bytes([keyboard.MODIFIERKEY_SHIFT, 0, keyboard.KEY_6, 0, 0, 0, 0, 0]),
	"_": bytes([keyboard.MODIFIERKEY_SHIFT, 0, keyboard.KEY_MINUS, 0, 0, 0, 0, 0]),
	"`": bytes([0, 0, keyboard.KEY_TILDE, 0, 0, 0, 0, 0]), # Not tested
	"{": bytes([keyboard.MODIFIERKEY_SHIFT, 0, keyboard.KEY_LEFT_BRACE, 0, 0, 0, 0, 0]),
	"|": bytes([keyboard.MODIFIERKEY_SHIFT, 0, KEY_BACKSLASH, 0, 0, 0, 0, 0]),
	"}": bytes([keyboard.MODIFIERKEY_SHIFT, 0, keyboard.KEY_RIGHT_BRACE, 0, 0, 0, 0, 0]),
	"~": bytes([keyboard.MODIFIERKEY_SHIFT, 0, KEY_ASH, 0, 0, 0, 0, 0]),


	"£": bytes([keyboard.MODIFIERKEY_SHIFT, 0, keyboard.KEY_3, 0, 0, 0, 0, 0]),
	"à": bytes([keyboard.MODIFIERKEY_RIGHT_ALT, 0, keyboard.KEY_A, 0, 0, 0, 0, 0]),
	"é": bytes([keyboard.MODIFIERKEY_RIGHT_ALT, 0, keyboard.KEY_E, 0, 0, 0, 0, 0]),
	"ù": bytes([keyboard.MODIFIERKEY_RIGHT_ALT, 0, keyboard.KEY_U, 0, 0, 0, 0, 0]),
	"€": bytes([keyboard.MODIFIERKEY_RIGHT_ALT, 0, keyboard.KEY_4, 0, 0, 0, 0, 0]),


	"\n": bytes([0, 0, keyboard.KEY_ENTER, 0, 0, 0, 0, 0]),
	" ": bytes([0, 0, keyboard.KEY_SPACE, 0, 0, 0, 0, 0]),
}

keys = {
	"CTRL": bytes([0, 0, keyboard.KEY_LEFT_CTRL, 0, 0, 0, 0, 0]),
	"ALT": bytes([0, 0, keyboard.KEY_LEFT_ALT, 0, 0, 0, 0, 0]),
	"SHIFT": bytes([0, 0, keyboard.KEY_LEFT_SHIFT, 0, 0, 0, 0, 0]),
	"COMMAND": bytes([0, 0, keyboard.KEY_COMMAND, 0, 0, 0, 0, 0]),
	"GUI": bytes([0, 0, keyboard.KEY_LEFT_GUI, 0, 0, 0, 0, 0]),

	"RIGHT": bytes([0, 0, keyboard.KEY_RIGHT, 0, 0, 0, 0, 0]),
	"LEFT": bytes([0, 0, keyboard.KEY_LEFT, 0, 0, 0, 0, 0]),
	"UP": bytes([0, 0, keyboard.KEY_UP, 0, 0, 0, 0, 0]),
	"DOWN": bytes([0, 0, keyboard.KEY_DOWN, 0, 0, 0, 0, 0]),

	"ESC":bytes([0, 0, keyboard.KEY_ESC, 0, 0, 0, 0, 0]),
	"DELETE":bytes([0, 0, keyboard.KEY_DELETE, 0, 0, 0, 0, 0]),
	"ENTER":bytes([0, 0, keyboard.KEY_ENTER, 0, 0, 0, 0, 0]),
	"TAB":bytes([0, 0, keyboard.KEY_TAB, 0, 0, 0, 0, 0]),
	"BACKSPACE":bytes([0, 0, keyboard.KEY_BACKSPACE, 0, 0, 0, 0, 0]),
	"SPACE": bytes([0, 0, keyboard.KEY_SPACE, 0, 0, 0, 0, 0]),
	
	"F1":bytes([0, 0, keyboard.KEY_F1, 0, 0, 0, 0, 0]),
	"F2":bytes([0, 0, keyboard.KEY_F2, 0, 0, 0, 0, 0]),
	"F3":bytes([0, 0, keyboard.KEY_F3, 0, 0, 0, 0, 0]),
	"F4":bytes([0, 0, keyboard.KEY_F4, 0, 0, 0, 0, 0]),
	"F5":bytes([0, 0, keyboard.KEY_F5, 0, 0, 0, 0, 0]),
	"F6":bytes([0, 0, keyboard.KEY_F6, 0, 0, 0, 0, 0]),
	"F7":bytes([0, 0, keyboard.KEY_F7, 0, 0, 0, 0, 0]),
	"F8":bytes([0, 0, keyboard.KEY_F8, 0, 0, 0, 0, 0]),
	"F9":bytes([0, 0, keyboard.KEY_F9, 0, 0, 0, 0, 0]),
	"F10":bytes([0, 0, keyboard.KEY_F10, 0, 0, 0, 0, 0]),
	"F11":bytes([0, 0, keyboard.KEY_F11, 0, 0, 0, 0, 0]),
	"F12":bytes([0, 0, keyboard.KEY_F12, 0, 0, 0, 0, 0]),

	"A": bytes([0, 0, keyboard.KEY_A, 0, 0, 0, 0, 0]),
	"B": bytes([0, 0, keyboard.KEY_B, 0, 0, 0, 0, 0]),
	"C": bytes([0, 0, keyboard.KEY_C, 0, 0, 0, 0, 0]),
	"D": bytes([0, 0, keyboard.KEY_D, 0, 0, 0, 0, 0]),
	"E": bytes([0, 0, keyboard.KEY_E, 0, 0, 0, 0, 0]),
	"F": bytes([0, 0, keyboard.KEY_F, 0, 0, 0, 0, 0]),
	"G": bytes([0, 0, keyboard.KEY_G, 0, 0, 0, 0, 0]),
	"H": bytes([0, 0, keyboard.KEY_H, 0, 0, 0, 0, 0]),
	"I": bytes([0, 0, keyboard.KEY_I, 0, 0, 0, 0, 0]),
	"J": bytes([0, 0, keyboard.KEY_J, 0, 0, 0, 0, 0]),
	"K": bytes([0, 0, keyboard.KEY_K, 0, 0, 0, 0, 0]),
	"L": bytes([0, 0, keyboard.KEY_L, 0, 0, 0, 0, 0]),
	"M": bytes([0, 0, keyboard.KEY_M, 0, 0, 0, 0, 0]),
	"N": bytes([0, 0, keyboard.KEY_N, 0, 0, 0, 0, 0]),
	"O": bytes([0, 0, keyboard.KEY_O, 0, 0, 0, 0, 0]),
	"P": bytes([0, 0, keyboard.KEY_P, 0, 0, 0, 0, 0]),
	"Q": bytes([0, 0, keyboard.KEY_Q, 0, 0, 0, 0, 0]),
	"R": bytes([0, 0, keyboard.KEY_R, 0, 0, 0, 0, 0]),
	"S": bytes([0, 0, keyboard.KEY_S, 0, 0, 0, 0, 0]),
	"T": bytes([0, 0, keyboard.KEY_T, 0, 0, 0, 0, 0]),
	"U": bytes([0, 0, keyboard.KEY_U, 0, 0, 0, 0, 0]),
	"V": bytes([0, 0, keyboard.KEY_V, 0, 0, 0, 0, 0]),
	"W": bytes([0, 0, keyboard.KEY_W, 0, 0, 0, 0, 0]),
	"X": bytes([0, 0, keyboard.KEY_X, 0, 0, 0, 0, 0]),
	"Y": bytes([0, 0, keyboard.KEY_Y, 0, 0, 0, 0, 0]),
	"Z": bytes([0, 0, keyboard.KEY_Z, 0, 0, 0, 0, 0]),

}

modifiers = {
	"CTRL": bytes([keyboard.MODIFIERKEY_LEFT_CTRL, 0, 0, 0, 0, 0, 0, 0]),
	"SHIFT": bytes([keyboard.MODIFIERKEY_LEFT_SHIFT, 0, 0, 0, 0, 0, 0, 0]),
	"ALT": bytes([keyboard.MODIFIERKEY_LEFT_ALT, 0, 0, 0, 0, 0, 0, 0]),
	"COMMAND": bytes([keyboard.MODIFIERKEY_GUI, 0, 0, 0, 0, 0, 0, 0]),
	"GUI": bytes([keyboard.MODIFIERKEY_GUI, 0, 0, 0, 0, 0, 0, 0]),
}