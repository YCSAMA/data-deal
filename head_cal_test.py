import numpy as np
import math

E = 1.96*10**5
mu = 0.3
np.set_printoptions(precision=3, suppress=True)

'''
#椭圆0.2
test_strain_phi = np.array([26.8,28.7,31.3,15.3,15.3,1.3,5.1,24.9])*10**-6
test_strain_theta = np.array([26.8,26.8,18.5,-1.9,-13.4,-21.1,0.6,24.9])*10**-6
'''
'''
#椭圆0.4
test_strain_phi = np.array([53.6,59.4,64.5,32.6,31.3,2.5,11.5,51.7])*10**-6
test_strain_theta = np.array([53.6,55.5,35.8,-1.9,-28.7,-43.4,-16.6,53.6])*10**-6
'''
'''
#椭圆0.6
test_strain_phi = np.array([80.4,90.0,97.7,47.9,46.0,4.4,15.3,76.6])*10**-6
test_strain_theta = np.array([80.4,84.3,57.4,-1.9,-40.2,-63.2,-72.8,80.4])*10**-6
'''
'''
#椭圆0.8
test_strain_phi = np.array([107.2,118.7,130.2,63.2,61.9,7.0,22.4,101.5])*10**-6
test_strain_theta = np.array([107.2,113.0,76.6,-1.9,-51.7,-84.3,-75.3,107.2])*10**-6
'''
'''
#椭圆1
test_strain_phi = np.array([134.0,149.4,162.8,80.4,78.5,7.7,26.8,126.4])*10**-6
test_strain_theta = np.array([134,143.6,95.7,-1.9,-65.1,-105.3,-79.8,134.7])*10**-6
'''
'''
#平盖0.2
test_strain_phi = np.array([32.6,27.4,21.1,9.6,0,0,0])*10**-6
test_strain_theta = np.array([32.6,14,28.1,15.3,19.1,0,-1.9])*10**-6
'''
'''
#平盖0.4
test_strain_phi = np.array([56.1,48.5,37.7,17.8,-0.6,0,-1.3])*10**-6
test_strain_theta = np.array([56.1,26.8,51.7,27.4,36.4,-2.5,-3.8])*10**-6
'''
'''
#平盖0.6
test_strain_phi = np.array([86.8,75.3,54.2,26.8,-0.6,0,-3.8])*10**-6
test_strain_theta = np.array([86.8,44,76.6,40.2,53.6,4.4,-7.7])*10**-6
'''
'''
#平盖0.8
test_strain_phi = np.array([120.6,105.3,72.8,36.4,3.2,0,-5.7])*10**-6
test_strain_theta = np.array([120.6,63.2,102.8,55.5,71.5,17.8,-9.6])*10**-6
'''
'''
#平盖1
test_strain_phi = np.array([149.4,129.6,91.3,44.7,3.8,0,-7.7])*10**-6
test_strain_theta = np.array([149.4,79.8,128.3,69.6,90.0,21.7,-13.4])*10**-6
'''
'''
#蝶形0.2
test_strain_phi = np.array([26.8,28.1,26.2,19.1,3.8,1.3,3.2,23])*10**-6
test_strain_theta = np.array([26.8,21.7,18.5,1.9,-10.9,-14.0,-1.3,24.9])*10**-6
'''
'''
#蝶形0.4
test_strain_phi = np.array([56.1,56.8,53.6,39.6,8.3,4.4,6.4,50.4])*10**-6
test_strain_theta = np.array([56.1,44.7,37.0,3.8,-20.4,-27.4,-1.3,51.1])*10**-6
'''
'''
#蝶形0.6
test_strain_phi = np.array([82.3,84.3,78.5,57.4,11.5,5.7,7.7,74.4])*10**-6
test_strain_theta = np.array([82.3,65.1,54.2,3.8,-32.6,-42.1,-3.8,74.7])*10**-6
'''
'''
#蝶形0.8
test_strain_phi = np.array([108.5,111.1,103.4,76.6,15.3,7.7,9.6,101.5])*10**-6
test_strain_theta = np.array([108.5,86.2,70.9,3.8,-42.7,-56.1,-6.4,99.6])*10**-6
'''
'''
#蝶形1
test_strain_phi = np.array([136.0,139.2,129.6,97.0,19.1,10.2,12.8,126.4])*10**-6
test_strain_theta = np.array([136.0,108.5,89.4,4.4,-54.2,-71.5,-8.3,125.8])*10**-6
'''
'''
#筒体锥头0.2
test_strain_phi = np.array([7.7,10.9,12.1,12.1,12.8,9.6,10.2,9,7.7,7])*10**-6
test_strain_theta = np.array([18.5,18.5,19.8,22.4,26.2,30.0,31.3,33.9,34.5,30.6])*10**-6
'''
'''
#筒体锥头0.4
test_strain_phi = np.array([15.9,21.7,23.6,23.6,23.6,18.5,19.8,17.8,14,14])*10**-6
test_strain_theta = np.array([37,35.1,37,42.1,48.5,56.8,58.1,62.6,62.6,56.1])*10**-6
'''
'''
#锥头0.6
test_strain_phi = np.array([19.8,28.7,32.6,32.6,32.6,23.6,26.8,23,18.5,17.2])*10**-6
test_strain_theta = np.array([51.7,47.9,51.7,59.4,69.6,82.3,84.3,90,90,80.4])*10**-6
'''
'''
#锥头0.8
test_strain_phi = np.array([26.8,38.3,42.1,42.1,42.1,32.6,34.5,31.3,24.9,24.3])*10**-6
test_strain_theta = np.array([68.3,64.5,68.9,79.1,91.9,108.5,113,120.6,120.6,107.2])*10**-6
'''
#锥头1
test_strain_phi = np.array([60063.3,42.1,49.8,51.1,52.3,44,47.9,41.5,30.6,30.6])*10**-6
test_strain_theta = np.array([76.6,76.0,83.6,98.3,114.9,139.8,145.5,152.6,150.7,133.4])*10**-6

test_stress_phi = E/(1-mu**2)*(test_strain_phi+mu*test_strain_theta)
test_stress_theta = E/(1-mu**2)*(test_strain_theta+mu*test_strain_phi)

print(test_stress_phi)
print(test_stress_theta)