class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for ch in key:
            h += ord(ch)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        # self.arr[h] = value   # override the already exist key - value
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]

if __name__ == "__main__":
    t = HashTable()
    t['march 6'] = 130
    t['march 1'] = 20
    t['dec 7'] = 27
    print(t.arr)

    del t['march 1']
    t['march 17'] = 27
    print(t.arr)

    print(t['march 6'])
    print(t['march 17'])

    del t['march 17']
    print(t.arr)