#!/usr/bin/ruby

require 'prime'
b=81
p ((b*100+10**5)..(b*100+10**5+17000)).step(17).select { |n| !Prime.prime?(n) }.length

