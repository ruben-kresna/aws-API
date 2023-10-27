# aws_jitto
Jitto Techincal Challenge

This API calls a DynamoDB table called MyTable using Lambda Functions through the AWS API Gateway. MyTable's partition key is a String 'id' and its attributes are 'name' and 'description' which are also both strings. There is no sort key.

The API Key is required to invoke the API, which can be found in import requests.py (this is bad practice, but it is just for a demonstration, so I think it is fine)

The import requests.py file is an example of how to use the APIs.

The API Invoke URL is
https://c1fla4vbr8.execute-api.us-east-2.amazonaws.com/MyTableAPI

There are 4 methods for the API:
1. getItem(id)
2. getItemAll()
3. addItem(requestBody)
4. deleteItem(id)

getItem(id) is a GET method that retrieves an item with the associated id in MyTable. The id parameter must be an integer.
  The method path is /mytable
  Example:
  https://c1fla4vbr8.execute-api.us-east-2.amazonaws.com/MyTableAPI/mytable?id=2

getItemAll() is a GET method that retrieves all items in MyTable
  The method path is /mytable_all
  Example:
  https://c1fla4vbr8.execute-api.us-east-2.amazonaws.com/MyTableAPI/mytable_all

addItem(requestBody) is a POST method that adds an requestBody as an item to MyTable. requestBody must be in json format.
  The method path is /mytable
  Example:
  requestBody = {
    'id': '15',
    'name': 'Doll',
    'description': 'Pikachu plushie'
  }

deleteItem(id)  is a DELETE method that deletes an item in MyTable with an id of id. id must be in json format.
  The method path is /mytable
  Example:
  requestBody = {
    'id': '15'
  }
