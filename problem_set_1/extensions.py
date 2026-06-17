name = input("What is file name? ")
ext: str = name.rsplit(".", 1)[-1].lower()
if ext == "gif":
    print("image/gif")
elif ext == "jpg" or ext == "jpeg":
    print("image/jpeg")
elif ext == "png":
    print("image/png")
elif ext == "pdf":
    print("application/pdf")
elif ext == "txt":
    print("text/plain")
else:
    print("application/octet-stream")
