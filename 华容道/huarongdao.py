#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/11/13 20:49
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : huarongdao.py
import time


class SearchItem:
    """
    搜索节点
    """

    def __init__(self, status=None, dir=None, last_item=None):
        self.status = status
        self.dir = dir
        self.last_item = last_item
        self.next = None

    def get_status(self): return self.status

    def get_dir(self): return self.dir

    def get_last_item(self): return self.last_item

    def get_next(self): return self.next

    def set_next(self, node): self.next = node


class HuaRongDao2:
    def __init__(self):
        self.up = 0  # 向上
        self.down = 1  # 向下
        self.left = 2  # 向左
        self.right = 3  # 向右

        self.win_state = '123456780'  # 胜利的状态

        self.dxdy = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 辅助方向数组
        self.arr = [[]]

        self.x = 0  # 空格所在 x 坐标
        self.y = 0  # 空格所在 y 坐标

        self.move_arr = []  # 移动方向记录
        self.status_set = set()  # 保存已经搜索过的状态
        self.status = []  # 当前状态
        self.status_to_search = []  # 广搜储存队列

    def huarongdao2(self, data):
        """
        初始状态输入
        :param data:初始状态
        :return:
        """
        # print('请按照顺序依次输入3*3华容道初始值（0到8且数字不可重复）: ')
        # data = input()
        self.show_status(data, 0)
        l = []
        for item in data:
            l.append(int(item))

        arr = []
        tmp1 = []
        tmp2 = []
        tmp3 = []
        for m in range(0, 3):
            tmp1.append(l[m])
        for m in range(3, 6):
            tmp2.append(l[m])
        for m in range(6, 9):
            tmp3.append(l[m])
        arr.append(tmp1)
        arr.append(tmp2)
        arr.append(tmp3)
        self.arr = arr

        for i in range(len(self.arr)):
            for j in range(len(self.arr[0])):
                if self.arr[i][j] == 0:
                    self.x = i
                    self.y = j

    def can_move(self, direction):
        """
        判断 direction 方向能不能前进
        :param direction: 方向
        :return:
        """
        if direction == self.left:
            return self.y > 0
        elif direction == self.right:
            return self.y < 2
        elif direction == self.up:
            return self.x > 0
        elif direction == self.down:
            return self.x < 2
        else:
            return False

    def get_back_dir(self, direction):
        """
        往 direction 方向后退一步
        :param direction: 方向
        :return:
        """
        if direction == self.left:
            return self.right
        elif direction == self.right:
            return self.left
        elif direction == self.up:
            return self.down
        elif direction == self.down:
            return self.up
        else:
            return False

    def move(self, direction):
        """
        往 direction 方向移动一步
        :param direction: 方向
        :return:
        """
        self.arr[self.x + self.dxdy[direction][0]][self.y + self.dxdy[direction][1]], self.arr[self.x][self.y] = \
            self.arr[self.x][self.y], self.arr[self.x + self.dxdy[direction][0]][self.y + self.dxdy[direction][1]]

        self.x = self.x + self.dxdy[direction][0]
        self.y = self.y + self.dxdy[direction][1]

    def move_forward(self, direction):
        """
        往 direction 方向前进一步
        :param direction: 方向
        :return:
        """
        self.move(direction)

    def move_back(self, direction):
        """
        往 direction 方向退一步, 操作对应前进一步
        :param direction: 方向
        :return:
        """
        self.move(self.get_back_dir(direction))

    def get_status(self):
        """
        获取当前状态
        :return:
        """
        status = ''
        for i in range(len(self.arr)):
            for j in range(len(self.arr[0])):
                x = self.arr[i][j]
                status += str(x)
        return status

    def get_x_y(self):
        """
        获取当前状态下，空格所在位置的 x, y 坐标
        :return:
        """
        for i in range(3):
            for j in range(3):
                if self.arr[i][j] == 0:
                    self.x = i
                    self.y = j

    def recover_status(self, status):
        """
        让 self.arr 恢复到 status 表示的状态
        :param status:状态
        :return:
        """
        for i in range(len(self.arr)):
            for j in range(len(self.arr[0])):
                self.arr[i][j] = int(status[i * 3 + j])

        self.get_x_y()

    def record_route(self, item):
        """
        1. 清空 self.move_arr
        2. 从 item 链表内取出路径
        3. 存放到 self.move_arr 里
        :param item:
        :return:
        """
        self.move_arr = []  # 每次调用的时候清空一次路径记录
        while item.get_last_item():  # 从 item 链表里取每一步的方向，因为是倒序取的，所以取出来也是倒序的
            self.move_arr.append(item.dir)
            item = item.get_last_item()
        self.move_arr = self.move_arr[::-1]  # 做一次倒序，将路径调整为顺序

    def print_route(self):
        """
        转换方向表达方式
        将数字表示的方向，以中文方式打印出来
        :return:
        """
        for dir in self.move_arr:
            print(self.get_dir_string(dir), end=' ')

    def get_dir_string(self, dir):
        """
        数字转中文
        :param dir:
        :return:
        """
        if dir == self.left:
            return '左'
        elif dir == self.right:
            return '右'
        elif dir == self.up:
            return '上'
        elif dir == self.down:
            return '下'
        else:
            return False

    def print(self):
        for i in range(3):
            for j in range(3):
                print(self.arr[i][j])

    @staticmethod
    def show_status(status, offset):
        """
        以 3 x 3 表格的方式打印状态
        :param status: 状态
        :param offset: 显示的偏移量
        :return:
        """
        data = status
        print('当前的状态为: ')
        for i in [0, 3, 6]:
            print(' ' * offset + '{}  {}  {}'.format(data[i], data[i + 1], data[i + 2]))

    def show_dir(self, dir):
        """
        打印方向
        :param dir: 方向
        :return:
        """
        if dir == self.up:
            print(f'方向: 上')
        elif dir == self.down:
            print(f'方向: 下')
        elif dir == self.left:
            print(f'方向: 左')
        elif dir == self.right:
            print(f'方向: 右')
        else:
            print('方向不正确')

    def search(self):
        while self.status_to_search:
            item = self.status_to_search.pop(0)  # 取出队列首位
            status = item.status

            # print('-------------------------------------------------------------------------------------')
            # self.record_route(item)  # 记录下到这个状态的路径
            # self.print_route()
            # print('\t')
            if len(self.move_arr) > 100:  # 如果移动步数大于 1000 则舍弃这个状态，换个状态继续搜索
                continue
            # self.show_status(status, 0)   # 3x3 表格形式显示状态

            if status == self.win_state:
                print('可以胜利, 胜利路径如下: ')
                self.record_route(item)
                self.print_route()
                return

            self.recover_status(status)

            # print('四个方向: ')
            for dir in range(4):  # 4 个方向遍历
                if self.can_move(dir):
                    self.move_forward(dir)
                    status = self.get_status()

                    if status in self.status_set:
                        self.move_back(dir)
                        continue

                    self.status_set.add(status)
                    _item = SearchItem(status, dir, item)
                    self.status_to_search.append(_item)

                    # self.show_dir(dir)    # 显示当前方向
                    # self.show_status(status, 9)   # 以 3x3 表格方式显示状态
                    self.move_back(dir)
        print('无法取得胜利')

    def solve(self):
        status = self.get_status()
        if status == self.win_state:
            return
        self.status_set.add(status)
        self.status_to_search.append(SearchItem(status))
        self.search()


if __name__ == '__main__':
    sc = '341560827'  # 左 左 上 右 下 左 下 右 右 上 左 上 右 下 左 左 下 右 上 左 上 右 下 右 下
    # sc = '413705826'    # 下 左 上 上 右 下 右 下
    # sc = '013425786'    # 右 下 右 下

    start = time.perf_counter()
    hrd = HuaRongDao2()
    hrd.huarongdao2(sc)
    hrd.solve()
    print(time.perf_counter() - start)
