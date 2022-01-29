=begin
    
codewars

7 kyu

DescendingOrder    
=end

def descending_order(n)
    return n.to_s.chars.sort.reverse.join.to_i
end