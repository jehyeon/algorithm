def solution(dartResult):
    # dartResult를 round 별로 나눔
    rounds = []
    round = ''
    for index, ele in enumerate(dartResult):
        if ele.isdigit() and round != '':
            if dartResult[index] == '0' and dartResult[index - 1] == '1':
                round += ele
            else:
                rounds.append(round)
                round = ele
        else:
            round += ele
            
            if index == len(dartResult) - 1:
                rounds.append(round)
    
    # 라운드 별 점수 계산
    scores = []
    for index, round in enumerate(rounds):
        score = 0
        option = ''
        
        if 'S' in round:
            score += int(round.split('S')[0])
        elif 'D' in round:
            score += int(round.split('D')[0]) ** 2
        elif 'T' in round:
            score += int(round.split('T')[0]) ** 3
        
        if score == 10:
            option = round[3:]
        else:
            option = round[2:]
            
        if option == '*':
            score *= 2
            if index > 0:
                scores[index - 1] *= 2
        elif option == '#':
            score *= -1
        
        scores.append(score)
        
    return sum(scores)