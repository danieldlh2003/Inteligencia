def two_fer(name = None):
    if name is None:
        return "One for you, one for me."
    elif name != None:
        return "One for " + name + ", one for me."
