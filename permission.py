import os
import stat

filename = "permission.txt"

before = oct(os.stat(filename).st_mode)[-3:]
print(f"Before: {before}")


os.chmod(filename,0o775)

after = oct(os.stat(filename).st_mode)[-3:]
print(f"After: {after}")

