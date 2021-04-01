# Development of Resume backend

The backend of the application consist of a serverless architecture making use of DynamoDB,Lambda and APIGateway.
We make use of SAM to Deploy our serverless components to a S3 bucket which can be used by CloudFormation to create our resources.

# Deploying a DynamoDB table with cloudformation
* The purpose of DynamoDB is this usecase is to hold the count for the visitors.
* Deploying AWS resources using CF is easier to update and manage.
* We create single attribute called id and make sure to mention Lambda DynamoDBCrudPolicy to reference our DynamoDB.

![db](https://user-images.githubusercontent.com/57376468/113338122-4d332000-92ee-11eb-9778-bedec4c40b40.PNG)
![db2](https://user-images.githubusercontent.com/57376468/113338129-4e644d00-92ee-11eb-9455-16ad6eb8bc9d.PNG)

# Deploying serverless API using Lambda and API Gateway.
* The website counter needs an interface to communicate with DynamoDB.
* API Gateway makes it smoother to set up rate limits, throttling, and other usage plan metrics for the API.
* To deploy we make use of SAM(Serveless Application Model) CLI.
* The `Handler: app.lambda_handler` statement informs SAM that lambda function is provided in the file named app.py.
* We make use of Lambda proxy integration which means all requests from API gateway shall be proxied to Lambda which allows it process appropriate response.

![api_gateway](https://user-images.githubusercontent.com/57376468/113338248-78b60a80-92ee-11eb-810e-da4f5a33dcb4.PNG)
![lamda](https://user-images.githubusercontent.com/57376468/113338685-0c87d680-92ef-11eb-8455-3f9744aac7c8.PNG)

![backend1](https://user-images.githubusercontent.com/57376468/113339346-f29ac380-92ef-11eb-83ff-8dcddee965c7.PNG)

# Using Github actions to run CICD steps such as configuring AWS,running test cases ,building and deploying SAM template.
![image](https://user-images.githubusercontent.com/57376468/113339484-237af880-92f0-11eb-9e15-7925c13ac4f5.png)

