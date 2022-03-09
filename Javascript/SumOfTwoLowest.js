/**
#
# codewars
#
# 7 kyu
#
# Sum of two lowest positive integers
#
*/

function sumTwoSmallestNumbers(numbers) {
    return numbers.sort((a, b) => a - b).shift() + numbers.sort((a, b) => a - b).shift()
}