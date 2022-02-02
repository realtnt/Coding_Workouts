#
# codewars
#
# 8 kyu
#
# A Needle in the Haystack
#

def find_needle(haystack)
    return "found the needle at position #{haystack.index('needle')}"
end


puts find_needle(['3', '123124234', nil, 'needle', 'world', 'hay', 2, '3', true, false])