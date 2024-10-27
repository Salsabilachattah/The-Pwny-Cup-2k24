#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/ptrace.h>
#include <locale.h>
#include <ctype.h>
#include <openssl/sha.h>


#define HASH_SIZE 64 // Length of SHA-256 hash in hexadecimal
#define SHA256_DIGEST_LENGTH 32 // SHA-256 produces a 32-byte digest
#define NUM_HASHES 80



int hmm(char *emoji_output[], int emoji_count, char *hashes[], int hash_count) {
    
    
    if (NUM_HASHES != 2 * emoji_count) {
        return 0; 
    }

    for (int i = 0; i < emoji_count; i++) {
        unsigned char hash[SHA256_DIGEST_LENGTH];
        char computed_hash[HASH_SIZE + 1]; 
        computed_hash[HASH_SIZE] = '\0'; 

       
        SHA256((unsigned char *)emoji_output[i], strlen(emoji_output[i]), hash);
        
        
        for (int j = 0; j < SHA256_DIGEST_LENGTH; j++) {
            sprintf(&computed_hash[j * 2], "%02x", hash[j]);
        }
        int hash_index = i * 2; 
        if (hash_index < hash_count) {
   
            for (int j = 0; j < HASH_SIZE; j++) {
               

                if ((computed_hash[j] ^ hashes[hash_index][j]) != 0) {
                    return 0; 
                }
            }
        }
    }
    return 1; // Return true if all hashes match in order
}
char *hashes[80]={
    
        "d06f1525f791397809f9bc98682b5c13318eca4c3123433467fd4dffda44fd14","eCb2Cda38120eC89fe68AC5356cDD4ee9Eaed5BF1DEDD0C111bE7753900C39DC","82ce29f5a7735b3f245bff0f54878f0f68c2a47a8cf86d2423013950f66a63e9","55bE0ceFf1fcfD86ec54EF4a78dbF2Db7569eAba56Aaadb91eaE1f959CedDABa","9d7a8df67a2b9e38082ae5b91f5f6f1b40de1b69e94413fe9fe72ad34366a0cd","1A0CA4A1e9AbF09EdAaa2f093F7B1b3E6b3CC0069DDe06fafe15cac9cCBACefE","3041c8745f9678c2642b3b9b425b8a408262b9d8c5b93139942de3b1adb43b1c","DBcaf8dd51EE6607fb9C3b5D16faF8eFb7ceaA83aA6100ccF27aDcADe7a25C43","3041c8745f9678c2642b3b9b425b8a408262b9d8c5b93139942de3b1adb43b1c","Bfd2AD5C45e6453a41B2BB127FaCdc81F7c3FCbC6b1fd07c3Bcd25Cdf79Ae5Aa","453cb3b789e7b403d4cb5342bc1469fb418be79e1ef74f30b79e6f699f20a39d","DB574EF9069Dc9beBcEedc8395dbC9Fda7E22E2F1A2F0C8Be8F63498Dd2f05D6","f0443a342c5ef54783a111b51ba56c938e474c32324d90c3a60c9c8e3a37e2d9","6FC4aa1Af9868B4b72Ba1FB1eaD2fEAD93aC5B680a212a52BF0EaEacBB6dd7B6","4dfbcab9041276596339508f642e6ad755f7981625e17b692a4e0c0c9bae4494","0CC549C3Ace2aF10aAF4cD6da62561EdB6E3FCCB127ABBAC8aBebfdFfb10908E","9d7a8df67a2b9e38082ae5b91f5f6f1b40de1b69e94413fe9fe72ad34366a0cd","FF7Bce5aEcf272d23CeDDC1B06fD7523b68dcD4BE19Cc96d104C2b972c4fCcDF","d06f1525f791397809f9bc98682b5c13318eca4c3123433467fd4dffda44fd14","f9e62402bbea85831C792AdcAE6Ac72C3Dcdc5D9ae7B55B141F2BDEc88Ef8701","bde54945ea129fe0b2cbd2edfdb9196e3ddcd44c285454d74b616272544549d3","DEcb6FC59FB3FDCfE357Fc88D6fdEBfbcad1A8Bd4A7FBbFcE217162C751bCE0b","3a3fbeedf9e3ad420195612da4eec4c54d9f3503e80b136278eb4a439b84a1f2","d39cEDcb67DFb1b6bCDf9eec3B34Ac40DF8e16A0CFaD1842B6E7c3C5dfB74bE2","9d7a8df67a2b9e38082ae5b91f5f6f1b40de1b69e94413fe9fe72ad34366a0cd","31e6CcFF889CE4A08Aa7B4aB99bFA26bfD35fcad6eCd2B74D2e5eB7B41fe2AbD","3041c8745f9678c2642b3b9b425b8a408262b9d8c5b93139942de3b1adb43b1c","d08A1C393cfa419FB99a83BBf2Eb9Bf57e56f75B04EFbCf27DF0CFA546Fd9395","ed8d830565bfcc5cb5b15e7deef7b6d07645d06597c8d17c7bdd49ad6f0e310a","bb72BDAFAcED9C9f5A2CCD1f0dC5BC9b01CBAd1b2cBAEE74f43E8FBB8Cec4B2F","db206256b9c864dafa3080742a40fe876f0aea623c45f4cb16643b25c0be6553","9Ef0C34Cc24a9FfaF4CCCEB1caDFDA3f5754Eeb04Ee4Bd58244474D7db49E37B","453cb3b789e7b403d4cb5342bc1469fb418be79e1ef74f30b79e6f699f20a39d","04500BFF4Ea1A750d80Abf53f1830D6D7E0fF7DD8Ac4BAe96eC09e0dCAd15b62","49f997d69946f39b7753ba9f6677ae13607a19b4b59a605a86a3803eba7de049","A8Fec02df42AB0Fc72b1549045040Dc5B96D7faafDfc37c702caA098B96ebBFC","b76ca5afa83f2d1a5609b7f3955bf9d297122dcb785cdd5adfbe319e87c91659","Bc067bE99dF67Ff30cf7Ed03eBf334F8BC1bf097fAe817eE8750E023Ff8DCBd0","4dfbcab9041276596339508f642e6ad755f7981625e17b692a4e0c0c9bae4494","fda395F5D01599Afe8EDBE2BB7B5BEa9fe4a5aB42EEF55f56f015f1CbA2F0eaE","db206256b9c864dafa3080742a40fe876f0aea623c45f4cb16643b25c0be6553","867bD5ABc8fa45Bb14AA76E64A9E4D4357bF42c6eC41D8bbCC7884CF59e393dE","b76ca5afa83f2d1a5609b7f3955bf9d297122dcb785cdd5adfbe319e87c91659","EBBe264A5b4e11ABA5fF28A0Cb2D4a2C05F24f02Cf3b9631e693148d7D050e76","c0cc703f13e3462db4f167120b062b6dcf27dad6dca1b150d9e3367cb79d0a83","0F3E0937d9a0d0D2eCc91CF41F5c4ec9BCbeeFa43f01cb929723CAFa4A009289","453cb3b789e7b403d4cb5342bc1469fb418be79e1ef74f30b79e6f699f20a39d","b6D38C8b4060dbdFCf0D5Df3Bd2F383Abfb9D708eA8Cf9fBCfaD7ee6BbcA902D","c46dddf1242ca083bbbf9888b6c77ba0c86d1ca9ef81c6069e13cec04670cb42","6a287a31c1F2dE53f6D3DdC7AdC4AfBd129aB24cCb7bd9cfD250ee1CA217f86F","08081c499cdeab015ad5c888c4aac3e8a4ba2333be9862f69482732bd817411d","afEAf95Ec61fF4c6a2f2BbddCa492eD24E98B9bF1a1c29A4fBa60a1C8FdE1f2B","3a54154ed9521ac47fb973d028932325fa75f99fea9a0d50958bb32878f5cd0b","FCA3E0edA6A7cEefaCC1e01BBf7d70CFc033Cf2C5Ab12ACBCA031C3F53d6f0Fb","d06f1525f791397809f9bc98682b5c13318eca4c3123433467fd4dffda44fd14","Fe4aF23b83eBF816a2ed6B8d8Dad85D7e07daEb7d7F7bcEfEdaA9a5ddF2CD0dC","b76ca5afa83f2d1a5609b7f3955bf9d297122dcb785cdd5adfbe319e87c91659","7fC33a2eC3cD3CB64Fce0DEFd7118fa85E3DCbA7b6F5Bc9e24591D38D9ef6AB5","6005b82f88dccf881d116a94daa3ba058970390322111d64af9c2fdd851995a6","FA8fEc5E3BDC72B6D6Ffac5c2Fd9558bd60CcFFA6ad83A9D605c2b8FfE8cC24F","d09a1368b48ada06ff3de7927acc79b7f053d1b6b43ef3708db68b65113d7954","D2b7a19ebA1aCffBf41ACE2BB7fC1dB0dFEbeACBAEa9FBF13DBeCa80b204e010","f0443a342c5ef54783a111b51ba56c938e474c32324d90c3a60c9c8e3a37e2d9","2e7AF097dCdECDdBAd32D19cf4f9EA8b61cC44DacFAFbFFd8fEFB3833c94518D","4dfbcab9041276596339508f642e6ad755f7981625e17b692a4e0c0c9bae4494","2da42d6BDDb6B9f71aaC26E5CAF7f0d76d30bfEBDFb7f599Ec9B75FbF67bCA9b","d09a1368b48ada06ff3de7927acc79b7f053d1b6b43ef3708db68b65113d7954","311b65e6c0d9b7a3Dd1ca0c08E83Ed2936ffdA689E6bf83d1Caf0bbd2e6a8ed5","6146299cd54818a0e659eb6ac88e80f6f8f70536bbbd962d36973f2d2323f26c","FbC2d5f3B5A19c1dfEaAD64D7fc085dcdF423cefCcD47f671CF2a21d23f4cE80","f0443a342c5ef54783a111b51ba56c938e474c32324d90c3a60c9c8e3a37e2d9","ef50BC7f1c0B10eCFB1fF05fc75231cAabFbdbf7958fcdDF1EE5C78a13e34b85","e94e8b04547b50aa5904e44b17189c348ad0a8929803725b136ac3548a194ef6","A536C7Ef7dfdC62db15bE01862d5DfECaE8bB6D18eA4889DD5bb2cefC8BD9D6D","49f997d69946f39b7753ba9f6677ae13607a19b4b59a605a86a3803eba7de049","aF21c3D50Ab5378FA9d3BC5cf7FC40Caf3C38B5bb7A4C17aB92CA07C36abC4B6","072bd54358b1170a2d5a55b2d90438a53d41b85924c73038e466ca324cb69ab0","4c79E5851831DCDBaf24a7aEb2Cf63BE6aD7f2D269F3F4aa22CDc09E0AcDa56b","b44793a1df6cc2d26458bc8f2db2094acc9885c1a390bf1b3b743bc5167adfe5","eb74E8dfb53e9B9CAd3A83Cb5eE1D9dd5fD3E2B4FFFe10bcbBD065DcC3824cCF"

};   




