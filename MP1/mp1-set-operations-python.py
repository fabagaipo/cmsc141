import copy

# Set class
class Set:
    def __init__(self, s1, s2, dt, sdt, item):
        self.set1 = s1
        self.set2 = s2
        self.data = dt
        self.setdata = sdt
        self.items = item
        self.result = []

    # Parser
    def parse(self, index):
        # Parse operation
        self.result.clear()
        if int(self.items[index][0]) == 1:
            if self.data == 1 or self.data == 2:
                self.insert(int(self.items[index][1]), int(self.items[index][2]))
            elif self.data >= 3 and self.data <= 4:
                self.insert(int(self.items[index][1]), self.items[index][2])
            elif self.data == 5:
                self.insertSet(int(self.items[index][1]), self.items[index][2])
        elif int(self.items[index][0]) == 2:
            if self.data == 1 or self.data == 2:
                self.remove(int(self.items[index][1]), int(self.items[index][2]))
            elif self.data >= 3 and self.data <= 4:
                self.remove(int(self.items[index][1]), self.items[index][2])
            elif self.data == 5:
                self.removeSet(int(self.items[index][1]), self.items[index][2])
        elif int(self.items[index][0]) == 3:
            self.subset()
        elif int(self.items[index][0]) == 4:
            self.union()
        elif int(self.items[index][0]) == 5:
            self.intersection()
        elif int(self.items[index][0]) == 6:
            self.difference()
        elif int(self.items[index][0]) == 7:
            if int(self.items[index][1]) == 1:
                self.power(self.set1)
            elif int(self.items[index][1]) == 2:
                self.power(self.set2)
                
# Set operators:

    # 1.1 Insert set to a set
    def insertSet(self, setter, value):
        if '{' in value:
            if self.setdata == 1:
                tsplit = value[1:-1].split(',')
                value = sorted(list(map(int, tsplit)))
            elif self.setdata == 2:
                tsplit = value[1:-1].split(',')
                value = sorted(list(map(float, tsplit)))

        self.insert(setter, value)

    # 1.2 Insert item to a set
    def insert(self, setter, value):
        if setter == 1:
            if value not in self.set1:
                self.set1.append(value)
            else:
                pass
            self.preformat(self.set1)
        if setter == 2:
            if value not in self.set2:
                self.set2.append(value)
            else:
                pass
            self.preformat(self.set2)

    # 2.1 Remove set from a set
    def removeSet(self, setter, value):
        if '{' in value:
            if self.setdata == 1:
                tsplit = value[1:-1].split(',')
                value = list(map(int, tsplit))
            elif self.setdata == 2:
                tsplit = value[1:-1].split(',')
                value = list(map(float, tsplit))

        self.remove(setter, value)

    # 2.2 Remove item from a set
    def remove(self, setter, value):
        if setter == 1:
            if value in self.set1:
                self.set1 = [item for item in self.set1 if item != value]
            else:
                self.append("Not in set!")
            self.preformat(self.set1)

        if setter == 2:
            if value in self.set2:
                self.set2 = [item for item in self.set2 if item != value]
            else:
                self.append("Not in set!")
            self.preformat(self.set2)
    
    # 3. Checks whether S1 is a subset of S2
    def subset(self):
        if len(self.set1) > len(self.set2):
            self.append("false")
        elif len(self.set1) == len(self.set2) or len(self.set1) < len(self.set2):
            subset = 0
            iterator = 0
            while iterator < len(self.set1):
                if self.set1[iterator] in self.set2:
                    subset += 1
                iterator += 1
            if subset < len(self.set1):
                self.append("false")  # Returns true if a subset
            else:
                self.append("true")   # Returns false if not a subset
    
    # 4. Union of two sets (S1 U S2)
    def union(self):
        self.result = copy.copy(self.set1)
        for item in self.set2:
            if item not in self.result:
                self.result.append(item)
            else:
                continue
        self.preformat(self.result)

    # 5. Intersection of two sets (S1 ∩ S2)
    def intersection(self):
        for item in self.set1:
            if item in self.set2:
                self.result.append(item)
            else:
                continue
        self.preformat(self.result)

    # 6. Difference of two sets (S1-S2)
    def difference(self):
        for item in self.set1:
            if item not in self.set2:
                self.result.append(item)
            else:
                continue
        self.preformat(self.result)
        
    # 7. Power set given a set
    def power(self, val):
        init = ['empty']
        for item in val:
            init.append(item)
        rest = (2**len(val))-len(init)
        if rest == 1:
            init.append(val)
            self.preformat(init)
        else:
            init.append('None')
            self.preformat(init)

