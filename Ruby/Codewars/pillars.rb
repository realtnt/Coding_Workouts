#
# codewars
#
# 8 kyu
#
# Pillars
#

def pillars(num_of_pillars, distance, width)
    num_of_pillars-1 == 0 ? 0 :  (num_of_pillars-1)*(distance*100 + width) - width
end

puts pillars(1, 10, 10)
puts pillars(2, 20, 25)
puts pillars(11, 15, 30)