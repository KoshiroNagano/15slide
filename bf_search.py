# -*- coding: utf-8 -*-
# python 3.6.7

import sys
import heapq
import math

def best_first_search():
    stdin = input("Please type the number of initial state : ")
    if stdin == "1" :
        field = ["1","2","3","4","5","6","7","8","9","11","14","*","13","10","15","12"]
        
    if stdin == "2" :
        field = ["14","2","3","4","5","8","7","6","9","12","*","11","13","1","15","10"]
    L = int(math.sqrt(len(field)))
    # for line in sys.stdin:
    #     sp = line.split()
    #     L = len(sp)
    #     field += sp


    cur = field.index('*')

    #移動可能な場所を列挙
    RIGHT, LEFT, DOWN, UP = [1, -1, L, -L]
    move = []
    for i in range(L * L):
        temp = []
        if i % L != L - 1:
            temp.append(RIGHT)
        if i % L != 0:
            temp.append(LEFT)
        if i // L != L - 1:
            temp.append(DOWN)
        if i // L != 0:
            temp.append(UP)
        move.append(temp)

    END = list(map(str, range(1, L * L))) + ['*']

    #マンハッタン距離を計算
    md = 0
    for i, n in enumerate(field):
        n = int(n) if n != '*' else L * L
        ox = (n - 1) % L
        oy = (n - 1) / L
        x = i % L
        y = i / L
        md += abs(ox - x) + abs(oy - y)
    # print(md)
    q = []
    heapq.heappush(q, (2.5 * md, md, 0, field[::], cur, 0, []))

    visited = set([tuple(field)])

    for i in range(10**8):
        if not q:
            break   
        cost_est, md, cost, state, cur, last, history = heapq.heappop(q)
        item = [t for t in [cost_est, md, cost, state, cur, last, history]]
        for d in move[cur]:
            #直前の状態に逆戻りしない
            if d == -last:
                continue
            
            temp = state[::]
            #交換する
            temp[cur], temp[cur + d] = temp[cur + d], temp[cur]
            #マンハッタン距離の差分を計算
            md_diff = 0
            for i, n in [(cur, temp[cur]), (cur + d, temp[cur + d])]:
                n = int(n) if n != '*' else L * L
                ox = (n - 1) % L
                oy = (n - 1) / L
                x = i % L
                y = i / L
                md_diff += abs(ox - x) + abs(oy - y)
            for i, n in [(cur, temp[cur + d]), (cur + d, temp[cur])]:
                n = int(n) if n != '*' else L * L
                ox = (n - 1) % L
                oy = (n - 1) / L
                x = i % L
                y = i / L
                md_diff -= abs(ox - x) + abs(oy - y)
            #終了確認
            key = tuple(temp)
            if temp == END:
                # print (state)
                num = [int(i) for i in history + [temp[cur]]]
                return num
            #訪問済みかどうかを確認
            if key in visited or cost + 1 + md + md_diff > 1000:
                continue
            else:
                visited.add(key)
            heapq.heappush(q, (cost + 1 + 2.5 * (md + md_diff), md + md_diff, cost + 1, temp, cur + d, d, history + [temp[cur]]))

        else:
            continue
        break
if __name__ == "__main__":
    pass
#     num_list = best_first_search()
#     print(num_list)