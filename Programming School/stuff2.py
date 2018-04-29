gist="""Hello World. My name is Agozie Favour. I am an aspiring computer programmer and I'm here to say that the quick
brown fox jumped over the lazy dogs. Hopefully, what I'm writing write now will serve as an unnecessarily long sentence.
Abeg, enough gist, off to work. Btw, I wanna sleep like hell."""
list1=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
list2=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

count=0
ini=0

while count<26:
    for list1[count] in gist:
        if list1[count]is list2[count]:
            ini=ini+1
            print(ini)
            i=0
            count=count+1
        