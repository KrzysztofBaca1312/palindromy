def is_palindrom(text):
 """funkcja sprawdza czy podany tekst jest palindromem 
 """

 if text == text[::-1]:
	 return True
 return False
print(is_palindrom("kajak"))
print(is_palindrom("potop"))
print(is_palindrom("rower"))
print(is_palindrom("natan"))