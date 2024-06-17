import plyvel

# Path to the LevelDB database
db_path = 'path_to_leveldb_directory'  # Replace with your actual path

# Open the LevelDB database
db = plyvel.DB(db_path, create_if_missing=False)

# Fetch specific value
specific_key = b'hello'
value = db.get(specific_key)
if value:
    print(f'Key: {specific_key.decode()}, Value: {value.decode()}')
else:
    print(f'Key: {specific_key.decode()} not found')

# Iterate and display all stored values
for key, value in db:
    print(f'Key: {key.decode()}, Value: {value.decode()}')

# Close the database
db.close()
