# CodeForces for Python
>Competitive programming solutions

This project contains CodeForces solutions and related source code, tips, tricks, and more.  This repository is dedicated to Python submissions, but I've done many problems in C++ which you can check out at https://github.com/cbarnson/uva.

## Getting started

![](img/demo.gif)

I have a utility batch script `new.cmd` in the root folder, which eliminates the hassle of copying problem input/output into local files, as well as making a copy of a solution template.  If you frequently use a number of utility functions in all your solutions, throw the boilerplate code into `bin/default_template.py`.  At the time of this writing (June 4, 2019) I'm mostly working in a Windows environment, so most of the scripts and whatnot cater to that.

Start working on a new problem by running `new.cmd 123 A`, for example, which pulls the input/output files for problem `123A` *(Most CodeForces problems follow the labeling pattern of `<number><letter>`, for contests you'll see the number is the same, but letter specifies the problem of that set; my script takes it in the form of two args for convenience)*.

## Past Solutions

Everything in `accepted/` has been submitted to CodeForces, where the filename is the problem identifier, and has received **accepted**.

## Resources

Take a look inside `archive/` to find relevant competitive programming material.  Much of it is in C or C++, but the concepts are transferrable.  Note, since Python is a much slower language than C or C++, some problems will simply be unsolvable with Python due to time limitations.  Often we'll use Python for easy problems or when there is a clear advantage over C or C++, such as arbitrary integer precision provided by the former.  You may even see some Java for its Gregorian calendar or Big number calculations.  It helps to be multi-lingual `:)`.

## License

```
The MIT License (MIT)

Copyright (c) 2019 Barnson

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
```