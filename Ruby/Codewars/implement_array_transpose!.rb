#
# codewars
#
# 7 kyu
#
# Implement Array#transpose!
#

class Array
    def transpose!
      self.replace(transpose)
    end
end

arr = [[1, 2, 7], [3, 5, 6]]

print arr.transpose!   # [[1, 3], [2, 5], [7, 6]]
