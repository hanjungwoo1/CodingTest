def changecode(music_):
    music_ = music_.replace('C#', 'c')
    music_ = music_.replace('D#', 'd')
    music_ = music_.replace('F#', 'f')
    music_ = music_.replace('G#', 'g')
    music_ = music_.replace('A#', 'a')
    return music_


def get_time(start: str, end: str) -> int:
    start_hour, start_min = map(int, start.split(':'))
    end_hour, end_min = map(int, end.split(':'))

    start_min += start_hour * 60
    end_min += start_hour * 60


    return end_min - start_min


def solution(m, musicinfos):
    answer = []

    m = changecode(m)

    for idx, music in enumerate(musicinfos):
        start, end, title, notes = music.split(',')
        notes = changecode(notes)
        time = get_time(start, end)

        # 길이가 시간보다 더 긴 경우
        if len(notes) >= time:
            melody = notes[0:time]
        else:
            # 시간을 계산해서 몫과 나머지로 계산
            # 다른 사람 풀이 : q, r = divmod(time,len(musicinfo[3]))
            a = time // len(notes)
            b = time % len(notes)
            melody = notes * a + notes[0:b]

        if m in melody:
            answer.append([idx, time, title])

    # 정답이 있는 경우
    if len(answer) != 0:
        # time -> index 기준으로 정렬
        answer = sorted(answer, key=lambda x: (-x[1], x[0]))
        return answer[0][2]
    # 정답이 없는 경우
    return "(None)"
