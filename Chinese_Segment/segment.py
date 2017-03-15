#coding=utf-8
'''
create on 2017 3-14
@auther: Ellie
'''


class csegment:

    def __init__(self,maxlen):
        self.maxLen = maxlen
        self.dictionary = self.loadDict()

    @property
    def maxLen(self):
        return self.maxLen
    @maxLen.setter
    def maxLen(self,maxLen):
        self.maxLen = maxLen

    def loadDict(self):
        f=open('chineseDict.txt','r')
        f.readline()
        dictionary = {}
        for line in f:
            wp = line.decode('gbk').strip().split(',')
            dictionary[wp[0]] = wp[1]
        return dictionary

    def MMsegment(self,sentence):
        sentence = sentence.decode('utf-8')
        index = 0
        currlen = self.maxLen
        result = ''
        length = len(sentence)
        if len(sentence)==0:
            return ''

        while index < len(sentence):
            #若剩下为切分的词长度小于最大长度，则最大长度减一
            if index+currlen > len(sentence) and currlen > 0:
                currlen -= 1
                continue
            word = sentence[index:index+currlen]
            if word in self.dictionary:
                result += word+'\\'
                index += currlen
                currlen = self.maxLen
            else:
                if currlen > 1:
                    currlen -= 1
                else:
                    if word>='0' and word<='9':
                        result += word + '\\'
                        index += currlen
                        currlen = self.maxLen
                    else:
                        result += "<!未收录该子串__".decode('utf-8')+ word +">\\"
                        index += currlen
                        currlen = self.maxLen
        return result

    def RMMsegment(self,sentence):
        sentence = sentence.decode('utf-8')
        index = len(sentence)
        currlen = self.maxLen
        result = ''
        length = len(sentence)
        if len(sentence)==0:
            return ''

        while index > 0:
            #若剩下为切分的词长度小于最大长度，则最大长度减一
            if index-currlen < 0 and currlen > 0:
                currlen -= 1
                continue
            word = sentence[index-currlen:index]
            if word in self.dictionary:
                result = word+'\\'+ result
                index -= currlen
                currlen = self.maxLen
            else:
                if currlen > 1:
                    currlen -= 1
                else:
                    if word>='0' and word<='9':
                        result = word + '\\' + result
                        index -= currlen
                        currlen = self.maxLen
                    else:
                        result = "<!未收录该子串__".decode('utf-8')+ word +">\\" + result
                        index -= currlen
                        currlen = self.maxLen
        return result

    def getResult(self):
        return self.result



if __name__ == '__main__':
    seg = csegment(3)
    print seg.MMsegment('结合成分子时1234')
    print seg.RMMsegment('结合成分子时111')
    seg.maxLen = 1
    print seg.MMsegment('结合成分子时')
    print seg.RMMsegment('结合成分子时')