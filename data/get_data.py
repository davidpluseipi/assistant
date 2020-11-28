
import csv

# class Contact:
#     def __init__(self,
#                  first_name,
#                  last_name,
#                  phone,
#                  email):  # initialize attributes
#         self.first_name = first_name
#         self.last_name = last_name
#         self.phone = phone
#         self.email = email


the_string = 'Anders'
with open(r'c:\g\code\assistant\data\contacts.csv') as csv_file:
    reader = csv.DictReader(csv_file, delimiter=',')
    column_names = reader.fieldnames
    print(column_names)
    first_name = ''  # to prevent reporting duplicates
    for row in reader:
        if row["Given Name"] != '':  # comparing string.find to someone without a first name does not result in -1
            if the_string.find(f'{row["Given Name"]}') != -1:
                if first_name != row["Given Name"]:  # to prevent reporting duplicates
                    first_name = row["Given Name"]
                    last_name = row["Family Name"]
                    phone_type = row["Phone 1 - Type"]
                    phone = row["Phone 1 - Value"]
                    email_type = row["E-mail 1 - Type"]
                    email = row["E-mail 1 - Value"]
                    print(f'{first_name} {last_name}')
                    print(f'{phone_type}: {phone}')
                    print(f'{email_type}: {email}')









