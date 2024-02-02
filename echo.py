#echo.py

def echo(text: str, repetitions: int = 3) -> str:
    result = text + " \n" + text[-3:] + " \n" + text[-2:] + " \n" + text[-1:] + " \n"
    return result
                             

if __name__ == "__main__":
    text = input("Yell something at a mountain:")
    print(echo(text))