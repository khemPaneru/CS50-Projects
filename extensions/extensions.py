def main():

    user_input = input("Enter file name: ").lower()
    #create a dic
    media_types = {
        ".gif": "image/gif",
        ".jpg": "image/jpg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip",
    }

    for media in media_types:
#endswith():  method in Python is used to check if a string ends
# with a specified suffix (or substrings) like .gif,.jpg
        if user_input.endswith(media):
            return media_types[media]

    return "application/octet-stream"

print(main())
