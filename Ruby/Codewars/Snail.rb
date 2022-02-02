#
# codewars
#
# 4 kyu
#
# Snail
#

def snail(array)
    a=[]
    a += array[0]
    print array
    print array.transpose.map(&:reverse)
    (0..array.length-1).each { |x| a<<array.transpose[x][array.length-1-x] }#[x+1][array.length-x-1] }
    print a
end


snail( [[1,2,3,4],[4,5,6,5],[7,8,9,6],[7,8,9,6]] )