# -*- coding: utf-8 -*-
# python 3.6.7
import math

'''TODO: Breadth First Search '''

class Queue:
    '''
    パズルオブジェクトを格納するキュークラス
    '''
    def __init__(self, puzzle):
        self.puzzle_list = []

        self.puzzle_list.append(puzzle)

    # パズルをリストの末端に追加
    def enqueue(self, puzzle):
        self.puzzle_list.append(puzzle)

    # パズルをリストの先頭から取得
    def dequeue(self):
        return self.puzzle_list.pop(0)

    # パズルリストが空かチェック
    def is_empty(self):
        return len(self.puzzle_list) == 0


class Puzzle:
    '''
    現在のパネル配置、チェックしたパネル配置のリスト、パズルのサイズを持つパズルクラス
    '''
    def __init__(self, panel_list, state_list, size):
        self.panel_list = panel_list

        # 自身が通過してきたパネル配置の状態を保持しておくリスト
        self.state_list = state_list
        self.state_list.append(panel_list)

        self.size = size

    # パネルの0を左右上下に移動させたときのパネル配置を返すジェネレーター
    def gene_next_panel(self, puzzle):
        zero_pos = puzzle.panel_list.index(0)

        col = zero_pos // self.size
        raw = zero_pos % self.size

        def __get_next_panel():
            panel_list = puzzle.panel_list[:]
            n = panel_list[next_pos]
            panel_list[next_pos] = 0
            panel_list[zero_pos] = n
            return panel_list

        if self.size > col + 1:
            next_pos = (col + 1) * self.size + raw
            panel_list = __get_next_panel()
            yield tuple(panel_list)

        if col - 1 >= 0:
            next_pos = (col - 1) * self.size + raw
            panel_list = __get_next_panel()
            yield tuple(panel_list)

        if self.size > raw + 1:
            next_pos = col * self.size + raw + 1
            panel_list = __get_next_panel()
            yield tuple(panel_list)

        if raw - 1 >= 0:
            next_pos = col * self.size + raw - 1
            panel_list = __get_next_panel()
            yield tuple(panel_list)

    def result_print(self):

        for s in self.state_list:
            print(s)

def breadth_first(size, goal, panel_list):
    puzzle = Puzzle(panel_list, [], size)
    queue = Queue(puzzle)
    checked_dict = {}

    while queue.is_empty() is False:
        puzzle = queue.dequeue()

        for next_panel in puzzle.gene_next_panel(puzzle):
            next_puzzle = Puzzle(list(next_panel), puzzle.state_list[:], size)

            if next_panel in checked_dict:
                continue

            if list(next_panel) == goal:
                return next_puzzle

            # 出現済みのパネル配置を記録
            checked_dict[next_panel] = True
            queue.enqueue(next_puzzle)

if __name__ == '__main__':
    
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
    size = int(math.sqrt(len(goal)))
    stdin = input("Please type the number of initial state : ")
    if stdin == "1" :
        panel_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 14, 0, 13, 10, 15, 12]
    if stdin == "2" :
        panel_list = [2, 10, 3, 4, 1, 14, 6, 7, 5, 0, 11, 8, 9, 13, 15, 12]
    if stdin == "3" :
        panel_list = [14, 3, 6, 4, 10, 2, 11, 7, 1, 5, 15, 8, 9, 13, 0, 12]
    if stdin == "4" :
        panel_list = [14, 3, 11, 6, 10, 15, 5, 4, 13, 9, 2, 7, 1, 12, 8, 0]



    puzzle = breadth_first(size, goal, panel_list)

    puzzle.result_print()