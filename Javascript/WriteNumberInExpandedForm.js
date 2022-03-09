/**
#
# codewars
#
# 6 kyu
#
# Write Number in Expanded Form
#
*/

function expandedForm(num) {
    let expanded = ""
    const numStr = num.toString()
    let exp = numStr.length - 1;

    [...numStr].forEach((digit, index) => {
        mult = 10 ** exp
        if (digit != 0) {
            if (index > 0) {
                expanded = expanded.concat(" + ")
            }
            expanded = expanded.concat(digit * mult)
        }
        exp -= 1
    })

    console.log(expanded)
    return expanded
}