# Other functons:

    # Function for set of sets
    def preformat(self, setter):
        if self.data != 5:
            self.format(setter)
        else:
            tmpstr = str(setter)
            tmpstr = tmpstr.replace('[', '{')
            tmpstr = tmpstr.replace(']', '}')
            tmpstr = tmpstr.replace(' ', '')
            if "'" in tmpstr:
                tmpstr = tmpstr.replace("'", '')
            self.append(tmpstr)
    
    # Function for set of data types
    def format(self, lst):
        string = '{'
        for item in lst:
            string += str(item) + ','
        string = string[:-1] + '}'
        self.append(string)

    # Append results to output file
    def append(self, string):
        with open('lastName.out', 'a') as file:
            file.write(string + '\n')
            file.close()

# Parser Class
class Parser:
    def __init__(self):
        self.lineitems = []
        self.tmpline = []
        self.num_testcase = 0
        self.tmpdatatype = None
        self.tmpsetdatatype = None
        self.tmpset1 = None
        self.tmpset2 = None

    # Convert each line of text to list
    def toList(self, line):
        for item in line:
            self.tmpline = item.split(' ')
            self.lineitems.append(self.tmpline)
        self.num_testcase = len(self.lineitems)

    # Converts input file containing test inputs
    def parse(self, startline):
        if startline + 1 == len(self.lineitems):
            return
        else:
            start = 1
            initset = 3
            position = 1 + startline
            operation = 0

            while initset > 0:
                if start == 1:
                    self.tmpdatatype = self.checkType(int(
                        self.lineitems[position][0]))
                    if self.tmpdatatype == 5:
                        self.tmpsetdatatype = self.checkType(int(
                            self.lineitems[position][1]))
                if start == 2:
                    self.tmpset1 = self.getSet(self.lineitems[position])
                if start == 3:
                    self.tmpset2 = self.getSet(self.lineitems[position])
                start += 1
                initset -= 1
                position += 1

            myset = Set(self.tmpset1, self.tmpset2,
                        self.tmpdatatype, self.tmpsetdatatype, self.lineitems)

            if start == 4:
                operation = int(self.lineitems[position][0])
                position += 1
                while operation > 0:
                    myset.parse(position)
                    operation -= 1
                    position += 1
            self.parse(position-1)

    def checkType(self, datatype):
        # checks datatype by number
        # 1. int
        # 2. double
        # 3. char
        # 4. string
        # 5. set
        return datatype

    # Sets temporary list
    def getSet(self, tmplist):
        if self.tmpdatatype == 1:
            return list(map(int, tmplist))
        elif self.tmpdatatype == 2:
            return list(map(float, tmplist))
        elif self.tmpdatatype >= 3 and self.tmpdatatype <= 4:
            return tmplist
        elif self.tmpdatatype == 5:
            tmpsetlist = []
            if self.tmpsetdatatype == 1:
                for index, item in enumerate(tmplist):
                    tsplit = tmplist[index][1:-1].split(',')
                    tmpsetlist.append(list(map(int, tsplit)))
                return tmpsetlist
            elif self.tmpsetdatatype == 2:
                for index, item in enumerate(tmplist):
                    tsplit = tmplist[index][1:-1].split(',')
                    tmpsetlist.append(list(map(float, tsplit)))
                return tmpsetlist
            elif self.tmpsetdatatype >= 3 and self.tmpsetdatatype <= 4:
                return tmplist

# Main function
def main():
    fileinput = input("Enter input file: ")
    with open(fileinput) as inputfile:
        line = [ln.strip() for ln in inputfile]

    open("lastName.out", 'w').close()
    setp = Parser()
    setp.toList(line)
    setp.parse(0)
    print("File has been made. Open lastName.out")

if __name__ == "__main__":
    main()

# References:
# https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/
# https://www.oreilly.com/library/view/python-cookbook/0596001673/ch05s18.html
# https://coderbyte.com/algorithm/print-all-subsets-given-set
# https://www.kite.com/python/answers/how-to-convert-each-line-in-a-text-file-into-a-list-in-python
