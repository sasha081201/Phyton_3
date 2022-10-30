import itertools

def compress_string(s):
    return [(len(list(g)), k) for k, g in itertools.groupby(s)]


print(compress_string('1222311'))