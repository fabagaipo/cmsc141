import re

# process:
# converts regular expression into python regular expression format
# compares with test string

ans = []
ncase = int(input())
for i in range(ncase):
    #print("case " + str(i+1))
    rgxp = input()
    rgxp = rgxp.replace("+", "|")
    rgxp = rgxp.replace(" ", "")
    rgxp = rgxp.replace("*", "*?")

    rgxp = rgxp.replace("e", "^(?![\s\S])") # replacement string for e is a regex that accepts empty strings only (taken from online source). needed in case of a regex:a+b+e for example. e should be a valid test case here.

    rgxp = "(" + rgxp + ")"
    rgxp = "^" + rgxp + "$"

    #print("This is the regex: " + rgxp)
    ntest = int(input())
    for j in range(ntest):
        test = input()
        if test == "e": #e is equal to the empty string
          test = ""
        result = re.match(rgxp, test)
        if(result):
            ans.append("yes")
        else:
            ans.append("no")

print(*ans, sep = "\n") #prints all the answers in the list, separated by a newline
