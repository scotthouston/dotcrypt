from random import randint
import pyperclip

#i need these for little compressed tokens
def base62_encode(num):
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    if num == 0:
        return chars[0]
    result = ""
    while num > 0:
        result = chars[num % 62] + result
        num //= 62
    return result

def base62_decode(s):
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    num = 0
    for c in s:
        num = num * 62 + chars.index(c)
    return num


user_data2enc = ""

#this is for starting and functioning of program
def initialize():
    global user_data2enc
    try:
        user_opinion = int(input("""Choose the option below:
1.Encryption
2.Decryption
3.Exit
Option>: """))
        if user_opinion==1:
            user = encrypt(input("Enter what u want to encrypt: "))
        elif user_opinion==2:
            user_data2enc = input("Enter your encrypted message: ")
            decrypt()
        elif user_opinion==3:
            exit()
    except Exception as e:
        print("Enter options as numbers")
        print(e)
        initialize()

class encrypt:
    def __init__(self, user_input):
        output = ""
        hint = ""
        token = {}
        alpha = {
            'a': "", 'b': "", 'c': "", 'd': "", 'e': "", 'f': "", 'g': "", 'h': "", 'i': "", 'j': "", 
            'k': "", 'l': "", 'm': "", 'n': "", 'o': "", 'p': "", 'q': "", 'r': "", 's': "", 't': "", 
            'u': "", 'v': "", 'w': "", 'x': "", 'y': "", 'z': "",
    
             # Uppercase letters
            'A': "", 'B': "", 'C': "", 'D': "", 'E': "", 'F': "", 'G': "", 'H': "", 'I': "", 'J': "", 
            'K': "", 'L': "", 'M': "", 'N': "", 'O': "", 'P': "", 'Q': "", 'R': "", 'S': "", 'T': "", 
            'U': "", 'V': "", 'W': "", 'X': "", 'Y': "", 'Z': "",
    
            # Numbers
            '0': "", '1': "", '2': "", '3': "", '4': "", '5': "", '6': "", '7': "", '8': "", '9': "",
    
            # Basic punctuation
            '.': "", ',': "", '!': "", '?': "", ';': "", ':': "", "'": "", '"': "", 
    
            # Mathematical and logical symbols
            '+': "", '-': "", '*': "", '/': "", '=': "", '<': "", '>': "", '%': "", '^': "", '&': "",
    
            # Brackets and parentheses
            '(': "", ')': "", '[': "", ']': "", '{': "", '}': "",
    
            # Common symbols
            '@': "", '#': "", '$': "", '~': "", '`': "", '|': "", '\\': "", '_': "", '§': "",
    
            # Whitespace and formatting
            ' ': "", '\t': "", '\n': "",
    
            # Extended ASCII and special characters
            '©': "", '®': "", '™': "", '°': "", '±': "", '×': "", '÷': "", '€': "", '£': "", '¥': "",
            'á': "", 'é': "", 'í': "", 'ó': "", 'ú': "", 'ñ': "", 'ü': "", 'ö': "", 'ä': "", 'ß': "",
            'À': "", 'È': "", 'Ì': "", 'Ò': "", 'Ù': "", 'Ñ': "", 'Ü': "", 'Ö': "", 'Ä': "",
    
            # Emoji (basic set)
            '😀': "", '😃': "", '😄': "", '😊': "", '😍': "", '🤔': "", '👍': "", '❤': "", '🔥': "", '💯': ""
        }
        for i in alpha:
            nm1 = randint(3, 500)
            nm2 = randint(3, 500)
            nm3 = randint(3, 500)
            nm4 = randint(3, 500)
            nm5 = randint(3, 500)
            nm6 = randint(3, 500)
            nm7 = randint(3, 500)
            nm8 = randint(3, 500)
            nm9 = randint(3, 500)
            nm0 = randint(3, 500)
            # i changed this for base62
            encoded_values = [nm1*100, nm2*2, nm3*3, nm4*4, nm5*5, nm6*6, nm7*7, nm8*8, nm9*9, nm0*10]
            hint = " ".join(base62_encode(n) for n in encoded_values)
            token[i]=hint
            alpha[i]="."*nm1+" "+"."*nm2+" "+"."*nm3+" "+"."*nm4+" "+"."*nm5+" "+"."*nm6+" "+"."*nm7+" "+"."*nm8+" "+"."*nm9+" "+"."*nm0
        print("Encryption Successful")
        for i in user_input:
            output = output + "  ..  "+ alpha[i]
        def keygen(key):
            with open("bokachokabeho.ab", "wb") as f:
                f.write(key)
        token_list = list(token.values())
        token_string = ""
        for i in range(0, len(token_list)):
            token_string = token_string +" "+ f"{token_list[i]}\n"
        token_byte = token_string.encode('utf-8')
        keygen(token_byte)
        pyperclip.copy(output)
        print("Output copied to clipboard")
        initialize()
        
