// Why BlockChains? 
// Inflating currencies, Fractional reserve Banking, INR Depreciation
// Currencies are not backed by assets anymore

// Blockchain Demo:  https://andersbrownworth.com/blockchain/


// Introduction to Hashing
/* Hashing is the process of transforming any given key or a string of characters into 
another fixed-length value or key that represents and makes it easier to find or employ 
the original string. */

const crypto = require('crypto');
const input = "hivemet";
const hash = crypto.createHash('sha256').update(input).digest('hex');
console.log(hash)


// "hivemet":  df49b2a73a7fae138eb2b7bb3324279c8a7c4bda13ddd2c4a35f2dd53849cc84 (256/4 = 64)
