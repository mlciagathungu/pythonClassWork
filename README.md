## PYTHON FUNDAMENTALS
variables
## primitives
1. Data types
   1. String
   2. Number
      -interger
      -float
      -complex
## non primitives
1. list :: ordered mutabilty
    variablename=("","","")
2. Tuple :: ordered ,immutable collection
  variablename =(,)
3. Range
     variablename =(,)
4. set::collection of items

## PYTHON OPERATORS
1. Ariithmetic operators
2. Comparison operators
3. Logic operators
   -And ::&:: returns true if both conditions are true
   -Or ::||:: returns true if one conditions is true
   - Not ::!:: reverses the result 
5. Assignment operators
   = : assign x=4
   += :add and assign eg. x+=2,(x=x+2)
   -= :subtracts and assign eg. x-=2,(x=x-2)
   *= : multiples and assigns x*= 3 , ( x = x* 3)
   /= : divides and assigns x/= 3 ,( x = x/3)
   %= : modulus and assigns %=3 , ( x = x%3)

   7. Identity operators
      Is : returns true if both comparisons refer to the same object.
      Is not : returns true if they refer to different objects.
## 3. Conditional statement 
1. If ,elif and else statements
   If condition:
    Code to be executed
2. Ternary operator/ conditional
   Shorthand way of writing an if, else statements
   Age= 18 
Variableresult = ( What to be evaluated if true
3. Nested if
   An if statement with an if statement.
   If condition:
         Code to be executed.
   If condition:
         Code to be executed.
4. Match-case
   Matches a code logic as per selection.
   Variable=""
Match variable:
           Case "selection": 
                    Code execution 
## Loops 
1. For loop
   Iterates (loop) over sequences \; list, dictionary, tuple, string and range.
2. While loop
While condition: 
         Code to be repeated 
              Stop
## Loop control statements
1. Break  :: Exists a loop earlier. 
2. Continue :: skips and moves to the next.
3. Pass :: It's simply a placeholder.
## TO CONVERT 
1. Integer = int (value to be converted)
2. Float  =float (value to be converted)
3. String = str (value to be converted)
4. Boolean = bool (value to be converted)
5. List= list  (value to be converted)
6. Tuple = tuple (value to be converted)
7. Set= set (value to be converted)
   
## FUNCTIONS 
Block of code logic or series of code logic that can return a value or be void.Functions in python are defined using a def keyword 
Def functionName ():
       Code logic For a function to be executed it has to be invoked/ called/ python has two groups of functions.
# In built
1. String function:
text = " Hello world"
      Print( len(text)):: returns the length of the string 
      Print(text.upper()):: into caps 
      Print(text.lower()):: into lower case letters 
      Print (text.replace(_old:"", _ new:""):: replaces                               
      text
      Print ( text.split()):: deconstructs and returns a
      list version of the referred string.
3. Integer function:
    pos_num= 10
    neg_ num =-1
    float_ num=10.5
   
    Print(abs( neg_ num)):: returns the positive version 
    of the no
    Print (pow(2,3)) ::2^3 =2*2*2= 8
    Print (divmod(pos_ num,neg_num)):: (10,-1) quotient
    and remainder are returned as tuple 
    Print (round (float_num,1))
    Print( sum([ pos_num, float_num]))::10+ 10.5 List functions nums = [ 3,5,6,8]
    Print ( lens( nums)):: returns the number of items in 
    the list 
    Print (list( reversed( nums))):: reverses the list 
    Print ( min(nums)) returns the minimum number 
    Print( max ( nums)) returns the maximum number 
    nums.append(5)
    Print( nums):: adds an item in the list
    Print( nums.pop()):: removes the added item in 
    the list and returns it 

