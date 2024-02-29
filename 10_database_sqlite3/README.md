```python
def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. exit App")
        choice = input("enter your choice: ")

        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == "3":
            list_videos()
            video_id = input("Enter video ID to update: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_video(video_id, name, time)
        elif choice == "4":
            list_videos()
            video_id = input("Enter video ID to Delete: ")
            delete_video(video_id)
        elif choice == "5":
            break
        else:
            print("Invalid Choice")

    conn.close()


if __name__ == "__main__":
    main()
```

- The code defines a Python function `main()` that serves as the entry point of the program.
- Inside the `main()` function, there's an infinite loop created by `while True:` which continuously prompts the user with a menu for managing YouTube videos.
- The menu displays options for listing videos, adding videos, updating videos, deleting videos, and exiting the app.
- The user's input is captured through the `input()` function and stored in the variable `choice`.
- Depending on the user's choice, different functions are called:
  - If the choice is '1', the `list_videos()` function is called to display a list of videos.
  - If the choice is '2', the user is prompted to input the name and time of the video, which are then passed to the `add_video()` function.
  - If the choice is '3', the user is first shown the list of videos, then prompted to input the ID of the video to update along with the new name and time, which are then passed to the `update_video()` function.
  - If the choice is '4', similar to option 3, the user selects a video ID to delete, which is then passed to the `delete_video()` function.
  - If the choice is '5', the loop breaks, terminating the program.
- If the user enters an invalid choice, a message "Invalid Choice" is displayed.
- After the loop ends, the database connection is closed using `conn.close()`.
- Finally, the `main()` function is called if the script is executed directly (not imported as a module).

```python
import sqlite3

conn = sqlite3.connect("youtube_videos.db")

cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER Primary Key,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
"""
)
```

- The code establishes a connection to a SQLite database named "youtube_videos.db" using the `sqlite3.connect()` function, and assigns the connection object to the variable `conn`.
- It creates a cursor object using `conn.cursor()`, which allows executing SQL commands against the database.
- With the cursor, it executes a SQL command to create a table named "videos" if it doesn't already exist within the database.
- The table has three columns: "id" of type INTEGER which serves as the primary key, "name" of type TEXT which stores the name of the video, and "time" of type TEXT which stores the duration of the video.
- The `CREATE TABLE IF NOT EXISTS` statement ensures that the table is created only if it doesn't already exist in the database, preventing errors if the table structure is already defined.

```python
def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)


def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()


def update_video(video_id, new_name, new_time):
    cursor.execute(
        "UPDATE videos SET name = ?, time = ? WHERE id = ?",
        (new_name, new_time, video_id),
    )
    conn.commit()


def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()
```

- The code defines four functions to interact with the SQLite database established earlier.
- The `list_videos()` function executes a SQL query to select all rows from the "videos" table and then iterates over the result set, printing each row to the console.
- The `add_video(name, time)` function inserts a new record into the "videos" table with the provided name and time values, using parameterized SQL queries to prevent SQL injection attacks.
- The `update_video(video_id, new_name, new_time)` function updates an existing video record identified by its ID with the provided new name and time values, again utilizing parameterized queries for safety.
- The `delete_video(video_id)` function deletes a video record from the "videos" table based on the provided video ID, safeguarded by parameterized queries.
- All database modifications (`add_video`, `update_video`, `delete_video`) are followed by `conn.commit()` to ensure that the changes are saved permanently in the database.
