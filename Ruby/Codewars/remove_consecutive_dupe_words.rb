=begin
    
codewars

7 kyu

Remove consecutive duplicate words

=end

def remove_consecutive_duplicates(s)
    prev = ''
    out = []
    s.split.each do |word| 
        if word != prev 
            out << word
        end
        prev = word
    end
    return out.join(" ")
end