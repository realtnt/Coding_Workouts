# Rock Paper Scissors
# Let's play! You have to return which player won! In case of a draw return Draw!.

# Examples:

# rps('scissors','paper') // Player 1 won!
# rps('scissors','rock') // Player 2 won!
# rps('paper','paper') // Draw!


def rps(p1, p2)
    win = {'rock'=>'scissors', 'paper'=>'rock', 'scissors'=>'paper'}
    return "Draw!" if p1 == p2
    win[p1]==p2 ? "Player 1 won!" : "Player 2 won!"
end

puts rps('rock', 'scissors')  #, "Player 1 won!")
puts rps('scissors', 'paper') #, "Player 1 won!")
puts rps('paper', 'rock')     #, "Player 1 won!")
puts rps('scissors', 'rock')  #, "Player 2 won!")
puts rps('paper', 'scissors') #, "Player 2 won!")
puts rps('rock', 'paper')     #, "Player 2 won!")
puts rps('paper', 'paper')    #, "Draw!")