int Hacker_welcome(){
    int a=0;
    int b=0;
    if(a==b){
        printf("Please enter your flag to see if it exists in our database.\n");
    }


    return 0;
}

int GG(){
    
    printf("\nYou did a Great job , it was a correct flag \n");
    return 0;
}







int main() {

    char computed_hash[HASH_SIZE + 1];
    

    printf("Welcome to shellmates flags DB : \n");
    Hacker_welcome();
    

  

    // Set locale for UTF-8 (to print emojis correctly)
    setlocale(LC_ALL, "");

    // Emoji mappings for lowercase letters 'a' to 'z' (26 emojis)
    char *emoji_map_lower[26] = {
        "😀", "😁", "😂", "🤣", "😃", "😄", "😅", "😆", "😉", "😊",  // a-j
        "😋", "😎", "😍", "😘", "😗", "😙", "😚", "☺", "🙂", "🤗",  // k-t
        "🤔", "😐", "😑", "😶", "🙄", "😏"   // u-z
    };

    // Emoji mappings for uppercase letters 'A' to 'Z' (26 emojis)
    char *emoji_map_upper[26] = {
        "🚀", "🎉", "🔥", "💎", "✨", "🌟", "🎯", "🏆", "🎶", "🎨",  // A-J
        "💼", "📚", "🎓", "💡", "🛠", "🎤", "🎸", "🏅", "🎲", "🎮",  // K-T
        "🔧", "📱", "🚗", "✈", "💻", "🏢"    // U-Z
    };



    // Input string from the user
    char input[256];
    printf("Enter The flag: ");
    fgets(input, sizeof(input), stdin);


    // Remove the newline character from fgets (if present)
    input[strcspn(input, "\n")] = 0;


    // Emoji mappings for numbers '0' to '9' (10 emojis)
    char *emoji_map_numbers[10] = {
        "🔢", "1️⃣", "2️⃣", "3️⃣", "4️⃣",  // 0-4
        "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"  // 5-9
    };


    // Emoji mappings for common special characters (punctuation, symbols)
    char *emoji_map_special[128] = {
        ['!'] = "❗", ['@'] = "📧", ['#'] = "🔢", ['%'] = "💯",  // ! @ # %
        ['$'] = "💵", ['&'] = "🔗", ['*'] = "⭐", ['('] = "🌀",  // $ & * (
        [')'] = "🔘", ['-'] = "➖", ['+'] = "➕", ['='] = "🔗",  // ) - + =
        ['.'] = "⚫", [','] = "⚪", [':'] = "🔔", [';'] = "💬",  // . , : ;
        ['?'] = "❓", ['/'] = "🔪", ['\\'] = "🔙", ['\''] = "💡", // ? / \ '
        ['"'] = "🔏", ['{'] = "🦠", ['}'] = "🛡", ['_'] = "🔻"  // { } _
    };


    // Output array of emojis (same length as input)
    char *emoji_output[256];
    
    
    // Process each character in the input string
    for (int i = 0; i < strlen(input); i++) {
        char ch = input[i];

        // Handle lowercase letters
        if (islower(ch)) {
            int emoji_index = ch - 'a';  // Map 'a' to 'z' (0-25)
            emoji_output[i] = emoji_map_lower[emoji_index];
        }
        // Handle uppercase letters
        else if (isupper(ch)) {
            int emoji_index = ch - 'A';  // Map 'A' to 'Z' (0-25)
            emoji_output[i] = emoji_map_upper[emoji_index];
        }
        // Handle digits
        else if (isdigit(ch)) {
            int emoji_index = ch - '0';  // Map '0' to '9' (0-9)
            emoji_output[i] = emoji_map_numbers[emoji_index];
        }
        // Handle special characters
        else if (ch >= 33 && ch <= 126 && emoji_map_special[ch] != NULL) {
            emoji_output[i] = emoji_map_special[ch];
        }
        
        
        else {
            emoji_output[i] = "❓";  // Default emoji for unknown characters
        }   
    }
    
    int emojis_count=strlen(input);
    

     if (hmm(emoji_output, emojis_count, hashes, NUM_HASHES)) {
        GG();
        return 0; // Success
    } 
    else {
        return 1; // Failure
    }
 
    return 0;
}
