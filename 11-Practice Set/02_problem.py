class animal:
    pass

class pets(animal):
    pass

class dog(pets):
    @staticmethod
    def bow():
        print("bow bow!.")
d = dog()
d.bow()