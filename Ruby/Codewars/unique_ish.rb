#
# codewars
#
# 7 kyu
#
# Unique(ish)
#

def unique strings
    clean_strings = strings.map { |s| s.downcase.gsub(/[^a-z]/i, '') }
    (0...strings.length).map { |i| strings[i] unless clean_strings[0,i].include?(clean_strings[i]) }.compact
end

print unique(["Hello", "world!"]) # , ["Hello", "world!"])
puts
print unique(["Hello", "hello", "HeLlo!", "world!","world"]) # , ["Hello", "world!"])