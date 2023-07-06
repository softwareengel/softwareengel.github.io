---
layout: post
title: Pandas Cheats  
categories: [Pandas]
tags: [Pandas, Cheats, Python]
--- 

![](../pics/20230705141110_pandas_cheat_sheet.png)

# Pandas Cheat Sheet 

<https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf>

<https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html>

## convert column to datetime 

    df['col'] = pd.to_datetime(df['col'])

## (time) windowing 

nre column "previous_timestamp" with value of previous value (in line -1) of column "timestamp"
    df['previous_timestamp'] = df['timestamp'].shift(1)

