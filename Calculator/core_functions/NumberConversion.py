import math
class NumberConversion :
    def bin_to_decimal(self, binary_str):
        try:
            # Remove prefix if present
            if binary_str.startswith(('0b', '0B')):
                binary_str = binary_str[2:]#remove first 2 characters 
            if '.' in binary_str:
                int_part, frac_part = binary_str.split('.')
            else:
                int_part, frac_part = binary_str, ''
            # Integer part
            decimal = int(int_part, 2) if int_part else 0
            # Fractional part
            for i, digit in enumerate(frac_part):#i = index,digit= character in that index
                if digit not in '01':
                    raise ValueError
                decimal += int(digit) * (2 ** -(i + 1))
            return decimal
        except ValueError:
            print("Error: Invalid binary string.")
            return None      
    def decimal_to_bin(self,num,fd =10 ):
        intpart = int(num)
        fracpart = abs(num-intpart)
        intbin = bin(abs(intpart)).replace('0b','')
        fracbin = ''
        for _ in range(fd):
            fracpart *= 2
            bit = int(fracpart)
            fracbin += str(bit)
            fracpart -= bit
            if fracpart == 0:
                break
        sign = '-'if  num < 0 else ''
        return f"{sign}{intbin}"+('.'+fracbin if fracbin else '')
            
    def decimal_to_octal(self,num,fd=10):
        intpart = int(num)
        fracpart = abs(num-intpart)
        intoct = bin(abs(intpart)).replace('0b','')
        fracoct = ''
        for _ in range(fd):
            fracpart *= 8
            bit = int(fracpart)
            fracoct += str(bit)
            fracpart -= bit
            if fracpart == 0:
                break
        sign = '-'if  num < 0 else ''
        return f"{sign}{intoct}"+('.'+fracoct if fracoct else '')
        
    def decimal_to_hex(self,num,fd=10):
        intpart = int(num)
        fracpart = abs(num-intpart)
        inthex = bin(abs(intpart)).replace('0b','')
        frachex = ''
        for _ in range(fd):
            fracpart *= 8
            bit = int(fracpart)
            frachex += str(bit)
            fracpart -= bit
            if fracpart == 0:
                break
        sign = '-'if  num < 0 else ''
        return f"{sign}{inthex}"+('.'+frachex if frachex else '')
        
    def oct_to_decimal(self,octal_str):
        try:
            if octal_str.startswith(('0o', '0O')):
                octal_str = octal_str[2:]
            if '.' in octal_str:
                int_part, frac_part = octal_str.split('.')
            else:
                int_part, frac_part = octal_str, ''
            decimal = int(int_part, 8) if int_part else 0
            for i, digit in enumerate(frac_part):
                if digit not in '01234567':
                    raise ValueError
                decimal += int(digit) * (8 ** -(i + 1))
            return decimal
        except ValueError:
            print("Error: Invalid octal string.")
            return None
    def hex_to_decimal(self,hex_str):
        try:
            if hex_str.startswith(('0x', '0X')):
                hex_str = hex_str[2:]
            if '.' in hex_str:
                int_part, frac_part = hex_str.split('.')
            else:
                int_part, frac_part = hex_str, ''
            decimal = int(int_part, 16) if int_part else 0
            for i, digit in enumerate(frac_part):
                if digit.isdigit():
                    val = int(digit)
                elif digit.upper() in 'ABCDEF':
                    val = 10 + ord(digit.upper()) - ord('A')
                else:
                    raise ValueError
                decimal += val * (16 ** -(i + 1))
            return decimal
        except ValueError:
            print("Error: Invalid hexadecimal string.")
            return None           
    def bit_and(self,n1,n2):
        return n1 & n2 
    def bit_or(self,n1,n2):
        return n1 | n2 
    def bit_xor(self,n1,n2):
        return n1 ^ n2
    def bit_xnor(self,x1,x2):
        return ~(x1 ^ x2)
    def bit_not(self,n):
        return ~n
    def bit_left_shift(self,n,shift:int):
        if shift < 0:
            print("Error:Shift values must be non-negative.")
            return None
        return n << shift 
    def bit_right_shift(self,n,shift : int):
        if shift < 0:
            print("Error:Shift values must be non-negative.")
            return None
        return n  >> shift
    

        
    
