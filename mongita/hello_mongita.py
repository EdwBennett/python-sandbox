from mongita import MongitaClientDisk

client = MongitaClientDisk(host="./mongita_data")
db = client.sample_db
collection = db.books

collection.delete_many({})

collection.insert_one({
    "russian_text": "Война и мир"
})

first_record = collection.find_one()

print(first_record["russian_text"])
