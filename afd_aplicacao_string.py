#AUTÔMATO COM TESTE DE STRING
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
  seq_valida = True
  string = input("\nDigite a sequência de comandos: ").lower()
  estado_atual = 'DESARMADO'

  print("\nSeja bem-vindo à central de alarme!\n")
  print(f"A sua sequência de comandos é {string}\n")

  for c in string:
    if c in sigma:
      estado_ant = estado_atual
      estado_atual = automata.delta[estado_atual][c]

      print(f"Com o comando {c}, o autômato ", end="")

      if estado_ant == estado_atual:
        print(f"permanece no estado {estado_atual}")
      else:
        print(f"vai do estado {estado_ant} para o estado {estado_atual}")
    else:
      print("\n*****ATENÇÃO! INDETERMINAÇÃO NO AUTÔMATO*****")
      print(f"A simulação foi encerrada pois o comando {c} não é válido!\n")
      seq_valida = not seq_valida
      break
  if seq_valida:
    print(f"\nAssim, essa sequência de comandos finaliza no estado {estado_atual}\n")