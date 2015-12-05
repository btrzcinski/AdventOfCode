#pragma once

#ifndef WIN32_LEAN_AND_MEAN
#define WIN32_LEAN_AND_MEAN
#endif
#include <Windows.h>

#include <iostream>
#include <iomanip>
#include <functional>

void print_time_for_run(std::function<void(void)> f)
{
    auto start = GetTickCount64();
    f();
    auto t = GetTickCount64() - start;
    std::cout << "(" << (t / 1000) << "." << std::setw(3) << (t % 1000) << "s)" << std::endl;
}
