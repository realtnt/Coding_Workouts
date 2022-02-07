def pig_latin(word)
    first_vowel = word=~/[aeiou]/
    first_vowel == 0 ? word += "ay" : word[first_vowel..-1] + word[0..first_vowel-1] + "ay"
end


puts pig_latin("elevator")
puts pig_latin("ruby")
puts pig_latin("where")