=begin
    
codewars

7 kyu

Square Every Digit
    
=end

def square_digits num
    num.to_s.split('').map{|x| x.to_i**2 }.join.to_i
end