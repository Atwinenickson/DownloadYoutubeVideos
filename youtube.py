from pytube import YouTube
from pathlib import Path
import pandas as pd
import schedule
import time
import numpy as np
import os

def job():
    df = pd.read_excel('kabali.xlsx')
    df=df.dropna()
    print(df)
    links = df['URL'].tolist()
    print(links)

    data_with_index = df.set_index("URL")
    print(data_with_index.head())
    downloaded = []
    for link in links:
        # download each link
        url = YouTube(link)

        print("downloading....")

        video = url.streams.get_highest_resolution()

        path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))

        video.download(path_to_download_folder)
        print("Downloaded! :)")
        print("JOB FINISHED")
        # add downloaded link to the downloaded list
        downloaded.append(link)


    # create a new column for downloaded urls   
    df["Downloaded"] = downloaded   
    print(df["Downloaded"])

    # create excel writer object
    writer = pd.ExcelWriter('downloaded.xlsx')
    # write dataframe to excel
    df["Downloaded"].to_excel(writer)
    # save the excel
    writer.save()
    print('DataFrame is written successfully to Excel File.')

    df2 = pd.read_excel('downloaded.xlsx')

    #Get not downloaded list
    df["URL"].compare(df2["Downloaded"])
    nodownloaded = df["URL"].compare(df2["Downloaded"], keep_equal=True, keep_shape=True)
    # df["NotDownloaded"] = no_downloaded  
    print(nodownloaded)
    nodownloaded.columns = ['Original List', 'Downloaded List']

    # create excel writer object
    writer = pd.ExcelWriter('Notdownloaded.xlsx')
    # write dataframe to excel
    nodownloaded.to_excel(writer)
    # save the excel
    writer.save()
    print('DataFrame is written successfully to Excel File.')

schedule.every().day.at("18:00").do(job)

'''
SCHEDULE ANY TIME YOU WANT WITH THE FOLLOWING COMMANDS
schedule.every(10).seconds.do(job)
schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every(5).to(10).minutes.do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().minute.at(":17").do(job)
'''

while True:
    schedule.run_pending()
    time.sleep(1)