#
# codewars
#
# 7 kyu
#
# Complementary DNA
#

def dna_strand(dna)
    pairs = { 'A'=>'T', 'T'=>'A', 'G'=>'C', 'C'=>'G' }
    dna.chars.map {|c| pairs[c] }.join
end

puts dna_strand('')      # 
puts dna_strand('ATGC')  # TACG
puts dna_strand('GTAT')  # CATA
puts dna_strand('AAAA')  # TTTT