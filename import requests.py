import requests
import json
api_key = 'R9nYbNH26ba25iDZG3oQB8ylYHrWk1Vc4RcYhjk6'
headers = {'X-API-Key': api_key}

# getItem GET method with id to get an item from DynamoDB table MyTable
response = requests.get('https://c1fla4vbr8.execute-api.us-east-2.amazonaws.com/MyTableAPI/mytable?id=1', headers=headers)
print(response.text)
response = requests.get('https://c1fla4vbr8.execute-api.us-east-2.amazonaws.com/MyTableAPI/mytable?id=2', headers=headers)
print(response.text)
# example if item with that id does not exist
response = requests.get('https://c1fla4vbr8.execute-api.us-east-2.amazonaws.com/MyTableAPI/mytable?id=5', headers=headers)
print(response.text+"\n")

# getItemAll GET method to get all items from DynamoDB table MyTable
response = requests.get('https://c1fla4vbr8.execute-api.us-east-2.amazonaws.com/MyTableAPI/mytable_all', headers=headers)
print(response.text+"\n")

# addItem POST method to add a new item to DynamoDB table MyTable
requestBody = {
    'id': '5',
    'name': 'Bottle',
    'description': 'Adidas Sports bottle'
}
response = requests.post('https://c1fla4vbr8.execute-api.us-east-2.amazonaws.com/MyTableAPI/mytable', data=json.dumps(requestBody), headers=headers)
print(response.text)
# check to make sure item was added successfully
response = requests.get('https://c1fla4vbr8.execute-api.us-east-2.amazonaws.com/MyTableAPI/mytable?id=5', headers=headers)
print(response.text)

# deleteItem DELETE method to delete an item from DynamoDB table MyTable
requestBody = {
    'id': '5'
}
response = requests.delete('https://c1fla4vbr8.execute-api.us-east-2.amazonaws.com/MyTableAPI/mytable', data=json.dumps(requestBody), headers=headers)
print(response.text)
# check to make sure item was deleted successfully
response = requests.get('https://c1fla4vbr8.execute-api.us-east-2.amazonaws.com/MyTableAPI/mytable?id=5', headers=headers)
print(response.text)