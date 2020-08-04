# Python-Code_Formatting

Code and notes from a series of tutorials on code formatting in python

## Notes

1. Code is read much more often than it is written.
   1. Following a code standard like PEP-8 ensures that everyone writes code of the same standard, and thus it can eb understood by everyone.
2. Naming conventions can be used to convey metadata about tokens in the program. Refer to table at the end.
3. Names must have meaning

    ```python
    # Not recommended
    x = "John Smith"
    y, z = x.split()
    print(z, y, sep=", ")
    "Smith, John"
    ```

    ```python
    # Recommended
    name = "John Smith"
    first_name, last_name = name.split()
    print(last_name, first_name, sep=", ")
    "Smith, John"
    ```

4. Try not to use abbreviations either
5. Surround top-level functions and classes with two blank lines
6. Surround method definitions inside classes with a single blank line
7. Use concise and descriptive names whenever possible

    ```python
    # Not recommended
    def db(x):
        return x * 2
    ```

    ```python
    # Recommended
    def multiply_by_two(x):
        return x * 2
    ```

8. Surround method definitions inside classes with a single blank line

    ```python
    class MyClass:
        def first_method(self):
            return None

        def second_method(self):
            return None
    ```

9. Functions should follow Single Responsibility principle
10. Modularisation helps with DRY
11. Consider breaking up a complex function into multiple parts

    ```python
    class MyFirstClass:
        pass


    class MySecondClass:
        pass


    def top_level_function():
        return None
    ```

12. Use blank lines sparingly inside functions to show clear steps

    ```python
    def calculate_variance(number_list):
        sum_list = 0
        for number in number_list:
            sum_list = sum_list + number
        mean = sum_list / len(number_list)

        sum_squares = 0
        for number in number_list:
            sum_squares = sum_squares + number ** 2
        mean_squares = sum_squares / len(number_list)

        return mean_squares - mean ** 2
    ```

13. Limit line lengths to 79 characters, Python will assume line continuation if code is contained within parentheses, brackets, or braces
14. If it is impossible to use implied continuation, then you can use backslashes to break lines instead

    ```python
    from mypkg import example1, example2, example3
    ```

15. If line breaking needs to occur around binary operators, like + and *, it should occur before the operator. This rule stems from mathematics. Mathematicians agree that breaking before binary operators improves readability.

    ```python
    # Recommended
    total = first_variable + second_variable - third_variable
    ```

16. The key indentation rules laid out by PEP 8 are the following
    1. Use 4 consecutive spaces to indicate indentation.
    2. Prefer spaces over tabs.
17. You should use spaces instead of tabs when indenting code. Python 3 does not allow mixing of tabs and spaces.
18. An alternative style of indentation following a line break is a hanging indent. This is a typographical term meaning that every line but the first in a paragraph or statement is indented. You can use a hanging indent to visually represent a continuation of a line of code.

    ```python
    var = function(arg_one, arg_two, arg_three, arg_four)
    ```

19. To improve readability, you should indent a continued line to show that it is a continued line. There are two ways of doing this. The first is to align the indented block with the opening delimiter. The second is to use a hanging indent.
20. PEP 8 provides two options for the position of the closing brace in implied line continuations

    ```python
    list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ```

21. You should use comments to document code as it’s written. It is important to document your code so that you, and any collaborators, can understand it. When you or someone else reads a comment, they should be able to easily understand the code the comment applies to and how it fits in with the rest of your code.
22. Limit the line length of comments and docstrings to 72 characters.
23. Use complete sentences, starting with a capital letter.
24. Make sure to update comments if you change your code.
25. Use block comments to document a small section of code. They are useful when you have to write several lines of code to perform a single action, such as importing data from a file or updating a database entry. They are important as they help others understand the purpose and functionality of a given code block.
26. Indent block comments to the same level as the code they describe.
27. Start each line with a # followed by a single space.
28. Separate paragraphs by a line containing a single #.

    ```python
    def quadratic(a, b, c, x):
        # Calculate the solution to a quadratic equation using the quadratic
        # formula.
        #
        # There are always two solutions to a quadratic equation, x_1 and x_2.
        x_1 = (-b + (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a)
        x_2 = (-b - (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a)
        return x_1, x_2
    ```

