import pandas as pd
import numpy as np

def dataPipeline(pathToData: str):
    df = pd.read_csv(pathToData)
    dfNY = df[df.State == 'NY']
    dfNY.drop(columns=["Description"], inplace=True)

    # We chose to use 2021 since we have the most accidents in a year(55000)
    dfNY['Start_Time'] = dfNY['Start_Time'].apply(lambda x: str(x).__contains__("2021") == True)

    # Data Preparation Stage
    dfNY.drop(columns=["Number", "Street", "Side", "City", "County",
                       "State", "Country", "Timezone", "Airport_Code", "Weather_Timestamp"], inplace=True)


    dfNY.drop(columns=["Turning_Loop", "Traffic_Signal", "Traffic_Calming", "Stop", "Station",
                       "Roundabout", "Railway", "No_Exit", "Junction", "Give_Way", "Crossing", "Bump", "Amenity"], inplace=True)

    dfNY['Astronomical_Twilight'] = dfNY['Astronomical_Twilight'].apply(lambda x: 0 if x == "Day" else 1)
    dfNY['Nautical_Twilight'] = dfNY['Nautical_Twilight'].apply(lambda x: 0 if x == "Day" else 1)
    dfNY['Civil_Twilight'] = dfNY['Civil_Twilight'].apply(lambda x: 0 if x == "Day" else 1)
    dfNY['Sunrise_Sunset'] = dfNY['Sunrise_Sunset'].apply(lambda x: 0 if x == "Day" else 1)

    dfNY['Weather_Condition'] = pd.factorize(dfNY.Weather_Condition)[0] + 1

    trainX = []
    trainY = []

    n_future = 1   # Number of days we want to look into the future based on the past days.
    n_past = 14  # Number of past days we want to use to predict the future.

    #Reformat input data into a shape: (n_samples x timesteps x n_features)
    #In my example, my df_for_training_scaled has a shape (12823, 5)
    #12823 refers to the number of data points and 5 refers to the columns (multi-variables).
    for i in range(n_past, len(dfNY) - n_future + 1):
        trainX.append(dfNY[i - n_past:i, 0:dfNY.shape[1]])
        trainY.append(dfNY[i + n_future - 1:i + n_future, 0])

    trainX, trainY = np.array(trainX), np.array(trainY)

    #Reformat input data into a shape: (n_samples x timesteps x n_features x channels)
    trainY.reshape((-1, 1))
    trainX.reshape((-1, 1))

    return trainX, trainY
