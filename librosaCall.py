import os
import librosa
import pandas as pd

#extracting music data from uploaded file
def extractFeatures(music):
    audio, sr = librosa.load(music)

    #extracting features from the audio file using the librosa library
    tempo, _ = librosa.beat.beat_track(y=audio, sr=sr)
    spectral_centroid = librosa.feature.spectral_centroid(y=audio, sr=sr)[0]
    zero_crossing_rate = librosa.feature.zero_crossing_rate(y=audio)[0]
    contrast = librosa.feature.spectral_contrast(y=audio, sr=sr)[0]
    flatness = librosa.feature.spectral_flatness(y=audio)[0]

    #Creating the right dataframe
    df = pd.DataFrame({
        'tempo': tempo,
        'spectral_centroid': spectral_centroid,
        'zero_crossing_rate': zero_crossing_rate,
        'contrast': contrast,
        'flatness': flatness
    })

    #Writing the dataframe into a csv file, and outputing that file
    output_file = 'output/file.csv'
    df.to_csv(output_file, index=False)

