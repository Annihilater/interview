package test;

import java.util.*;

/*
 * 华容道广度优先搜索解法
 * 只能找出最佳路径
 * */
class HuaRongDao {
    //方向定义
    private static final int UP = 0;
    private static final int DOWN = 1;
    private static final int LEFT = 2;
    private static final int RIGHT = 3;
    //终点状态定义
    private static final Integer WIN_STATE = 123456780;
    /* 定义辅助数组
    二维数组，相当于dxdy[4][2],四个数对代表四个方向，方向数值与二维数组第一维相对应，
    dxdy[0][0] = -1;dxdy[0][1] = 0;dxdy[1][0] = 1;dxdy[1][1] = 0 ........
    */
    private static final int[][] dxdy = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    // 3x3的九宫格
    private int[][] arr;

    // 记录空格的位置
    private int x;
    private int y;

    // 定义移动的数组
    private List<Integer> moveArr = new LinkedList<>();
    // 保存已经搜索过的状态
    private Set<Integer> statusSet = new HashSet<>();


    // 代表广搜的每一步，通过lastItem链起来,记录每一步的状态和移动方向并保存上一步的同样的信息
    private class SearchItem {
        private Integer status;
        private Integer dir;
        private SearchItem lastItem;

        SearchItem(Integer status, Integer dir, SearchItem lastItem) {
            this.status = status;
            this.dir = dir;
            this.lastItem = lastItem;
        }

        Integer getStatus() {
            return status;
        }

        Integer getDir() {
            return dir;
        }

        SearchItem getLastItem() {
            return lastItem;
        }
    }

    // 广搜的存储队列
    private List<SearchItem> statusToSearch = new LinkedList<SearchItem>();

