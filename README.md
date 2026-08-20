Controle PID com Velocidade Dinâmica - LEGO SPIKE Prime
Este repositório contém a implementação de um algoritmo de Controle PID (Proporcional, Integral e Derivativo) com Velocidade Dinâmica desenvolvido para robôs seguidores de linha utilizando o LEGO Education SPIKE Prime.

📌 Sobre o Projeto

O objetivo deste código é permitir um controle preciso da trajetória do robô em um seguidor de linha, ajustando automaticamente a velocidade de acordo com a complexidade da pista (curvas acentuadas vs. trechos retos).

🚀 Destaques do Algoritmo:

Controle Proporcional (KP): Corrige o desvio atual em relação à linha com base na leitura da luz refletida dos sensores (Sensor F e Sensor A).

Controle Integral (KI): Acumula erros passados para eliminar pequenos desvios sistemáticos.

Controle Derivativo (KD): Antecipa mudanças bruscas para suavizar a trajetória.

Velocidade Dinâmica: O robô calcula a intensidade da curva e reduz a velocidade base (vbase) em curvas fechadas (alto valor de correção) e acelera em trechos retos (vmax) para otimizar o tempo de percurso.

🛠️ Variáveis Utilizadas

KP: Ganho Proporcional (Ex: 1.5)

KI: Ganho Integral (Ex: 0.1)

KD: Ganho Derivativo (Ex: 0.5)

KM: Coeficiente de Redução de Velocidade (Ex: 2)

error: Diferença entre as leituras dos sensores (Luz F - Luz A)

integral: Acúmulo dos erros passados

derivada: Taxa de variação do erro (error - lasterror)

correcao: Valor total de correção calculado pelo algoritmo

vbase: Velocidade base atual dos motores

vmax: Velocidade máxima para trechos retos (Ex: 20)

vmin: Velocidade mínima para curvas (Ex: 10)

lasterror: Registro do erro da iteração anterior

🧠 Lógica do Algoritmo (Word Blocks)

Inicialização: Configuração da cor da luz do Hub e ajuste de ganhos iniciais.

Leitura e Cálculo do Erro:
error = Luz Refletida (Sensor F) - Luz Refletida (Sensor A)

Integral e Derivada:
integral = (error + integral) * 0.5
derivada = error - lasterror

Cálculo da Correção PID:
correcao = (KP * error) - (KI * integral) + (KD * derivada)

Ajuste Dinâmico da Velocidade (vbase):
vbase = vmax - (modulo de correcao * KM)
Se vbase for menor que vmin, a velocidade base é travada no limite inferior (vmin) e o LED do botão central muda de cor para sinalizar a curva acentuada.

Atuação nos Motores:
Ajusta a velocidade de movimento para vbase %.
Aplica a movimentação direcional combinando os ganhos com o erro, integral e derivada.
Atualiza lasterror = error.

📂 Arquivos no Repositório

README.md: Documentação explicativa do algoritmo.

LICENSE: Licença Creative Commons (CC BY-NC 4.0).

teste_pid.llsp3: Arquivo original do projeto para importar no aplicativo LEGO SPIKE.

📜 Licença

Este projeto é de código aberto e está licenciado sob a Creative Commons Atribuição-NãoComercial 4.0 Internacional (CC BY-NC 4.0).

Você é livre para utilizar, adaptar e compartilhar este código para fins educacionais ou de estudo, desde que dê o devido crédito ao autor. É proibido o uso ou venda comercial deste projeto.
