#
# codewars
#
# 6 kyu
#
# Counting Duplicates
#

def duplicate_count(text)
  # convert string to array and make all chars lowercase (ignore numbers)
  text_lowercase = text.chars.map { |c| c.match(/[[:alpha:]]/) ? c.downcase : c }
  # iterates over the array passing a hash with initial value of -1
  # we get rid of the nil values with compact and return the length
  text_lowercase.each_with_object(Hash.new(-1)) do |key, hash|
    hash[key] += 1 # for every key (ie each array element) we increase it's value by 1
  end.map do |k, v|
    k if v > 0 # so, if value is >0 indicates that this element was seen more than once
  end.compact.length
end
