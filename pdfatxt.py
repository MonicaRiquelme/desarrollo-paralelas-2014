# -*- coding: utf-8 -*-
import sys
import random
import commands
import re


print "Transformando de pdf a txt... " + sys.argv[1]
#pasamos el pdf por argumento
comando = commands.getoutput("pdftotext "+sys.argv[1])
txt= sys.argv[1].replace(".pdf", ".txt");
#eliminamos tildes y la ñ
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
#eliminams todo menos letras
new_str = re.sub('[^a-zA-Z]', '', string)
#todo a minusculas
str = new_str.lower()
open(txt, 'w').write(str)
#str = 'todotextounidosinnada....'
