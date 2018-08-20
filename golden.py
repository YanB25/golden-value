from random import *
history = []
def read():
    line, cnt = input().split('    ') # 读第一行的两个数字
    line, cnt = (int(line), int(cnt))
    for _ in range(line):
        goldValue, *playerValues = input().strip().split('\t') # 读第i行的内容
        history.append({
            'goldValue': float(goldValue),
            'playValues': list(map((lambda x:float(x)), playerValues))
            })
        #print(history)
def show():
    print(history)

def calculate():
    acculateValue = 0
    alpha = 0.8
    for idx, historyData in enumerate(history):
        gv = historyData['goldValue']
        acculateValue = acculateValue * (1-alpha) + gv * alpha
    if (abs(history[-1]['goldValue']-history[-2]['goldValue'] <= 1)) or random() <= 0.25:
        err = random() * 10 + 85
        return err, acculateValue + err/46*0.618
    else:
        return acculateValue, acculateValue

def main():
    try:
        read()
        ret = calculate()
        print('{:f}\t{:f}'.format(ret[0], ret[1]))
    except:
        print('{:f}\t{:f}'.format(random() * 3 + 20, random()*5 + 20))



if __name__ == "__main__":
    main()


