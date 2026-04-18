for _ in range(4):
    q_scores = [float(x) for x in input().split()]
    qAVG = (sum(q_scores))/3

    neededFinalScore = (90-(qAVG*0.75))*4
    neededFinalScore = round(neededFinalScore, 2)

    neededFinalScoreStr = str(neededFinalScore)
    dotpos = neededFinalScoreStr.index(".")

    if dotpos == (len(neededFinalScoreStr) - 2):
        neededFinalScoreStr = neededFinalScoreStr + "0"
    print(neededFinalScoreStr)