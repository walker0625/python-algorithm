def temperature_days(temperatures):
    answer = [0] * len(temperatures)
    stack = []
    
    for cur_day, cur_temp in enumerate(temperatures):
        # [-1]은 stack의 최상단 값(pop()하면 나오므로 확인만 하는 용도)
        while stack and stack[-1][1] < cur_temp: 
            prev_day, _ = stack.pop() # temp 값은 더 이상 필요 없으므로 '_' 처리
            answer[prev_day] = cur_day - prev_day

        stack.append((cur_day, cur_temp))

    return answer

print(temperature_days([73, 74, 75, 71, 69, 72, 76, 73]))