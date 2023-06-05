def create
  @mobile_number = params[:session][:mobile_number]
  puts "Mobile Number: #{@mobile_number}"
  File.open("mobile_numbers.txt", "a") do |f|
    f.puts @mobile_number
  end
end
