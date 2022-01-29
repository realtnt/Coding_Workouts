#
# codewars
#
# 5 kyu
#
# Pete, the baker
#

def cakes(recipe, available)
  recipe.map { |k, v| !available[k].nil? ? available[k] / v : 0 }.min
end
