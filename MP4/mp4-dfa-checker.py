class DFA:
    def __init__(self, line1, line2):
        self.line1 = line1      # added for which kind (1 for var declaration and 2 for func declaration)
        self.line2 = line2      # added for actual string to be tested
        self.istype = [0,0,0,0,0]
        self.ischar = 0
        self.isarray = 0
        self.iseqarray = 0
        self.isequal = 0
        self.existtype = 0

    # Function for processing inputs from main
    def process(self):
        kind = int(self.line1)
        string = self.line2
        self.execute(kind, string)

    # Function for executing extraction and checking
    def execute(self, kind, string):
        xstr = self.extract(string)
        self.check(kind, xstr)

    def extract(self, string):
        xstr = []
        tmp = ''
        for char in string:
            if char == ' ':
                xstr.append(tmp)
                tmp = ''
            elif char in ',;(){}[]=+-*/"\'':
                xstr.append(tmp)
                xstr.append(char)
                tmp = ''
            else:
                tmp += char

        xstr.append(tmp)
        xstr = list(filter(None, xstr))
        return xstr

    def evaluate(self, st):
        result = 0
        types = ['int', 'float', 'char', 'double', 'void']
        if st in types:
            result = self.checktype(st)
            return result
        elif st.isdigit():
            result = self.checknumber(st)
        elif '.' in st:
            if st.replace('.', '').isdigit():
                if st.count('.') == 1:
                    result = 4
                else:
                    result = 20
            else:
                result = 20
        elif st.isalpha() and len(st) == 1:
            result = self.checkname(st)
        elif st == ',':
            result = 5
        elif st == ';':
            result = 6
        elif st == '=':
            result = 7
            self.isequal = 1
        elif st == 'return':
            result = 15
        elif st == '"' or st == "'":
            result = 8
            self.ischar = 1
        elif st == '{':
            result = 9
        elif st == '}':
            result = 10
        elif st == '[':
            result = 11
            self.isarray = 1
        elif st == ']':
            result = 12
        elif st == '(':
            result = 13
        elif st == ')':
            result = 14
        elif st in '+-*/':
            result = 17
        elif len(st) > 1 and st.isalnum():
            if st.isalnum():
                result = self.checkname(st)
            else:
                result = 20
        else:
            result = 20
        return result

    def checktype(self, st):
        if st == 'int':
            self.istype = [1, 0, 0, 0, 0]
        elif st == 'char':
            self.istype = [0, 1, 0, 0, 0]
        elif st == 'double':
            self.istype = [0, 0, 1, 0, 0]
        elif st == 'float':
            self.istype = [0, 0, 0, 1, 0]
        elif st == 'void':
            self.istype = [0, 0, 0, 0, 1]
        self.existtype = 1
        return 0

    def checkname(self, st):
        keywords = [
            'auto', 'double', 'int', 'struct',
            'break', 'else', 'long', 'switch',
            'case', 'enum', 'register', 'typedef',
            'char', 'extern', 'return', 'union',
            'const', 'float', 'short', 'unsigned',
            'continue', 'for', 'signed', 'void',
            'default', 'goto', 'sizeof', 'volatile',
            'do', 'if', 'static', 'while'
        ]
        if st[0].isdigit():
            return 20
        elif self.existtype == 1 or self.existtype == 0:
            if st in keywords:
                return 20
            elif self.iseqarray == 1 and self.isarray == 0:
                return 20
            elif self.ischar == 1:
                self.ischar = 0
                if self.istype == [0, 1, 0, 0, 0] and len(st) == 1:
                    return 3
                else:
                    return 20
            else:
                return 1

    def checknumber(self, st):
        if self.isequal == 1:
            if self.istype == [1, 0, 0, 0, 0]:
                if self.ischar == 1:
                    self.ischar = 0
                    return 20
                elif self.iseqarray == 1 and self.isarray == 0:
                    return 20
                else:
                    return 4
            elif self.istype == [0, 1, 0, 0, 0]:
                if self.ischar == 1:
                    self.ischar = 0
                    return 3
                else:
                    return 4
        elif self.isarray == 1:
            return 16
        else:
            return 20

    def check(self, kind, lst):
        codes = []
        i = 0
        while i < len(lst):
            codes.append(self.evaluate(lst[i]))
            i += 1

        i = 0
        while i < len(codes):
            if codes[i] == None:
                codes[i] = 20
            i += 1

        # VARIABLE DECLARATION
        if kind == 1:
            table = [
                [ 1, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20],
                [20,  2, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 19, 20, 20],
                [20, 20, 20, 20, 20, 15,  3,  4, 20, 20, 20, 16, 20, 20, 20, 20, 20, 20, 20, 20, 20],
                [ 1, 20, 20, 20, 20, 20,  3, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20],
                [20,  5, 20, 20,  5, 20, 20, 20,  6,  8, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20],
                [20, 20, 20, 20, 20, 15,  3, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20],
                [20, 20, 20,  7, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20],
                [20, 20, 20, 20, 20, 20, 20, 20,  5, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20],
                [20, 20, 20, 20, 13, 20, 20, 20,  9, 20,  5, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20],
                [20, 20, 20, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20],
                [20, 20, 20, 20, 20, 20, 20, 20, 11, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20],
                [20, 20, 20, 20, 20, 12, 20, 20, 20, 20,  5, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20],
                [20, 20, 20, 20, 20, 20, 20, 20,  9, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20],
                [20, 20, 20, 20, 20, 14, 20, 20, 20, 20,  5, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20],
                [20, 20, 20, 20, 13, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20],
                [20,  2, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20],
                [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 17, 20, 20, 20, 20],
                [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 18, 20, 20, 20, 20, 20, 20, 20, 20],
                [20, 20, 20, 20, 20, 15,  3,  4, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20],
                [20,  2, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20],
                [20,  2, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
            ]
            state = 0
            i = 0
            while i < len(codes):
                state = table[state][codes[i]]
                i += 1
            if state == 3:
                self.result("VALID VARIABLE DECLARATION")
            else:
                self.result("INVALID VARIABLE DECLARATION")

        # FUNCTION DECLARATION
        elif kind == 2:
            table = [
                [ 1,  2, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20],
                [20,  2, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20],
                [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20,  3, 20, 20, 20, 20, 20, 20, 20],
                [ 6, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20,  4, 20, 20, 20, 20, 20, 20],
                [20, 20, 20, 20, 20, 20,  5, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20],
                [ 1,  2, 20, 20, 20, 20,  5, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20],
                [20,  8, 20, 20, 20,  7, 20, 20, 20, 20, 20, 10, 20, 20,  9, 20, 20, 20, 20, 20, 20],
                [ 6, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20],
                [20, 20, 20, 20, 20,  7, 20, 20, 20, 20, 20, 10, 20, 20,  9, 20, 20, 20, 20, 20, 20],
                [20, 20, 20, 20, 20, 20,  5, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20],
                [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 11, 20, 20, 20, 20, 20, 20, 20, 20],
                [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20,  9, 20, 20, 20, 20, 20, 20],
                [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20],
                [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20],
                [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20],
                [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20],
                [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20],
                [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20],
                [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20],
                [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20],
                [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
            ]
            state = 0
            i = 0
            while i < len(codes):
                state = table[state][codes[i]]
                i += 1
            if state == 5:
                self.result("VALID FUNCTION DECLARATION")
            else:
                self.result("INVALID FUNCTION DECLARATION")

    # Print results to console
    def result(self, string):
        print(string)

# Main Function
def main():
    case = int(input()) # input number of test cases
    for i in range(case):
        line1, line2 = input().split(maxsplit=1) # splits input in two lines 1 for which kind (var or func declaration) and 2 for the string to be tested
        line2 = line2.strip() # removes spaces on the string to be tested
        
        par = DFA(line1, line2)
        par.process()

if __name__ == "__main__":
    main()
