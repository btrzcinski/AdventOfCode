#include "stdafx.h"
#include "CppUnitTest.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

#include "Day10.h"

using namespace std::string_literals;

namespace AdventOfCodeLibTests
{
    TEST_CLASS(Day10Tests)
    {
    public:
        TEST_METHOD(day10_test_case_1)
        {
            auto input = "1"s;
            auto expected = "11"s;
            auto actual = Day10::lookandsay(input, 1);
            Assert::AreEqual(expected, actual);
        }

        TEST_METHOD(day10_test_case_11)
        {
            auto input = "11"s;
            auto expected = "21"s;
            auto actual = Day10::lookandsay(input, 1);
            Assert::AreEqual(expected, actual);
        }

        TEST_METHOD(day10_test_case_21)
        {
            auto input = "21"s;
            auto expected = "1211"s;
            auto actual = Day10::lookandsay(input, 1);
            Assert::AreEqual(expected, actual);
        }

        TEST_METHOD(day10_test_case_1211)
        {
            auto input = "1211"s;
            auto expected = "111221"s;
            auto actual = Day10::lookandsay(input, 1);
            Assert::AreEqual(expected, actual);
        }

        TEST_METHOD(day10_test_case_111221)
        {
            auto input = "111221"s;
            auto expected = "312211"s;
            auto actual = Day10::lookandsay(input, 1);
            Assert::AreEqual(expected, actual);
        }

        TEST_METHOD(day10_test_case_1_5x)
        {
            auto input = "1"s;
            auto expected = "312211"s;
            auto actual = Day10::lookandsay(input, 5);
            Assert::AreEqual(expected, actual);
        }
    };
}