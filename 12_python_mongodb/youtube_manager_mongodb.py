from pymongo import MongoClient
from bson import ObjectId

client = MongoClient(
    "mongodb+srv://youtubepy:*******@cluster0.hqvneut.mongodb.net/", tlsAllowInvalidCertificates=True
)
# Not a good idea to include id and password incode files
# tlsAllowInvalidCertificates=True - Not a good way to handle ssl


db = client["ytmanager"]

video_collection = db["videos"]

print(video_collection)

def list_videos():
    for video in video_collection.find():
        print(f"ID: {video["_id"]}, Name: {video['name']} and Time: {video['time']}")

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def update_video(video_id, new_name, new_time):
    video_collection.update_one(
        {'_id': ObjectId(video_id)}, 
        {"$set": {"name": new_name, "time": new_time}}
    )

def delete_video(video_id):
    video_collection.delete_one({"_id": ObjectId(video_id)})


def main():
    while True:
        print("\n Youtube manager App")
        print("1. List all videos")
        print("2. Add a new video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit the App")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == "3":
            video_id = input("Enter the video id: ")
            name = input("Enter the updated video name: ")
            time = input("Enter the updated video time: ")
            update_video(video_id, name, time)
        elif choice == "4":
            video_id = input("Enter the video id: ")
            delete_video(video_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
