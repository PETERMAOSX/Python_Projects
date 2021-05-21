from imageai.Prediction.Custom import CustomImagePrediction
import os
execution_path = os.getcwd()

prediction = CustomImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath(os.path.join(execution_path,"model_ex-100_acc-0.593750.h5"))
prediction.setJsonPath(os.path.join(execution_path,"model_class.json"))
prediction.loadModel(num_objects=2)

predictions,probabilities = prediction.predictImage(os.path.join(execution_path,"01798_00001.png"))

for eachPrediction,eachProbability in zip(predictions,probabilities):
    print(eachPrediction + " : "+eachProbability)
