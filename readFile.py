def read_file(filename):
    tonnetz_list = []
    zero_crossing_rate_list = []
    tempo_list = []
    spectral_centroid_list = []
    spectral_contrast_list = []

    #loops through each line in the file sent
    for line in open(filename, 'r'):
        #splits each of the 5 elements
        te, s, z, t,c = line.strip().split(',')
        #appending the right value to each list
        tonnetz_list.append(t)
        zero_crossing_rate_list.append(z)
        tempo_list.append(te)
        spectral_centroid_list.append(s)
        spectral_contrast_list.append(c)


    #blank lists to append the final data
    z_list = []
    te_list = []
    s_list = []
    t_list = []
    c_list = []

    #loops through each list with the string values, and converts it to floats so calculations can be done later on
    for i in range(1, len(zero_crossing_rate_list)):
        z_list.append(float(zero_crossing_rate_list[i]))

    for i in range(1, len(tempo_list)):
        te_list.append(float(tempo_list[i]))

    for i in range(1, len(spectral_centroid_list)):
        s_list.append(float(spectral_contrast_list[i]))

    for i in range(1, len(tonnetz_list)):
        t_list.append(float(tonnetz_list[i]))

    for i in range(1, len(spectral_contrast_list)):
        c_list.append(float(spectral_contrast_list[i]))


    #resturns all 4 lists of floats
    return(z_list, te_list, s_list, t_list, c_list)

