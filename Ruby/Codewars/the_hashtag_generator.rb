=begin
    
codewars

5 kyu

The Hashtag Generator
    
=end

def generateHashtag(str)
    str = str.split.map {|w| w.capitalize}.join
    str.empty? || str.length >=140 ? false : "#" + str
end