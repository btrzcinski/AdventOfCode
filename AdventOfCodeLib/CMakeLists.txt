add_library (AdventOfCodeOpenLib Day4_Open.cpp Day10.cpp)
set_property (TARGET AdventOfCodeOpenLib PROPERTY CXX_STANDARD 11)
set_property (TARGET AdventOfCodeOpenLib PROPERTY CXX_STANDARD_REQUIRED ON)

find_package (OpenSSL REQUIRED)
include_directories (${OPENSSL_INCLUDE_DIR})
target_link_libraries (AdventOfCodeOpenLib PUBLIC ${OPENSSL_LIBRARIES})

target_include_directories (AdventOfCodeOpenLib PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

