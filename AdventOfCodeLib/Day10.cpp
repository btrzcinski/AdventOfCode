#include "Day10.h"

#include <vector>
#include <sstream>
#include <iostream>

namespace
{
    std::vector<int> list_from_string(std::string const& input)
    {
        auto results = std::vector<int>{};
        for (auto const c : input)
        {
            results.push_back(int(c) - 48); // quick and dirty
        }
        return results;
    }

    std::string string_from_list(std::vector<int> const& input)
    {
        std::stringstream results;
        for (auto const i : input)
        {
            results << i;
        }
        return results.str();
    }

    std::vector<int> lookandsay_on_list(std::vector<int> const& input)
    {
        auto results = std::vector<int>{};
        for (auto i = 0; i < input.size();)
        {
            auto num = input[i];
            auto count = 1;
            while (++i < input.size() && input[i] == num) ++count;
            results.push_back(count);
            results.push_back(num);
        }
        return results;
    }
}

std::string Day10::lookandsay(std::string const& input, int num_reps)
{
    auto list = list_from_string(input);
    for (auto i = 0; i < num_reps; ++i)
    {
        list = lookandsay_on_list(list);
    }

    return string_from_list(list);
}
