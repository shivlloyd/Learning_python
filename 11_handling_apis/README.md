# Handling API in python

1. **Purpose**: This code fetches random user data from a public API and prints out the username and country of the fetched user.

2. **Libraries Used**:

   - `requests`: Used to make HTTP requests to the API.

3. **Function `fetch_random_user_freeapi()`**:

   - **Purpose**: Fetches random user data from a public API.
   - **Steps**:
     1. Constructs the URL for the API endpoint.
     2. Sends a GET request to the API.
     3. Parses the JSON response.
     4. Extracts the username and country from the response data.
     5. Returns the username and country.

4. **Function `main()`**:

   - **Purpose**: Executes the main functionality of the code.
   - **Steps**:
     1. Calls the `fetch_random_user_freeapi()` function to get user data.
     2. Prints the username and country obtained from the API.
     3. Handles any exceptions that might occur during the process and prints an error message.

5. **Exception Handling**:

   - If there is any failure in fetching user data (e.g., network issues, API errors), an exception is raised with an appropriate error message.

6. **Execution**:

   - The `main()` function is called when the script is executed directly.
   - If executed, it prints out the username and country of a randomly fetched user.

7. **Notes**:
   - The code assumes that the API endpoint is reachable and returns valid JSON data.
   - It's a good practice to handle potential errors in API requests, such as network errors or unexpected responses.
   - The code can be further expanded to perform additional processing on the fetched user data, such as displaying more details or storing it in a database.
