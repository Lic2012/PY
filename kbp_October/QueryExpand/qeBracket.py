#!/usr/bin/python  
#-*-coding:utf-8-*- 
'''
Created on 2014年2月27日

@author: Administrator
'''
#function: list returnsearchlist(test)
#input test list: 2D LIST
#1-D qid, qname
#2-D query set(here is acronym words)
#output list: 2D LIST
#1-D qid, qname, expand-string
#2-D query set(here is acronym & not expand None)
import string
import re
def qeBracket(qid, name, back_dir = "D:\\桌面待分类\\query_text_2013\\"):
    path = back_dir + qid
    f= open(path)
    doc = ""
    stp = ['from','and','for','of','at','in','on','before','after','by','with','about','around','over','above','under','below','between','among','behind','along','to']
    punc ='''`~:,.'?/<>|\{}[]-=+_!@#$%^&*()1234567890'''
    ##READ FILE, AND STORE IN A WORD LIST
    for line in f:
        doc += " "+line.strip("\n")
    wordList = doc.split(" ")
    #THE ACRONYM WORD

    for i in range(len(wordList)):
        if '('+name+')' in wordList[i]: 
        #FIND ACRONYM FORMMAT: (ACRO)
            outprint = "" # THE FINAL EXPAND
            
            #FIRST CHAR SET OF ACRONYM WORDS
            first_char = []
            for c in name:
                first_char.append(c)
                
            l = i - 1
            l_secure = i - 1
            while(len(first_char) > 0 and i-l<2*(len(name))):
                if wordList[l] in stp: 
                    outprint = wordList[l] + " " + outprint
                    l -= 1
                    continue
                m = len(first_char)-1
                while (m>=0):
                    if wordList[l] == '': break
                    elif wordList[l][0] == first_char[m]: 
                        #find can expand pre to acronym
                        del first_char[m]
                        outprint = wordList[l] + " " +outprint
                        break
                    m -= 1                    
                l -= 1
            if outprint != '':
                if outprint.rstrip(" ")[-1] == ',':
                #print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
                    outprint += wordList[l_secure]                    
                    
                if outprint.strip(" ").split(" ")[-1] in stp:
                    #print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    #print wordList
                    index = i-1
                    word_cnt = 0
                    outprint1 = ''
                    while(word_cnt<=len(first_char)):
                        if wordList[index] not in stp:
                            word_cnt += 1
                        outprint1 = wordList[index] + " " + outprint1
                        index -= 1
                    outprint = outprint1
                
                outprintList = outprint.strip(" ").split(" ")
                n = len(outprintList)-1
                while(n>=0):
                    if outprintList[n] in stp:
                        del outprintList[n]
                    n-=1
                if len(outprintList) < len(name):
                    #print "***********************************************"
                    #NOT EXPAND THE UPPERWORDS, FIND THE FAREAST UPPERWORDS
                    outprint2 = ''
                    flag1 = 0
                    while(l_secure>0):
                        if wordList[l_secure] != '':
                            if wordList[l_secure][0] not in string.lowercase and wordList[l_secure][0] not in punc: 
                                flag1 = 1
                                outprint2 = wordList[l_secure]+" "+outprint2
                            elif wordList[l_secure] in stp:
                                outprint2 = wordList[l_secure]+" "+outprint2
                            elif flag1 == 1:
                                if outprint2.split(" ")[0] in stp:
                                    #print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
                                    outprint2 = outprint2[len(outprint2.split(" ")[0])+1:]
                                break
                            else:
                                outprint2 = wordList[l_secure]+" "+outprint2                        
                        l_secure-=1
                    outprint = outprint2
            return outprint                    
            #break #BREAK FOR LINE 33

def buildcountry(dicdir = "C:\\Users\\Administrator\\Desktop\\"):
    countryDir = dicdir + "country1.dic"
    country = []
    for line in open(countryDir):
        country.append(line.strip("\r\n"))
    return country
def buildcity(dicdir = "C:\\Users\\Administrator\\Desktop\\"):
    city = {}
    for i in string.lowercase:
        city[i] = []
        cityDir = dicdir + "city\\" + i + ".txt"
        for line in open(cityDir):
            city[i].append(line.strip("\r\n"))
    return city

