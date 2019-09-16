import pandas as pd

def detectFramerate(file):
    with open(file, 'rb') as source_file:
        with open("file-utf8.das", 'w+b') as dest_file:
            contents = source_file.read()
            dest_file.write(contents)
    with open ("file-utf8.das") as f:
        lines = f.readlines()
        documentFramerate = lines[2]
        frameMultiplier = 0
        dropFrame = False
    if "23.98" in documentFramerate:
        frameMultiplier += 24
        dropFrame = False
    elif "24" in documentFramerate:
        frameMultiplier += 24
        dropFrame = False
    elif "PAL" in documentFramerate:
        frameMultiplier += 25
        dropFrame = False
    elif "NTSC NDF" in documentFramerate:
        frameMultiplier += 30
        dropFrame = False
    elif "NTSC DF" in documentFramerate:
        frameMultiplier += 30
        dropFrame = True
    return lines, frameMultiplier, dropFrame

print(detectFramerate("y-eng-ft.das"))