dramatic
========

The `dramatic` module includes utilities to cause cause all text output to display character-by-character (it prints *dramatically*).

![dramatic printing within a terminal](demo1.gif)

There are four primary ways to use the utilities in the `dramatic` module:

1. As a context manager that temporarily makes output display dramatically
2. As a decorator that temporarily makes output display dramatically
3. Using a `dramatic.start()` function that makes output display dramatically
4. Using a `dramatic.print` function to display specific text dramatically


Dramatic Context Manager
------------------------

The `dramatic.output` context manager will temporarily cause all standard output and standard error to display dramatically:

```python
import dramatic

def main():
    print("This function prints")

with dramatic.output:
    main()
```

To change the printing speed from the default of 75 characters per second to another value (30 characters per minute in this case) use the `at_speed` method:


```python
import dramatic

def main():
    print("This function prints")

with dramatic.output.at_speed(30):
    main()
```


Dramatic Decorator
------------------

The `dramatic.output` decorator will cause all standard output and standard error to display dramatically while the decorated function is running:

```python
import dramatic

@dramatic.output
def main():
    print("This function prints")

main()
```

The `at_speed` method works as a decorator as well:


```python
import dramatic

@dramatic.output.at_speed(30)
def main():
    print("This function prints")

main()
```


Manually Starting and Stopping
------------------------------

Instead of enabling dramatic printing temporarily with a context manager or decorator, the `dramatic.start` function may be used to enable dramatic printing:

```python
import dramatic

def main():
    print("This function prints")

dramatic.start()
main()
```

The `speed` keyword argument may be used to change the printing speed:

```python
import dramatic

def main():
    print("This function prints")

dramatic.start(speed=30)
main()
```

To make *only* standard output dramatic (but not standard error) pass `stderr=False` to `start`:

```python
import dramatic

def main():
    print("This function prints")

dramatic.start(stderr=False)
main()
```


To disable dramatic printing, the `dramatic.stop` function may be used:

```python
import dramatic


class CustomContextManager:
    def __enter__(self):
        print("Printing will become dramatic now")
        dramatic.start()
    def __exit__(self):
        dramatic.stop()
        print("Dramatic printing has stopped")
```


Dramatic Print
--------------

The `dramatic.print` function acts just like the built-in `print` function, but it prints dramatically:

```python
import dramatic
dramatic.print("This will print some text dramatically")
```


Other Features
--------------

Pressing `Ctrl-C` while text prints dramatically will cause the remaining text-to-be-printed to print immediately.

To start a dramatic Python REPL:

```bash
$ python3 -m dramatic
>>>
```

To dramatically run a Python module:

```bash
$ python3 -m dramatic -m this
```

To dramatically run a Python file:

```bash
$ python3 -m dramatic hello_world.py
```


Credits
-------

This package was inspired by the `dramatic` Python Morsels exercise, which was partially inspired by Brandon Rhodes' [adventure][] Python port (which displays its text at 1200 baud).


[adventure]: https://pypi.org/project/adventure/
