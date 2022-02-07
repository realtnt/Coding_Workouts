#
# Ruby Essential Training - Part 1
#
# Control Structures
#
# Blanket patterns
#

def blanket_pattern( string )
    20.times do
        string = string[1..-1]+string[0]
        puts string
    end
end

blanket_pattern("RRGGBBYYKK")
puts
blanket_pattern("|@@#/\#@@|")
puts
blanket_pattern("~^/*\/*\^~")
