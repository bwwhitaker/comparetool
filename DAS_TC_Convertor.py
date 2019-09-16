def TimecodeConvertor(timecode):
    timecode_split = timecode.replace("." , ":").split(":")
    Hours = int(timecode_split[0])
    Minutes = int(timecode_split[1])
    Seconds = int(timecode_split[2])
    Frames = int(timecode_split[3])
    detectedFrameRate = 24
    dropFrame = True
    TC_inFrames = 0
    TC_inFrames += ((Hours * 60 * 60) + (Minutes * 60) + Seconds) * detectedFrameRate + Frames
    if dropFrame == True:
        DF_Minutes_Total = Hours * 60 + Minutes
        DF_Minutes_Modulo = (DF_Minutes_Total % 10)
        DF_Minutes_10_chunk = (DF_Minutes_Total - DF_Minutes_Modulo) / 10
        TC_inFrames -= (DF_Minutes_10_chunk * 18 + DF_Minutes_Modulo * 2)
        return int(TC_inFrames)
    else:
        return TC_inFrames