#include "Day4.h"

#include <sstream>

#include <Windows.h>
#include <wincrypt.h>

namespace
{
    bool md5_for_string_has_leading_hex_zeroes(HCRYPTPROV hProv, std::string const& input, int num_hex_zeroes)
    {
        HCRYPTHASH hHash = 0;
        CryptCreateHash(hProv, CALG_MD5, 0, 0, &hHash);
        CryptHashData(hHash, (const BYTE*)input.data(), input.length(), 0);
        
        BYTE md5Hash[16];
        DWORD md5Len = 16;
        CryptGetHashParam(hHash, HP_HASHVAL, md5Hash, &md5Len, 0);
        auto leadingHexZeroes = 0;
        for (auto i = 0; i < md5Len; ++i)
        {
            if ((md5Hash[i] >> 4) != 0)
                break;

            ++leadingHexZeroes;

            if ((md5Hash[i] & 0xf) != 0)
                break;

            ++leadingHexZeroes;
        }

        CryptDestroyHash(hHash);
        return leadingHexZeroes >= num_hex_zeroes;
    }
}

int Day4::lowest_salt_with_leading_zeroes(std::string const& secret_key, int num_zeroes)
{
    HCRYPTPROV hProv = 0;
    CryptAcquireContext(&hProv, nullptr, nullptr, PROV_RSA_FULL, CRYPT_VERIFYCONTEXT);

    int salt = 0;
    bool has_leading_zeroes = false;
    while (!has_leading_zeroes)
    {
        ++salt;
        has_leading_zeroes = md5_for_string_has_leading_hex_zeroes(hProv, secret_key + std::to_string(salt), num_zeroes);
    }

    CryptReleaseContext(hProv, 0);

    return salt;
}
