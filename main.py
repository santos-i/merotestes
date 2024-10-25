import glob
import pandas as pd

from dotenv import dotenv_values

from script import *
from script.plots import plot_generator
from script.equipments import defineSN, mean_dir_calc


serialNumbers = dotenv_values(".env")
sn_ane, sn_bar, sn_th = defineSN(serialNumbers)

file = glob.glob(f"{INPUT_PATH}*.log")[0]

df = pd.read_csv(file, sep=",", header=None)
df.columns=TRANSLATOR_COLS


df['datetime'] = pd.to_datetime(
            df['date']+' '+df['time'],
            format='%y-%m-%d %H:%M:%S'
)
df.set_index('datetime', inplace=True)
df = df.drop(['date','time'], axis='columns')
df = df.astype(float)


for period in ['1s','10min','1h']:
    if period != '1s':
        df_resampled = df.resample(period).mean()
        df_resampled['wdir_1'] = df['wdir_1'].resample(period).apply(lambda x: mean_dir_calc(x))
        df_resampled['wdir_2'] = df['wdir_2'].resample(period).apply(lambda x: mean_dir_calc(x))
    
    else:
        df_resampled = df.copy()

    wspeed_fig = plot_generator(
            df=df_resampled,
            parameter='wspeed',
            title=f'Wind Speed (m/s) - {period}',
            xlabel='DateTime',
            ylabel='Wind Speed (m/s)',
            equipments_sn=sn_ane
        )
    wspeed_fig.write_html(f"{OUTPUT_PATH}wspeed_{period}.html")


    wdir = plot_generator(
            df=df_resampled,
            parameter='wdir',
            title=f'Wind direction (°) - {period}',
            xlabel='DateTime',
            ylabel='Wind direction (°)',
            mode='markers',
            equipments_sn=sn_ane
        )
    wdir.write_html(f"{OUTPUT_PATH}wdir_{period}.html")


    pressure_fig = plot_generator(
            df=df_resampled,
            parameter='pressure',
            title=f'Pressure (hPa) - {period}',
            xlabel='DateTime',
            ylabel='Pressure (hPa)',
            equipments_sn=sn_bar
        )
    pressure_fig.write_html(f"{OUTPUT_PATH}pressure_{period}.html")


    temperature = plot_generator(
            df=df_resampled,
            parameter='temperature',
            title=f'Temperature (°C) - {period}',
            xlabel='DateTime',
            ylabel='Temperature (°C)',
            equipments_sn=sn_th
        )
    temperature.write_html(f"{OUTPUT_PATH}temperature_{period}.html")


    humidity_fig = plot_generator(
            df=df_resampled,
            parameter='humidity',
            title=f'Humidity (%) - {period}',
            xlabel='DateTime',
            ylabel='Humidity (%)',
            equipments_sn=sn_th
        )
    humidity_fig.write_html(f"{OUTPUT_PATH}humidity_{period}.html")
