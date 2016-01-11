#ifndef __DAY4_CONSOLE_H
#define __DAY4_CONSOLE_H

#include <iostream>

#include "Day4.h"
#include "TimedRun.h"

void Day4Console()
{
    constexpr auto secret_key = "yzbqklnj";
    
    std::cout << "Secret key: " << secret_key << ", 5 zeroes: ";
    print_time_for_run([secret_key] {
        std::cout << Day4::lowest_salt_with_leading_zeroes(secret_key) << std::endl;
    });
    
    std::cout << "Secret key: " << secret_key << ", 6 zeroes: ";
    print_time_for_run([secret_key] {
        std::cout << Day4::lowest_salt_with_leading_zeroes(secret_key, 6) << std::endl;
    });
}

#endif // __DAY4_CONSOLE_H

