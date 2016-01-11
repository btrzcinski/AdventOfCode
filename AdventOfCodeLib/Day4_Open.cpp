#include "Day4.h"

#include <openssl/md5.h>

#include <sstream>

namespace
{
    bool md5_for_string_has_leading_hex_zeroes(std::string const& input, int num_hex_zeroes)
    {
        static MD5_CTX c;
        static unsigned char out[MD5_DIGEST_LENGTH];

        MD5_Init(&c);
        MD5_Update(&c, (const void *)(input.data()), input.size());
        MD5_Final(out, &c);

        auto leadingHexZeroes = 0;
        for (auto i = 0; i < MD5_DIGEST_LENGTH; ++i)
        {
            if ((out[i] >> 4) != 0)
                break;

            ++leadingHexZeroes;

            if ((out[i] & 0xf) != 0)
                break;

            ++leadingHexZeroes;
        }

        return leadingHexZeroes >= num_hex_zeroes;
    }
}

int Day4::lowest_salt_with_leading_zeroes(std::string const& secret_key, int num_zeroes)
{
    int salt = 0;
    bool has_leading_zeroes = false;
    while (!has_leading_zeroes)
    {
        ++salt;
        has_leading_zeroes = md5_for_string_has_leading_hex_zeroes(secret_key + std::to_string(salt), num_zeroes);
    }

    return salt;
}
