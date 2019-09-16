import pandas as pd
import codecs

def detectFramerate(file):
    filecontent = []
    f = codecs.open(file, 'r', 'utf-16le')
    filecontent += f
    documentFramerate = filecontent[2]
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
    return frameMultiplier, dropFrame