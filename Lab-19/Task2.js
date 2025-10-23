function checkNumber(num) {
    if (num > 0) {
        console.log("The number is positive");
    } else if (num < 0) {
        console.log("The number is negative");
    } else {
        console.log("The number is zero");
    }
}

// Test cases
checkNumber(-5);  // Output: The number is negative
checkNumber(0);   // Output: The number is zero
checkNumber(7);   // Output: The number is positive