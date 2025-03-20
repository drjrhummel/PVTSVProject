import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()



# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date", parse_dates=True)

# Clean data
df = df.loc[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]
df_clean = df.copy()

def draw_line_plot():
    # Draw line plot
    df_line = df_clean.copy()
    #fig, ax = plt.subplots()
    shape = plt.figure()
    shape.set_figwidth(24)
    shape.set_figheight(7.5)
    line_plot = plt.plot('value', data=df_line, color='#d62728', linewidth=2)
    plt.tick_params(axis='both', which='major', pad=6)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019', fontdict={'size': 18}, pad=8)
    plt.xlabel('Date', fontdict={'size': 15}, labelpad=8)
    plt.ylabel('Page Views', fontdict={'size': 15}, labelpad=8)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)

    fig = line_plot[0].figure
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar0 = df_clean.copy()
    df_bar0['year'] = df_bar0.index.year
    df_bar0['month'] = df_bar0.index.month
    df_bar1 = df_bar0.reset_index(drop=True)
    df_bar2 = df_bar1.groupby(['year', 'month'])['value'].mean().reset_index(name='monthly_visits')

    # Draw bar plot
    years = sorted(df_bar2['year'].unique().tolist())
    years = tuple(years)
    years_str = tuple([str(year) for year in years])

    df_bar_jan = df_bar2.loc[df_bar2['month'] == 1].sort_values(by='year')
    v_jan = df_bar_jan['monthly_visits'].tolist()
    v_jan.insert(0, 0)
    df_bar_feb = df_bar2.loc[df_bar2['month'] == 2].sort_values(by='year')
    v_feb = df_bar_feb['monthly_visits'].tolist()
    v_feb.insert(0, 0)
    df_bar_mar = df_bar2.loc[df_bar2['month'] == 3].sort_values(by='year')
    v_mar = df_bar_mar['monthly_visits'].tolist()
    v_mar.insert(0, 0)
    df_bar_apr = df_bar2.loc[df_bar2['month'] == 4].sort_values(by='year')
    v_apr = df_bar_apr['monthly_visits'].tolist()
    v_apr.insert(0, 0)
    df_bar_may = df_bar2.loc[df_bar2['month'] == 5].sort_values(by='year')
    v_may = df_bar_may['monthly_visits'].tolist()
    df_bar_jun = df_bar2.loc[df_bar2['month'] == 6].sort_values(by='year')
    v_jun = df_bar_jun['monthly_visits'].tolist()
    df_bar_jul = df_bar2.loc[df_bar2['month'] == 7].sort_values(by='year')
    v_jul = df_bar_jul['monthly_visits'].tolist()
    df_bar_aug = df_bar2.loc[df_bar2['month'] == 8].sort_values(by='year')
    v_aug = df_bar_aug['monthly_visits'].tolist()
    df_bar_sep = df_bar2.loc[df_bar2['month'] == 9].sort_values(by='year')
    v_sep = df_bar_sep['monthly_visits'].tolist()
    df_bar_oct = df_bar2.loc[df_bar2['month'] == 10].sort_values(by='year')
    v_oct = df_bar_oct['monthly_visits'].tolist()
    df_bar_nov = df_bar2.loc[df_bar2['month'] == 11].sort_values(by='year')
    v_nov = df_bar_nov['monthly_visits'].tolist()
    df_bar_dec = df_bar2.loc[df_bar2['month'] == 12].sort_values(by='year')
    v_dec = df_bar_dec['monthly_visits'].tolist()
    vm_list = [tuple(v_jan), tuple(v_feb), tuple(v_mar), tuple(v_apr), tuple(v_may), tuple(v_jun), tuple(v_jul),
               tuple(v_aug), tuple(v_sep), tuple(v_oct), tuple(v_nov), tuple(v_dec)]
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                   'November', 'December']
    month_dict = dict(zip(month_names, vm_list))

    l = len('years')
    xl = []
    for i in range(l - 1):
        xl.append(i)
    x = pd.array(xl, dtype=float)
    width = 0.025
    multiplier = 0

    fig, ax = plt.subplots(figsize=(10, 10))

    for month, value in month_dict.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, value, width, label=month)
        multiplier += 1

    ax.set_xlabel('Years', fontsize=15)
    ax.set_ylabel('Average Page Views', fontsize=15)
    ax.set_xticks(x + (width * 5.4), years_str, rotation=90, fontsize=15)
    ax.legend(loc='upper left', fontsize='large')


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, figsize=(14, 4.5))
    sns.boxplot(data=df_box,
                x='year',
                y='value',
                order=[2016, 2017, 2018, 2019],
                whis=(10, 90),
                ax=ax0)
    ax0.set(xlabel='Year',
            ylabel='Page Views',
            ylim=(0, 200000),
            yticks=(0, 20000, 40000, 60000, 80000, 100000, 120000, 140000, 160000, 180000, 200000),
            title='Year-wise Box Plot (Trend)')
    sns.boxplot(data=df_box,
                x='month',
                y='value',
                order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
                whis=(10, 90),
                ax=ax1)
    ax1.set(xlabel='Month',
            ylabel='Page Views',
            ylim=(0, 200000),
            yticks=(0, 20000, 40000, 60000, 80000, 100000, 120000, 140000, 160000, 180000, 200000),
            title='Month-wise Box Plot (Seasonality)')
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

