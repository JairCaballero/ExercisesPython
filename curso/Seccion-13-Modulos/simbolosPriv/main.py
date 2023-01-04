#al importar un modulo este se convierte en objeto
#y las variables dentro de este pasan a ser parte del objeto
#nombres precedidos con barrabajo no seran copiados a menos que se importen uno a uno
# las variables con _ son de uso local(privado) solo para ese archivo por ende el no las importa


from herramientas  import *
from pprint import pprint
#from herramientas import _a

pprint(globals())