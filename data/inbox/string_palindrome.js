// A function that checks if a string is a palindrome
function isPalindrome(str) {
  // Convert the string to lowercase and remove non-alphanumeric characters
  str = str.toLowerCase().replace(/[^a-z0-9]/g, "");
  // Loop from both ends of the string and compare characters
  for (let i = 0; i < str.length / 2; i++) {
    if (str[i] !== str[str.length - i - 1]) {
      return false; // Not a palindrome
    }
  }
  return true; // Palindrome
}
