# Python Project Youtube manager with mongoDB

1. **Importing Libraries**:

   - The code begins by importing necessary libraries, `MongoClient` from `pymongo` for connecting to the MongoDB database, and `ObjectId` from `bson` for handling MongoDB document IDs.

2. **Connecting to MongoDB**:

   - The `MongoClient` is used to establish a connection to the MongoDB Atlas cluster. The connection string includes the username, password, and cluster URL.

3. **Accessing Database and Collection**:

   - After connecting to MongoDB, the code selects the `ytmanager` database and the `videos` collection within that database.

4. **Defining Functions**:

   - Several functions are defined to perform CRUD (Create, Read, Update, Delete) operations on the video collection in the database:
     - `list_videos()`: Retrieves all videos from the collection and prints their details.
     - `add_video(name, time)`: Inserts a new video document into the collection with the given name and time.
     - `update_video(video_id, new_name, new_time)`: Updates the name and time of a video with the specified ID.
     - `delete_video(video_id)`: Deletes a video document with the specified ID from the collection.

5. **Main Function**:

   - The `main()` function serves as the entry point of the program.
   - It contains a loop that repeatedly displays a menu of options and prompts the user to choose an action.
   - Based on the user's input, it calls the appropriate function to perform the desired operation on the video collection.
   - The loop continues until the user chooses to exit the application.

6. **Menu Options**:

   - The menu options allow the user to:
     - List all videos.
     - Add a new video by providing its name and time.
     - Update an existing video by specifying its ID and providing new name and time values.
     - Delete a video by specifying its ID.
     - Exit the application.

7. **Handling User Input**:

   - The user's choice is read from the input and then used to determine which function to call.
   - If the choice is not recognized, an error message is displayed.

8. **Executing the Main Function**:
   - Finally, the code checks if the script is being run directly (**name** == "**main**") and calls the `main()` function to start the application.

Overall, the code provides a simple command-line interface for managing a collection of videos stored in a MongoDB database. It allows users to perform CRUD operations on the video collection easily.
