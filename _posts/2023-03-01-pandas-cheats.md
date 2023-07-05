---
layout: post
title: Pandas Cheats 
categories: [Notes]
tags: [Pandas, Cheats]
--- 
# Pandas Cheats 

<https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html>

## convert column to datetime 

    df['col'] = pd.to_datetime(df['col'])

## (time) windowing 

nre column "previous_timestamp" with value of previous value (in line -1) of column "timestamp"
    df['previous_timestamp'] = df['timestamp'].shift(1)