def decrypt():
    decrypted = ""
    decrypted_byte = ""
    decrypted_tl = []
    decrypted_alpha = {
            'a': "", 'b': "", 'c': "", 'd': "", 'e': "", 'f': "", 'g': "", 'h': "", 'i': "", 'j': "", 
            'k': "", 'l': "", 'm': "", 'n': "", 'o': "", 'p': "", 'q': "", 'r': "", 's': "", 't': "", 
            'u': "", 'v': "", 'w': "", 'x': "", 'y': "", 'z': "",
    
            # Uppercase letters
            'A': "", 'B': "", 'C': "", 'D': "", 'E': "", 'F': "", 'G': "", 'H': "", 'I': "", 'J': "", 
            'K': "", 'L': "", 'M': "", 'N': "", 'O': "", 'P': "", 'Q': "", 'R': "", 'S': "", 'T': "", 
            'U': "", 'V': "", 'W': "", 'X': "", 'Y': "", 'Z': "",
    
            # Numbers
            '0': "", '1': "", '2': "", '3': "", '4': "", '5': "", '6': "", '7': "", '8': "", '9': "",
    
            # Basic punctuation
            '.': "", ',': "", '!': "", '?': "", ';': "", ':': "", "'": "", '"': "", 
        
            # Mathematical and logical symbols
            '+': "", '-': "", '*': "", '/': "", '=': "", '<': "", '>': "", '%': "", '^': "", '&': "",
    
            # Brackets and parentheses
            '(': "", ')': "", '[': "", ']': "", '{': "", '}': "",

            # Common symbols
            '@': "", '#': "", '$': "", '~': "", '`': "", '|': "", '\\': "", '_': "", '§': "",

            # Whitespace and formatting
            ' ': "", '\t': "", '\n': "",

            # Extended ASCII and special characters
            '©': "", '®': "", '™': "", '°': "", '±': "", '×': "", '÷': "", '€': "", '£': "", '¥': "",
            'á': "", 'é': "", 'í': "", 'ó': "", 'ú': "", 'ñ': "", 'ü': "", 'ö': "", 'ä': "", 'ß': "",
            'À': "", 'È': "", 'Ì': "", 'Ò': "", 'Ù': "", 'Ñ': "", 'Ü': "", 'Ö': "", 'Ä': "",

            # Emoji (basic set)
            '😀': "", '😃': "", '😄': "", '😊': "", '😍': "", '🤔': "", '👍': "", '❤': "", '🔥': "", '💯': ""
        }
    data = ""
    with open("bokachokabeho.ab", "rb") as f:
        for x in f:
            temp = x
            temp = temp.decode('utf-8')
            data = data + temp
    data = data.split("\n")
    letters = list(decrypted_alpha.keys())
    for x in range(len(data)):
        if x < len(letters):
            decrypted_alpha[letters[x]] = data[x].strip()
    decrypted = og_values(decrypted_alpha)

