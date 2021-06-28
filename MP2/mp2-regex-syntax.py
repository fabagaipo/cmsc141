import re

fvld = "VALID FUNCTION DECLARATION"
fnvld = "INVALID FUNCTION DECLARATION"
vvld = "VALID VARIABLE DECLARATION"
vnvld = "INVALID VARIABLE DECLARATION"
ans = []

#VARIABLE REGEX

#valid pattern for int (single declaration)
v_int_pattern = "(?:int)( )+(?!int|char|float|double|void)([a-zA-Z_][a-zA-Z0-9_]*( )*(;+|=( )*[0-9][0-9]*( )*;+))"

#int cases for multiple declaration (segmented by comma)
startv_int = "(?:int)( )+(?!int|char|float|double|void)[a-zA-Z_][a-zA-Z0-9_]*( )*(=( )*[0-9][0-9]*( )*)*" #valid case for string before first comma
middlev_int = "( )*(?!int|char|float|double|void)[a-zA-Z_][a-zA-Z0-9_]*( )*(=( )*[0-9][0-9]*( )*)*" #valid case for any of the middle segments
lastv_int = "(?!int|char|float|double|void)[a-zA-Z_][a-zA-Z0-9_]*( )*(=( )*[0-9][0-9]*( )*)*( )*;+" #valid case for final segment

#valid pattern for double/float (single declaration)
v_df_pattern = "((?:double|float)( )+(?!int|char|float|double|void)([a-zA-Z_][a-zA-Z0-9_]*( )*;+)|(?:double|float)( )+(?!int|char|float|double|void)([a-zA-Z_][a-zA-Z0-9_]*( )*=( )*([0-9][0-9]*)|(([0-9][0-9]*)(\.)[0-9][0-9]*)( )*;+))"

#double/float cases for multiple declaration (segmented by comma)
startv_df = "(?:double|float)( )+(?!int|char|float|double|void)[a-zA-Z_][a-zA-Z0-9_]*( )*(( )*|=( )*([0-9][0-9]*)|(([0-9][0-9]*)(\.)[0-9][0-9]*)( )*)" #valid case for string before first comma
middlev_df = "( )*(?!int|char|float|double|void)[a-zA-Z_][a-zA-Z0-9_]*( )*|( )*=( )*(( )*=( )*[0-9][0-9]*)|(([0-9][0-9]*)(\.)[0-9][0-9]*)( )*" #valid case for any of the middle segments
lastv_df = "( )*(?!int|char|float|double|void)[a-zA-Z_][a-zA-Z0-9_]*( )*|( )*=( )*([0-9][0-9]*)|( )*=( )*(([0-9][0-9]*)(\.)[0-9][0-9]*)( )*;+" #valid case for final segment

#valid pattern for char (single declaration)
v_c_pattern ="(?:char)( )+(?!int|char|float|double|void)([a-zA-Z_][a-zA-Z0-9_]*( )*(;+|=( )*(').(')( )*;+))"

#char cases for multiple declaration (segmented by comma)
startv_c = "((?:char)( )+(?!int|char|float|double|void)([a-zA-Z_][a-zA-Z0-9_]*( )*))|(?:char)( )+(?!int|char|float|double|void)([a-zA-Z_][a-zA-Z0-9_]*( )*=( )*(').(')( )*)"

middlev_c = "( )*(?!int|char|float|double|void)([a-zA-Z_][a-zA-Z0-9_]*( )*)|(?:char)( )+(?!int|char|float|double|void)([a-zA-Z_][a-zA-Z0-9_]*( )*=( )*(').(')( )*)"

lastv_c = "( )*(?!int|char|float|double|void)([a-zA-Z_][a-zA-Z0-9_]*( )*)|(?:char)( )+(?!int|char|float|double|void)([a-zA-Z_][a-zA-Z0-9_]*( )*=( )*(').(')( )*;+)"

#FUNCTION REGEX

#no arg, single declaration
f_pattern1 = "(?:int|char|float|double|void)( )+(?!int|char|float|double|void)[a-zA-Z_][a-zA-Z0-9_]*( )*\(( )*\);+"

#has nameless args, single declaration (possibly redundant given that we have pattern3)
f_pattern2 = "(?:int|char|float|double|void)( )+(?!int|char|float|double|void)[a-zA-Z_][a-zA-Z0-9_]*( )*\((( )*(?:int|char|float|double|void)( )*,)*(( )*(?:int|char|float|double|void)( )*)\);+"

