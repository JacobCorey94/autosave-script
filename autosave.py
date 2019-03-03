import SendKeys
import time

def main():
    while True:
        time.sleep(300)
        SendKeys.SendKeys("^(s)")

main()