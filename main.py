from utils import read_credentials_from_file, try_login


file_path = 'megaaccounts.txt' #os.path.join(os.path.dirname(__file__), 'credentials')

credentials = read_credentials_from_file(file_path)

# credentials = [
#     {'email':'samuray5996@yandex.ru', 'password':'Rainbowdasfsfh96@'},
#     {'email':'jam0857es@gmail.com', 'password':'James0857'}]


# Print extracted credentials
for cred in credentials:
    try_login(cred["email"], cred["password"])

# email = 'samuray996@yandex.ru'
# password = 'Rainbowdash96@'
# try_login(email, password)

if '__init__' == '__main__':
    main()