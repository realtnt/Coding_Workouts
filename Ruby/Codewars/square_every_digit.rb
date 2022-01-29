#
# codewars
#
# 7 kyu
#
# Square Every Digit
#

def square_digits(num)
  num.to_s.split('').map { |x| x.to_i**2 }.join.to_i
end
