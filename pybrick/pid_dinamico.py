from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.parameters import Direction, Port, Color
from pybricks.tools import wait

hub = PrimeHub()

# Motores
motor_esq = Motor(Port.B, Direction.COUNTERCLOCKWISE)
motor_dir = Motor(Port.C, Direction.CLOCKWISE)

# Sensores
sensor_esq = ColorSensor(Port.E)
sensor_dir = ColorSensor(Port.A)

# PID
kp = 5
ki = 0.0 # Ki ajustado para um valor menor (evita estouro)
kd = 2.5
km = 4  # Ajustado para a nova escala de velocidade

error = 0
integral = 0
derivada = 0
last_error = 0

# Velocidades (em graus por segundo - deg/s)
Vbase = 0
Vmax = 300
Vmin = 80


while True:
  # 1. Leitura correta dos dois sensores
  reflexo_esq = sensor_esq.reflection()
  reflexo_dir = sensor_dir.reflection()

    

  # 2. Cálculo do PID
  error = reflexo_esq - reflexo_dir

  # Limita a integral para evitar acúmulo excessivo (Anti-Windup)
  integral += error
  if integral > 100:
    integral = 100
  elif integral < -100:
    integral = -100

  derivada = error - last_error
  pid = (kp * error) + (ki * integral) + (kd * derivada)
  last_error = error

  # 3. Correção de velocidade dinâmica
  Vbase = Vmax - (abs(pid) * km)
  if Vbase < Vmin:
    Vbase = Vmin

  # 4. Aplicação nos motores (Sinais corrigidos para virar corretamente)
  motor_esq.run(int(Vbase + pid))
  motor_dir.run(int(Vbase - pid))


  wait(10)