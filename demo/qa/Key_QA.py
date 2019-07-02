import jieba
import jieba.posseg as pseg #词性标注
import jieba.analyse as anls #关键词提取



class QA():

    def Qa(self,question):
        QA_Data={
'什么是FlashBank？':'FlashBank是一站式的网上银行系统，可以满足您从储蓄到投资等的一切业务需求。更多详细信息可以通过页面下方的”Request a free quote”联系我们。',
'怎么开银行卡？':'开银行卡请带好身份证到线下银行办理开户服务。',
'我想开银行卡':'开银行卡请带好身份证到线下银行办理开户服务。',
'如何查询余额':'在客户端查询界面输入卡号即可查询。',
'如何登录':'页面导航栏端”Login in”。',
'如何注册':'在登陆界面点击注册按钮，提交对应信息即可。',
'如何修改个人信息':'点击页面右上角Me，根据指引修改信息。',
'如何查看交易记录':'点击页面下方” Wealth Management”，选择” Transaction History”，输入相关信息即可。',
'如何注销账户':'点击页面下方” More Service”，选择” accountClosure”，输入对应accountnumber即可',
'如何开户':'登陆后，点击网页顶部导航栏”Account Creation”，根据指引填写相关信息即可。',
'我想开户':'登陆后，点击网页顶部导航栏”Account Creation”，根据指引填写相关信息即可。',
'如何转账？':'登陆后，点击网页顶部导航栏”Transaction”功能，选择”Transfer”,输入自己账户、转账账户以及转账金额即可。',
'如何办理转账业务？':'登陆后，点击网页顶部导航栏”Transaction”功能，选择”Transfer”,输入自己账户、转账账户以及转账金额即可。',
'我想转账？':'登陆后，点击网页顶部导航栏”Transaction”功能，选择”Transfer”,输入自己账户、转账账户以及转账金额即可。',
'如何存款':'登陆后，点击网页顶部导航栏” Transaction”，根据指引填写相关信息即可。',
'如何办理存款业务':'登陆后，点击网页顶部导航栏” Transaction”，根据指引填写相关信息即可。',
'我想存款':'登陆后，点击网页顶部导航栏” Transaction”，根据指引填写相关信息即可。',
'如何存款':'登陆后，点击网页顶部导航栏” Transaction”，根据指引填写相关信息即可。',
'如何办理存款业务':'登陆后，点击网页顶部导航栏” Transaction”，根据指引填写相关信息即可。',
'我想存款':'登陆后，点击网页顶部导航栏” Transaction”，根据指引填写相关信息即可。',
'如何创建支票本':'选中网页顶部导航栏”Transaction”，下拉后点击” chequeBookCreation”，根据指引填写相关信息即可。',
'有什么投资服务':'FlashBank为您提供包括Mutual Fund、Stock、Foreign Exchange等投资业务，更多详细信息请查看对应页面描述。',
'如何进行投资':'首先您需要创建一个投资账户，然后点开您想投资的对应商品界面，根据指示输入信息即可。',
'如何购买基金':'首先您需要创建一个投资账户，然后打开” Mutual Fund”界面，根据指示选择对应模块完成操作即可。',
'如何购买股票':'首先您需要创建一个投资账户，然后打开”Stock Trading”界面，根据指示选择对应模块完成操作即可。',
'如何进行股票操作':'首先您需要创建一个投资账户，然后打开”Stock Trading”界面，根据指示选择对应模块完成操作即可。',
'如何进行外国货币互换':'首先您需要创建一个投资账户，然后打开” Foreign Currency Exchange”界面，根据指示选择对应模块完成操作。',
'如何兑换外汇':'首先您需要创建一个投资账户，然后打开” Foreign Currency Exchange”界面，根据指示选择对应模块完成操作。',
'如何办理信用卡业务':'首先您需要创建一个信用卡账户，然后点击网页顶部导航栏” Credit Card Service”模块或者网页底部”Credit Card”模块，选择需要办理的业务即可。',
'如何开设信用卡账户':'点击网页顶部导航栏” Credit Card Service”或者网页底部”Credit Card”模块，选择” accountOpening”，根据指示填写相关信息即可。',
'如何查看信用卡账户详细信息':'点击打开网页底部”Credit Card”模块页面，选择” Credit card limit detail”服务，根据指示填写相关信息即可。',
'如何删除信用卡账户':'打开网页顶部导航栏” Credit Card Service”界面或者网页底部”Credit Card”模块，选择” cancellation”模块，根据指示填写相关信息即可。',
'删除信用卡':'打开网页顶部导航栏” Credit Card Service”界面或者网页底部”Credit Card”模块，选择” cancellation”模块，根据指示填写相关信息即可。',
'如何进行信用卡转账':'打开网页底部”Credit Card”模块界面，选择” transactionPosting”模块，根据指示填写相关信息即可。',
'如何查看信用卡账户转账记录':'打开网页底部”Credit Card”模块界面，选择” transactionDetails”功能，根据指示填写相关信息即可。',
'如何查看信用卡账户还款信息':'打开网页底部”Credit Card”模块界面，选择” outstandingPayment”功能，根据指示填写相关信息即可。',
'如何信用卡账户积分查询':'打开网页底部”Credit Card”模块界面，选择” CreditPoint”模块，根据指示进行操作即可。',
'如何进行信用卡账户还款':'打开网页顶端导航栏” Credit card payment”或者网页底部”Credit Card”模块界面，选择” Credit card payment”功能，根据指示填写相关信息即可。',
}
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
