# Shallow and Deep CNN architechtures for age and gender classification
#### COGS 181 Final Project
#### David Justo and Kareem Moussa


#### Abstract
In this paper, we evaluate the strengths and limitations of two opposing strategies to tackling the very challenging problem of accurate
age and gender classification on an unconstrained image domain. Namely, we compare the shallow CNN architecture proposed by Levi and Hassner for age and gender classification against a VGG16-Face model adapted for these two classification tasks. We perform minor variations to the structure of these two models to explore just how much we can improve their performance. However, our goal is not to maximize the performance of either model given that our resources are limited. Instead, we focus on performing an extensive evaluation of the merits of each approach in a limited training window in order to identify the architectural and hyper-parameter changes that appear to improve performance on the long run. We find that fine-tuning deep networks such as VGG16-Face provide, in general, a higher accuracy than their shallow counterparts. However, we also find that, in our limited training window, our shallow models are capable of performing very similarly to VGG16-Face given the right hyper-parameters  and that, when taking advantage of the Adam optimization strategy, they can severely outperform VGG16-Face in the early stages of training when performing age classification.
