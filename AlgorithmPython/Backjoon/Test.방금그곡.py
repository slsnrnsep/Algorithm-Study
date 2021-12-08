m = "CC#BCC#BCC#BCC#B"
musicinfos = ["00:00,23:59,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]



def solution(m, musicinfos):
    count = 0
    answertime = []
    answertitle = []
    m = m.replace("C#", "V")
    m = m.replace("D#", "W")
    m = m.replace("F#", "X")
    m = m.replace("G#", "Y")
    m = m.replace("A#", "Z")
    for i in range(len(musicinfos)):
        timeMinute = int(musicinfos[i].split(',')[1].split(':')[1]) - int(musicinfos[i].split(',')[0].split(':')[1])
        timeHour = int(musicinfos[i].split(',')[1].split(':')[0]) - int(musicinfos[i].split(',')[0].split(':')[0])
        title = musicinfos[i].split(',')[2]
        pattern = musicinfos[i].split(',')[3]
        pattern=pattern.replace("C#", "V")
        pattern=pattern.replace("D#", "W")
        pattern=pattern.replace("F#", "X")
        pattern=pattern.replace("G#", "Y")
        pattern=pattern.replace("A#", "Z")
        realtime = timeMinute + timeHour * 60
        realplay = ""

        if(len(pattern) <= realtime):
            realplay = pattern * (realtime//len(pattern)) + pattern[:realplay%len(pattern)]
        else:
            realplay = pattern[0:realtime]

        if m in realplay:
            count += 1
            answertime.append(realtime)
            answertitle.append(title)

    if(count>0):
        maxtime =max(answertime)
        index =answertime.index(maxtime) #최대값이 여러개일 경우 앞에꺼가 나옴
        return print(answertitle[index])
    else:
        return "(None)"

solution(m,musicinfos)



