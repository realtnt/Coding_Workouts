=begin
    
codewars

6 kyu

Playing with digits
    
=end

def dig_pow(n, p)
    sum_of_digits = n.digits.reverse.each_with_index.map { |d, i| d**(p+i)}.sum
    sum_of_digits % n == 0 ? sum_of_digits/n : -1
end