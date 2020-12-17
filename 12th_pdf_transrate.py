#(1)googletrans        ...Google翻訳、学習中
#---------------------------------------------------始めていきましょう！
# -*- coding: utf-8 -*-
# translator = Translator()
# translation = translator.translate("Der Himmel ist blau und ich mag Bananen", dest='en')
# print(translation.text)
from googletrans import Translator
import sys #システムパラメータと関数¶

args= sys.argv
if len(args) < 2:
    print('Command should be like')
    print('python3 this.py textfile.txt')
else:
    print('open '+args[1])
    f = open(args[1])
    lines = f.readlines()
    f.close()

    translator = Translator()
    for line in lines:
        print(line) # English            #-----------------------?
        translated = translator.translate(line, dest="ja");
        print(translated.text) # Japanese#-----------------------?
        print()
    print('finished')