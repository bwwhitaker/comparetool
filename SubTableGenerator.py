import pandas as pd
import codecs
from DAS_TC_Convertor import TimecodeConvertor as TCConv

def generateTable(file):
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
    grid['TC_in_frames'] = grid.TC_in.apply(TCConv)
    grid['TC_out_frames'] = grid.TC_out.apply(TCConv)
    return grid


### DAS_TC_Convertor.py is assuming 24 FPS. Need to program to have it detect file value.



print(generateTable('ystar-tra1-swe-vod-2398-876590.das'))