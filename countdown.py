import time

def countdown(tim):

    while tim:
        mins, secs = divmod(tim, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end='\r')
        time.sleep(1)
        tim -= 1

    print('Timer completed')


tim = input('Enter the time in seconsds: ')

countdown(int(tim))


if __name__ == '__main__':
    pass