class primary_colour:
    def red(self, red):
        self.red = red
        return "red"
    def blue(self, blue):
        self.blue = blue
        return "blue"
    def yellow(self, yellow):
        self.yellow = yellow
        return "yellow"
    
class secondary_colour(primary_colour):
    def green(self):
        green = primary_colour.red and primary_colour.yellow
        return "yellow"
C = secondary_colour()
print(issubclass(secondary_colour, primary_colour))
