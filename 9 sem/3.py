import os
import re
import os.path


class TextLoader:
    def __init__(self, adress):
        self.adress = adress
        self.file_paths = os.listdir(self.adress)

    def __len__(self):
        return len(self.file_paths)

    def __getitem__(self, i):
        with open(self.adress + '/' + self.file_paths[i]) as f:
            b = f.read().lower()
        return re.sub(r"[^\w\s]", '', b)

    def __iter__(self): 
        for i in self.fil_paths:
            with open(self.adress + '/' + i) as f:
                a = f.read().lower()
                yield re.sub(r'[^\w\s]', '', a)

if __name__ == "__main__":
    file = TextLoader('C:/Users/1/Desktop/Studies/mipt/3 semestr/Phyton/scripts1/9 lesson/sample')
    print(len(file))
    print(file[8])