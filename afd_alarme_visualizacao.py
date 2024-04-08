#APENAS AUTÔMATO COM VISUALIZAÇÃO
!pip install automathon --upgrade
from automathon import DFA

Q = {'DESARMADO', 'DIURNO', 'NOTURNO', 'TOTAL', 'DISPARADO'}
sigma = {'a', 'd', 'i', 'e'}
delta = { 'DESARMADO' : {'a' : 'DIURNO',    'd' : 'DESARMADO', 'i' : 'DESARMADO', 'e' : 'DESARMADO'},
          'DIURNO'    : {'a' : 'NOTURNO',   'd' : 'DESARMADO', 'i' : 'DISPARADO', 'e' : 'DIURNO'},
          'NOTURNO'   : {'a' : 'TOTAL',     'd' : 'DESARMADO', 'i' : 'NOTURNO',   'e' : 'DISPARADO'},
          'TOTAL'     : {'a' : 'TOTAL',     'd' : 'DESARMADO', 'i' : 'DISPARADO', 'e' : 'DISPARADO'},
          'DISPARADO' : {'a' : 'DISPARADO', 'd' : 'DESARMADO', 'i' : 'DISPARADO', 'e' : 'DISPARADO'}
        }
initial_state = 'DESARMADO'
F = {}

automata = DFA(Q, sigma, delta, initial_state, F)

if automata.is_valid():
  automata.view(
      file_name="AFD_alarme_residencial",
      node_attr={'fontsize': '20'},
      edge_attr={'fontsize': '20pt'}
  )