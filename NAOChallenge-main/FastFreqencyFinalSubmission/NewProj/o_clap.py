from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.333333, 0.666667, 1, 1.44444, 1.77778, 2.22222, 2.66667, 3.11111, 3.44444, 3.88889, 4.22222, 4.55556])
keys.append([0.121144, 0.121144, -0.230143, 0.0996681, -0.0859459, 0.139552, 0.138018, 0.136484, -0.185656, 0.118076, -0.185656, 0])

names.append("HeadYaw")
times.append([0.333333, 0.666667, 1, 1.44444, 1.77778, 2.22222, 2.66667, 3.11111, 3.44444, 3.88889, 4.22222, 4.55556])
keys.append([0.091998, 0.093532, 0.105804, 0.0812601, 0.54146, -0.18719, -0.737896, -0.0690719, -0.0798099, -0.075208, -0.0798099, -0.00148157])

names.append("LAnklePitch")
times.append([0.333333, 0.666667, 1, 1.44444, 1.77778, 2.22222, 2.66667, 3.11111, 3.44444, 3.88889, 4.22222, 4.55556])
keys.append([0.0291041, 0.010696, -4.19617e-05, -0.00617796, -0.021518, -0.0245859, -0.032256, -0.00771196, -0.00924597, -0.00617796, -0.00924597, -0.343734])

names.append("LAnkleRoll")
times.append([0.333333, 0.666667, 1, 1.44444, 1.77778, 2.22222, 2.66667, 3.11111, 3.44444, 3.88889, 4.22222, 4.55556])
keys.append([-0.067454, -0.0735901, -0.075124, -0.0735901, -0.075124, -0.075124, -0.078192, -0.075124, -0.0735901, -0.0735901, -0.0735901, -0.00538947])

names.append("LElbowRoll")
times.append([0.333333, 0.666667, 1, 1.44444, 1.77778, 2.22222, 2.66667, 3.11111, 3.44444, 3.88889, 4.22222, 4.55556])
keys.append([-0.659577, -0.71787, -0.724006, -1.00473, -0.438682, -0.843657, -0.421808, -0.860533, -0.496974, -0.770025, -0.496974, -1.00097])

names.append("LElbowYaw")
times.append([0.333333, 0.666667, 1, 1.44444, 1.77778, 2.22222, 2.66667, 3.11111, 3.44444, 3.88889, 4.22222, 4.55556])
keys.append([-1.02475, -0.605971, -0.607505, -0.43263, -0.470981, -0.472515, -0.506262, -0.480184, -0.497058, -0.451038, -0.497058, -1.3869])

names.append("LHand")
times.append([0.333333, 0.666667, 1, 1.44444, 1.77778, 2.22222, 2.66667, 3.11111, 3.44444, 3.88889, 4.22222, 4.55556])
keys.append([57.2958, 57.2958, 57.2958, 1, 57.2958, 57.2958, 57.2958, 57.2958, 57.2958, 57.2958, 57.2958, 0.25])

names.append("LHipPitch")
times.append([0.333333, 0.666667, 1, 1.44444, 1.77778, 2.22222, 2.66667, 3.11111, 3.44444, 3.88889, 4.22222, 4.55556])
keys.append([0.452573, 0.460242, 0.460242, 0.458707, 0.460242, 0.455639, 0.464844, 0.46331, 0.477115, 0.467912, 0.477115, -0.45])

names.append("LHipRoll")
times.append([0.333333, 0.666667, 1, 1.44444, 1.77778, 2.22222, 2.66667, 3.11111, 3.44444, 3.88889, 4.22222, 4.55556])
keys.append([0.119694, 0.121228, 0.119694, 0.119694, 0.121228, 0.119694, 0.121228, 0.121228, 0.121228, 0.119694, 0.121228, 0.00225446])

names.append("LHipYawPitch")
times.append([0.333333, 0.666667, 1, 1.44444, 1.77778, 2.22222, 2.66667, 3.11111, 3.44444, 3.88889, 4.22222, 4.55556])
keys.append([-0.371186, -0.343573, -0.345107, -0.348176, -0.348176, -0.34971, -0.338973, -0.335904, -0.322099, -0.317496, -0.322099, -0.00594032])

names.append("LKneePitch")
times.append([0.333333, 0.666667, 1, 1.44444, 1.77778, 2.22222, 2.66667, 3.11111, 3.44444, 3.88889, 4.22222, 4.55556])
keys.append([-0.0923279, -0.0923279, -0.0923279, -0.0923279, -0.0923279, -0.0923279, -0.0923279, -0.0923279, -0.0923279, -0.0923279, -0.0923279, 0.699999])

names.append("LShoulderPitch")
times.append([0.333333, 0.666667, 1, 1.44444, 1.77778, 2.22222, 2.66667, 3.11111, 3.44444, 3.88889, 4.22222, 4.55556])
keys.append([1.68429, 0.46476, 0.467829, 0.516916, 0.418739, 0.394197, 0.371186, 0.472429, 0.446352, 0.434081, 0.446352, 1.3967])

names.append("LShoulderRoll")
times.append([0.333333, 0.666667, 1, 1.44444, 1.77778, 2.22222, 2.66667, 3.11111, 3.44444, 3.88889, 4.22222, 4.55556])
keys.append([0.216252, 0.944902, 0.937231, 0.05825, 0.931096, -0.124296, 0.926494, -0.135034, 0.917291, -0.14884, 0.917291, 0.300931])

