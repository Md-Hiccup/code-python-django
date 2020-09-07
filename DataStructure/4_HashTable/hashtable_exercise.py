import pprint

def sol1():
    # we only need temperature, so best data structure to use is LIST
    weathers = []
    with open('nyc_weather.csv', 'r') as f:
        for line in f:
            data = line.split(',')
            try:
                temperature = int(data[1])
                weathers.append(temperature)
            except:
                print('Invalid temperature. Ignore the row')

    # Average temperature in first week of Jan
    # Maximum temperature in first 10 days of Jan
    avg = sum(weathers[:7])/len(weathers[:7])
    max_temp = max(weathers[:10])
    print(f"Average temperature: {avg:.2f}")
    print(f"Maximum temperature: {max_temp}")

def sol2():
    # we need to get temp on particular day, so best data structure to use is DICTIONARY
    weathers = {}
    with open('nyc_weather.csv', 'r') as f:
        for line in f:
            data = line.split(',')
            try:
                weathers[data[0]] = int(data[1])
            except:
                print('Invalid temperature. Ignore the row')

    print(f"Temperature on Jan 9: {weathers['Jan 9']}")
    print(f"Temperature on Jan 9: {weathers['Jan 4']}")

def sol3():
    words_count = {}
    with open('poem.txt', 'r') as f:
        word_list = f.read().split()

    for word in word_list:
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1

    pprint.pprint(words_count)


class Solution4:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for ch in key:
            hash += ord(ch)
        return hash % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key, value)
        else:
            new_h = self.find_slot(key, h)
            self.arr[new_h] = (key, value)
        print(self.arr)

    def get_prob_range(self, index):
        return [*range(index, len(self.arr))] + [*range(0, index)]

    def find_slot(self, key, index):
        prob_range = self.get_prob_range(index)
        for prob_index in prob_range:
            element = self.arr[prob_index]
            if  element is None:
                return prob_index
            if element[0] == key:
                return prob_index
        raise Exception("HashMap Full")

    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h] is None:
            return
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            element = self.arr[prob_index]
            if element is None:
                return
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            element = self.arr[prob_index]
            if element is None:
                return  # item not found so return. You can also throw exception
            if element[0] == key:
                element = None
        print(self.arr)


if __name__ == "__main__":
    # sol1()
    # sol2()
    # sol3()

    t = Solution4()
    t["march 6"] = 20
    t["march 17"] = 88
    t["march 17"] = 29
    t["nov 1"] = 1
    t["march 33"] = 234
    #
    print(t["dec 1"])       # None
    print(t["march 33"])    # 234
    #
    t["march 33"] = 999
    print(t["march 33"])    # 999
    #
    t["april 1"] = 87
    t["april 2"] = 123
    t["april 3"] = 234234
    t["april 4"] = 91
    t["May 22"] = 4
    t["May 7"] = 47
    # t["Jan 1"] = 47       # Exceptions: HashMap Full
