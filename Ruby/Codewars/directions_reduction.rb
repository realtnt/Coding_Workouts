#
# codewars
#
# 5 kyu
#
# Directions Reduction
#

def dirReduc(a)
  del_el = [] # keep track of elements to delete
  found = true
  while found == true # keep going if we deleted elements in the last pass
    found = false
    a.each_with_index do |item, index|
      if item == 'NORTH' && a[index + 1] == 'SOUTH' ||
         item == 'SOUTH' && a[index + 1] == 'NORTH' ||
         item == 'EAST' && a[index + 1] == 'WEST' ||
         item == 'WEST' && a[index + 1] == 'EAST'
        # add to delete array
        del_el << index
        del_el << index + 1
        found = true
      end
      # delete them in reverse order (so that it doesn't affect the index)
      del_el.reverse_each { |i| a.delete_at(i) }
      del_el = [] # initialize the delete array
    end
  end
  a
end