# Note 1: code for adding titles and axis labels to Matplotlib plots adapted from tutorials on the following webpage: https://www.w3schools.com/python/matplotlib_labels.asp
# Note 2: code for altering Matplotlib plot figures adapted from tutorials on the following page: https://www.geeksforgeeks.org/change-plot-size-in-matplotlib-python/
# Note 3: code for altering Matplotlib plot tick labels adapted from results to the following Google search: https://www.google.com/search?q=python+matplotlib+change+tick+label+size&sca_esv=830a0b600f7af676&biw=1280&bih=593&sxsrf=AHTn8zqHJHCfdEDiSSvXMjiASVvl6ArB7g%3A1742483921548&ei=0THcZ5CNId7ewN4P8M7U2Qw&ved=0ahUKEwjQua65-piMAxVeL9AFHXAnNcsQ4dUDCBI&uact=5&oq=python+matplotlib+change+tick+label+size&gs_lp=Egxnd3Mtd2l6LXNlcnAiKHB5dGhvbiBtYXRwbG90bGliIGNoYW5nZSB0aWNrIGxhYmVsIHNpemUyBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjILEAAYgAQYhgMYigUyCxAAGIAEGIYDGIoFMgsQABiABBiGAxiKBTILEAAYgAQYhgMYigUyCBAAGKIEGIkFMggQABiiBBiJBUjqL1BdWLkscAF4AZABAJgBtAGgAdMaqgEEMC4yNrgBA8gBAPgBAZgCGKAC6RjCAgoQABiwAxjWBBhHwgIEECMYJ8ICCxAAGIAEGJECGIoFwgIFEAAYgATCAggQABgWGAoYHsICBhAAGA0YHsICBRAAGO8FwgIIEAAYgAQYogSYAwCIBgGQBgiSBwQxLjIzoAfR2AGyBwQwLjIzuAfkGA&sclient=gws-wiz-serp
# Note 4: use of the 'pad' argument inspired by results to the following Google search: https://www.google.com/search?q=python+matplotlib+setting+distance+between+tick+mark+and+label&sca_esv=830a0b600f7af676&biw=1280&bih=593&sxsrf=AHTn8zpmK3_AdNbTawtGOUh4HROBmn-LiQ%3A1742484152101&ei=uDLcZ-TvBdXEp84P7M_C6A4&ved=0ahUKEwjkq6an-5iMAxVV4skDHeynEO0Q4dUDCBI&uact=5&oq=python+matplotlib+setting+distance+between+tick+mark+and+label&gs_lp=Egxnd3Mtd2l6LXNlcnAiPnB5dGhvbiBtYXRwbG90bGliIHNldHRpbmcgZGlzdGFuY2UgYmV0d2VlbiB0aWNrIG1hcmsgYW5kIGxhYmVsSM91UIYEWL5zcAF4AJABAZgB3QGgAchCqgEHMTEuNTEuM7gBA8gBAPgBAZgCMKAC3DLCAgoQABiwAxjWBBhHwgIEECMYJ8ICBhAAGBYYHsICCxAAGIAEGIYDGIoFwgIIEAAYgAQYogTCAgUQABiABMICCxAAGIAEGJECGIoFwgIKEAAYgAQYFBiHAsICChAjGIAEGCcYigXCAgUQABjvBcICBRAhGKABwgIFECEYnwXCAgcQIRigARgKwgIEECEYCsICBRAhGKsCwgIIEAAYogQYiQWYAwCIBgGQBgiSBwY1LjQwLjOgB4uOBLIHBjQuNDAuM7gH1zI&sclient=gws-wiz-serp
# Note 5: code separating date index into year and month columns adapted from Erfan's response in the following discussion thread: https://stackoverflow.com/questions/55776571/how-to-split-a-date-column-into-separate-day-month-year-column-in-pandas
# Note 6: code for dropping date index adapted from results to the following Google search: https://www.google.com/search?q=python+pandas+dropping+index+from+dataframe&sca_esv=d90a51759e2b0159&sxsrf=AHTn8zqTS8d6KczqcHbQAw3VIOIGSytRlA%3A1742486383274&ei=bzvcZ__BEKPewN4P7K7EoAU&ved=0ahUKEwi_tZrPg5mMAxUjL9AFHWwXEVQQ4dUDCBI&uact=5&oq=python+pandas+dropping+index+from+dataframe&gs_lp=Egxnd3Mtd2l6LXNlcnAiK3B5dGhvbiBwYW5kYXMgZHJvcHBpbmcgaW5kZXggZnJvbSBkYXRhZnJhbWUyBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yCxAAGIAEGIYDGIoFMgsQABiABBiGAxiKBTIIEAAYgAQYogQyCBAAGIAEGKIEMggQABiABBiiBEjX-wVQlAdYrvoFcA94AZABAJgBzwGgAacoqgEHMTcuMzEuMbgBA8gBAPgBAZgCQKAC9irCAgoQABiwAxjWBBhHwgINEAAYgAQYsAMYQxiKBcICChAjGIAEGCcYigXCAgQQIxgnwgIKEAAYgAQYQxiKBcICDRAAGIAEGLEDGBQYhwLCAg0QABiABBixAxhDGIoFwgIIEAAYgAQYsQPCAhAQABiABBixAxiDARgUGIcCwgILEAAYgAQYsQMYgwHCAgUQABiABMICChAAGIAEGBQYhwLCAgcQABiABBgNwgIIEAAYogQYiQXCAgUQABjvBZgDAIgGAZAGCpIHBzI4LjM1LjGgB4qAA7IHBzEzLjM1LjG4B7sq&sclient=gws-wiz-serp
# Note 7: implementation of the '.unique()' option adapted from results to the following Google search: https://www.google.com/search?q=python+pandas+creating+a+list+of+unique+values+in+column&sca_esv=d90a51759e2b0159&sxsrf=AHTn8zpbJIbjVH_-ySxYch8Q3DKFkA2s6g%3A1742487860574&ei=NEHcZ93YIry2wN4Prey4qQM&ved=0ahUKEwjdwtGPiZmMAxU8G9AFHS02LjUQ4dUDCBI&uact=5&oq=python+pandas+creating+a+list+of+unique+values+in+column&gs_lp=Egxnd3Mtd2l6LXNlcnAiOHB5dGhvbiBwYW5kYXMgY3JlYXRpbmcgYSBsaXN0IG9mIHVuaXF1ZSB2YWx1ZXMgaW4gY29sdW1uMgYQABgWGB4yCxAAGIAEGIYDGIoFMggQABiABBiiBDIFEAAY7wUyBRAAGO8FSPxKUI8DWPNIcAF4AZABAJgB9AGgAdM4qgEGOS40NS4yuAEDyAEA-AEBmAI5oAK2OqgCFMICBxAjGCcY6gLCAhQQABiABBiRAhi0AhiKBRjqAtgBAcICFBAAGIAEGOMEGLQCGOkEGOoC2AEBwgIKEAAYgAQYQxiKBcICCxAAGIAEGJECGIoFwgIOEAAYgAQYsQMYgwEYigXCAggQABiABBixA8ICChAjGIAEGCcYigXCAgQQIxgnwgINEAAYgAQYsQMYFBiHAsICDRAAGIAEGLEDGEMYigXCAgoQABiABBgUGIcCwgIFEAAYgATCAggQABiiBBiJBZgDB_EF2hwmdqBYaN26BgYIARABGAGSBwY5LjQ2LjKgB-ifA7IHBjguNDYuMrgHrzo&sclient=gws-wiz-serp
# Note 8: code for bar plot adapted from a matplotlib example (https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py) and John Lyon's response on the following discussion forum (https://stackoverflow.com/questions/14270391/how-to-plot-multiple-bars-grouped)
# Note 9: code for creating space for two plots side-by-side adapted from responses in the following discussion thread: https://stackoverflow.com/questions/42818361/how-to-make-two-plots-side-by-side
# Note 10: test module code for this project did not run successfully under a newer version of numpy. In order for the test code to perform as expected, numpy needed to be downgraded to version 1.20.3. For more details on this process, please refer to the instructions in the following freeCodeCamp forum thread: https://forum.freecodecamp.org/t/page-time-visualiser/707347/37