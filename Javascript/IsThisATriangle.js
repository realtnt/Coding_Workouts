/**
#
# codewars
#
# 7 kyu
#
# Is this a triangle?
#
*/

function isTriangle(a, b, c) {
    return a + b > c && b + c > a && a + c > b
}