def lookUpDic(name, country, city): 
    if name == "": #IF NO INPUT
        return None
    if name[0] not in string.uppercase and name[0] not in string.lowercase: 
    #if not in 24 English char
        return None
    for c in country:
        if name.lower() == c.lower():
            #print name," is a ","Country"
            return c
    #open city name file as the first char
    for c in city[name[0].lower()]:
        if name.lower() == c.lower():
            #print name, " is a ","City"
            return c
    return None
            
def AcronymExpand(qid, qname, back_dir = "D:\\桌面待分类\\query_text_2013\\"):
    f = open(back_dir + qid) #query background doc
    bag = ""
    for linet in f:
        if len(linet) != 1:
            bag = bag + " " + linet.strip("\n")
    bag = bag.strip(" ")
    bag = bag.split()
    lenb = len(bag)
    lena = len(qname)
    tag = 0
    fullset = []
    period = ["Corp.","Inc."]
#     print "qname ", qname
#     print "lenb ",str(lenb)
#     print "lena ",str(lena)
#     print "leb-lena+1 ",str(lenb-lena+1)
    for i in range(0,lenb- lena + 1):
        full = ""
        if re.match("[A-Z]",bag[i][0]):#IF THE FIRST LETTER IS UPPERCASE
            tmp = []
            for j in range(i,i+ lena):
                tmp.append(bag[j][0])
                #print "append+"
                #print tmp
            for j in range(0,lena):
                if qname[j] in tmp:
                    tmp.remove(qname[j])
                    #print "remove-"
                    #print tmp
            if tmp == []:
                for j in range(i,i+lena):
                    #print "j: ","word-",str(j),bag[j]
                    full = full + " " + bag[j] #link with SPACE
                if full.endswith("'s"):
                    full = full.rstrip("s")
                    full = full.rstrip("'")
                full = full.strip(" ")
                full = full.strip(",")
                if full.split(" ")[-1] not in period:
                    full = full.strip(".")
                full = full.strip("'")
                full = full.strip("\"")
                full = full.strip(";")
                full = full.strip("?")
                full = full.strip(".)")
                full = full.strip("-")
                #print "full: ",full
                if (not "," in full) and (not "(" in full) and (not re.search("[a-z]\. ",full)):
                    fullset.append(full)
                    tag = 1
#                 print "fullset: "
#                 print fullset
                    
                    
    # window +1
    for i in range(0,lenb- lena + 1):
        full = ""
        if re.match("[A-Z]",bag[i][0]):
            tmp = []
            if i + lena + 1 >lenb: #edge detection
                lenbb = i + lena
                #print "lebb: ",lenbb
            else:
                lenbb = i + lena + 1
            for j in range(i,lenbb):
                if re.match("[A-Z]",bag[j][0]):
                    tmp.append(bag[j][0])
                    #print tmp
                else:
                    tmp.append(bag[j])
                    #print tmp
            for j in range(0,lena):
                if qname[j] in tmp:
                    tmp.remove(qname[j])
                    #print tmp
            if  (("of" in tmp) or ("and" in tmp) or ("for" in tmp)or ("in" in tmp) or ("at" in tmp)) and len(tmp) == 1: 
                for j in range(i,lenbb):
                    full = full + " " + bag[j]
                if full.endswith("'s"):
                    full = full.rstrip("s")
                    full = full.rstrip("'")
                full = full.strip(" ")
                full = full.strip(",")
                if full.split(" ")[-1] not in period:
                    full = full.strip(".")
                full = full.strip("'")
                full = full.strip("\"")
                full = full.strip(";")
                full = full.strip("?")
                full = full.strip(".)")
                full = full.strip("-")
                if (not "," in full) and (not re.search("[a-z]\. ",full)) and (not "(" in full) and (not re.search(" [a-z]+$",full)) and (not re.match("[a-z] ",full)):
                    fullset.append(full)
                    tag = 1
    #window +2
    beifen = ["and","of","for","in","the","at"]
    for i in range(0,lenb- lena + 1):
        full = ""
        if re.match("[A-Z]",bag[i][0]):
            tmp = []
            if i + lena + 2 >lenb:
                lenbb = i + lena
            else:
                lenbb = i + lena + 2
            for j in range(i,lenbb):
                if re.match("[A-Z]",bag[j][0]):
                    tmp.append(bag[j][0])
