import pandas as pd

class SubStream:
    def __init__(self, das):
        self.das = das
        self.generate_list = generate_list(self.das)
        self.frame_detection =frame_detection(self.das)
    def frame_detection(das):
        dasfile = das
        with open(das, 'rb') as source_file:
            with open(das, 'w+b') as dest_file:
                contents = source_file.read()
                dest_file.write(contents.decode('utf-16').encode('utf-8'))
        with open(das) as lines:
            for line in islice(lines, 2, 3):
                print line





    def math(x):
        frames = 0
        frames += float(x[0])*60*60*24 + float(x[1])*60*24 + float(x[2])*24 + float(x[3])
        return frames
    def export(grid):
        export = grid
        export.to_csv("export.csv")
    def generate_list(das):
        subtitles_raw = das.replace('*\n','\n').replace(': *',':  ').split('\n\n')[1:]
        ##replace('        ','  ').replace('     ','').replace('    ','').replace('   ','').split('\n\n',1)[1:]
        subtitle_raw = []
        for i in subtitles_raw:
            subtitle_raw.append(i.replace('\n        ','\n\n',1).replace('\n        ','\n').replace('     ','').replace('    ','').replace('   ','').replace('\n\n','  '))
        ##return subtitle_raw
        subtitle_split = []
        for i in subtitle_raw:
            subtitle_split.append(i.split('  '))
        ##return subtitle_split
        grid = pd.DataFrame.from_records(subtitle_split[:-1], columns=['Subtitle_number', 'TC_in', 'TC_out', 'Subtitle_text'])
        ##return df
        grid['TC_in_frames'] = grid.TC_in.str.replace('.',':').str.split(':').apply(SubStream.math)
        grid['TC_out_frames'] = grid.TC_out.str.replace('.',':').str.split(':').apply(SubStream.math)
        return grid


