=begin
    
codewars

8 kyu

Gravity Flip
    
=end

def flip(dir, boxes)
    if dir == 'R' 
      return boxes.sort { |a, b| a <=> b }
    else
      return boxes.sort { |a, b| b <=> a }
    end
end