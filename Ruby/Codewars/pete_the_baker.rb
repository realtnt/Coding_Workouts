=begin
    
codewars

5 kyu

Pete, the baker
    
=end

def cakes(recipe, available)
    return recipe.map{|k, v| available[k]!=nil ? available[k]/v : 0}.min
end
