# JavaScript Warm-Up Tasks

This project contains a series of tasks to help you warm up with JavaScript. Below is a brief description of each task and the requirements.

## Tasks

### 0. First constant, first print
Write a script that prints "JavaScript is amazing":

- You must create a constant variable called `myVar` with the value "JavaScript is amazing".
- You must use `console.log(...)` to print all output.
- You are not allowed to use `var`.

**File:** `0-javascript_is_amazing.js`

```sh
$ ./0-javascript_is_amazing.js 
JavaScript is amazing
```

### 1. 3 languages
Write a script that prints 3 lines:

- The first line: "C is fun"
- The second line: "Python is cool"
- The third line: "JavaScript is amazing"
- You must use `console.log(...)` to print all output.
- You are not allowed to use `var`.

**File:** `1-multi_languages.js`

```sh
$ ./1-multi_languages.js 
C is fun
Python is cool
JavaScript is amazing
```

### 2. Arguments
Write a script that prints a message depending on the number of arguments passed:

- If no arguments are passed to the script, print "No argument".
- If only one argument is passed to the script, print "Argument found".
- Otherwise, print "Arguments found".
- You must use `console.log(...)` to print all output.
- You are not allowed to use `var`.

**File:** `2-arguments.js`

```sh
$ ./2-arguments.js 
No argument
$ ./2-arguments.js Best
Argument found
$ ./2-arguments.js Best School
Arguments found
```

### 3. Value of my argument
Write a script that prints the first argument passed to it:

- If no arguments are passed to the script, print "No argument".
- You must use `console.log(...)` to print all output.
- You are not allowed to use `var`.
- You are not allowed to use `length`.

**File:** `3-value_argument.js`

```sh
$ ./3-value_argument.js 
No argument
$ ./3-value_argument.js School
School
```

### 4. Create a sentence
Write a script that prints two arguments passed to it, in the following format: " is ".

- You must use `console.log(...)` to print all output.
- You are not allowed to use `var`.

**File:** `4-concat.js`

```sh
$ ./4-concat.js c cool
c is cool
$ ./4-concat.js c 
c is undefined
$ ./4-concat.js
undefined is undefined
```

### 5. An Integer
Write a script that prints `My number: <first argument converted in integer>` if the first argument can be converted to an integer:

- If the argument can’t be converted to an integer, print "Not a number".
- You must use `console.log(...)` to print all output.
- You are not allowed to use `var`.
- You are not allowed to use `try/catch`.

**File:** `5-to_integer.js`

```sh
$ ./5-to_integer.js 
Not a number
$ ./5-to_integer.js 89
My number: 89
$ ./5-to_integer.js "89"
My number: 89
$ ./5-to_integer.js 89.89
My number: 89
$ ./5-to_integer.js School
Not a number
```

### 6. Loop to languages
Write a script that prints 3 lines (like `1-multi_languages.js`) but by using an array of string and a loop:

- The first line: "C is fun"
- The second line: "Python is cool"
- The third line: "JavaScript is amazing"
- You must use `console.log(...)` to print all output.
- You are not allowed to use `var`.
- You are not allowed to use any `if/else` statement.
- You can use only one `console.log`.
- You must use a loop (`while`, `for`, etc.).

**File:** `6-multi_languages_loop.js`

```sh
$ ./6-multi_languages_loop.js 
C is fun
Python is cool
JavaScript is amazing
```

### 7. I love C
Write a script that prints `x` times "C is fun":

- Where `x` is the first argument of the script.
- If the first argument can’t be converted to an integer, print "Missing number of occurrences".
- You must use `console.log(...)` to print all output.
- You are not allowed to use `var`.
- You can use only two `console.log`.
- You must use a loop (`while`, `for`, etc.).

**File:** `7-multi_c.js`

```sh
$ ./7-multi_c.js 2
C is fun
C is fun
$ ./7-multi_c.js 5
C is fun
C is fun
C is fun
C is fun
C is fun
$ ./7-multi_c.js 
Missing number of occurrences
$ ./7-multi_c.js -3
```

### 8. Square
Write a script that prints a square:

- The first argument is the size of the square.
- If the first argument can’t be converted to an integer, print "Missing size".
- You must use the character `X` to print the square.
- You must use `console.log(...)` to print all output.
- You are not allowed to use `var`.
- You must use a loop (`while`, `for`, etc.).

