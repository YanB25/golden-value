history = []
def read():
    line, cnt = input().split('    ')
    line, cnt = (int(line), int(cnt))
    for _ in range(line):
        goldValue, *playerValues = input().strip().split('\t')
        history.append({
            'goldValue': float(goldValue),
            'playValues': list(map((lambda x:float(x)), playerValues))
            })
        #print(history)
def show():
    print(history)

def main():
    read()
    show()

if __name__ == "__main__":
    main()


