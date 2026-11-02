# Test Ruby hash creation, lookup, update, and iteration

student = {
  "name" => "Ali",
  "age" => 21,
  "course" => "Computer Engineering"
}

puts "Name: #{student['name']}"
puts "Age: #{student['age']}"

student["age"] = 22
puts "Updated age: #{student['age']}"

puts "Student details:"
student.each do |key, value|
  puts "#{key}: #{value}"
end
