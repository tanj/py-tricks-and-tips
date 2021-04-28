==========
The Basics
==========

Lets go over some basic ideas.  EVERYTHING in python is an
object. Functions are objects. Integers are objects. (Seriously they
are, go ahead and type ``help(1)`` into an interactive python shell.)
Strings are objects. Does that really affect you? Probably not at this
point, but it can be helpful to know when you start to venture deeper.

Documentation
-------------

Ok, why not start here rather than it always being an after thought?
If you did as I suggested in the opening paragraph you would have seen
this documentation on the int object type.

.. code-block:: python
    
    >>>help(1)
    Help on int object:
    
    class int(object)
     |  int([x]) -> integer
     |  int(x, base=10) -> integer
     |
     |  Convert a number or string to an integer, or return 0 if no arguments
     |  are given.  If x is a number, return x.__int__().  For floating point
     |  numbers, this truncates towards zero.
     |
     |  If x is not a number or if base is given, then x must be a string,
     |  bytes, or bytearray instance representing an integer literal in the
     |  given base.  The literal can be preceded by '+' or '-' and be surrounded
     |  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
     |  Base 0 means to interpret the base from the string as an integer literal.
     |  >>> int('0b100', base=0)
     |  4
     |
     |  Built-in subclasses:
     |      bool
     |
     |  Methods defined here:
     |
     |  __abs__(self, /)
     |      abs(self)
     ...

One of the things that is great about python is the ability to work in
an interactive session and try things and explore. ``help()`` is very
useful to be able to quickly look at documentation for various
objects.

Writing documentation for your functions can aid you when you revisit
the code in the future. It is also very easy to do. Take a look in
``basics.py`` to see how simple it is to add documentations to a
function. Any string in the opening line of the function, class, or
file will be used as documentation for that item.

.. code-block:: python
    
    >>>help(greet)
    Help on function greet in module py_tricks_and_tips.basics:
    
    greet(name, greeting='Hi,')

    >>>help(greet_documented)
    greet_documented(name, greeting='Hi,')
        Greet `name` with `greeting`
    
        :param name: name of person we are greeting
        :param greeting: greeting we are using defaults to "Hi,"
        :returns: string of greeting and name

There are different styles of doc strings. The one I'm using here is
also the one that this document happens to use as well. It is called
ReStructured Text (rst) part of `Docutils
<https://docutils.sourceforge.io/>`_ and used by `Sphinx
<https://www.sphinx-doc.org/en/master/>`_ which is used by many python
projects to document their libraries. If you read documents for a
package on `readthedocs.org <https://readthedocs.org>`_ then those
documents were created using this format. I'd recommend using this
style.
