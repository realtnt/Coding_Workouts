#
# codewars
#
# 8 kyu
#
# Check same case
#

def same_case(a, b)
  if a.match?(/[[:alpha:]]/) && b.match?(/[[:alpha:]]/)
    if a == a.upcase && b == b.upcase || a == a.downcase && b == b.downcase
      1
    else
      0
    end
  else
    -1
  end
end
