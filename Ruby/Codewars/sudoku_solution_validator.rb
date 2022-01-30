#
# codewars
#
# 4 kyu
#
# Sudoku Solution Validator
#

def validSolution( board )
    return false if board.flatten.include?(0) || 
                    board.map { |r| r.uniq.length<9 }.include?(true) ||
                    board.transpose.map { |r| r.uniq.length<9 }.include?(true)
    subgrid = []
    [0, 3, 6].each do |subgrid_h|
        [0, 3, 6].each do |subgrid_v|
            (0..2).each { |r| (0..2).each { |c| subgrid << board[subgrid_h + r][subgrid_v + c] } }
            return false if subgrid.uniq.length < 9
            subgrid = []
        end
    end
    return true
end

puts validSolution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
               [6, 7, 2, 1, 9, 5, 3, 4, 8],
               [1, 9, 8, 3, 4, 2, 5, 6, 7],
               [8, 5, 9, 7, 6, 1, 4, 2, 3],
               [4, 2, 6, 8, 5, 3, 7, 9, 1],
               [7, 1, 3, 9, 2, 4, 8, 5, 6],
               [9, 6, 1, 5, 3, 7, 2, 8, 4],
               [2, 8, 7, 4, 1, 9, 6, 3, 5],
               [3, 4, 5, 2, 8, 6, 1, 7, 9]])

# true

puts validSolution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
               [6, 7, 2, 1, 9, 0, 3, 4, 9],
               [1, 0, 0, 3, 4, 2, 5, 6, 0],
               [8, 5, 9, 7, 6, 1, 0, 2, 0],
               [4, 2, 6, 8, 5, 3, 7, 9, 1],
               [7, 1, 3, 9, 2, 4, 8, 5, 6],
               [9, 0, 1, 5, 3, 7, 2, 1, 4],
               [2, 8, 7, 4, 1, 9, 6, 3, 5],
               [3, 0, 0, 4, 8, 1, 1, 7, 9]])
# false
