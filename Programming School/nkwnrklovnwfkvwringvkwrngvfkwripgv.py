
gist="""Hello World. My name is Agozie Favour. I am an aspiring computer programmer and I'm here to say that the quick
brown fox jumped over the lazy dogs. Hopefully, what I'm writing write now will serve as an unnecessarily long sentence.
Seems that's all I have to say, see you next time on 'LONG IRRELEVANT SENTENCES'. Btw, I wanna sleep like hell."""
total=0
char=[0]
List={"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}

for letter in gist:
    for one in List.keys():
        if letter==one:
            List[letter]=List[letter]+1
print(List.items())
    
    
        
    


