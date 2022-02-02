#
# codewars
#
# 8 kyu
#
# ASCII Total
#

def uni_total(string)
    string.chars.map { |c| c.ord }.sum
end

puts uni_total("a")
puts uni_total("aaa")