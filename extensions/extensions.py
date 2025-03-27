def main():

    user_input = input("Enter file name: ").lower()

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
        if user_input.endswith(media):
            return media_types[media]

    return application/octet-stream



result = main()
print(main)
