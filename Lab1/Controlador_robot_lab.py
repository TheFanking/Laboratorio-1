from controller import Robot
import math

robot = Robot()
timestep = int(robot.getBasicTimeStep())

left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

#Cambiar entre el 1,2,3 o el 4 para los
#Desafios
DESAFIO = 4


base_speed = 3.14

wheel_radius = 0.0205
distance_between_wheels = 0.052
length_side = 0.25
num_side = 4

linear_velocity = wheel_radius * base_speed
duration_side = length_side / linear_velocity

angle_of_rotation = (2 * math.pi) / num_side
rate_of_rotation = (2 * linear_velocity) / distance_between_wheels
duration_turn = (angle_of_rotation / rate_of_rotation) * 1.04

while robot.step(timestep) != -1:
    current_time = robot.getTime()
    vl, vr = 0.0, 0.0

    if DESAFIO == 1:#recto
        vl, vr = base_speed, base_speed 

    elif DESAFIO == 2:#curva
        vl, vr = base_speed * 0.90, base_speed 

    elif DESAFIO == 3:#circulo
        vl, vr = 2.0, 5.0 

    elif DESAFIO == 4:#cuadrado
        cycle_time = duration_side + duration_turn
        phase = current_time % cycle_time

        if phase < duration_side:
            vl = base_speed
            vr = base_speed
        else:
            vl = -base_speed
            vr = base_speed

    elif DESAFIO == 5:
        if (current_time % 10.0) < 5.0:
            vl, vr = 5.0, 1.5 
        else:
            vl, vr = 1.5, 5.0 

    left_motor.setVelocity(vl)
    right_motor.setVelocity(vr)
