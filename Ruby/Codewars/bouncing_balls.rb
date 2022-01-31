#
# codewars
#
# 6 kyu
#
# Bouncing Balls
#

def bouncingBall(h, bounce, window)
    return -1 if h < 0 || bounce <= 0 || bounce >= 1 || window > h
    no_of_bounces = 1
    while h > window do
        h *= bounce
        no_of_bounces += 2 if h > window
    end
    return no_of_bounces
end


puts bouncingBall(3, 0.66, 1.5) #, 3)
puts bouncingBall(30, 0.66, 1.5) #, 15)
puts bouncingBall(30, 0.75, 1.5) #, 21)
puts bouncingBall(30, 0.4, 10) #, 3)
puts bouncingBall(40, 1, 10) #, -1)
puts bouncingBall(-5, 0.66, 1.5) #, -1)