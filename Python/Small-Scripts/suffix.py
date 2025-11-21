def main():
    file = input("File name: ")
    if "." in file:
        suffix = file.split(".",1)[1]

        if suffix == "gif" or suffix == "png":
            print(f"image/{suffix}")
        elif suffix == "jpg" or suffix == "jpeg":
            print("image/jpeg")
        elif suffix == "pdf" or suffix == "txt" or suffix == "zip":
            print(f"application/{suffix}")
        else:
            print("application/octet-stream")
    else:
        print("application/octet-stream")


main()