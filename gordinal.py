ricxoci = ['ერთი', 'ორი', 'სამი', 'ოთხი', 'ხუთი', 'ექვსი', 'შვიდი', 'რვა', 'ცხრა', 'ათი', 'თერთმეტი',
'თორმეტი', 'ცამეტი', 'თოთხმეტი', 'თხუთმეტი', 'თექვსმეტი', 'ჩვიდმეტი', 'თვრამეტი', 'ცხრამეტი']

K = 1000

M = 1000000

G = 1000000000

T = G * 1000

def togordinal(x):
    if x == 20:
        return 'ოცი'
    elif x == 40:
        return 'ორმოცი'
    elif x == 60:
        return 'სამოცი'
    elif x == 80:
        return 'ოთხმოცი'
    elif x == 100:
        return 'ასი'
    elif x == K:
        return 'ათასი'
    elif x == M:
        return 'მილიონი'
    elif x == G:
        return 'მილიარდი'  
    elif x == T:
        return 'ტრილიონი'     
    elif x in range(20):
        return ricxoci[x-1]                        
    elif x > 20 and 100 > x:                      
        if x // 20 == 1:
            y = x - (x//20)*20
            return 'ოცდა'+ricxoci[y-1]
        if x // 20 == 2:
            y = x - (x//20)*20
            return 'ორმოცდა'+ricxoci[y-1]
        if x // 20 == 3:
            y = x - (x//20)*20
            return 'სამოცდა'+ricxoci[y-1]
        if x // 20 == 4:
            y = x - (x//20)*20
            return 'ოთხმოცდა'+ricxoci[y-1]
    elif x >= 100 and K > x:
        z = x // 100
        y = x - 100*z
        if z == 1:
            return 'ას'+togordinal(y)
        else:
            return togordinal(z)[:-1]+'ას'+togordinal(y)    
    elif x > K and x < M:
        z = x // K
        y = x - K*z
        if z == 1:
            return 'ათას'+togordinal(y)
        else:
            return togordinal(z)+'ათას'+togordinal(y)
    elif x > M and x <G:
        z = x // M
        y = x - M*z
        if z == 1:
            return 'მილიონ'+togordinal(y)
        else:
            return togordinal(z)+'მილიონ'+togordinal(y) 
    elif x > G and x < T:
        z = x // G
        y = x - G*z
        if z == 1:
            return 'მილიარდ'+togordinal(y)
        else:
            return togordinal(z)+'მილიარდ'+togordinal(y)
    elif x > T and x < 1000*T:
        z = x // T
        y = x - T*z
        if z == 1:
            return 'ტრილიონ'+togordinal(y)
        else:
            return togordinal(z)+'მილიარდ'+togordinal(y)  
    else:
        return 'უსახელო'
