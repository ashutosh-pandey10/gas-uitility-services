# Gas Utility Services

A Django Rest Framework backend to handle customer requests and provide them support.

## Setting up for Testing

1. Run the server, go to [http://localhost:8000/admin/](http://localhost:8000/admin/), and log in with your admin credentials. A superuser has already been created with the username "helloworld" and the password "123". Once on the admin dashboard, create a new user and remember the username and password.

2. To simulate authentication, you'll need to obtain an access token. You can do this by using a package like `django-rest-framework-simplejwt` to issue tokens. Generate an access token using the `/token/` endpoint. Send a POST request to [http://localhost:8000/token/](http://localhost:8000/token/) with the user's credentials (username and password) as the request body. The response will contain an access token.

## Testing UserProfile

Once you have the access token, you can test the `UserProfile` using Postman. Here's how:

- **Get User Profile:**
  Send a GET request to [http://localhost:8000/api/services/get-user-profile/](http://localhost:8000/api/get-user-profile/) and add the `Authorization` header with the value `Bearer YOUR_ACCESS_TOKEN`. Replace `YOUR_ACCESS_TOKEN` with the actual token you obtained.

- **Update User Profile:**
  Send a PUT request to [http://localhost:8000/api/services/update-user-profile/](http://localhost:8000/api/services/update-user-profile/). Add the `Authorization` header as before. Include the following JSON payload in the request body:

  ```json
  {
      "phone_number": "1234567890",
      "address": "123 Main St, City"
  }

You can also look through the application and test other API endpoints as well. Cheers!
