#
# codewars
#
# 7 kyu
#
# Remove consecutive duplicate words
#

def remove_consecutive_duplicates(s)
  prev = ''
  out = []
  s.split.each do |word|
    out << word if word != prev
    prev = word
  end
  out.join(' ')
end
