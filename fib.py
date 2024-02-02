from functools import lru_cache
import time
import matplotlib.pyplot as plt

times = []

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        execution_time = end - start
        times.append((args[0], execution_time))
        final_time = f"{end - start:0.099f}"
        print(f"Finished in {final_time}s: f({args[0]}) -> {result}")
        return result
    return wrapper

@lru_cache(maxsize=None)
@timer
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    fib(480)

    x_axis, y_axis = zip(*times)
    plt.plot(x_axis, y_axis)
    plt.title("Fibonacci Sequence Time Complexity")
    plt.xlabel("n")
    plt.ylabel("Time (seconds)")
    plt.show()