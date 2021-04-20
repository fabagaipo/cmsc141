# cmsc141
code list for cmsc 141 Automata Language Theory machine problems; c++ and python

# Machine Problem 1: Ready, Get, SET!

For this MP, you are to implement the set data structure.
The set data structure is a container that stores unique elements in no particular order which should
allow for fast access. For this MP, implement the following operations for the set data structure:
1. insert
2. remove
3. subset
4. union
5. intersection
6. difference
7. power set

Implement the set as a template or generic that should allow the user to create different types of sets.
- set <int> s;
- set <string> s1;
- set < set<int> > s2;
For our purpose, we are to include int, double, char, string, set, and object.

Input File
The input file (named mpa2.in) will contain a number of lines. The first line is the number of test
cases. Each test case will contain a series of lines as well. The first line will contain a number
representing what type of sets are to be created (exactly two sets will be created for each test case).
The following are the different types:
1. int
2. double
3. char
4. string
5. set
6. object

If the type is of type set (5), then a second number will be found specifying what kind of a set its
elements are. Take for instance the sample below:
1
5 1
This means that for this test case, the sets will contain sets of integers as elements.

The next line will contain the default elements (separated by a space) of the first set followed by
another line containing the default elements (separated by a space) of the second set.
Another line with one number will follow. This number, say x, represents the number of operations that
will be performed or executed for this particular test case.

x lines will complete the test case. Each line will contain the type of operation to be performed or
executed followed by the necessary parameters for it to work. The following are the types of
operations:
1. insert
2. remove
3. subset
4. union
5. intersection
6. difference
7. power set
For 1 (insert), two items will follow (separated by a space), a number (either 1 or 2) determining in
which set the item is to be inserted and the item to be inserted. The same applies for 2 (remove).
For 3 (subset), no additional items will be found. This operation will simply verify whether the first set
is a subset of the second.
The same goes for 4 (union), 5 (intersection), and 6 (difference).
- 4 : union of the two sets
- 5 : intersection of the two sets
- 6 : 1 - 2 (set difference)
For operation 7 (power set), a number will follow it (separated by a space) specifying for which set the
operation is to be performed (1 or 2).
Below is a sample input file.
3
1
1 5 7 8
10 -2 4 5
3
1 1 8
1 2 7
3
4
hello abcd wxyz
world wxyz abcd lmno
4
1 1 world
2 2 world
5
7 2
5 1
{1,2,3} {1,2} {7,8,9}
{1,2} {1,2,5} {7,8,9,10}
2
2 2 {7,8,9,10}
7 2
Output file
For each operation performed or executed, a line of output should be printed to a file named
<lastname>1.out.● for insert and remove, display the contents of the set affected
● for subset, simply print true or false, depending on the verification
● for union, intersection, difference and power set, the contents of the resulting set
Below is a sample output file of the sample input file above.
{1,5,7,8}
{10,-2,4,5,7}
false
{hello,abcd,wxyz,world}
{wxyz,abcd,lmno}
{abcd,wxyz}
{empty,{wxyz},{abcd},{lmno},{wxyz,abcd},{wxyz,lmno},{abcd,lmno},{wxyz,abcd,lmno}}
{{1,2},{1,2,5}}
{empty,{{1,2}},{{1,2,5}},{{1,2},{1,2,5}}}

# Machine Problem 2: Paparazzi, Grammar Nazi

