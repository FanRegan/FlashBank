import jieba
import jieba.posseg as pseg #词性标注
import jieba.analyse as anls #关键词提取



class QA():

    def Qa(self,question):
        QA_Data={'什么是区块链？':'区块链是一种基于分布式账本的新技术。',
         '怎么开银行卡？':'开银行卡请带好身份证到线下银行办理开户服务。',
         '我想开银行卡':'开银行卡请带好身份证到线下银行办理开户服务。',
         '如何查询余额':'输入卡号即可查询。'}
        qlist = jieba.lcut(question, cut_all=True)
        print(qlist)
        for q in QA_Data:
            count=0.0
            total=float(len(qlist))
            for x in qlist:
                if x in q:
                    count+=1.0
            if (count/total>0.5):
                return {'message': 'success','result': QA_Data[q]}
        return {'message': 'fail','result': "我无法回答你哦。"}
