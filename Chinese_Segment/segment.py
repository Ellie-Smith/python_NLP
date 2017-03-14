#coding=utf-8
'''
create on 2017 3-14
@auther: 温启帆
'''

class csegment:

    def __init__(self,maxlen):
        self.maxLen = maxlen*3
        self.dictionary = self.loadDict()

    def getMaxlen(self):
        return self.maxLen
    def setMaxLen(self,maxLen):
        self.maxLen = maxLen*3

    def loadDict(self):
        f=open('chineseDict.txt','r')
        f.readline()
        dictionary = {}
        for line in f:
            wp = line.decode('gbk').encode('utf-8').strip().split(',')
            dictionary[wp[0]] = wp[1]
        return dictionary

    def MMsegment(self,sentence):
        index = 0
        currlen = self.maxLen
        result = ''
        length = len(sentence)
        if len(sentence)==0:
            return ''

        while index < len(sentence):
            #若剩下为切分的词长度小于最大长度，则最大长度减一
            if index+currlen > len(sentence) and currlen > 0:
                currlen -= 3
                continue
            word = sentence[index:index+currlen]
            if word in self.dictionary.keys():
                result += word+'\\'
                index += currlen
                currlen = self.maxLen
            else:
                if currlen > 3:
                    currlen -= 3
                else:

                    result += "<!未收录该子串__"+ word +">\\"
                    index += currlen
                    currlen = self.maxLen
        return result

    def RMMsegment(self,sentence):
        index = len(sentence)
        currlen = self.maxLen
        result = ''
        length = len(sentence)
        if len(sentence)==0:
            return ''

        while index > 0:
            #若剩下为切分的词长度小于最大长度，则最大长度减一
            if index-currlen < 0 and currlen > 0:
                currlen -= 3
                continue
            word = sentence[index-currlen:index]
            if word in self.dictionary.keys():
                result = word+'\\'+ result
                index -= currlen
                currlen = self.maxLen
            else:
                if currlen > 3:
                    currlen -= 3
                else:
                    result = "<!未收录该子串__"+ word +">\\" + result
                    index -= currlen
                    currlen = self.maxLen
        return result

    def getResult(self):
        return self.result



if __name__ == '__main__':
    seg = csegment(3)
    # seg.setMaxLen(1)
    print seg.MMsegment('结合成分子时')
    print seg.RMMsegment('结合成分子时')