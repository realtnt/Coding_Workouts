#
# codewars
#
# 4 kyu
#
# Strip Comments
#

def solution(input, markers)
  m_found = false
  out = ''
  input.split("\n").each do |s|
    markers.each do |m|
      if s.include? m
        out << s[0...s.index(m)].strip << "\n"
        m_found = true
      end
    end
    out << s.strip << "\n" unless m_found
    m_found = false
  end
  out.chomp
end
