require 'rest-client'
require 'json'

def find_account_id_by_name(name)
  url = "https://api.rubika.ir/v1/accounts/search?term=#{name}"
  response = RestClient.get(url)
  json = JSON.parse(response.body)
  if json['accounts'].empty?
    return nil
  else
    return json['accounts'][0]['id']
  end
end

# Example usage:
account_id = find_account_id_by_name('example_username')
if account_id.nil?
  puts 'Account not found.'
else
  puts "Account ID: #{account_id}"
end
