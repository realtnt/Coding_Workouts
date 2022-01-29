=begin
    
codewars

4 kyu

StripComments
    
=end

def solution(number)
    (1...number).sum { |x| x%5==0 || x%3==0? x : 0 }
end