Multiple declarations, including those with initializations, are in scope. This also means that identifiers
have to be checked. They should follow the naming rule of c, i.e. they can start with '_' or any letter
from the English alphabet, followed by 0 or more alpha-numeric characters, including the '_'.
Samples
● int x;
● char c,h;
● float pi = 3.1416;
● double x, y, z = 6.022140857;
Function declaration
In a similar fashion, what will be in scope are functions returning primitive type values only. In addition,
functions that do not return any value, i.e. declared as void, will be in scope as well. Functions with
and without any argument list are in scope. And like in variable declarations, multiple function
declarations are in scope, too.
Samples
● void display();
● void compute(void);
● int square(int);
● int power(int,int);
● char toLower(char);● double squareRoot(float);
● int gcd(int,int), lcm(int,int);
● int isPrime(int n);
Input
The input is going to be a file. This file will contain a number of lines. This name of the input file should
be asked from the user. The first line of the input file will be a positive number. This positive, say c,
represents the number of test cases there are in the file. The actual test cases will follow in the next
line/s.
Output
The output is going to be a file. The file is going to contain c lines, c being the number of test cases. If
the test case is valid, print "VALID <type>." where <type> is any of the following:
● VARIABLE DECLARATION
● FUNCTION DECLARATION
Constraints and other instructions
● Implement this using c, c++, java, or python
● No use of built-in regex
● You are to include all the references you have used in solving this MP. The references may
be your old notes, online resources, etc. Include them in your source file as comments.
● If you have any questions about the MP, post them in the appropriate forum's discussion
board.
● As an additional reference, please check the sample input file and output file provided for this
MP.
Sample Input File:
4
int x, y, z = 10;
double a
int function();
INT function2(void);
int solve(int,char,double x,float,int,int);
Sample Output File:
VALID VARIABLE DECLARATION
INVALID VARIABLE DECLARATION
INVALID FUNCTION DECLARATION
VALID FUNCTION DECLARATION

# Machine Problem 3: Smiling Must me a Regular Expression

union
The symbol ‘+’ will be used to denote union or “OR”. Single symbols or concatenated strings may
surround it.
- a + b
- e+a + b
- aba + bba + e
concatenation
No symbol will be used for concatenation. Symbols that are beside each other are considered to have
been concatenated. And possibly enclosed with parentheses
- aaabbb
- ab
- bbbbbb
- a(a+b)a
Kleene star
The use of the Kleene is limited to single symbols and grouped/concatenated symbols. It will not be
used with “OR-ed” symbols or strings. And “starring” starred grouped/concatenated symbols is not in
scope as well.
- aaa*
- a*bb*
- (ab)*
- ((ab)(ba)*)* or ((aba)*(bab)*)* - FORMS LIKE THIS ARE NOT IN SCOPE
- (a+b)* or (ab+ ba)* - FORMS LIKE THIS ARE NOT IN SCORE AS WELLInput
The input file consists of a number of lines. The first line contains the number of test cases. The
following lines contain the test cases. Each test case consists of the regular expression, followed by a
number representing the number of strings that need to be verified or tested (whether the regular
expression generates the string (yes) or not (no) ). What follows next are the actual strings to be
tested.
Sample Input:
3
a*b*
3
aaabbbbbb
aaaaaa
bbbbbaaaaa
a + b
2
a
b
(ab)*(aa + bb)
6
aa
e
abababbb
abababaaaa
aaaaaabbbbbb
bbbbbbababab
Output
Simply print “yes” or “no” in one line for every test case. Below is the sample output of the sample
input above.
yes
yes
no
yes
yes
yes
yes
yes
no
no
no

# Machine Problem 4: Paparazzi, Grammar Nazi 2.0

Multiple declarations, including those with initializations, are in scope. This also means that identifiers
have to be checked. They should follow the naming rule of c, i.e. they can start with '_' or any letter
from the English alphabet, followed by 0 or more alpha-numeric characters, including the '_'.
Samples
- int x;
- char c,h;
- float pi = 3.1416;
- double x, y, z = 6.022140857;
Function declaration
In a similar fashion, what will be in scope are functions returning primitive type values only. In addition,
functions that do not return any value, i.e. declared as void, will be in scope as well. Functions with
and without any argument list are in scope. And like in variable declarations, multiple function
declarations are in scope, too.
Samples
- void display();
- void compute(void);
- int square(int);
- int power(int,int);
- char toLower(char);
- double squareRoot(float);● int gcd(int,int), lcm(int,int);
- int isPrime(int n);
Input
The input is going to be a file. This file will contain a number of lines. This name of the input file should
be asked from the user. The first line of the input file will be a positive number. This positive, say c,
represents the number of test cases there are in the file. The actual test cases will follow in the next
line/s.
Output
The output is going to be a file. The file is going to contain c lines, c being the number of test cases. If
the test case is valid, print "VALID <type>." where <type> is any of the following:
- VARIABLE DECLARATION
- FUNCTION DECLARATION
Sample Input File:
4
int x, y, z = 10;
double a
int function();
INT function2(void);
int solve(int,char,double x,float,int,int);
Sample Output File:
VALID VARIABLE DECLARATION
INVALID VARIABLE DECLARATION
INVALID FUNCTION DECLARATION
VALID FUNCTION DECLARATION

