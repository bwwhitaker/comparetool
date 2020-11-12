import pandas as pd
import codecs
import difflib

class SubStreamToGrid:
    def __init__(self, file):
        self.file = file
        self.generateTable = generateTable(self.file)

    def generateTable(file):
        filecontentForFM = []
        f = codecs.open(file, 'r', 'utf-16le')
        filecontentForFM += f
        documentFramerate = filecontentForFM[2]
        frameMultiplier = 0
        dropFrame = False
        if "23.98" in documentFramerate:
            frameMultiplier = 24
            dropFrame = False
        elif "FILM" in documentFramerate:
            frameMultiplier = 24
            dropFrame = False
        elif "PAL" in documentFramerate:
            frameMultiplier = 25
            dropFrame = False
        elif "NDF" in documentFramerate:
            frameMultiplier = 30
            dropFrame = False
        elif "DF" in documentFramerate:
            frameMultiplier = 30
            dropFrame = True

        def TimecodeConvertor(timecode):
            timecode_split = timecode.replace(".", ":").split(":")
            Hours = int(timecode_split[0])
            Minutes = int(timecode_split[1])
            Seconds = int(timecode_split[2])
            Frames = int(timecode_split[3])
            if dropFrame == False:
                TC_inFrames = 0
                TC_inFrames += ((Hours * 60 * 60) + (Minutes * 60) + Seconds) * frameMultiplier + Frames
            if dropFrame == True:
                DF_Minutes = Hours * 60 + Minutes
                if DF_Minutes >= 10:
                    DF_Modulo = DF_Minutes % 10
                    DF_10_chunk = (DF_Minutes - DF_Modulo) / 10
                    TC_adjuster = Minutes * ((DF_10_chunk * 18) + (DF_Modulo * 2))
                elif DF_Minutes <= 9:
                    TC_adjuster = Minutes * 2
                TC_inFrames = 0
                TC_inFrames += ((Hours * 60 * 60) + (Minutes * 60) + Seconds) * frameMultiplier + Frames - TC_adjuster
            return int(TC_inFrames)

        filecontent = []
        f = codecs.open(file, 'r', 'utf-16le')
        filecontent += f
        filecontent_cleaned = []
        for i in filecontent:
            filecontent_cleaned.append(i.replace('\ufeff', '').replace('0000.00\r\n',''))
        string_content = ""
        for i in filecontent_cleaned:
            string_content += i
        subtitle_split = string_content.split('\r\n\r\n')
        cleaned_sub_list = []
        for i in subtitle_split[1:]:
            cleaned_sub_list.append(i.replace(':  ',':\rr\n').replace(': *',':\rr\n').replace('\r\n','\rr\n',1).replace('  00','\rr\n00').replace('  01','\rr\n01').replace('*\rr','\rr').replace('  ','').replace('\rr\n','@@@').replace('\r\n','\n'))
        subs_broken = []
        for i in cleaned_sub_list:
            subs_broken.append(i.split('@@@'))
        grid = pd.DataFrame.from_records(subs_broken[:-1], columns=['Subtitle_number', 'TC_in', 'TC_out', 'Subtitle_text'])
        grid['TC_in_frames'] = grid.TC_in.apply(TimecodeConvertor)
        grid['TC_out_frames'] = grid.TC_out.apply(TimecodeConvertor)
        return grid

##print(SubStreamToGrid.generateTable('ystar-tra1-swe-vod-2398-876590.das'))
##print(SubStreamToGrid.generateTable('24eng.das'))
print(SubStreamToGrid.generateTable('NTSCDF2997ENg.das'))
print(SubStreamToGrid.generateTable('NTSCS30ENg.das'))