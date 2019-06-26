# we depend on the `silly` package from pypi

import silly

if __name__ == "__main__":
    name = silly.name(capitalize=True)
    name2 = silly.name(capitalize=True)
    thing = silly.thing()
    noun = silly.noun()
    adj = silly.adjective()
    print("My name is {0}.  My favourite thing is {1}.  I am a {2}.  I love {3}".format(name, thing,
                                                                                        noun, name2))