# In a file called extensions.py, implement a program
# that prompts the user for the name of a file and then
# outputs that file's media type if the file's name ends,
# case-insensitively, in any of these suffixes:
# .gif, .jpg, .jpeg, .png, .pdf, .txt., .zip
# If the file's name ends with some other suffix or has
# no suffix at all, output application/octet-stream instad,
# which is a common default.


nime_types = [
    {"extension": ".gif", "nime_type": "image/gif"},
    {"extension": ".jpg", "nime_type": "image/jpeg"},
    {"extension": ".jpeg", "nime_type": "image/jpeg"},
    {"extension": ".png", "nime_type": "image/png"},
    {"extension": ".pdf", "nime_type": "application/pdf"},
    {"extension": ".txt", "nime_type": "text/plain"},
    {"extension": ".zip", "nime_type": "application/zip"}
    ]
# source: https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types


def main():
    print(check_media_type(input("File name: ").strip().lower()))


def check_media_type(file_name):
    for nime_type in nime_types:
        if file_name.endswith(nime_type["extension"]):
            result = nime_type["nime_type"]
            
            return result
            
        else:
            result = "application/octet-stream"

    return result


if __name__ == "__main__":
    main()
          