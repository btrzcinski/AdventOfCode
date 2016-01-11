#ifndef __DAY10_CONSOLE_H
#define __DAY10_CONSOLE_H

#include <iostream>

#include "Day10.h"
#include "TimedRun.h"

void Day10Console()
{
    constexpr auto input = "1113122113";

    for (auto t : { 40, 50 })
    {
        std::cout << t << "x: " << input << " => ";
        print_time_for_run([input, t] {
            std::cout << "... (len = " << Day10::lookandsay(input, t).size() << ")" << std::endl;
        });
    }
}

#endif // __DAY10_CONSOLE_H

