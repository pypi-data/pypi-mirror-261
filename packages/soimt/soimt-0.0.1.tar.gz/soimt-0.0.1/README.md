1.Model_Test_Program
Our project can be used to evaluate the reliability of image classification models. We generate adversarial samples by adding cloud layers and Gaussian blur to visible light images. For SAR images, we introduce high-scattering noise points in the background area and modify pixel blocks in the object area to generate adversarial samples. By introducing these interferences, we can assess the robustness of the models.

[Github-flavored Markdown](https://github.com/Agiraffea/model_test_program)

2.How to use the soimt

pip install soimt
from soimt import main

main.optic_img_test(testcalss,datapath,model,datatransform)

testclass:the disturbed data class you want to generate
you can select "cloud" or "blur"
datapath:your dataset path.(adversarial data can be saved in the same path)
model:the model to be tested
datatransform:the transform to preprocess your dataset

main.SAR_img_test(testcalss, datapath, model)

testclass:the disturbed data class you want to generate
you can select "one/three/fivescatter" or "patch"
datapath:your dataset path
model:the model to be tested	