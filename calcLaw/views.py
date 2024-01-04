import json
from django.shortcuts import render, get_object_or_404, get_list_or_404
import logging
from calcLaw.get_Law import Servo
from systemStewartPlatform.models import law_for_platform, stewart_platform, system_stewart_platform

logger = logging.getLogger('TEST_LOGGER_NAME')

def systemLawView(request, pk):
    logger.info("Сформирован закон движения")
    law = get_object_or_404(law_for_platform, pk=pk)
    SERVO_HORN = 40
    SERVO_ROD = 200
    BASE_RADIUS = 100
    PLATFORM_RADIUS = 100
    SERVO_DEFAULT_ANGLE_LIST = [0,0,0,0,0,0]
    BASE_ANGLE_PIVOT_LIST = [30,90,150,210,270,330]
    HORN_ANGLE_BASE_LIST = [270,210,30,330,150,90]
    PLATFORM_DEFAULT_HEIGHT = 195
    BASE_DEFAULT_HEIGHT = 0

    DX = law.dx
    DY = law.dy
    DZ = law.dz
    PHI = law.phi
    THETA = law.theta
    PSI = law.psi

    servo0 = Servo(radius=BASE_RADIUS, height=BASE_DEFAULT_HEIGHT, base_angle_pivot=BASE_ANGLE_PIVOT_LIST[0],
                                platform_height=PLATFORM_DEFAULT_HEIGHT, horn_length=SERVO_HORN, rod_length=SERVO_ROD,
                                horn_angle=SERVO_DEFAULT_ANGLE_LIST[0], horn_angle_base=HORN_ANGLE_BASE_LIST[0],
                                dx=DX, dy=DY, dz=DZ, phi=PHI, psi=PSI,theta=THETA)

    servo1 = Servo(radius=BASE_RADIUS, height=BASE_DEFAULT_HEIGHT, base_angle_pivot=BASE_ANGLE_PIVOT_LIST[1],
                                platform_height=PLATFORM_DEFAULT_HEIGHT, horn_length=SERVO_HORN, rod_length=SERVO_ROD,
                                horn_angle=SERVO_DEFAULT_ANGLE_LIST[1], horn_angle_base=HORN_ANGLE_BASE_LIST[1],
                                dx=DX, dy=DY, dz=DZ, phi=PHI, psi=PSI,theta=THETA)

    servo2 = Servo(radius=BASE_RADIUS, height=BASE_DEFAULT_HEIGHT, base_angle_pivot=BASE_ANGLE_PIVOT_LIST[2],
                                platform_height=PLATFORM_DEFAULT_HEIGHT, horn_length=SERVO_HORN, rod_length=SERVO_ROD,
                                horn_angle=SERVO_DEFAULT_ANGLE_LIST[2], horn_angle_base=HORN_ANGLE_BASE_LIST[2],
                                dx=DX, dy=DY, dz=DZ, phi=PHI, psi=PSI,theta=THETA)

    servo3 = Servo(radius=BASE_RADIUS, height=BASE_DEFAULT_HEIGHT, base_angle_pivot=BASE_ANGLE_PIVOT_LIST[3],
                                platform_height=PLATFORM_DEFAULT_HEIGHT, horn_length=SERVO_HORN, rod_length=SERVO_ROD,
                                horn_angle=SERVO_DEFAULT_ANGLE_LIST[3], horn_angle_base=HORN_ANGLE_BASE_LIST[3],
                                dx=DX, dy=DY, dz=DZ, phi=PHI, psi=PSI,theta=THETA)

    servo4 = Servo(radius=BASE_RADIUS, height=BASE_DEFAULT_HEIGHT, base_angle_pivot=BASE_ANGLE_PIVOT_LIST[4],
                                platform_height=PLATFORM_DEFAULT_HEIGHT, horn_length=SERVO_HORN, rod_length=SERVO_ROD,
                                horn_angle=SERVO_DEFAULT_ANGLE_LIST[4], horn_angle_base=HORN_ANGLE_BASE_LIST[4],
                                dx=DX, dy=DY, dz=DZ, phi=PHI, psi=PSI,theta=THETA)

    servo5 = Servo(radius=BASE_RADIUS, height=BASE_DEFAULT_HEIGHT, base_angle_pivot=BASE_ANGLE_PIVOT_LIST[5],
                                platform_height=PLATFORM_DEFAULT_HEIGHT, horn_length=SERVO_HORN, rod_length=SERVO_ROD,
                                horn_angle=SERVO_DEFAULT_ANGLE_LIST[5], horn_angle_base=HORN_ANGLE_BASE_LIST[5],
                                dx=DX, dy=DY, dz=DZ, phi=PHI, psi=PSI,theta=THETA)

    ser0 = servo0.get_angle_of_rod()
    ser1 = servo1.get_angle_of_rod()
    ser2 = servo2.get_angle_of_rod()
    ser3 = servo3.get_angle_of_rod()
    ser4 = servo4.get_angle_of_rod()
    ser5 = servo5.get_angle_of_rod()
    value = [ser0, ser1, ser2, ser3, ser4, ser5]
    lawOK = json.dumps(value)
    data = {
        'title': law.law_type_plat,
        'lawOK': lawOK
    }
    if law.discription_lawJSON is None:
        law.discription_lawJSON = lawOK
        law.save()
    else:
        law.discription_lawJSON = law.discription_lawJSON+lawOK
        law.save()
    return render(request, 'systemStewartPlatform/system/systemLawView.html', data)

def ForFullLaw(request, pk):
    global a
    system = get_object_or_404(system_stewart_platform, pk=pk)
    platform = get_list_or_404(stewart_platform, system_stewart_platform=system)
    checkLaw = {}
    i=0
    e=0
    while i<len(platform):
        checkLaw[e] = platform[i].title_platform + ": " + platform[i].law_type.discription_lawJSON
        e=e+1
        i=i+1
    data = {
        'title': system.title_system,
        'lawOK': checkLaw
    }
    if system.discription_systemJSON is None:
        system.discription_systemJSON = checkLaw
        system.save()
    else:
        system.discription_systemJSON = system.discription_systemJSON+checkLaw
        system.save()
    return render(request, 'systemStewartPlatform/system/systemLawView.html', data)