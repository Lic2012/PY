'''
Created on 2014Äê2ÔÂ27ÈÕ

@author: Administrator
'''

if __name__ == '__main__':
    from gensim.models import word2vec
    import logging
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    #fin = "/home/rte/Public/wangrui/data/kbp/20131122_words2vect/part_rmstp"
    #sentences  = []
    #for line in open(fin):
    #    c = line.strip("\r\n").split(" ")
    #    sentences.append(c)
    #model = word2vec.Word2Vec(sentences, size=200, window=5, min_count=1, workers=12)
    #model.save("/home/rte/Public/wangrui/data/kbp/20131122_words2vect/1223model")
    #*****load model*******************************************************************************
    #model=word2vec.Word2Vec.load("/home/rte/Public/wangrui/data/kbp/20131122_words2vect/1223model")
    #model = word2vec.Word2Vec.load("/home/rte/Public/wangrui/data/kbp/20131122_words2vect/140225_model")
    model = word2vec.Word2Vec.load_word2vec_format('/home/rte/Public/wangrui/data/kbp/20131122_words2vect/LHFRTE.bin', binary=True)
    #***********print******************************************************************************
    f = open('/home/rte/Public/wangrui/data/kbp/20131122_words2vect/'+'tmp.txt')
    fo = open('xxx', 'w'))
    wordList = []
    for line in f:
        c = line.strip("\r\n").split(" ")
        v = c[1]
        if v not in wordList:
            wordList.append(v)
    for(i=0, i<len(wordList), i++):
        for(j=i+1, j<len(wordList), j++):
            fo.write(wordList[i]+"\t"+wordList[j]+"\t"+str(model.similarity(wordList[i],wordList[j])+"\n")
    fo.close()
#     print 'have','\t','own'
#     print model.similarity("have","own")
#     print 'have','\t','leave'
#     print model.similarity("have","leave")
    #print 'FSF','\t','Senegalese_football_federation'
    #print model.similarity('FSF','Senegalese_football_federation')
    #print 'Steelers','\t','Pissburgh'
    #print model.similarity('Steelers','Pissburgh')