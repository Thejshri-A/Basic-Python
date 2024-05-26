# This is a custom module.

from random import choice

capital = "Chennai"

bird = "Penguin"

flower = "Jasmine"

song = "Tamil"


def random_fun_fact():
    funfacts = ["Chennai is a city in the shores og Bay of Bengal.",
                "Chennai is beautiful.",
                "Chennai harbors numerous species",
                "Enjoy a vacation in Chennai"]
    index = choice("0123")
    print("::::", funfacts[int(index)])


# if __name__ == "__main__":
random_fun_fact()