**File:** `8-square.js`

```sh
$ ./8-square.js
Missing size
$ ./8-square.js School
Missing size
$ ./8-square.js 2
XX
XX
$ ./8-square.js 6
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
$ ./8-square.js -3
```

### 9. Add
Write a script that prints the addition of 2 integers:

- The first argument is the first integer.
- The second argument is the second integer.
- You have to define a function with this prototype: `function add(a, b)`.
- You must use `console.log(...)` to print all output.
- You are not allowed to use `var`.

**File:** `9-add.js`

```sh
$ ./9-add.js 
NaN
$ ./9-add.js 1
NaN
$ ./9-add.js 1 7
8
$ ./9-add.js 13 89
102
```

### 10. Factorial
Write a script that computes and prints a factorial:

- The first argument is an integer (argument can be cast as an integer) used for computing the factorial.
- Factorial of `NaN` is 1.
- You must do it recursively.
- You must use a function.
- You must use `console.log(...)` to print all output.
- You are not allowed to use `var`.

**File:** `10-factorial.js`

```sh
$ ./10-factorial.js 
1
$ ./10-factorial.js 3
6
$ ./10-factorial.js 89
1.6507955160908452e+136
$ ./10-factorial.js 333
Infinity
```

### 11. Second biggest!
Write a script that searches the second biggest integer in the list of arguments:

- You can assume all arguments can be converted to integers.
- If no argument is passed, print `0`.
- If the number of arguments is `1`, print `0`.
- You must use `console.log(...)` to print all output.
- You are not allowed to use `var`.

**File:** `11-second_biggest.js`

```sh
$ ./11-second_biggest.js 
0
$ ./11-second_biggest.js 1
0
$ ./11-second_biggest.js 4 2 5 3 0 -3
4
```

### 12. Object
Update this script to replace the value 12 with 89:

- You are not allowed to use `var`.

**File:** `12-object.js`

```sh
$ cat 12-object.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/* YOUR CODE HERE */
console.log(myObject);
$ ./12-object.js
{ type: 'object', value: 12 }
{ type: 'object', value: 89 }
```

### 13. Add file
Write a function that returns the addition of 2 integers:

- The function must be visible from outside.
- The name of the function must be `add`.
- You are not allowed to use `var`.

**File:** `13-add.js`

```sh
$ cat 13-main.js
#!/usr/bin/node
const add = require('./13-add').add;
console.log(add(3, 5));
$ ./13-main.js
8
```

### 14. Const or not const
Write a file that modifies the value of `myVar` to 333:

**File:** `100-let_me_const.js`

```sh
$ cat 100-main.js
#!/usr/bin/node
myVar = 89;
require('./100-let_me_const')
console.log(myVar);
$ ./100-main.js
333
```

### 15. Call me Moby
Write a function that executes `x` times a function:

- The function must be visible from outside.
- Prototype: `function (x,

 theFunction)`.
- You are not allowed to use `var`.

**File:** `101-call_me_moby.js`

```sh
$ cat 101-main.js
#!/usr/bin/node
const callMeMoby = require('./101-call_me_moby').callMeMoby;
callMeMoby(3, function () {
  console.log('C is fun');
});
$ ./101-main.js
C is fun
C is fun
C is fun
```

### 16. Add me maybe
Write a function that increments and calls a function:

- The function must be visible from outside.
- Prototype: `function (number, theFunction)`.
- You are not allowed to use `var`.

**File:** `102-add_me_maybe.js`

```sh
$ cat 102-main.js
#!/usr/bin/node
const addMeMaybe = require('./102-add_me_maybe').addMeMaybe;
addMeMaybe(4, function (nb) {
  console.log('New value: ' + nb);
});
$ ./102-main.js
New value: 5
```

### 17. Increment object
Update this script by adding a new function `incr` that increments the value:

- You are not allowed to use `var`.

**File:** `103-object_fct.js`

```sh
$ cat 103-object_fct.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
$ ./103-object_fct.js 
{ type: 'object', value: 12 }
{ type: 'object', value: 13 }
{ type: 'object', value: 14 }
{ type: 'object', value: 15 }
```
