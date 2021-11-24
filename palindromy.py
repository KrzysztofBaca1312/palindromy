def is_palindrom(text) :
 """funkcja sprawdza czy podany tekst jest palindromem 
 """
 return text == text[::-1]
print(is_palindrom("kajak"))
print(is_palindrom("potop"))
print(is_palindrom("rower"))
print(is_palindrom("natan"))
print("test")