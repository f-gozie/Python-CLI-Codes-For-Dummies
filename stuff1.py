gist="""Hello World. My name is Agozie Favour. I am an aspiring computer programmer and I'm here to say that the quick
brown fox jumped over the lazy dogs. Hopefully, what I'm writing write now will serve as an unnecessarily long sentence.
Abeg, enough gist, off to work. Btw, I wanna sleep like hell."""
letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
dict={}

for letter in letters:
    total=0
    for char in gist:
        if letter==char:
            total=total+1
        dict[letter]=total
print(dict)
