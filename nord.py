from utils import read_credentials_from_file, try_login_nordvpn

file_path = 'nordvpn.txt'

# Extracting email addresses and passwords
credentials = read_credentials_from_file(file_path)

print(credentials)
# Displaying extracted credentials
for cred in credentials:
    print(cred["email"], cred["password"])
    try_login_nordvpn(cred["email"], cred["password"])





