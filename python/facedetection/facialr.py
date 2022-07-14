from deepface import DeepFace
obj = DeepFace.analyze(img_path = "will.jpg", actions = ['age','gender','race','emotion'])
print (obj) 
