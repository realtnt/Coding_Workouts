=begin
    
codewars

6 kyu

Create Phone Number

=end

def create_phone_number(numbers)
    t = numbers.join()
    return "(#{t[0..2]}) #{t[3..5]}-#{t[6..9]}"
end