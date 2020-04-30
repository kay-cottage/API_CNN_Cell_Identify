# coding:utf-8
import time
from tensorflow.keras.models import load_model
import matplotlib.image as processimage
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from flask import Flask
import os
import json
from flask import request



app = Flask(__name__)
app.config['DEBUG'] = True



class Prediction(object):
    def __init__(self, ModelFile, PredictFile, CellType, Width=100, Height=100):
        self.modelfile = ModelFile
        self.predict_file = PredictFile
        self.Width = Width
        self.Height = Height
        self.CellType = CellType
    
    
    def Predict(self):
        model = load_model(self.modelfile)
        img_open = Image.open(self.predict_file)
        conv_RGB = img_open.convert('RGB')
        new_img = conv_RGB.resize((self.Width, self.Height), Image.BILINEAR)
        new_img.save(self.predict_file)
        #print('Image Processed')
        image = processimage.imread(self.predict_file)
        image_to_array = np.array(image) / 255.0
        image_to_array = image_to_array.reshape(-1, 100, 100, 3)
        #print('Image reshaped')
        prediction = model.predict(image_to_array)
        print(prediction)
        Final_prediction = [result.argmax() for result in prediction][0]
        print(Final_prediction)

       
        #生成预测结果json文件
        CellType = ['嗜酸性粒细胞', '嗜碱性粒细胞', '中性粒细胞', '空']
        probability = []
        count = 0
        for i in prediction[0]:
            percentage = '%.2f%%' % (i * 100)
            probability.append(percentage)
            count += 1
        print(probability)
        global dic2
        dic2 = dict(zip(DogType, probability))
        print(dic2)
        return json.dumps(dic2)

    
    
    def ShowPredImg(self):
        image = processimage.imread(self.predict_file)
        plt.imshow(image)
        plt.show()






def main():
    CellType = ['嗜酸性粒细胞', '嗜碱性粒细胞', '中性粒细胞', '空']
    Pred = Prediction(PredictFile='2.jpg', ModelFile='cellfinder.h5', Width=100, Height=100, CellType=CellType)
    Pred.Predict()
    


#设置路由
@app.route("/",methods = ["POST"])
def upload():
    file_obj = request.files.get("pic")
    if file_obj is None:
        return "上传失败"
    file_obj.save("2.jpg")
    print("上传成功")
    main()
    os.remove("2.jpg")
    return json.dumps((dic2))

#启动路由
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

