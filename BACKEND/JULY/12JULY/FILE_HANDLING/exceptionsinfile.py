try:
    with open("read.py","r") as file:
        print(file.read())
        
except Exception as e:
    print(e)
















# class thisiserror(Exception):
#     pass
# try:
#     a=3
#     if 2==a:
#         print("found")
#     else:
#         raise thisiserror("errrorrrrrrrrr")
# except Exception as e:
#     print(e)
# else:
#     print("hii this is avantika")
# finally:
#     print("finally")