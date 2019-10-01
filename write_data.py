import csv
import datetime
import shutil
from tempfile import NamedTemporaryFile

def get_length(file_path):
    with open("data2.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        reader_list = list(reader) #everthing in it become a list
        print(reader_list)
        print(len(reader_list))
        return len(reader_list)

def append_data(file_path, name, email):
    fieldnames = ['id', 'name', 'email']
    # the number of rows?
    next_id = get_length(file_path)
    with open(file_path, "a") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # writer.writeheader()
        writer.writerow({
            "id": next_id,
            "name": name,
            "email":email,
        })


# append_data("data2.csv", "David", "davidcc20111@gmail.com")



filename = "data2.csv"
temp_file = NamedTemporaryFile(delete=False)

with open(filename, "rb") as csvfile, temp_file:
    reader = csv.DictReader(csvfile)
    fieldnames = ['id', 'name', 'email', 'amount', 'sent', 'date']
    writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
    writer.writeheader()
    print(temp_file.name)
    for row in reader:
        og_data =
        if row['id'] ==4:
            print(row)
            writer.writerow({
                    "id": row["id"],
                    "name": row["name"],
                    "email": row["email"],
                    "amount": "1293.23",
                    "sent": "True",
                    "date": datetime.datetime.now()
                })
    shutil.move(temp_file.name, filename)
