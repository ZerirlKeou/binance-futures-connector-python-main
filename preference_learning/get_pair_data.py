import os
import sqlite3
import pandas as pd
import numpy as np
from visible import drawMainFigure

app = drawMainFigure.MplVisualIf()


def draw_picture(df, index, interval, windows=20):
    """
    通过输入dataframe格式的数据类型，来生成特定位置，特定窗口的比较图案。因为不能一次生成两个，所以还是采用顺序生成的方式，只不过对图片进行了标识，最终还是采用opencv的方式对所有生成的数据集进行比较工作。
    Args:
        df: dataframe格式的数据
        index: 当前需要决定的index位置
        windows: 向前并向后取的观测时间窗口
        interval:

    Returns: 返回的为int类型，表示哪一个好，0代表第一个好，1代表第二个好

    """
    begin_index = 0 if index < windows else index - windows
    point_index = index if index < windows else windows
    df = df.iloc[begin_index: index + windows]
    df['Open time'] = (df.index.astype(np.int64) // 10 ** 3).astype(int)

    layout_dict = {'df': df,
                   'draw_kind': ['kline_label', 'macd','stoch_rsi'],
                   'title': f"状态1",
                   'save_number': index,
                   'point_index':point_index,
                   'interval':interval}
    app.fig_output(**layout_dict)


def write_csv():
    pass


def test():
    intervals = ['1m','5m','15m','1h','1d']
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    for interval in intervals:
        data_folder = f"data\\data_base\\{interval}\\BTCUSDT.db"
        data_folder_path = os.path.join(parent_dir, data_folder)
        conn = sqlite3.connect(data_folder_path)

        df = pd.read_sql_query("select * from 'BTCUSDT';", conn, dtype='float', index_col='Open time')
        for i in range(len(df)):
            if df.iloc[i]['macd_back'] != 0:
                draw_picture(df, i, interval, windows=25)
