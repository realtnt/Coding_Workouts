puts "-"*12
puts "| Mad Libs |"
puts "-"*12

answer_type = ['verb', 'adjective', 'adjective', 'noun']
answers = []

answer_type.each do |i|
    i.match(/^[aeiou]/) ? article = "an" : article = "a"
    print "Give me #{article} #{i}? "
    answers << gets.chomp
end

print "I decided to #{answers[0]} a #{answers[1]} party for my #{answers[2]} #{answers[3]}."
