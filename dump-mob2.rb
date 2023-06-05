def create
  @mobile_number = params[:session][:mobile_number]
File.open("mobile_numbers.txt", "a") do |file|
  file.puts(params[:mobile_number])
  puts "Mobile Number: #{@mobile_number}"
end
