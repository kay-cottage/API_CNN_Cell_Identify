# API_CNN_Cell_Identify
基于Flask构造的的CNN卷积神经网络细胞形态学识别API接口


为个人想法的简单实现，旨在让更多人方便的用上AI技术。


第一个Github小项目，不喜勿喷！


注意：禁止用于商业用途，欢迎个人学习交流！


**原理**

1.首先，客户端把需要的识别的图像截取出来通过POST请求发送到服务器端


2.服务器端在收到客户端的请求后，把事先训练好的模型与需要识别的图像一同加载进预测函数中，然后将与测识别的结果返回给客户端

**使用**

服务器端：下载相应的库。新建好意额文件夹，将模型文件cell_finder.h5与API_server.py放在同一个文件夹中，然后将其部署到服务器端启动。

客户端：启动客户端API_Client.py，将需要识别的细胞图像保存（尽可能只保留需要识别的细胞）正确输入服务器端URL（例如http://192.168.31.31:5000/)，等待服务器返回识别结果！

返回Python字典数据类型



