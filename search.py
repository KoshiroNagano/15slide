# -*- coding: utf-8 -*-
# python 3.6.7

import sys
import heapq
import math

''' a*search '''

def a_search (init_list):
    
    field = list(map(str, init_list))
    L = int(math.sqrt(len(field)))

    cur = field.index('0')

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

    END = list(map(str, range(1, L * L))) + ['0']

    #マンハッタン距離を計算
    md = 0
    for i, n in enumerate(field):
        n = int(n) if n != '0' else L * L
        ox = (n - 1) % L
        oy = (n - 1) / L
        x = i % L
        y = i / L
        md += abs(ox - x) + abs(oy - y)
    # print(md)
    q = []
    # heapq.heappush(q, (2.5 * md, md, 0, field[::], cur, 0, []))
    heapq.heappush(q, (md, md, 0, field[::], cur, 0, []))
    visited = set([tuple(field)])

    for i in range(10**8):
        if not q:
            break   
        cost_est, md, cost, state, cur, last, history = heapq.heappop(q)
        item = [t for t in [cost_est, md, cost, state, cur, last, history]]
        # print("=="*20)
        # print(tuple(item))
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
                n = int(n) if n != '0' else L * L
                ox = (n - 1) % L
                oy = (n - 1) / L
                x = i % L
                y = i / L
                md_diff += abs(ox - x) + abs(oy - y)
            for i, n in [(cur, temp[cur + d]), (cur + d, temp[cur])]:
                n = int(n) if n != '0' else L * L
                ox = (n - 1) % L
                oy = (n - 1) / L
                x = i % L
                y = i / L
                md_diff -= abs(ox - x) + abs(oy - y)
            #終了確認
            key = tuple(temp)
            if temp == END:
                num = [int(i) for i in history + [temp[cur]]]
                return num 
            #訪問済みかどうかを確認
            if key in visited or cost + 1 + md + md_diff > 1000:
                continue
            else:
                visited.add(key)
            # heapq.heappush(q, (cost + 1 + 2.5 * (md + md_diff), md + md_diff, cost + 1, temp, cur + d, d, history + [temp[cur]]))
            heapq.heappush(q, (cost + 1 + (md + md_diff), md + md_diff, cost + 1, temp, cur + d, d, history + [temp[cur]]))
            # print(item)
        else:
            continue
        break
# if __name__ == "__main__":
#     pass
#     # num_list, panele_list = a_search ()
#     # print(num_list, panele_list)