#has args with names, single declaration
f_pattern3 = "(?:int|char|float|double|void)( )+(?!int|char|float|double|void)[a-zA-Z_][a-zA-Z0-9_]*( )*\(((( )*(?:int|char|float|double|void)( )*,)|(( )*(?:int|char|float|double|void)( )+(?!int|char|float|double|void)[a-zA-Z_][a-zA-Z0-9_]*( )*,))*((( )*(?:int|char|float|double|void)( )*)|(( )*(?:int|char|float|double|void)( )+(?!int|char|float|double|void)[a-zA-Z_][a-zA-Z0-9_]*( )*))\);+"

#multiple declaration with multiple args
f_pattern4 = "(?:int|char|float|double|void)( )+(( )*(?!int|char|float|double|void)[a-zA-Z_][a-zA-Z0-9_]*( )*\(((( )*(?:int|char|float|double|void)( )*,)|(( )*(?:int|char|float|double|void)( )+(?!int|char|float|double|void)[a-zA-Z_][a-zA-Z0-9_]*( )*,))*((( )*|(( )*(?:int|char|float|double|void)( )*)|(( )*(?:int|char|float|double|void)( )+(?!int|char|float|double|void)[a-zA-Z_][a-zA-Z0-9_]*( )*)))\),)*(( )*(?!int|char|float|double|void)[a-zA-Z_][a-zA-Z0-9_]*( )*\(((( )*(?:int|char|float|double|void)( )*,)|(( )*(?:int|char|float|double|void)( )+(?!int|char|float|double|void)[a-zA-Z_][a-zA-Z0-9_]*( )*,))*(((( )*(?:int|char|float|double|void)( )*)|(( )*(?:int|char|float|double|void)( )+(?!int|char|float|double|void)[a-zA-Z_][a-zA-Z0-9_]*( )*)|( )*))\))( )*;+"

n = int(input())

for i in range(n):
  tcase = input()
  tcase = tcase.strip() #removes extra spaces at beginning and end of string

  if "(" in tcase:
    #print(tcase + " is a function")
    if re.match(f_pattern1,tcase):
      ans.append(fvld)
    elif re.match(f_pattern2,tcase):
      ans.append(fvld)
    elif re.match(f_pattern3,tcase):
      ans.append(fvld)
    elif re.match(f_pattern4,tcase):
      ans.append(fvld)
    else:
      ans.append(fnvld)

  else:

    if "," in tcase:
      flag = 0

      splitcase = [x.strip() for x in tcase.split(',')] #splits the test case by commas

      if tcase.startswith("float") | tcase.startswith("double"):
        for i in range(len(splitcase)):
          if i == 0:
            if not (re.match(startv_df,splitcase[i])):
              flag = flag+1
              #print("flag start")
          elif i == len(splitcase):
            if not (re.match(lastv_df,splitcase[i])):
              flag = flag + 1
              #print("flag last")
          else:
            if not (re.match(middlev_df,splitcase[i])):
              flag = flag + 1
              #print("flag mid")

      elif tcase.startswith("char"):
        #print("char type")
        for i in range(len(splitcase)):
          if i == 0:
            if not (re.match(startv_c,splitcase[i])):
              flag = flag+1
              #print("flag start char")
          elif i == len(splitcase):
            if not (re.match(lastv_c,splitcase[i])):
              flag = flag + 1
              #print("flag last char")
          else:
            if not (re.match(middlev_c,splitcase[i])):
              flag = flag + 1
              #print("flag mid char")

      else:
        for i in range(len(splitcase)):
          if i == 0:
            if not (re.match(startv_int,splitcase[i])):
              flag = flag+1
              #print("flag int start")
          elif i == len(splitcase):
            if not (re.match(lastv_int,splitcase[i])):
              flag = flag + 1
              #print("flag int last")
          else:
            if not (re.match(middlev_int,splitcase[i])):
              flag = flag + 1
              #print("flag int mid")

      #print("No of flags: " + str(flag))

      if flag>0:
        ans.append(vnvld)
      else:
        ans.append(vvld)

    else:
      flag = 0;

      if tcase.startswith("float") | tcase.startswith("double"):
        if not re.match(v_df_pattern,tcase):
          flag = flag+1

      elif tcase.startswith("char"):
        if not re.match(v_c_pattern,tcase):
          flag = flag+1

      else:
        if not re.match(v_int_pattern,tcase):
          flag = flag+1

      if flag>0:
        ans.append(vnvld)
      else:
        ans.append(vvld)

print(*ans, sep = "\n")