    //给定华容道初始值，并遍历找出空格位置(构造方法)
    HuaRongDao() {
        arr = new int[3][3];
        System.out.println("请按照顺序依次输入3*3华容道初始值（0到8且数字不可重复）: ");
        Scanner sc = new Scanner(System.in);
        //键盘录入华容道初始值，对重复录入进行判断，并记录空格位置
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length; j++) {
                arr[i][j] = sc.nextInt();
                //检验是否重复输入
                for (int l = 0; l <= i; l++) {
                    for (int m = 0; m < j; m++) {     //检验到前一个
                        if (arr[l][m] == arr[i][j]) {
                            System.out.println("输入重复,请重新输入\n");
                            arr[i][j] = sc.nextInt();
                        }
                    }
                    //记录空格位置
                    if (arr[i][j] == 0) {
                        x = i;
                        y = j;
                    }
                }

            }
        }
    }

    // 判断是否可以朝某个方向进行移动
    private boolean canMove(int direction) {
        switch (direction) {
            // y > 0才能左移
            case LEFT:
                return y > 0;
            // y < 2才能右移
            case RIGHT:
                return y < 2;
            // x > 0才能上移
            case UP:
                return x > 0;
            // x < 2才能下移
            case DOWN:
                return x < 2;
        }
        return false;
    }

    // 找出该方向的相反方向
    private int getBackDir(int direction) {
        switch (direction) {
            // y > 0才能左移
            case LEFT:
                return RIGHT;
            // y < 2才能右移
            case RIGHT:
                return LEFT;
            // x > 0才能上移
            case UP:
                return DOWN;
            // x < 2才能下移
            case DOWN:
                return UP;
        }
        return 0;
    }

    // 朝某个方向进行移动，该函数不作判断，直接移动
    // 调用前请自行用canMove先行判断
    private void move(int direction) {
        int temp;
        temp = arr[x + dxdy[direction][0]][y + dxdy[direction][1]];   //方向与第一维数组位置相对应，该位置的数对代表x和y值相应变化，通过加法来实现。注意区分数组位置的0,1,2,3和方向数值的0,1，2,3
        arr[x + dxdy[direction][0]][y + dxdy[direction][1]] = 0;      //也可用 arr[x + dxdy[direction][0]][y + dxdy[direction][1]] = arr[x][y]
        arr[x][y] = temp;
        x = x + dxdy[direction][0];
        y = y + dxdy[direction][1];
    }

    // 某个方向的前进，该函数不作判断，直接移动
    private void moveForward(int direction) {
        move(direction);
        // 该方向记录
        //moveArr.add(direction);                 //步骤记录已经由item记录了，这步看不出有什么意义？？？
    }

    // 某个方向的回退，该函数不作判断，直接移动
    // 其操作和moveForward方法正好相反
    private void moveBack(int direction) {
        move(getBackDir(direction));
        // 记录的移动步骤出栈
        //moveArr.remove(moveArr.size() - 1);      //步骤记录已经由item记录了，这步看不出有什么意义？？？
    }

    // 获取状态，这里把9个数字按顺序组成一个整数来代表状态
    // 方法不唯一，只要能区分九宫格状态就行
    private Integer getStatus() {
        int status = 0;
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length; j++) {
                status = status * 10 + arr[i][j];
            }
        }
        return status;
    }

    // 根据状态还原九宫格数组
    // 该方法是getStatus的逆过程，感觉没必要用这个方法
    private void recoverStatus(Integer status) {
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length; j++) {
                arr[2 - i][2 - j] = status % 10;   //逆序赋值，除法取余数
                status = status / 10;       // 除法取整
            }
        }
        getXY();
    }

    // 获取空格的x和y坐标
    private void getXY() {
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length; j++) {
                if (arr[i][j] == 0) {
                    x = i;
                    y = j;
                }
            }
        }
    }

    // 搜索方法
    private void search() {
        // 如果还有要搜索的状态
        while (statusToSearch.size() > 0) {
            // 队首出列
            SearchItem item = statusToSearch.remove(0);
            Integer status = item.getStatus();
            // 搜到了
            if (status.equals(WIN_STATE)) {
                // 找到路径
                recordRoute(item);
                printRoute();
                return;
            }
            // 根据status还原arr和x，y，不过感觉不到这个方法的意义，画蛇添足
            recoverStatus(status);
            // 4个方向进行遍历
            for (int i = 0; i < 4; i++) {
                // 如果能够朝该方向行走
                if (canMove(i)) {
                    // 向前一步
                    moveForward(i);
                    status = getStatus();

                    // 之前搜过的状态
                    if (statusSet.contains(status)) {
                        moveBack(i);
                        // 放弃
                        continue;   //跳出本次循环，并开始执行下次循环
                    }
                    // 新状态加入待搜索
                    statusSet.add(status);
                    statusToSearch.add(new SearchItem(status, i, item));  //每一步存储节点的信息包含本步的状态以及上一步的节点信息
                    moveBack(i);
                }
            }
        }
    }


    // 根据链表顺藤摸瓜，找到路径
    private void recordRoute(SearchItem item) {
        while (null != item.getLastItem()) {
            moveArr.add(0, item.getDir());
            item = item.getLastItem();
        }
    }

    // 打印路径
    private void printRoute() {
        for (int i = 0; i < moveArr.size(); i++) {
            System.out.print(getDirString(moveArr.get(i)));
            System.out.print(" ");
        }
    }

    // 方向与其对应的字符串
    private String getDirString(int dir) {
        switch (dir) {
            case LEFT:
                return "左";
            case RIGHT:
                return "右";
            case UP:
                return "上";
            case DOWN:
                return "下";
        }
        return null;
    }

    // 打印当前华容道的状态
    private void print() {
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length; j++) {
                System.out.print(arr[i][j]);
                System.out.print(" ");
            }
            System.out.println();
        }
    }

    // 解题入口方法
    void solve() {
        Integer status = getStatus();
        // 如果已经是胜利状态，返回true
        if (WIN_STATE.equals(status)) {
            return;
        }
        // 初始状态先记录
        statusSet.add(status);
        // 初始状态进入搜索队列
        statusToSearch.add(new SearchItem(status, null, null));
        search();
    }
}

class TsetHuaRongDao {
    public static void main(String[] args) {
        long startTime = System.currentTimeMillis(); //获取开始时间
        HuaRongDao hrd = new HuaRongDao();
        hrd.solve();
        long endTime = System.currentTimeMillis(); //获取结束时间
        long spendTime = endTime - startTime;
        System.out.println("程序运行时间：" + spendTime + "ms"); //输出程序运行时间
    }
}