29. Inline comments explain a single statement in a piece of code. They are useful to remind you, or explain to others, why a certain line of code is necessary.
30. Use inline comments sparingly.
31. Write inline comments on the same line as the statement they refer to.
32. Separate inline comments by two or more spaces from the statement.
33. Start inline comments with a # and a single space, like block comments.
34. Don’t use them to explain the obvious.
35. This, however, ignores that coding practices change over time and inline comments can be used to describe code that might seem esoteric over a long period of time.

    ```python
    x = "John Smith"  # Student Name
    ```

36. Documentation strings, or docstrings, are strings enclosed in double (""") or single (''') quotation marks that appear on the first line of any function, class, method, or module. You can use them to explain and document a specific block of code.
37. Surround docstrings with three double quotes on either side, as in """This is a docstring""".
38. Write them for all public modules, functions, classes, and methods.
39. Put the """ that ends a multiline docstring on a line by itself:

    ```python
    def quadratic(a, b, c, x):
        """Solve quadratic equation via the quadratic formula.

        A quadratic equation has the following form:
        ax**2 + bx + c = 0

        There always two solutions to a quadratic equation: x_1 & x_2.
        """
        x_1 = (-b + (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a)
        x_2 = (-b - (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a)

        return x_1, x_2
    ```

40. Surround the following binary operators with a single space on either side:
    1. Assignment operators (=, +=, -=, and so forth)
    2. Comparisons (==, !=, >, <. >=, <=) and (is, is not, in, not in)
    3. Booleans (and, not, or)
41. When = is used to assign a default value to a function argument, do not surround it with spaces.
42. When there’s more than one operator in a statement, adding a single space before and after each operator can look confusing. Instead, it is better to only add whitespace around the operators with the lowest priority, especially when performing mathematical manipulation.
43. In slices, colons act as a binary operators. Therefore, there should be the same amount of whitespace either side.
44. The following list outlines some cases where you should avoid adding whitespace
    1. Immediately inside parentheses, brackets, or braces
    2. Before a comma, semicolon, or colon
    3. Before the open parenthesis that starts the argument list of a function call
    4. Before the open bracket that starts an index or slice
    5. Between a trailing comma and a closing parenthesis
    6. To align assignment operators
45. Don’t compare boolean values to True or False using the equivalence operator. You’ll often need to check if a boolean value is True or False.The use of the equivalence operator, ==, is unnecessary here. bool can only take values True or False.

    ```python
    # Not recommended
    my_bool = 6 > 5
    if my_bool == True:
        return "6 is bigger than 5"
    # Recommended
    if my_bool:
        return "6 is bigger than 5"
    ```

46. Use the fact that empty sequences are falsy in if statements. If you want to check whether a list is empty, you might be tempted to check the length of the list. If the list is empty, it’s length is 0 which is equivalent to False when used in an if statement. In Python any empty list, string, or tuple is falsy

    ```python
    # Not recommended
    my_list = []
    if not len(my_list):
        print("List is empty!")
    # Recommended
    my_list = []
    if not my_list:
        print("List is empty!")
    ```

47. Use `is not` rather than `not ... is` in if statements. If you are trying to check whether a variable has a defined value, there are two options. The first is to evaluate an if statement with `x is not None`. A second option would be to evaluate `x is None` and then have an if statement based on `not` the outcome. While both options will be evaluated correctly, the first is simpler, so PEP 8 encourages it.

    ```python
    # Recommended
    if x is not None:
        return "x exists!"
    # Not recommended
    if not x is None:
        return "x exists!"
    ```

48. Don’t use if x: when you mean if x is not None:. Sometimes, you may have a function with arguments that are None by default. A common mistake when checking if such an argument, arg, has been given a different value is to use

    ```python
    # Not Recommended
    if arg:
        pass
    ```

49. This code checks that arg is truthy. Instead, you want to check that arg is not None, so it would be better to use

    ```python
    # Recommended
    if arg is not None:
        pass
    ```

50. The mistake being made here is assuming that not None and truthy are equivalent. You could have set arg = []. As we saw above, empty lists are evaluated as falsy in Python. So, even though the argument arg has been assigned, the condition is not met, and so the code in the body of the if statement will not be executed
51. Use .startswith() and .endswith() instead of slicing. If you were trying to check if a string word was prefixed, or suffixed, with the word cat, it might seem sensible to use list slicing. However, list slicing is prone to error, and you have to hardcode the number of characters in the prefix or suffix. It is also not clear to someone less familiar with Python list slicing what you are trying to achieve. However, this is not as readable as using `.startswith()`. Similarly, the same principle applies when you’re checking for suffixes. You could use `.endswith()`.

    ```python
    # Not recommended
    if word[:3] == "cat":
        print('The word starts with "cat"')
    # Recommended
    if word.startswith("cat"):
        print('The word starts with "cat"')
    # Not recommended
    if file_name[-3:] == "jpg":
        print("The file is a JPEG")
    # Recommended
    if file_name.endswith("jpg"):
        print("The file is a JPEG")
    ```

52. Linters are programs that analyze code and flag errors. They provide suggestions on how to fix the error. Linters are particularly useful when installed as extensions to your text editor, as they flag errors and stylistic problems while you write.
53. pycodestyle is a tool to check your Python code against some of the style conventions in PEP 8.

    ```shell
    $ pycodestyle code.py
    code.py:1:17: E231 missing whitespace after ','
    code.py:2:21: E231 missing whitespace after ','
    code.py:6:19: E711 comparison to None should be 'if cond is None:'
    ```

54. flake8 is a tool that combines a debugger, pyflakes, with pycodestyle.

    ```shell
    $ flake8 code.py
    code.py:1:17: E231 missing whitespace after ','
    code.py:2:21: E231 missing whitespace after ','
    code.py:3:17: E999 SyntaxError: invalid syntax
    code.py:6:19: E711 comparison to None should be 'if cond is None:'
    ```

55. Autoformatters are programs that refactor your code to conform with PEP 8 automatically. Once such program is black, which autoformats code following most of the rules in PEP 8. One big difference is that it limits line length to 88 characters, rather than 79. If you want to alter the line length limit, then you can use the --line-length flag

    ```shell
    $ black --line-length=79 code.py
    reformatted code.py
    All done! ✨ 🍰 ✨
    ```

56. Two other autoformatters, autopep8 and yapf, perform actions that are similar to what black does.

## Notes help

```python
```

### Naming Conventions

| Type     |                                                Naming Convention                                                |                                Examples |
| :------- | :-------------------------------------------------------------------------------------------------------------: | --------------------------------------: |
| Function |              Use a lowercase word or words. Separate words by underscores to improve readability.               |                   function, my_function |
| Variable |     Use a lowercase single letter, word, or words. Separate words with underscores to improve readability.      |                     x, var, my_variable |
| Class    | Start each word with a capital letter. Do not separate words with underscores. This style is called camel case. |                          Model, MyClass |
| Method   |             Use a lowercase word or words. Separate words with underscores to improve readability.              |                    class_method, method |
| Constant |     Use an uppercase single letter, word, or words. Separate words with underscores to improve readability.     | CONSTANT, MY_CONSTANT, MY_LONG_CONSTANT |
| Module   |          Use a short, lowercase word or words. Separate words with underscores to improve readability.          |                 module.py, my_module.py |
| Package  |                  Use a short, lowercase word or words. Do not separate words with underscores.                  |                      package, mypackage |
