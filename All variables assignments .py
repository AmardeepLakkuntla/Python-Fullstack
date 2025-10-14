name=input(f"name of the person: ")
age=input(f"persons age: ")
city=input(f"persons city: ")
fav_color=input(f"persons fav_color: ")
print(name,age,city,fav_color)

text=input("enter the string: ")
upper=text.upper()
print(upper)
lower=text.lower()
print(lower)
length=len(text)
print(length)
text_index=text[0],text[-1]
print(text_index)
reverse=text[::-1]
print(reverse)


text=input("enter the text: ")
vowels=text.count("a")
vowels1=text.count("e")
vowels2=text.count("i")
vowels3=text.count("o")
vowels4=text.count("u")
vowels5=text.count("A")
vowels6=text.count("E")
vowels7=text.count("I")
vowels8=text.count("O")
vowels9=text.count("U")
total_vowels=vowels+vowels1+vowels2+vowels3+vowels4+vowels5+vowels6+vowels7+vowels8+vowels9
total_letters=len(text)
total_consonants=(total_letters-total_vowels)
print(f"vowels present: {total_vowels}")
print(f"consonants present: {total_consonants}")

text1=input("enter the string: ")
text2=input("enter the string: ")
substring1=text1[:2]
substring2=text2[:3]
nickname=(substring1 + substring2).upper()
print(nickname)

