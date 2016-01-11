#ifndef __TIMED_RUN_H
#define __TIMED_RUN_H

#include <chrono>
#include <iostream>
#include <iomanip>
#include <functional>

void print_time_for_run(std::function<void(void)> f)
{
    using std::chrono::steady_clock;
    auto start = steady_clock::now();
    f();
    auto end = steady_clock::now();
    auto t = std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count();
    std::cout << "(" << (t / 1000) << "." << std::setfill('0') << std::setw(3) << (t % 1000) << "s)" << std::endl;
}

#endif // __TIMED_RUN_H

