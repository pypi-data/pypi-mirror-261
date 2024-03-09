import re, os
from config import patterns
directory="/home/user1/Desktop/sensitiveInfoDetector/sensitiveInfoDetector"
fileName="data.txt"
file_path = os.path.join(directory, fileName)

file = open(file_path, "r")
contents = file.read()

def detect_secrets(contents):
        for pattern in patterns:
            if re.search(pattern, contents, flags=re.IGNORECASE):
                return True
        else:
            return False


print(detect_secrets(contents))    

# Output :  True
