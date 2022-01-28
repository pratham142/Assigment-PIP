Python 3.11.0a1 (tags/v3.11.0a1:7c12e48, Oct  5 2021, 15:38:19) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
if __name__ == '__main__':
    k = int(input())
    arr = map(int, input().split())
    print(sorted(list(set(arr)))[-2])

5
2 3 6 6 5
5