Machine Problem 5: Paparazzi, Grammar Nazi 3.0

Multiple declarations, including those with initializations with arithmetic expressions, are in scope. This
also means that identifiers have to be checked. They should follow the naming rule of c, i.e. they can
start with '_' or any letter from the English alphabet, followed by 0 or more alpha-numeric characters,
including the '_'.
Samples
- int x = 4+8-(4/2*(10-8)+249);
- char c,h;
- float pi = 3.1416;
- double x, y, z = 6.022140857;
Function declaration
In a similar fashion, what will be in scope are functions returning primitive type values only. In addition,
functions that do not return any value, i.e. declared as void, will be in scope as well. Functions with
and without any argument list are in scope. And like in variable declarations, multiple function
declarations are in scope, too.
Samples
- void display();
- void compute(void);
- int square(int);
- int power(int,int);
- char toLower(char);● double squareRoot(float);
- int gcd(int,int), lcm(int,int);
- int isPrime(int n);
Function definition
The same types of functions as those in function declaration are in scope. What will be interesting
here is that the variable declaration described above are in scope in function definition, including the
following:
- assignment statements
- assignment statements with arithmetic expressions
- assignment statements with arithmetic expressions that utilize the parentheses for grouping
operations
- return statements (all kinds of statements that are in scope for function definition
No control structures will be in scope for this MP. There will be no input/output statements as well.
Samples
void test(){
}
int square(int x){
int ans;
ans = x * x;
return ans;
}
int addition(int a, int b){
return a+b;
}
int compute(int n){
int val = (3*(n - 5)) - 49;
return val;
}
Input
The input is going to be a file. This file will contain a number of lines. This name of the input file should
be asked from the user. The first line of the input file will be a positive number. This positive, say c,
represents the number of test cases there are in the file. The actual test cases will follow in the next
line/s.
Output
The output is going to be a file. The file is going to contain c lines, c being the number of test cases. If
the test case is valid, print "VALID <type>." where <type> is any of the following:
- VARIABLE DECLARATION
- FUNCTION DECLARATION
- FUNCTION DEFINITION
Sample Input File
6
int x, y, z = 10;
double a
int function();int func(int){
int x = 10;
}
int square(int x){
return x * x;
}
INT function2(void);
int solve(int,char,double x,float,int,int);
Sample Output File
VALID VARIABLE DECLARATION
INVALID VARIABLE DECLARATION
INVALID FUNCTION DEFINITION
VALID FUNCTION DEFINITION
INVALID FUNCTION DECLARATION
VALID FUNCTION DECLARATION

Machine Problem 6: Turing Machine Simulation

Simulate the Turing machine solutions of the following problems:
- Palindrome over {0, 1}
- String Comparison problem
- Given two string inputs over {0, 1}, determine if the two input strings are the same
string
- Subtraction and multiplication over {1}
 This is the same subtraction and multiplication discussed in class
- The value of the string is simply the number of 1’s there are in the string (or
the length of the string)
- 111 is 3
- 11111111 is 8
 Subtraction
- 1111111 - 111 = 1111
 Multiplication
- 11 x 111 = 111111
The simulation may be done on the console or with any graphics
