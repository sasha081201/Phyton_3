class Meta(type):
    def __init__(cls, name, base, attrs):
        name = list(attrs.keys())
        for i in range(len(name)):
            if "line" in name[i]:
                if 'func' in  str(attrs[name[i]]):
                    raise Exception ('wrong name')
                    
        return super().__init__(name, base, attrs)




class Test(metaclass = Meta):
    def line_interesting():
        pass


Test
