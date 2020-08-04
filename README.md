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

40. .

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
