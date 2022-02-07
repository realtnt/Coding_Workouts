puts "-"*22
puts "| Ruby Guessing Game |"
puts "-"*22

print "What is your name? "
name = gets.chomp

puts "Hello, #{name}."
puts "We are going to play a guessing game."
puts "I will choose a random number between 1 and 10"
puts "and you will have three chances to guess it."
puts "Okay, I have my number."
number = rand(10)+1

guess = 0
(1..3).each do |i|
    print "Guess #{i}: "
    guess = gets.to_i
    break if guess == number
    puts "Sorry, that wasn't it."
end

if guess == number
    puts "\nWell done, you found it!"
else
    puts "\nThat was your last guess."
    puts "My number was #{number}."
end

puts "\n\nGoodbye!"
    