#                     print "extend+"
#                     print tmp
                else:
                    tmp.append(bag[j])
#                     print "extend+"
#                     print tmp
            for j in range(0,lena):
                if qname[j] in tmp:
                    tmp.remove(qname[j])
#                     print "remove-"
#                     print tmp
            if len(tmp)>2:
                if  (tmp[0] in beifen) and (tmp[1] in beifen)and (len(tmp) == 2): 
                    for j in range(i,lenbb):
                        full = full + " " + bag[j]
                    if full.endswith("'s"):
                        full = full.rstrip("s")
                        full = full.rstrip("'")
                    full = full.strip(" ")
                    full = full.strip(",")
                    if full.split(" ")[-1] not in period:
                        full = full.strip(".")
                    full = full.strip("'")
                    full = full.strip("\"")
                    full = full.strip(";")
                    full = full.strip("?")
                    full = full.strip(".)")
                    full = full.strip("-")
                    if (not "," in full) and (not re.search("[a-z]\. ",full)) and (not "(" in full) and (not re.search(" [a-z]+$",full)) and (not re.match("[a-z] ",full)):
                        fullset.append(full)
                        tag = 1
    #print fullset
    if tag == 0 : #No ACRONYM
        return None
    else:
        #print "^^^^^^^^^^^^^^^^^^^^^"
        if len(fullset) == 1:
            return fullset[0]
        else:
            Hash = {}
            for j in range(0,len(fullset)):
                if not Hash.has_key(fullset[j]):
                    Hash[fullset[j]] = 1
                else:
                    Hash[fullset[j]] += 1
            dic = sorted(Hash.iteritems(),key = lambda asd:asd[1],reverse = True)
            return dic[0][0]
def findLower(qid, qname, back_dir= "D:\\桌面待分类\\query_text_2013\\"):
    f = open(back_dir + qid) #query background doc
    bag = ""
    for linet in f:
        if len(linet) != 1:
            bag = bag + " " + linet.strip("\n")
    bag = bag.strip(" ")
    bag = bag.split()
    nameNew = qname[0]+qname[1:].lower()
    if nameNew in bag:
        return nameNew
    else:
        return None
    
def returnsearchlist(test):
    searchlist = []
    country = buildcountry()
    city = buildcity()
#     print "acronym: ",str(len(test))
    cntBracket = 0
    cntCity = 0
    cntExpand = 0
    cntFindLower = 0
    for item in test:
        nameBracket = qeBracket(item[0], item[1])
        if  nameBracket != None:
            cntBracket += 1
            searchlist.append([item[0],item[1],nameBracket])
        else:
            nameAcronym = AcronymExpand(item[0], item[1])
            if nameAcronym != None:
                cntExpand += 1
                searchlist.append([item[0],item[1],nameAcronym])
                #print item[0]," ",item[1],": ",nameAcronym
            else:
                c = lookUpDic(item[1], country, city)
                if c:
                    #print "#######################"
                    cntCity += 1
                    searchlist.append([item[0],item[1],c])
                    #print item[0]," ",item[1],": ",c
                else:
                    f = findLower(item[0], item[1])
                    if f != None and len(item[1])>3:
                        searchlist.append([item[0], item[1], f])
                        #print  item[0]," ",item[1],": ",f
                        cntFindLower += 1
                    else:
                        pass
                        #print item[0]," ",item[1],": ",nameBracket
#     print "bracket: ",str(cntBracket)
#     print "expand: ",str(cntExpand)
#     print "city: ",str(cntCity)
#     print "findlower",str(cntFindLower)    
    
    return searchlist    
             
