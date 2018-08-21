import jieba
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

data = [{"city": "Beijing", "temp": 100},
        {"city": "Shanghai", "temp": 60},
        {"city": "Shenzheng", "temp": 30}]


def dictvec():
    dict = DictVectorizer(sparse=False)
    data_new = dict.fit_transform(data)
    print(dict.get_feature_names())
    print(dict.inverse_transform(data_new))
    print(data_new)
    return None


def countvec():
    cv = CountVectorizer()
    data_new = cv.fit_transform(["人生 苦短，我 喜欢 Python", "人生 漫长，不用 Python"])
    print(cv.get_feature_names())
    print(data_new.toarray())
    return None


def hanzivec():
    c1, c2, c3 = cutword()
    print(c1, c2, c3)
    cv = CountVectorizer()
    data_new = cv.fit_transform([c1, c2, c3])
    print(cv.get_feature_names())
    print(data_new.toarray())
    return None


def cutword():
    con1 = jieba.cut("8月21日消息 今天下午360在北京召开新品发布会，会上正式发布了360 N7 Pro新机，该机主打大电池，软硬结合安全特性。")
    con2 = jieba.cut("外观方面，360 N7 Pro采用了双面玻璃设计，正面5.99英寸1080P 18:9全面屏，CNC金属中框采用双色阳极氧化工艺，前后面板沿用了N6 Pro上的双玻璃设计以及NCVM真空镀膜的旗舰级玻璃工艺。")
    con3 = jieba.cut("配置方面，360 N7 Pro搭载了骁龙710处理器，标配LPDDR4X的6GB内存和64GB容量存储空间，最高配备128GB容量存储。配备了4000mAh电池，支持18W快充，号称轻松续航两天。采用Type C接口，并且保留了3.5mm耳机孔。")

    content1 = list(con1)
    content2 = list(con2)
    content3 = list(con3)

    c1 = ' '.join(content1)
    c2 = ' '.join(content2)
    c3 = ' '.join(content3)

    return c1, c2, c3


def tfidfvec():
    c1, c2, c3 = cutword()
    print(c1, c2, c3)
    tf = TfidfVectorizer()
    data_new = tf.fit_transform([c1, c2, c3])
    print(tf.get_feature_names())
    print(data_new.toarray())
    return None


if __name__ == "__main__":
    # dictvec()
    # countvec()
    # hanzivec()
    tfidfvec()