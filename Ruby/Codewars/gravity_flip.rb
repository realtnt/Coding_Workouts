#
# codewars
#
# 8 kyu
#
# Gravity Flip
#

def flip(dir, boxes)
  if dir == 'R'
    boxes.sort { |a, b| a <=> b }
  else
    boxes.sort { |a, b| b <=> a }
  end
end
