import math
import streamlit as st
import altair as alt
import pandas as pd
from readFile import read_file
from editData import *
import numpy as np

#create zero crossing rate chart
def zeroCrossPattern(zeroCross1, zeroDraft):
    rangeCross = max(zeroCross1) - min(zeroCross1)
    zeroCross = []
    same2 = False

    #checking if all the values in the list are the same to avoid division by 0 later on
    for i in range(len(zeroCross1)-1):
        if zeroCross1[i] != zeroCross1[i+1]:
            break
        elif i + 1 == 179:
            same2 = True

    #if different, then the following is done to normalize the data so its all between 0 and 1
    if same2 == False:
        for i in range(len(zeroCross1)):
            zeroCross.append((zeroCross1[i] - min(zeroCross1))/rangeCross)
    #if all the same, default number is 0.5
    else:
        for i in range(len(zeroCross1)):
            zeroCross.append(0.5)

    #lists to hold x and y coordinates
    zeroCrossX = []
    zeroCrossY = []


    #setting max and min coordinates for scatter plot
    radiusmin = 49
    radiusmax = 63

    #looping 180 times, so through all the data
    for i in range(180):
        #setting value for angle
        theta = i*math.pi / (90)
        #calculating value for radius/distance of that particular point
        r = radiusmin + (radiusmax - radiusmin) * zeroCross[i]
        #based on how far through the loop we are, coordinates multiplied by -1, so they are plotting in a circular manner
        if i <=44:
            #setting x and y coordinates using trig
            x = r * math.cos(theta)
            y = r * math.sin(theta)
        elif i >44 and i<=89:
            x = r * math.cos(theta) *-1
            y = r * math.sin(theta) * -1
        elif i >89 and i<=134:
            x = r * math.cos(theta)
            y = r * math.sin(theta)
        else:
            x = r * math.cos(theta) *-1
            y = r * math.sin(theta) *-1

        #append coordinates to appropriate lists
        zeroCrossX.append(x)
        zeroCrossY.append(y)

    #creating data frame with x and y coordinates
    zero_data = pd.DataFrame({
        'x': zeroCrossX,
        'y': zeroCrossY,
        #colorZ to decide how dark/light the point will be
        'colorZ': zeroCross,
    })

    #deciding dark and light blue rgb values
    dark_blue = (235, 174, 21)
    light_blue = (255, 226, 152)

    #creating step size to create multiple shades of blue
    bStepR = (light_blue[0] - dark_blue[0]) / 180
    bStepG = (light_blue[1] - dark_blue[1]) / 180
    bStepB = (light_blue[2] - dark_blue[2]) / 180

    blues = []

    #creating a list of 180 shades of blue in hex
    for i in range(180):
        rB = int(light_blue[0] - bStepR * i)
        gB = int(light_blue[1] - bStepG * i)
        bB = int(light_blue[2] - bStepB * i)
        hex_blue = "#{:02x}{:02x}{:02x}".format(rB, gB, bB)
        blues.append(hex_blue)

    #creating blue color scale
    blue_color_scale = alt.Scale(
        domain=(min(zeroCross), max(zeroCross)),
        range=blues
    )

    #creating chart, with fixed size of the circle marks
    zero_chart = alt.Chart(zero_data).mark_circle(size = 100).encode(
        x='x',
        y='y',
        #color uses the custom blue scale, and is based off the zero crossing rate
        color=alt.Color('colorZ:Q', scale=blue_color_scale, legend=None),
    ).properties(
        width=600,
        height=600,
    )

    return(zero_chart)

#creates chart for spectral centroid
def spectralCentroidPattern(spectralCentroid, spectralDraft):
    #create a data frame
    df = pd.DataFrame({"category": spectralCentroid, "value": spectralCentroid})

    #so that order is kept the same as in the spectral centroid
    df['order'] = range(len(df))

    #getting the average
    averageSpectral = sum(spectralDraft)/len(spectralDraft)
    value = averageSpectral/(10000)

    #setting the dark and light values
    dark_purple = (237, 85, 100)
    light_purple = (250, 204, 209)

    #creating step size for the purple color scale
    stepR = (light_purple[0] - dark_purple[0]) / 60
    stepG = (light_purple[1] - dark_purple[1]) / 60
    stepB = (light_purple[2] - dark_purple[2]) / 60

    purples = []

    #creating 60 shades of pink in hex
    for i in range(60):
        r = int(light_purple[0] - stepR * i)
        g = int(light_purple[1] - stepG * i)
        b = int(light_purple[2] - stepB * i)
        hex_purple = "#{:02x}{:02x}{:02x}".format(r, g, b)
        purples.append(hex_purple)

    #creating a pink color scale for the chart
    purple_color_scale = alt.Scale(
        domain=(min(df['category']), max(df['category'])),
        range=purples
    )

    #creating a pie chart
    pie = alt.Chart(df).transform_window(
        #ensuring order is same as in the data
        order='count()'
    ).mark_arc().encode(
        theta='value',
        #custom color scale
        color=alt.Color('category:Q', scale=purple_color_scale, legend=None),  # Use your custom color scale
        order='order:O'  # Use 'order' as the order for the pie chart sectors
    ).properties(
        width=600,
        height=600  # Set the width and height to the same value for a square aspect ratio
    )

    #making the pie in the pie chart smaller
    pie_chart_smaller = pie.mark_arc(outerRadius=90)

    return(pie_chart_smaller)

