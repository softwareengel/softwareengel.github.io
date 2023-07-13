import requests
import os

# Get the directory of the script file
script_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the file path of the text file
file_path = os.path.join(script_directory, 'api-secret.key')  # Replace 'filename.txt' with the actual file name

# Open the file in read mode

with open(file_path, 'r') as file:
    # Read the contents of the file
    key = file.read()

# Print the content
print("Key: ", key)

# # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
# url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
# r = requests.get(url)
# data = r.json()

# print(data)

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=A2DVEZ&interval=5min&apikey={key}'
r = requests.get(url)
data = r.json()

print(data)