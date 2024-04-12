#APENAS AUTÔMATO COM VISUALIZAÇÃO DO DIAGRAMA E TABELA
!pip install automathon --upgrade
!pip install pandas
!pip install matplotlib

from automathon import DFA
import pandas as pd
import matplotlib.pyplot as plt

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

  df = pd.DataFrame(delta).fillna('-')
  df = df.T
  plt.figure(figsize=(8, 6))
  plt.table(cellText=df.values,
            colLabels=df.columns,
            rowLabels=df.index,
            loc='center',
            cellLoc='center',
            colWidths=[0.15] * len(df.columns))
  plt.axis('off')
  plt.savefig('tabela_transicoes_afd_alarme.png', bbox_inches='tight', pad_inches=0.05)
  plt.show()