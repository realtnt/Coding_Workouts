#
# codewars
#
# 5 kyu
#
# Regex Password Validation
#

def validate_password(password)
  regex = /(?=.*\w{6,})(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(^[A-Za-z0-9]*$)/

  regex.match?(password)
end