if __name__ == '__main__':
    test = [['EL13_ENG_0003', 'PNC'], ['EL13_ENG_0009', 'UKRAINE'], ['EL13_ENG_0014', 'PSF'], ['EL13_ENG_0023', 'PSC'], ['EL13_ENG_0034', 'ALASKA'], ['EL13_ENG_0044', 'CRC'], ['EL13_ENG_0059', 'CAIRO'], ['EL13_ENG_0060', 'HSE'], ['EL13_ENG_0065', 'TN'], ['EL13_ENG_0070', 'JT'], ['EL13_ENG_0072', 'MUFC'], ['EL13_ENG_0091', 'FAR'], ['EL13_ENG_0104', 'ROC'], ['EL13_ENG_0119', 'NPH'], ['EL13_ENG_0120', 'FCC'], ['EL13_ENG_0121', 'DC'], ['EL13_ENG_0126', 'MI'], ['EL13_ENG_0144', 'MN'], ['EL13_ENG_0145', 'FSF'], ['EL13_ENG_0149', 'LSU'], ['EL13_ENG_0155', 'CRC'], ['EL13_ENG_0159', 'NPA'], ['EL13_ENG_0163', 'PHOENIX'], ['EL13_ENG_0165', 'MTS'], ['EL13_ENG_0172', 'CFC'], ['EL13_ENG_0176', 'FNC'], ['EL13_ENG_0184', 'JB'], ['EL13_ENG_0185', 'NDF'], ['EL13_ENG_0203', 'JL'], ['EL13_ENG_0206', 'NH'], ['EL13_ENG_0216', 'OH'], ['EL13_ENG_0220', 'ATLANTA'], ['EL13_ENG_0221', 'WADA'], ['EL13_ENG_0225', 'ADI'], ['EL13_ENG_0233', 'NPA'], ['EL13_ENG_0240', 'FSF'], ['EL13_ENG_0242', 'ISF'], ['EL13_ENG_0245', 'NIGERIA'], ['EL13_ENG_0246', 'BAL'], ['EL13_ENG_0254', 'NEWCASTLE'], ['EL13_ENG_0259', 'TB'], ['EL13_ENG_0267', 'BARCELONA'], ['EL13_ENG_0277', 'UCLA'], ['EL13_ENG_0284', 'HOUSTON'], ['EL13_ENG_0287', 'TSU'], ['EL13_ENG_0288', 'NPD'], ['EL13_ENG_0302', 'DMV'], ['EL13_ENG_0315', 'ADL'], ['EL13_ENG_0316', 'CRC'], ['EL13_ENG_0319', 'JGL'], ['EL13_ENG_0320', 'CMAG'], ['EL13_ENG_0322', 'DFT'], ['EL13_ENG_0328', 'CRC'], ['EL13_ENG_0341', 'CEI'], ['EL13_ENG_0342', 'WV'], ['EL13_ENG_0347', 'NPD'], ['EL13_ENG_0352', 'BIS'], ['EL13_ENG_0353', 'TFF'], ['EL13_ENG_0356', 'ICA'], ['EL13_ENG_0376', 'RSA'], ['EL13_ENG_0393', 'TFF'], ['EL13_ENG_0394', 'BOS'], ['EL13_ENG_0400', 'PRC'], ['EL13_ENG_0409', 'FL'], ['EL13_ENG_0420', 'FNC'], ['EL13_ENG_0421', 'NZ'], ['EL13_ENG_0427', 'USF'], ['EL13_ENG_0435', 'SAR'], ['EL13_ENG_0436', 'BIS'], ['EL13_ENG_0442', 'ISF'], ['EL13_ENG_0444', 'PINSTRIPES'], ['EL13_ENG_0447', 'KC'], ['EL13_ENG_0450', 'PNC'], ['EL13_ENG_0457', 'JT'], ['EL13_ENG_0469', 'MD'], ['EL13_ENG_0475', 'KCC'], ['EL13_ENG_0480', 'NYJ'], ['EL13_ENG_0482', 'HKSAR'], ['EL13_ENG_0487', 'CFF'], ['EL13_ENG_0493', 'MMC'], ['EL13_ENG_0510', 'HSE'], ['EL13_ENG_0522', 'NCC'], ['EL13_ENG_0529', 'TTU'], ['EL13_ENG_0530', 'ADA'], ['EL13_ENG_0535', 'BCB'], ['EL13_ENG_0536', 'PNC'], ['EL13_ENG_0540', 'CFF'], ['EL13_ENG_0550', 'JT'], ['EL13_ENG_0551', 'NPA'], ['EL13_ENG_0557', 'CCF'], ['EL13_ENG_0560', 'KCC'], ['EL13_ENG_0598', 'NPH'], ['EL13_ENG_0602', 'FLA'], ['EL13_ENG_0605', 'AZ'], ['EL13_ENG_0619', 'CDL'], ['EL13_ENG_0622', 'CLEVELAND'], ['EL13_ENG_0624', 'VH'], ['EL13_ENG_0628', 'CCF'], ['EL13_ENG_0630', 'UA'], ['EL13_ENG_0642', 'LSU'], ['EL13_ENG_0645', 'FSU'], ['EL13_ENG_0646', 'CCF'], ['EL13_ENG_0658', 'GB'], ['EL13_ENG_0659', 'FRC'], ['EL13_ENG_0665', 'ADA'], ['EL13_ENG_0667', 'JT'], ['EL13_ENG_0672', 'FGR'], ['EL13_ENG_0676', 'FNC'], ['EL13_ENG_0682', 'DMV'], ['EL13_ENG_0686', 'NAACP'], ['EL13_ENG_0698', 'CFC'], ['EL13_ENG_0707', 'KCC'], ['EL13_ENG_0715', 'MRF'], ['EL13_ENG_0717', 'CCF'], ['EL13_ENG_0734', 'ASU'], ['EL13_ENG_0737', 'VCU'], ['EL13_ENG_0751', 'JT'], ['EL13_ENG_0752', 'MCD'], ['EL13_ENG_0754', 'MGMT'], ['EL13_ENG_0761', 'JT'], ['EL13_ENG_0765', 'AFC'], ['EL13_ENG_0770', 'NL'], ['EL13_ENG_0775', 'CSU'], ['EL13_ENG_0781', 'ICA'], ['EL13_ENG_0789', 'CNI'], ['EL13_ENG_0790', 'MCD'], ['EL13_ENG_0795', 'CMAG'], ['EL13_ENG_0805', 'JGL'], ['EL13_ENG_0806', 'SAS'], ['EL13_ENG_0824', 'NYG'], ['EL13_ENG_0830', 'ME'], ['EL13_ENG_0831', 'RM'], ['EL13_ENG_0836', 'FL'], ['EL13_ENG_0849', 'NPS'], ['EL13_ENG_0852', 'NTC'], ['EL13_ENG_0857', 'SINGAPOR'], ['EL13_ENG_0861', 'PNC'], ['EL13_ENG_0865', 'NFC'], ['EL13_ENG_0870', 'UA'], ['EL13_ENG_0875', 'ATD'], ['EL13_ENG_0885', 'MA'], ['EL13_ENG_0891', 'CFC'], ['EL13_ENG_0894', 'UCLA'], ['EL13_ENG_0919', 'CFC'], ['EL13_ENG_0926', 'NPS'], ['EL13_ENG_0927', 'TURKIYE'], ['EL13_ENG_0935', 'CFC'], ['EL13_ENG_0936', 'CFC'], ['EL13_ENG_0942', 'NJ'], ['EL13_ENG_0946', 'FSU'], ['EL13_ENG_0952', 'KPC'], ['EL13_ENG_0962', 'ICA'], ['EL13_ENG_0970', 'NTC'], ['EL13_ENG_0993', 'LA'], ['EL13_ENG_1004', 'ISI'], ['EL13_ENG_1006', 'JWOWW'], ['EL13_ENG_1011', 'BIEBER'], ['EL13_ENG_1017', 'PDL'], ['EL13_ENG_1027', 'PYONGYANG'], ['EL13_ENG_1031', 'SDS'], ['EL13_ENG_1037', 'NDC'], ['EL13_ENG_1039', 'NM'], ['EL13_ENG_1046', 'MRF'], ['EL13_ENG_1048', 'NPH'], ['EL13_ENG_1056', 'PCE'], ['EL13_ENG_1059', 'DAMASCUS'], ['EL13_ENG_1063', 'KCC'], ['EL13_ENG_1068', 'MIA'], ['EL13_ENG_1072', 'MCC'], ['EL13_ENG_1081', 'LDK'], ['EL13_ENG_1084', 'BND'], ['EL13_ENG_1093', 'MCC'], ['EL13_ENG_1111', 'TFF'], ['EL13_ENG_1112', 'JT'], ['EL13_ENG_1128', 'KCC'], ['EL13_ENG_1136', 'VA'], ['EL13_ENG_1137', 'MCD'], ['EL13_ENG_1139', 'NOLA'], ['EL13_ENG_1148', 'OK'], ['EL13_ENG_1152', 'NE'], ['EL13_ENG_1186', 'ADC'], ['EL13_ENG_1187', 'BRUINS'], ['EL13_ENG_1189', 'WI'], ['EL13_ENG_1196', 'NDF'], ['EL13_ENG_1208', 'BIS'], ['EL13_ENG_1211', 'ACLU'], ['EL13_ENG_1222', 'AK'], ['EL13_ENG_1230', 'ORLANDO'], ['EL13_ENG_1234', 'ASU'], ['EL13_ENG_1236', 'ADI'], ['EL13_ENG_1238', 'BASRAH'], ['EL13_ENG_1240', 'MOSUL'], ['EL13_ENG_1245', 'ISF'], ['EL13_ENG_1254', 'BOMMAS'], ['EL13_ENG_1262', 'MMC'], ['EL13_ENG_1276', 'UCI'], ['EL13_ENG_1284', 'MTS'], ['EL13_ENG_1285', 'ECFC'], ['EL13_ENG_1287', 'ACDC'], ['EL13_ENG_1288', 'CCF'], ['EL13_ENG_1290', 'TFF'], ['EL13_ENG_1299', 'ROK'], ['EL13_ENG_1305', 'SEAHAWKS'], ['EL13_ENG_1306', 'INDIANA'], ['EL13_ENG_1313', 'BIS'], ['EL13_ENG_1314', 'NDF'], ['EL13_ENG_1325', 'JT'], ['EL13_ENG_1328', 'JT'], ['EL13_ENG_1332', 'SYRIA'], ['EL13_ENG_1335', 'AFC'], ['EL13_ENG_1342', 'KHRUSHCHEV'], ['EL13_ENG_1353', 'SD'], ['EL13_ENG_1355', 'DALLAS'], ['EL13_ENG_1360', 'MHF'], ['EL13_ENG_1364', 'HSE'], ['EL13_ENG_1370', 'ISF'], ['EL13_ENG_1380', 'MCD'], ['EL13_ENG_1383', 'PA'], ['EL13_ENG_1385', 'PCE'], ['EL13_ENG_1388', 'LAL'], ['EL13_ENG_1408', 'JT'], ['EL13_ENG_1409', 'ADA'], ['EL13_ENG_1412', 'TX'], ['EL13_ENG_1415', 'IL'], ['EL13_ENG_1420', 'AUSTIN'], ['EL13_ENG_1424', 'CCF'], ['EL13_ENG_1425', 'ADC'], ['EL13_ENG_1438', 'TSU'], ['EL13_ENG_1440', 'COULTER'], ['EL13_ENG_1441', 'JT'], ['EL13_ENG_1456', 'SDS'], ['EL13_ENG_1478', 'DDCF'], ['EL13_ENG_1481', 'MOGADISHU'], ['EL13_ENG_1487', 'PNC'], ['EL13_ENG_1494', 'ADI'], ['EL13_ENG_1505', 'NC'], ['EL13_ENG_1507', 'CVC'], ['EL13_ENG_1508', 'OR'], ['EL13_ENG_1509', 'CNI'], ['EL13_ENG_1528', 'VALENCIA'], ['EL13_ENG_1539', 'USA'], ['EL13_ENG_1543', 'ICA'], ['EL13_ENG_1549', 'CCF'], ['EL13_ENG_1561', 'FNC'], ['EL13_ENG_1566', 'ROMANIA'], ['EL13_ENG_1567', 'BEIRUT'], ['EL13_ENG_1570', 'JAC'], ['EL13_ENG_1578', 'UNC'], ['EL13_ENG_1591', 'TAMPA'], ['EL13_ENG_1597', 'PNC'], ['EL13_ENG_1598', 'PNA'], ['EL13_ENG_1604', 'IPI'], ['EL13_ENG_1610', 'JT'], ['EL13_ENG_1615', 'NPA'], ['EL13_ENG_1619', 'CA'], ['EL13_ENG_1620', 'CFC'], ['EL13_ENG_1626', 'BELGRADE'], ['EL13_ENG_1636', 'CFF'], ['EL13_ENG_1642', 'FSF'], ['EL13_ENG_1652', 'FRC'], ['EL13_ENG_1658', 'MOGE'], ['EL13_ENG_1667', 'GSF'], ['EL13_ENG_1678', 'EU'], ['EL13_ENG_1680', 'BCB'], ['EL13_ENG_1682', 'NDC'], ['EL13_ENG_1683', 'KS'], ['EL13_ENG_1684', 'SF'], ['EL13_ENG_1685', 'NDC'], ['EL13_ENG_1692', 'HI'], ['EL13_ENG_1698', 'NCC'], ['EL13_ENG_1699', 'JT'], ['EL13_ENG_1721', 'NTC'], ['EL13_ENG_1729', 'CANADA'], ['EL13_ENG_1732', 'AFC'], ['EL13_ENG_1739', 'NAIROBI'], ['EL13_ENG_1749', 'JQA'], ['EL13_ENG_1756', 'SD'], ['EL13_ENG_1760', 'PSF'], ['EL13_ENG_1767', 'PDL'], ['EL13_ENG_1772', 'TEHRAN'], ['EL13_ENG_1796', 'KPC'], ['EL13_ENG_1797', 'CCF'], ['EL13_ENG_1805', 'PHILADELPHIA'], ['EL13_ENG_1818', 'VT'], ['EL13_ENG_1819', 'GSF'], ['EL13_ENG_1830', 'KCR'], ['EL13_ENG_1831', 'TFF'], ['EL13_ENG_1835', 'ACFC'], ['EL13_ENG_1843', 'NYC'], ['EL13_ENG_1846', 'CT'], ['EL13_ENG_1852', 'VT'], ['EL13_ENG_1858', 'WTF'], ['EL13_ENG_1875', 'MRF'], ['EL13_ENG_1876', 'USADA'], ['EL13_ENG_1879', 'HK'], ['EL13_ENG_1889', 'NO'], ['EL13_ENG_1892', 'CHI'], ['EL13_ENG_1895', 'ASU'], ['EL13_ENG_1902', 'CDL'], ['EL13_ENG_1906', 'SC'], ['EL13_ENG_1912', 'KABUL'], ['EL13_ENG_1922', 'MMC'], ['EL13_ENG_1924', 'SPAIN'], ['EL13_ENG_1932', 'BLAGOJEVICH'], ['EL13_ENG_1970', 'IPI'], ['EL13_ENG_1998', 'TSU'], ['EL13_ENG_2005', 'LFC'], ['EL13_ENG_2011', 'KHARTOUM'], ['EL13_ENG_2017', 'JGL'], ['EL13_ENG_2022', 'ADC'], ['EL13_ENG_2023', 'NTC'], ['EL13_ENG_2035', 'KSA'], ['EL13_ENG_2036', 'DENVER'], ['EL13_ENG_2039', 'TT'], ['EL13_ENG_2052', 'AROD'], ['EL13_ENG_2054', 'NDC'], ['EL13_ENG_2056', 'HERM'], ['EL13_ENG_2058', 'WMO'], ['EL13_ENG_2061', 'PSF'], ['EL13_ENG_2064', 'PSC'], ['EL13_ENG_2066', 'NDC'], ['EL13_ENG_2067', 'CMAG'], ['EL13_ENG_2071', 'ROME'], ['EL13_ENG_2073', 'LAC'], ['EL13_ENG_2082', 'ADC'], ['EL13_ENG_2086', 'MIA'], ['EL13_ENG_2088', 'LA'], ['EL13_ENG_2092', 'PNC'], ['EL13_ENG_2104', 'ICA'], ['EL13_ENG_2111', 'MMC'], ['EL13_ENG_2112', 'DUBAI'], ['EL13_ENG_2116', 'UAE'], ['EL13_ENG_2122', 'CPC'], ['EL13_ENG_2139', 'NCC'], ['EL13_ENG_2142', 'SDS'], ['EL13_ENG_2146', 'MCC'], ['EL13_ENG_2154', 'NYY'], ['EL13_ENG_2164', 'KOSOVO'], ['EL13_ENG_2172', 'ISLAMABAD'], ['EL13_ENG_2173', 'CFF'], ['EL13_ENG_2186', 'MCC'], ['EL13_ENG_2190', 'DPRK']]
    searchlist = returnsearchlist(test)          
    print searchlist