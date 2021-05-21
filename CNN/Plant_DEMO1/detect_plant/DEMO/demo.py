from imageai.Prediction.Custom import CustomImagePrediction
import os
execution_path = os.getcwd()

prediction = CustomImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath(os.path.join(execution_path,"model_ex-090_acc-0.723214.h5"))
prediction.setJsonPath(os.path.join(execution_path,"model_class.json"))
prediction.loadModel(num_objects=2)

predictions,probabilities = prediction.predictImage(os.path.join(execution_path,"008.jpg"))

for eachPrediction,eachProbability in zip(predictions,probabilities):
    if(eachPrediction == "BaiFenBing"):
        print("白粉病 : "+eachProbability+"%")
    elif(eachPrediction == "YaChongBing"):
        print("蚜虫病 : "+eachProbability+"%")
    else:
        print(eachPrediction + " : "+ eachProbability)
    
    
