# 標準入力に使うコードのメモ

# 一番良くある形　基本これを採択する
# sys.stdin.readline()
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

# 文字列を1行入力
s = input()

# 整数を1行から1つ入力
n = int(input())

# 1行内 スペース区切りの文字列を個別の変数に入力
a, b, c = input().split()

# 1行内 スペース区切りの整数を個別の変数に入力
x, y, z = map(int, input().split())

# 1行内のスペース区切りの文字列をリストへ入力
l = input().split()

# 1行内のスペース区切りの整数をリストへ入力
l = list(map(int, input().split()))

# 改行区切りの複数行の文字列をリストに入力
l = [input() for _ in range(N)]

# 改行区切りの複数行の整数をリストに入力
l = [int(input()) for _ in range(N)]

# 区切り文字を指定して入力を受け取る
m, d = map(int, input().split("/"))
