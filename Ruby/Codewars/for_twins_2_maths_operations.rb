#
# codewars
#
# 8 kyu
#
# For Twins: 2. Math operations
#

def ice_brick_volume(radius, bottle_length, rim_length)
    (bottle_length - rim_length) * ((radius*2)**2)/2
end

puts ice_brick_volume(1, 10, 2)
puts ice_brick_volume(5, 30, 7)