names.append("LWristYaw")
times.append([0.333333, 0.666667, 1, 1.44444, 1.77778, 2.22222, 2.66667, 3.11111, 3.44444, 3.88889, 4.22222, 4.55556])
keys.append([-0.768577, -0.768577, -0.768577, -0.770111, -0.768577, -0.768577, -0.768577, -0.770111, -0.768577, -0.770111, -0.768577, -0.00264529])

names.append("RAnklePitch")
times.append([0.333333, 0.666667, 1, 1.44444, 1.77778, 2.22222, 2.66667, 3.11111, 3.44444, 3.88889, 4.22222, 4.55556])
keys.append([0.0782759, 0.0690719, 0.058334, 0.0537319, 0.0414599, 0.038392, 0.030722, 0.0537319, 0.0598679, 0.0537319, 0.0598679, -0.342427])

names.append("RAnkleRoll")
times.append([0.333333, 0.666667, 1, 1.44444, 1.77778, 2.22222, 2.66667, 3.11111, 3.44444, 3.88889, 4.22222, 4.55556])
keys.append([0.0767419, 0.084412, 0.084412, 0.084412, 0.0859459, 0.0890139, 0.093616, 0.0890139, 0.090548, 0.090548, 0.090548, 0.00647707])

names.append("RElbowRoll")
times.append([0.333333, 0.666667, 1, 1.44444, 1.77778, 2.22222, 2.66667, 3.11111, 3.44444, 3.88889, 4.22222, 4.55556])
keys.append([0.368202, 0.794654, 0.833004, 1.16435, 0.799256, 1.11219, 0.889762, 1.2748, 1.22724, 1.26559, 1.22724, 1.01917])

names.append("RElbowYaw")
times.append([0.333333, 0.666667, 1, 1.44444, 1.77778, 2.22222, 2.66667, 3.11111, 3.44444, 3.88889, 4.22222, 4.55556])
keys.append([0.914223, 0.656511, 0.656511, 0.536858, 0.602819, 0.596684, 0.638103, 0.538392, 0.665714, 0.469363, 0.665714, 1.38749])

names.append("RHand")
times.append([0.333333, 0.666667, 1, 1.44444, 1.77778, 2.22222, 2.66667, 3.11111, 3.44444, 3.88889, 4.22222, 4.55556])
keys.append([57.2958, 57.2958, 57.2958, 1, 57.2958, 57.2958, 57.2958, 57.2958, 57.2958, 57.2958, 57.2958, 0.25])

names.append("RHipPitch")
times.append([0.333333, 0.666667, 1, 1.44444, 1.77778, 2.22222, 2.66667, 3.11111, 3.44444, 3.88889, 4.22222, 4.55556])
keys.append([0.377323, 0.375789, 0.375789, 0.37272, 0.374254, 0.37272, 0.378857, 0.377323, 0.378857, 0.378857, 0.378857, -0.45])

names.append("RHipRoll")
times.append([0.333333, 0.666667, 1, 1.44444, 1.77778, 2.22222, 2.66667, 3.11111, 3.44444, 3.88889, 4.22222, 4.55556])
keys.append([-0.122678, -0.124212, -0.124212, -0.124212, -0.124212, -0.124212, -0.124212, -0.124212, -0.125746, -0.125746, -0.125746, -0.00217122])

names.append("RKneePitch")
times.append([0.333333, 0.666667, 1, 1.44444, 1.77778, 2.22222, 2.66667, 3.11111, 3.44444, 3.88889, 4.22222, 4.55556])
keys.append([-0.0812601, -0.0812601, -0.0812601, -0.0812601, -0.0812601, -0.0812601, -0.0812601, -0.0797261, -0.0812601, -0.0812601, -0.0812601, 0.699999])

names.append("RShoulderPitch")
times.append([0.333333, 0.666667, 1, 1.44444, 1.77778, 2.22222, 2.66667, 3.11111, 3.44444, 3.88889, 4.22222, 4.55556])
keys.append([1.53251, 0.435699, 0.435699, 0.490923, 0.426494, 0.405018, 0.401949, 0.521602, 0.510863, 0.535408, 0.510863, 1.39694])

names.append("RShoulderRoll")
times.append([0.333333, 0.666667, 1, 1.44444, 1.77778, 2.22222, 2.66667, 3.11111, 3.44444, 3.88889, 4.22222, 4.55556])
keys.append([-0.14884, -0.974133, -0.944986, -0.250085, -1.06157, -0.257754, -1.09072, -0.335988, -1.14134, -0.389678, -1.14134, -0.302905])

names.append("RWristYaw")
times.append([0.333333, 0.666667, 1, 1.44444, 1.77778, 2.22222, 2.66667, 3.11111, 3.44444, 3.88889, 4.22222, 4.55556])
keys.append([1.06149, 0.920358, 0.921892, 0.935697, 0.937231, 1.0262, 1.03081, 1.10751, 1.09523, 1.16733, 1.09523, 0.00864514])

# copy paste the printed value and uncomment
keysValue = [0.27728374932829286, 21.120515048696664, 0.03269801236078676, 0.2189875865504537, 0.41467410361962936, 0.4680490603882603, 0.21180898101056378]
finalPositionValue = [-1.3869, 0.25, 0.00225446, 0.699999, 1.3967, 0.300931, -0.00264529]