#the most difficult part for me to understand at first, cause i didnt know much about enumerate or i didnt know at all, and also about dictionary comprehension
class og_values:
    def __init__(self,hint_val):
        dot_num = ['nm1', 'nm2', 'nm3', 'nm4', 'nm5', 'nm6', 'nm7', 'nm8', 'nm9', 'nm0']
        self.hint_val = hint_val
        dot_dec = {letters:{dot_num[i]:base62_decode(val) for i, val in enumerate(numbers.split())}
                   for letters, numbers in hint_val.items()}

        for i in dot_dec:
           for num, ognum in dot_dec[i].items(): # at first i did for num, ognum in i ,,,, which was wrong cause i is just a string
                if num=='nm1':
                    dot_dec[i][num]=ognum//100
                elif num=='nm2':
                    dot_dec[i][num]=ognum//2
                elif num=='nm3':
                    dot_dec[i][num]=ognum//3
                elif num=='nm4':
                    dot_dec[i][num]=ognum//4
                elif num=='nm5':
                    dot_dec[i][num]=ognum//5
                elif num=='nm6':
                    dot_dec[i][num]=ognum//6
                elif num=='nm7':
                    dot_dec[i][num]=ognum//7
                elif num=='nm8':
                    dot_dec[i][num]=ognum//8
                elif num=='nm9':
                    dot_dec[i][num]=ognum//9
                elif num=='nm0':
                    dot_dec[i][num]=ognum//10
        decoded_alpha = {
            'a': "", 'b': "", 'c': "", 'd': "", 'e': "", 'f': "", 'g': "", 'h': "", 'i': "", 'j': "", 
            'k': "", 'l': "", 'm': "", 'n': "", 'o': "", 'p': "", 'q': "", 'r': "", 's': "", 't': "", 
            'u': "", 'v': "", 'w': "", 'x': "", 'y': "", 'z': "",
    
            # Uppercase letters
            'A': "", 'B': "", 'C': "", 'D': "", 'E': "", 'F': "", 'G': "", 'H': "", 'I': "", 'J': "", 
            'K': "", 'L': "", 'M': "", 'N': "", 'O': "", 'P': "", 'Q': "", 'R': "", 'S': "", 'T': "", 
            'U': "", 'V': "", 'W': "", 'X': "", 'Y': "", 'Z': "",

            # Numbers
            '0': "", '1': "", '2': "", '3': "", '4': "", '5': "", '6': "", '7': "", '8': "", '9': "",

            # Basic punctuation
            '.': "", ',': "", '!': "", '?': "", ';': "", ':': "", "'": "", '"': "", 

            # Mathematical and logical symbols
            '+': "", '-': "", '*': "", '/': "", '=': "", '<': "", '>': "", '%': "", '^': "", '&': "",

            # Brackets and parentheses
            '(': "", ')': "", '[': "", ']': "", '{': "", '}': "",

            # Common symbols
            '@': "", '#': "", '$': "", '~': "", '`': "", '|': "", '\\': "", '_': "", '§': "",

            # Whitespace and formatting
            ' ': "", '\t': "", '\n': "",

            # Extended ASCII and special characters
            '©': "", '®': "", '™': "", '°': "", '±': "", '×': "", '÷': "", '€': "", '£': "", '¥': "",
            'á': "", 'é': "", 'í': "", 'ó': "", 'ú': "", 'ñ': "", 'ü': "", 'ö': "", 'ä': "", 'ß': "",
            'À': "", 'È': "", 'Ì': "", 'Ò': "", 'Ù': "", 'Ñ': "", 'Ü': "", 'Ö': "", 'Ä': "",

            # Emoji (basic set)
            '😀': "", '😃': "", '😄': "", '😊': "", '😍': "", '🤔': "", '👍': "", '❤': "", '🔥': "", '💯': ""
        }
        for i in decoded_alpha:
            nm1 = dot_dec[i]['nm1']
            nm2 = dot_dec[i]['nm2']
            nm3 = dot_dec[i]['nm3']
            nm4 = dot_dec[i]['nm4']
            nm5 = dot_dec[i]['nm5']
            nm6 = dot_dec[i]['nm6']
            nm7 = dot_dec[i]['nm7']
            nm8 = dot_dec[i]['nm8']
            nm9 = dot_dec[i]['nm9']
            nm0 = dot_dec[i]['nm0']
            decoded_alpha[i]="."*nm1+" "+"."*nm2+" "+"."*nm3+" "+"."*nm4+" "+"."*nm5+" "+"."*nm6+" "+"."*nm7+" "+"."*nm8+" "+"."*nm9+" "+"."*nm0
            decoded_alpha[i]=decoded_alpha[i].strip()
        print("Retrieved Encrypted data")
        dotmap = user_data2enc.split(" .. ")
        for i in range(0,len(dotmap)):
            dotmap[i]= dotmap[i].strip()
        #for checking and identifying
        decrypted_text = ""
        for i in dotmap:
            valid_alpha = {alpha: dot_patterns for alpha, dot_patterns in decoded_alpha.items() if i == dot_patterns}
            for x in valid_alpha:
                decrypted_text = decrypted_text+x
        print("Decryption Successfull")
        print(f"""The Text Retrieved was:
{decrypted_text}""")
        initialize()

initialize()