import math

#when the length of the data list is greater than 360
#requires a blank list and the list of data
def binning(data, final, length):
    #binSize is the size of the number of items that need to be merged each time
    binSize = len(data)/length
    for i in range(length):
        #start position
        binStart = int(i*binSize)
        #end position
        binEnd = int((i+1)*binSize)
        #getting all the values from the start to the end
        binValues = data[binStart:binEnd]
        sumV = 0
        #looping through binValues to add them up
        for y in range(len(binValues)):
            sumV += binValues[y]
        #getting the average of those values
        add = sumV/len(binValues)
        #Adding the averages to the final list
        final.append(add)
    return final

# when dif/((len list)-1) is greater than 1, meaning multiple values or 1 value between each value in the current data list need to be added
def perGaps(data, final, length):
    #dif = the number of values that need to be added to get to final length
    dif = length - len(data)
    #the number of values that will still needed to be added to the data once an integer number of values is added in each gap
    extra = dif%((len(data)-1))
    #the integer number of values that need to be added between each existing value in the data
    numsPerGap = int((dif-extra)/(len(data)-1))

    #looping through the data list, -1, which is the number of gaps between values
    for i in range(len(data)-1):
        #setting num, num2, and appending num to the final list
        num = data[i]
        final.append(num)
        num2 = data[i+1]
        #count is set to num
        count = data[i]
        #looping, the number of values that are added per gap
        for i in range(numsPerGap):
            #count is count plus the average of num and num2 divided by the number of numbers per gap
            count += (((num2-num)/2)/numsPerGap)
            #count added to final list
            final.append(count)
    #appending the very last value in the original data list to the final list
    final.append(data[len(data)-1])


    index = 0
    #looping for extra number of times, the number of values that still need to be added
    for i in range(extra):
        num = final[index]
        num2 = final[index+1]
        final.insert(i, num+((num2-num)/2))
        index += 2

    return(final)

def jumpGap(data, length): #when dif/len list -1 is less than 1
    #dif = the number of values that need to be added to get to final length
    dif = length - len(data)
    decimal = dif/ (len(data)-1)
    #everyGap is number of extra elements that need to be inserted inbetween each data point
    everyGap = math.ceil(1/decimal)
    #start at second element in list
    position = 1

    #inserting/interpolating between data points
    for i in range(1, int(len(data)/everyGap)+1):
        num = data[position-1]
        num2 = data[position]
        data.insert(position, num+(num2-num)/2)
        position += everyGap+1

    #adding the extra points that still need to be added
    loop = length - len(data)
    loopPlace = 0
    #interpolating the remaining extra values needed
    for i in range(loop):
        num = data[loopPlace]
        num2 = data[loopPlace+1]
        data.insert(loopPlace+1, num+ (num2-num)/2)
        loopPlace+=2

    return(data)

#function that uses previous functions to cut all feature lists
def dataCut(zeroDraft, tempoDraft, centroidDraft, contrastDraft, flatnessDraft):
    #create empty lists that need to be sent to the data editing functions
    zeroCross = []
    tempo = []
    spectralContrast = []
    tonnetz = []
    tempFlat = []

    tempZ = []
    tempTe = []
    tempcentroid = []
    tempContrast = []

    #editing zero cross rate data
    if len(zeroDraft) == 180:
        zeroCross = zeroDraft
    elif len(zeroDraft) > 180:
        zeroCross = binning(zeroDraft, tempZ, 180)
    elif len(zeroDraft) < 180:
        dif = 180 - len(zeroDraft)
        if dif/(len(zeroDraft)-1) < 1:
            zeroCross = jumpGap(zeroDraft, 180)
        else:
            zeroCross = perGaps(zeroDraft, tempZ, 180)

    #editing tempo data
    if len(tempoDraft) == 360:
        tempo = tempoDraft
    elif len(tempoDraft) > 360:
        tempo = binning(tempoDraft, tempTe, 360)
    elif len(tempoDraft) < 360:
        dif = 360 - len(tempoDraft)
        if dif/(len(tempoDraft)-1) < 1:
            tempo = jumpGap(tempoDraft)
        else:
            tempo = perGaps(tempoDraft, tempTe, 360)

    #editing spectral centroid data
    if len(centroidDraft) == 60:
        centroid = centroidDraft
    elif len(centroidDraft) > 60:
        centroid = binning(centroidDraft, tempcentroid, 60)
    elif len(centroidDraft) < 60:
        dif = 60 - len(centroidDraft)
        if dif/(len(centroidDraft)-1)<1:
            centroid = jumpGap(centroidDraft)
        else:
            centroid = perGaps(centroidDraft, tempcentroid, 60)

    #editing spectral flatness data
    if len(flatnessDraft) == 60:
        flatness = flatnessDraft
    elif len(flatnessDraft) > 60:
        flatness = binning(flatnessDraft, tempFlat, 60)
    elif len(flatnessDraft) < 60:
        dif = 60 - len(flatnessDraft)
        if dif/(len(flatnessDraft)-1)<1:
            flatness = jumpGap(flatnessDraft)
        else:
            flatness = perGaps(flatnessDraft, tempFlat, 60)

    #editing central contrast data
    if len(contrastDraft) == 180:
        contrast = contrastDraft
    elif len(contrastDraft) > 180:
        contrast = binning(contrastDraft, tempContrast, 180)
    elif len(contrastDraft) < 180:
        dif = 180 - len(contrastDraft)
        if dif/(len(contrastDraft)-1) < 1:
            contrast = jumpGap(contrastDraft, 180)
        else:
            contrast = perGaps(contrastDraft, tempContrast, 180)

    #returning all the edited data back for chart creeation
    return(zeroCross, tempo, centroid, contrast, flatness)


