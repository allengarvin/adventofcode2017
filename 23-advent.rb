#!/usr/bin/ruby
# Problem 2 only. Not the one I submitted. I didn't figure what it was doing until about 15 minutes 
#   after I had reduced it to a series of modulos over the range

require 'prime'
b=81
p "Answer 2:", ((b*100+10**5)..(b*100+10**5+17000)).step(17).select { |n| !Prime.prime?(n) }.length