#tempo chart
def tempoPattern(tempo1, tempoDraft):
    rangeTempo = max(tempo1) - min(tempo1)
    tempo = []
    same = False

    #checking if all the values in tempo are the same or not
    for i in range(len(tempo1)-1):
        if tempo1[i] != tempo1[i+1]:
            break
        elif i+1 == 359:
            same = True


    #normalizing tempo data so its all between 0 and 1
    if same == False:
        for i in range(len(tempo1)):
            tempo.append((tempo1[i] - min(tempo1))/rangeTempo)
    #If all the same, default is 0.5
    else:
        for i in range(len(tempo1)):
            tempo.append(0.5)

    #for the x and y coordinates
    tempoX = []
    tempoY = []

    #creating 360 coordinates
    for i in range(360):
        r = 82 + tempo[i]
        #converting angle into radians
        theta = i * math.pi /180
        #calculating x and y coordinates using trig
        x = r * math.cos(theta)
        y = r * math.sin(theta)

        #appedending coordinates to lists
        tempoX .append(x)
        tempoY.append(y)

    #creating data frame
    circle_data = pd.DataFrame({
        'x': tempoX,
        'y': tempoY,
    })

    #setting size of circles based on how high/low the value of the average tempo is
    averageTempo = sum(tempoDraft)/len(tempoDraft)
    if averageTempo > 300:
        sizeTempo = 1200
    else:
        sizeTempo = int(5 + ((averageTempo/300)*995))

    #creating tempo chart
    tempo_chart = alt.Chart(circle_data).mark_point(color = '#4fc2e8', size = sizeTempo).encode(
        x='x',
        y='y',
    ).properties(
        width=600,
        height=600,
    )

    return(tempo_chart)

#spectral flatness chart
def flatnessPattern(flatness1, flatnessDraft):
    #creates 60 angles, which are all equally distanced, from 0 to 2pi (full circle)
    angles = np.linspace(0, 2 * np.pi, 60, endpoint=False)

    lengths = []
    maxFlat = max(flatness1)
    minFlat = min(flatness1)
    rangeFlat = maxFlat-minFlat

    #maximum and minimum x/y coordinates for the bars in the chart
    maxLength= 135
    minLength = 100
    rangeLength = maxLength-minLength

    #creating scaling factor because values are too small in spectral flatness lists
    #dividing by value smaller than 0, so will be creater than rangeLength
    factor = (rangeLength)/(rangeFlat)

    #populating lengths list
    for i in range(60):
        #scaling up the spectral flatness values, so that it is between maxLength and minLength
        value =  (flatness1[i]-minFlat)*(factor) + minLength
        lengths.append(value)


    points = pd.DataFrame({
        "angle": angles,
        "length": lengths
    })

    #calculating average spectral flatness
    averageFlatness = sum(flatnessDraft)/len(flatnessDraft)

    #setting the 2 shades of colors
    dark_red = (97, 75, 150)
    light_red = (222, 211, 247)

    #calculating step sizes to create different shades of red/orange
    rStepR = (light_red[0] - dark_red[0]) / 60
    rStepG = (light_red[1] - dark_red[1]) / 60
    rStepB = (light_red[2] - dark_red[2]) / 60

    reds = []

    #creating list of 60 shades of red
    for i in range(60):
        rR = int(light_red[0] - rStepR * i)
        gR = int(light_red[1] - rStepG * i)
        bR = int(light_red[2] - rStepB * i)
        hex_red = "#{:02x}{:02x}{:02x}".format(rR, gR, bR)
        reds.append(hex_red)

    #creating red color scale
    red_color_scale = alt.Scale(
        domain=(100,135),
        range=reds
    )

    #calculating the final x and y coordinates using trig, columns to add to data frame
    points["x1"] = points["length"] * np.cos(points["angle"])
    points["y1"] = points["length"] * np.sin(points["angle"])

    center = []

    #creating array of zeroes, so that all lines start at the center
    for i in range(60):
        center.append(0)

    #creating data fram to get the lines drawn
    lines_df = pd.DataFrame({
        #starting coordinates, so that it starts at 0
        "x0": center,
        "y0": center,
        #final coordinates for the lines
        "x1": points["x1"],
        "y1": points["y1"],
        #setting the length based on the length
        "length": lengths,
        #setting the color based on that specific length of the line
        'colorF': lengths
    })

    #creating circular plot for spectral flatness
    #setting width of bars to 10
    flatness_chart = alt.Chart(lines_df).mark_rule(strokeWidth=10).encode(
        #setting the starting coordinates, and the range
        x=alt.X("x0:Q", scale=alt.Scale(domain=(-135, 135))),
        y=alt.Y("y0:Q", scale=alt.Scale(domain=(-135, 135))),
        #setting final coordinates
        x2=alt.X2("x1:Q"),
        y2=alt.Y2("y1:Q"),
        #using the custom color scale
        color=alt.Color("colorF:Q", scale=red_color_scale, legend=None),
        #setting the opacity
        opacity=alt.value(0.9)
    ).properties(
        width=600,
        height=600
    )

    return(flatness_chart)

