import sys
def prim(graph,n):
    '''
    prim算法求最小生成树
    :param graph: 图
    :return: 最小的权值
    :n:点的个数
    '''
    lowcost = [] #记录当前顶点集合到剩下的点的最低权值，“-1”表示已访问过的点，无需访问
    mst = [] #记录当前被更新的最低权值来自于哪个点，相当于记录是边的起始点，lowcost的下标表示的是最低权值的终止点
    cost = 0 #记录整个最小生成树的权值
    for i in range(n): #初始化lowcost与mst，默认先选择第0个点，把第0个点到其余所有点的权值赋给lowcost，mst内全部赋值为0（也就是第0个点为起始）
        lowcost.append(graph[0][i])
        mst.append(0)
    v = 0 #记录当前被选择的点
    lowcost[0] = -1 #用“-1"来标记被选择的点，
    for i in range(n-1):
        min = sys.maxsize #初始为最大值，作用是记录当前最低权值
        for j in range(n):
            if(min > lowcost[j] and lowcost[j] != -1):
                min = lowcost[j]
                v = j
        cost += min
        print(traver(mst[v]),"->",traver(v),": ",min)
        lowcost[v] = -1 #用”-1“标记被选择的点
        for k in range(n): #更新lowcost
            if(lowcost[k] > graph[v][k]):
                lowcost[k] = graph[v][k]
                mst[k] = v #如果有被更新的权值，就把当前点作为被更新权值的那条边的起始点

    return cost

def traver(x):
    '''
    把数字转换为字母
    只使用与26个小写字母
    :param x: 待转换数字
    :return: 字母
    '''
    return chr(x+97)


if __name__=='__main__':
    MAX = sys.maxsize
  
    graph = [[MAX,6,1,5,MAX,MAX],
             [6,MAX,5,MAX,3,MAX],
             [1,5,MAX,5,6,4],
             [5,MAX,5,MAX,MAX,2],
             [MAX,3,6,MAX,MAX,6],
             [MAX,MAX,4,2,6,MAX]]
    
    print(prim(graph,len(graph)))
