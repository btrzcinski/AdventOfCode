#include "stdafx.h"
#include "CppUnitTest.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

#include "Day4.h"

namespace AdventOfCodeLibTests
{		
	TEST_CLASS(Day4Tests)
	{
	public:
		
		TEST_METHOD(day4_test_case_1)
		{
            auto secret_key = "abcdef";
            auto expected = 609043;
            auto actual = Day4::lowest_salt_with_leading_zeroes(secret_key);
            Assert::AreEqual(expected, actual);
		}

        TEST_METHOD(day4_test_case_2)
        {
            auto secret_key = "pqrstuv";
            auto expected = 1048970;
            auto actual = Day4::lowest_salt_with_leading_zeroes(secret_key);
            Assert::AreEqual(expected, actual);
        }

	};
}