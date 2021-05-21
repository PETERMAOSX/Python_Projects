from imageai.Prediction.Custom import CustomImagePrediction
import os
import argparse
import sys

def name_translate(name):
    if name == "BaiFenBing":
        return '白粉病'
    elif name == 'BanKuBing':
        return '斑枯病'
    elif name == 'YaChongBing':
        return '蚜虫病'
    elif name == 'Normal_leaf':
        return '正常树叶'
    else :
        return name

def args_parse():
    ap = argparse.ArgumentParser()
    ap.add_argument('-i',required=True)
    args = vars(ap.parse_args())
    return args


execution_path = os.getcwd()

prediction = CustomImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath(os.path.join(execution_path,"model_ex-100_acc-0.473958.h5"))
prediction.setJsonPath(os.path.join(execution_path,"model_class.json"))
prediction.loadModel()

predictions,probabilities = prediction.predictImage(os.path.join(execution_path,sys.argv[1]),result_count=4)
# print(predictions)
# print('--------------')
# print(probabilities)



print('----------------------')
print('概率列表 :')
for eachPrediction,eachProbability in zip(predictions,probabilities):
    print(name_translate(eachPrediction) + " : "+eachProbability+'%')
print('----------------------')
print('预测结果 :')
print(name_translate(predictions[0]) + " : " +probabilities[0]+'%')


# for eachPrediction,eachProbability in zip(predictions,probabilities):
#     if(eachPrediction == "BaiFenBing"):
#         print("白粉病 : "+eachProbability+"%")
#     elif(eachPrediction == "YaChongBing"):
#         print("蚜虫病 : "+eachProbability+"%")
#     elif(eachPrediction == "BanKuBing"):
#         print("斑枯病 : "+eachProbability+"%")
#     elif(eachPrediction == "Normal_leaf"):
#         print("正常树叶 :"+eachProbability+"%")
#     else:
#         print(eachPrediction + " : "+ eachProbability)
    
    
