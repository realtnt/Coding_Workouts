=begin
    
codewars

8 kyu

Check same case
    
=end

def same_case(a, b)
    if a.match?(/[[:alpha:]]/) && b.match?(/[[:alpha:]]/)
      if a == a.upcase && b == b.upcase || a == a.downcase && b == b.downcase
        return 1
      else
        return 0    
      end
    else
      return -1
    end 
end