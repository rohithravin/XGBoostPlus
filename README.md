# XGBoostPlus

Patients suffering from symptomatic spinal deformity have a significantly reduced quality of life, and are unable to perform daily routine activities. Various surgical options exist to optimize functional outcomes while limiting morbidity; Proximal junctional kyphosis (PJK) is one of these complications following spinal deformity surgery that may require reoperation and have a serious impact on a patient’s postoperative course. In this paper, we propose a new method, XGBoost+, that utilizes the Learning Using Privilege Information (LUPI) paradigm by combining XGBoost and Iterative Privilege Learning (IPL) framework. We evaluate the proposed methodology based on metrics crucial for successful deployment in a clinical setting- AUC, sensitivity, specificity, and precision. Our results show an increase of 5% in AUC between XGBoost and XGBoost+, highlighting the significance of privileged information. We further showcase the feature importance of our model, highlight that sagittal vertical alignment and sacrum slope play a major role in predicting PJK - which is supported by previous work. Lastly, we discuss the relative contribution of the privileged features in refining the decision boundary of our model.




### Acknowledgements
`model.py` contains code obtained from https://github.com/Ekeany/XGBoost-From-Scratch repo.
