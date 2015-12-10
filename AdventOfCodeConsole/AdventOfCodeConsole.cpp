#include "stdafx.h"

#include <iostream>

#include "Day4Console.h"
#include "Day10Console.h"

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        std::cout << "Usage: " << argv[0] << " day" << std::endl;
        std::cout << "Example: " << argv[0] << " 4" << std::endl;
        return 1;
    }

    auto day = atoi(argv[1]);

    switch (day)
    {
    case 4:
        Day4Console();
        break;
    case 10:
        Day10Console();
        break;
    default:
        std::cout << "Day " << day << " not implemented" << std::endl;
    }

    return 0;
}

