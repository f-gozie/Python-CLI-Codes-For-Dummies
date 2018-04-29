document='''We humans are born with an inner drive to explore the nature
of our surroundings. As young men, both Kevin Mitnick and
I were intensely curious about the world and eager to prove
ourselves. We were rewarded often in our attempts to learn new things,
solve puzzles, and win at games. But at the same time, the world around
us taught us rules of behavior that constrained our inner urge toward free
exploration. For our boldest scientists and technological entrepreneurs, as
well as for people like Kevin Mitnick, following this inner urge offers the
greatest thrills, letting us accomplish things that others believe cannot be
done.

Kevin Mitnick is one of the finest people I know. Ask him, and he will
say forthrightly that what he used to do - social engineering - involes
conning people. But Kevin is no longer a social engineer. And even when
he was, his motive never was to enrich himself or damage others. That's
not to say that there aren't dangerous and destructive criminals out there
who use social engineering to cause real harm. In fact, that's exactly why
Kevin wrote this book - to warn you about them.

The Art of Deception shows how vulnerable we all are - government,
business, and each of us personally - to the intrusions of the social
engineer. In this security-conscious era, we spend huge sums on technology
to protect our computer networks and data. This book points out how easy
it is to trick insiders and circumvent all this technological protection.
Whether you work in business or government, this book provides a
powerful road map to help you understand how social engineers work and
what you can do to foil them. Using fictionalized stories that are both
entertaining and eye-opening, Kevin and co-author Bill Simon bring to life
the techniques of the social engineering underworld. After each story,
they offer practical guidelines to help you guard against the breaches and
threats they're described.
'''
print("Document Analysis")
length = len("Document Analysis")
print(length*"=")
print("Characters:", len(document), "characters")

'''def countchar(document):
    totalchar=0
    for char in document:
        totalchar += 1
    return totalchar
print("Characters:", countchar(document))'''

def countspace(document):
    totalspace = 0
    for space in document:
        if space == ' ':
            totalspace += 1 
    return totalspace
print("No of Empty Spaces:", countspace(document))

def countwords(document):
    words= document.split()
    return len(words)
print("No. Of Words:", countwords(document))

def shortest_word(document):
    paragraph = document.split("\n")
    min = "*" * 1000
    for para in paragraph:
        words = para.split(" ")
        for word in words:
            if len(word) < len(min) and word != "":
                
                min = word
    return min
print("Shortest Word:", shortest_word(document))

def longest_word(document):
    paragraph = document.split("\n")
    max = "*"
    for para in paragraph:
        words = para.split(" ")
        for word in words:
            if len(word) > len(max):
                
                max = word
    return max
print("Longest Word:", longest_word(document))

