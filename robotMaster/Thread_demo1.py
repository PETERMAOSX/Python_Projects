import threading
from time import sleep,ctime

loops=[1,2,3,4]

class ThreadFunc(object):
    def __init__(self,func,args,name=''):
        self.name=name
        self.func = func
        self.args=args
        
    def __call__(self):
        self.func(*self.args)
        
def loop(nloop,nsec):
    print('开始循环',nloop,'在：'+str(ctime()))
    sleep(nsec)
    print('结束循环',nloop,'于：'+str(ctime()))
def main():
    print('程序开始于：'+str(ctime()))
    threads = []
    nloops = range(len(loops))
    
    for i in nloops:
        t = threading.Thread(target=ThreadFunc(loop,(i,loops[i]),loop.__name__)) #传递一个可调用类的实例
        threads.append(t)
        
    for i in nloops:
        threads[i].start()  #开始所有的线程
        
    for i in nloops:
        threads[i].join()   #等待所有的线程执行完毕
        
    print('任务完成于：'+str(ctime()))
    
if __name__=='__main__':
    main()