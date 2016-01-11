# AdventOfCodeLib

The Visual Studio project requires [Visual Studio 2015 Update 1](http://www.visualstudio.com) with the new Clang/C2 codegen feature.

This project produces a static library that links into the AdventOfCodeConsole application and the AdventOfCodeLibTests unit test library.

The CMake project targets "open" versions of routines that would otherwise use Win32 functions. They usually require outside libraries - for example, the "open" version of Day 4 requires OpenSSL.

