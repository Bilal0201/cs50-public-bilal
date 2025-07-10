def get_ext(file):
     file = file.lower().strip()
     if "." in file:
         return file.rsplit(".", 1)[1]
     else: return file


file = input("File name: ")
ext = get_ext(file)
match ext:
    case "gif":
        print("image/gif")
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")


