class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for ch in key:
            h += ord(ch)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        self.arr[h] = value

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

if __name__ == "__main__":
    t = HashTable()
    t['march 6'] = 130
    t['march 1'] = 20
    t['dec 7'] = 27
    print(t.arr)

    del t['march 1']
    t['march 17'] = 27
    print(t.arr)