#black circle chart to create black background
def black_circle():
    #creating basic data frame with x and y starting position and size
    data = pd.DataFrame({'x': [-12], 'y': [0], 'size': [60]})

    #creating the chart
    black_circle_chart = alt.Chart(data).mark_circle(color='#121212', size=100550).encode(
        x='x',
        y='y',
        opacity=alt.value(1)
    ).properties(
        width=600,
        height=600
    )

    return(black_circle_chart)

#black circle chart for balck background
def black_circle2():
    #data frame for starting coordinates and size
    data = pd.DataFrame({'x': [12], 'y': [0], 'size': [60]})

    #creating the chart
    black_circle_chart = alt.Chart(data).mark_circle(color='#121212', size=100550).encode(
        x='x',
        y='y',
        opacity=alt.value(1)
    ).properties(
        width=600,
        height=600
    )

    return(black_circle_chart)

#spectral contrast chart
def contrastPattern(contrast1, contrastDraft):
    rangeContrast = max(contrast1) - min(contrast1)
    contrast = []
    same2 = False

    #checking if all values are the same or not
    for i in range(len(contrast1)-1):
        if contrast1[i] != contrast1[i+1]:
            break
        elif i + 1 == 179:
            same2 = True

    #normalizing all the spectral contrast values
    if same2 == False:
        for i in range(len(contrast1)):
            contrast.append((contrast1[i] - min(contrast1))/rangeContrast)
    #if all the same, then default value is 0.5
    else:
        for i in range(len(contrast1)):
            contrast.append(0.5)

    #for the x and y coordinates
    contrastX = []
    contrastY = []

    #setting the max and min x/y coordinates
    radiusmin = 62
    radiusmax = 73

    #calculating all 180 coordinates
    for i in range(180):
        #calculating the angle, so that each point is 2 degrees away from eachother
        theta = i*math.pi / (90)
        #calculating the radius/distance
        r = radiusmin + (radiusmax - radiusmin) * contrast[i]
        #based on how far through the circle, x/y coordinate multiplied by -1 do form a circle
        if i <=44:
            #x and y coordinates using trig
            x = r * math.cos(theta)
            y = r * math.sin(theta)
        elif i >44 and i<=89:
            x = r * math.cos(theta) *-1
            y = r * math.sin(theta) * -1
        elif i >89 and i<=134:
            x = r * math.cos(theta)
            y = r * math.sin(theta)
        else:
            x = r * math.cos(theta) *-1
            y = r * math.sin(theta) *-1
        #appending coordinates to appropriate lists
        contrastX.append(x)
        contrastY.append(y)

    #creating data frame
    zero_data = pd.DataFrame({
        #setting up the x and y coordinates
        'x': contrastX,
        'y': contrastY,
        #connecting color to the value of the spectral contrast
        'colorC': contrast,
    })

    #setting dark green and light green rgb values
    dark_green = (96, 153, 35)
    light_green = (199, 231, 164)

    #getting the steps for each rgb values to generate multiple shades of green
    gStepR = (light_green[0] - dark_green[0]) / 180
    gStepG = (light_green[1] - dark_green[1]) / 180
    gStepB = (light_green[2] - dark_green[2]) / 180

    greens = []

    #creating a list of 180 shades of green, in hex
    for i in range(180):
        rG = int(light_green[0] - gStepR * i)
        gG = int(light_green[1] - gStepG * i)
        bG = int(light_green[2] - gStepB * i)
        hex_green = "#{:02x}{:02x}{:02x}".format(rG, gG, bG)
        greens.append(hex_green)

    #forming the green color scale
    green_color_scale = alt.Scale(
        domain=(min(contrast), max(contrast)),
        range=greens
    )

    #creating the spectral contrast chart, with a fized size of 100
    contrast_chart = alt.Chart(zero_data).mark_circle(size = 100).encode(
        #x and y coordinates
        x=alt.X('x', axis=alt.Axis(title=None)),
        y=alt.X('y', axis=alt.Axis(title=None)),
        #using custom color scale
        color=alt.Color('colorC:Q', scale=green_color_scale, legend=None),
    ).properties(
        width=600,
        height=600,
    )

    return(contrast_chart)
