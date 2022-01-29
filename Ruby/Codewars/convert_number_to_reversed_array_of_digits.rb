#
# codewars
#
# 8 kyu
#
# Convert number to reversed array of digits
#

def digitize(n)
  # convert n to string, get a list of chars, reverse them
  # and then run the block to convert back to integer
  n.to_s.chars.reverse.map { |z| z.to_i }
end
