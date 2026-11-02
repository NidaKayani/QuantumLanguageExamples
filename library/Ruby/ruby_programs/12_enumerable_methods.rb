# Test Ruby Enumerable methods: map, select, and reduce

numbers = [1, 2, 3, 4, 5]

doubled = numbers.map { |n| n * 2 }
puts "Doubled: #{doubled}"

even_numbers = numbers.select { |n| n % 2 == 0 }
puts "Even numbers: #{even_numbers}"

total = numbers.reduce(0) { |sum, n| sum + n }
puts "Total: #{total}"
