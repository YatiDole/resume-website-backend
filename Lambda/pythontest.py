import os
import boto3
import unittest
from moto import mock_dynamodb2
from app import lambda_handler

def testCreds():  
  DEFAULT_REGION = "us-east-1"  
  os.environ['AWS_ACCESS_KEY_ID'] = '${{ secrets.AWS_ACCESS_KEY_ID }}'
  os.environ['AWS_SECRET_ACCESS_KEY'] = '${{ secrets.TABLE_NAME }}'
  os.environ["AWS_REGION"] = '${{ secrets.AWS_DEFAULT_REGION }}'
 
  os.environ['TABLE_NAME'] = 'table_name' 

class testDynamo(unittest.TestCase): 
  @mock_dynamodb2
  def test_handler(self):
    dynamo = boto3.client('dynamodb', region_name='us-east-1')
    table_name = os.environ['TABLE_NAME']
    dynamo.create_table(
      TableName = table_name,
      BillingMode='PAY_PER_REQUEST',
      AttributeDefinitions=[
          {   
              'AttributeName': 'id',
              'AttributeType': 'S' 
          },
      ],
      KeySchema=[
          {
              'AttributeName': 'id',
              'KeyType': 'HASH'
          },
      ]
    )

    response = lambda_handler(0, 0)
    print("Response: ", response)

    self.assertEqual(200, response['statusCode'])

if __name__ == '__main__':
  testCreds()
  unittest.main() 