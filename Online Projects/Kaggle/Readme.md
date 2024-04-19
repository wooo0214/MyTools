You can upload jypter notbooks to Kaggle
> Kaggle account: 163/2>1

## Kaggle projects followed
>
> See notebooks on Kaggle for details.

1. Galaxy Multi-Image Classification with LeNet-5
<https://www.kaggle.com/code/tenzinmigmar/galaxy-multi-image-classification-with-lenet-5>

    中文知乎搬运： <https://zhuanlan.zhihu.com/p/396047236>

    - Tags: 图像分类classifying, 卷积神经网络LeNet-5
    - Dataset: galaxy10
    - More readings:
        - Python案例｜使用卷积网络对星系图片进行分类 <https://bbs.huaweicloud.com/blogs/405941>
        - Galaxy Zoo: reproducing galaxy morphologies via machine learning <https://academic.oup.com/mnras/article/406/1/342/1073212?login=false>

1. Time Series with Facebook Prophet  
<https://www.kaggle.com/code/kashnitsky/topic-9-part-2-time-series-with-facebook-prophet>

    - Tags: 时间序列Time Series, 预测forcasting
    - library: Prophet
    - More readings:
        - Facebook时序预测工具Prophet实战分析 <https://cloud.tencent.com/developer/article/2097105>

1. Movie recommendation system  
<https://www.kaggle.com/code/ibtesama/getting-started-with-a-movie-recommendation-system>

    - Tags: 推荐recommendation, 人口统计推荐demographic recommender, 基于内容的筛选content based filtering
    - dataset: TMDB 5000 movie
    - Abstracts
        > 3 tries to do recommendation, and it's getting more complex and reasonable:
        > - Demographic recommender
        > - Plot description based Recommender
        > - Credits, Genres and Keywords Based Recommender


        1. text processing, word vector, Term Frequency-Inverse Document Frequency (TF-IDF) - `TfIdfVectorizer` class
        1. smilarity score (euclidean, the Pearson and the cosine similarity scores)

            - 余弦相似性：通过测量两个向量的夹角的余弦值来度量它们之间的相似性。
            https://en.wikipedia.org/wiki/Cosine_similarity
        1. Credits, Genres and Keywords Based Recommender
        1. 使用到的库、类、函数
            - linear_kernel(), `from sklearn.metrics.pairwise import linear_kernel`
            - `TfIdfVectorizer` class, `from sklearn.feature_extraction.text import TfidfVectorizer`, https://zhuanlan.zhihu.com/p/67883024
                
                > Q: Understanding how to construct the word matrix from Overview description, and what each element stands for in this metrix:

                    `tfidf_matrix = tfidf.fit_transform(df2['overview'])`

                > Q: How liner_kernel calculates the sosine similarity: 
                
                    `cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)`

            - enumberate(sequence, [start=0]) : group an object (array, tuple, string) into an index series:

                https://www.runoob.com/python/python-func-enumerate.html
                
                In this projects enumberate pairs similarity scores with corresponding movie, such as (1, 0.007866023160589344) when input title is Deadpool.

## My projects

Add all tec line projects from tx:

- Classifying Iris Flower Types with K-Means
