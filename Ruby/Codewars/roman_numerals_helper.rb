#
# codewars
#
# 4 kyu
#
# Roman Numerals Helper
#

# TODO: create a RomanNumerals helper class

class RomanNumerals
    @@roman = {'I'=>1, 'IV'=>4, 'V'=>5, 'X'=>10, 'L'=>50, 'C'=>100, 'D'=>500, 'M'=>1000}
    def to_roman(number)
        puts "to_roman"
    end

    def from_roman(string)
        prev_val = 0
        total = 0
        string.reverse.chars.each do |r|
            int_val = @@roman[r].to_i
            if int_val > prev_val
                total += int_val
                prev_val = int_val
            else
                total -= int_val
                prev_val += int_val
            end
        end
        return total
    end
end

obj = RomanNumerals.new
obj.to_roman(10)

obj.from_roman("asdf")

puts obj.from_roman('M')
puts obj.from_roman('MI')
puts obj.from_roman('MIX')
puts obj.from_roman('MIV')
puts obj.from_roman('MXL')
puts obj.from_roman('MDCLXVI')
puts obj.from_roman('MCMXC')
puts obj.from_roman('MCMXCIX')
puts obj.from_roman('MCMXXVII')
puts obj.from_roman('MMVIII')