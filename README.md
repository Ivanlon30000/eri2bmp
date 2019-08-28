# eri2bmp
## 描述 Description
转换.eri文件为.bmp文件. (Convert .eri files to .bmp files.)

## 用法 Usage
1. 下载 ericvt.exe . (Download ericvt.exe)  
[下载地址(Download page)](http://www.entis.jp/eridev/download/index.html)

2. 创建 ```Eri2Bmp``` 类并调用成员函数 ```eris2bmps```. (Instantiate class ```Eri2Bmp``` and invoke method ```eris2bmps```)
```python
#####

if __name__ == '__main__':
    src_folder = r"eri文件所在位置(where your .eri files locate)"     # 例: src_folder = r"D:\Downloads\ev"
    dst_folder = r"输出文件夹(output folder)"        # 例: dst_folder = r"D:\output\4"
    cvter = r"ericvt.exe文件路径(ericvt.exe file path)"   # 例: cvter = r"D:\Downloads\ericvt\ericvt.exe"

    e2b = Eri2Bmp(cvter, log=None)
    e2b.eris2bmps(src_folder, dst_folder, workers=4)
```

## 其他说明 Other Information
+ 构造函数参数 ```log``` (param ```log```)
参数 ```log``` 是 .log 文件的路径.  (The param ```log``` defines the path of the .log file.)  
```log``` 的缺省值是(The default vaule of ```log```): ```"Eri2Bmp_{}.log".format(time.strftime("%Y_%m_%d_%H_%M_%S"))```. 

+ 成员函数 ```eris2bmps``` 的参数 ```workers``` (The param ```workers``` of method ```eris2bmps```)  
使用线程池 ```ThreadPoolExecutor``` 实现的多线程, ```workers``` 是最大线程. (Multithread implemented with ```ThreadPoolExecutor```, where ```workers``` is the largest threads)
