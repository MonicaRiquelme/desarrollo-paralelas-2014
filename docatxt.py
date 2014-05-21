# -*- coding: utf-8 -*-
import sys
import random
import commands
import re
#caso doc
print "Transformando de doc a txt... " + sys.argv[1]
#Pasamos el .doc como argumento.
txt= sys.argv[1].replace(".doc", ".txt");
#eliminamos tildes de minusculas y mayusculas y la ñ
comando = commands.getoutput("catdoc "+sys.argv[1]+" > "+txt)
comando = commands.getoutput("perl -pi -e 's[á][a]g' "+txt)
comando = commands.getoutput("perl -pi -e 's[é][e]g' "+txt)
comando = commands.getoutput("perl -pi -e 's[í][i]g' "+txt)
comando = commands.getoutput("perl -pi -e 's[ó][o]g' "+txt)
comando = commands.getoutput("perl -pi -e 's[ú][u]g' "+txt)
comando = commands.getoutput("perl -pi -e 's[Á][a]g' "+txt)
comando = commands.getoutput("perl -pi -e 's[É][e]g' "+txt)
comando = commands.getoutput("perl -pi -e 's[Í][i]g' "+txt)
comando = commands.getoutput("perl -pi -e 's[Ó][o]g' "+txt)
comando = commands.getoutput("perl -pi -e 's[Ú][u]g' "+txt)
comando = commands.getoutput("perl -pi -e 's[ñ][n]g' "+txt)
comando = commands.getoutput("perl -pi -e 's[Ñ][n]g' "+txt)

string = open(txt).read()
#eliminamos todo menos letras minusculas y mayusculas
new_str = re.sub('[^a-zA-Z]', '', string)
#dejamos todo en minusculas
str = new_str.lower()
open(txt, 'w').write(str)
#al final str = 'muchasletrasjuntassinespacio.....'
