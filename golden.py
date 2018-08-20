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
    return 50*0.618, 50*0.618

def main():
    read()
    ret = calculate()
    print(ret[0], ret[1], end='\t')

if __name__ == "__main__":
    main()


