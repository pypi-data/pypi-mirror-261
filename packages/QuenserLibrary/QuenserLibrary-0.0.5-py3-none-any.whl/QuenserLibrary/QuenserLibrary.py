from robot.api.deco import keyword

class QuenserLibrary:
    @keyword(name="Quenser", doc="Says hello to the world.")
    def quenser_keyword(self):
        """ This keyword prints 'Hello, world!' to the console. """
        print("Hello, world!")
