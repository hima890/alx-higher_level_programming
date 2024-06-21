#!/usr/bin/node
exports.converter = function (base) {
  // Define the recursive function within the main function
  function convert (num) {
    // Check if num is zero, which marks the base case
    if (num === 0) return ''; // Return empty string to terminate recursion

    // Recursively calculate the remainder and convert the quotient
    return convert(Math.floor(num / base)) + (num % base).toString(base);
  }

  // Return the inner function to be used as the converter
  return convert;
};
