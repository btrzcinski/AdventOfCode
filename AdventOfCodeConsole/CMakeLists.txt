add_executable (AdventOfCodeOpenConsole AdventOfCodeConsole.cpp)
set_property (TARGET AdventOfCodeOpenConsole PROPERTY CXX_STANDARD 11)
set_property (TARGET AdventOfCodeOpenConsole PROPERTY CXX_STANDARD_REQUIRED ON)

target_link_libraries (AdventOfCodeOpenConsole LINK_PUBLIC AdventOfCodeOpenLib)

