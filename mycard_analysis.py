import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rc('font', family='Microsoft JhengHei')

# 模擬MyCard版位數據（一個月）
data = {
    '版位': ['官網Banner', '娛樂中心Banner', '會員活動頁Banner', 
             'APP推播', '電子報EDM', '簡訊'],
    '類型': ['Banner', 'Banner', 'Banner', 
             '直效型', '直效型', '直效型'],
    '曝光次數': [850000, 620000, 430000, 
                280000, 195000, 150000],
    '點擊次數': [12800, 11160, 5590, 
                16800, 7605, 7500],
    '導流人數': [9600, 8370, 4190, 
                14280, 6465, 6375]
}

df = pd.DataFrame(data)

# 計算點擊率和轉換率
df['點擊率CTR'] = (df['點擊次數'] / df['曝光次數'] * 100).round(2)
df['導流轉換率'] = (df['導流人數'] / df['點擊次數'] * 100).round(2)

print(df[['版位', '類型', '曝光次數', '點擊率CTR', '導流轉換率']])

# 圖一：各版位點擊率比較
plt.figure(figsize=(10, 5))
plt.bar(df['版位'], df['點擊率CTR'], color=['steelblue']*3 + ['coral']*3, edgecolor='black')
plt.title('各版位點擊率（CTR）比較')
plt.xlabel('版位')
plt.ylabel('點擊率（%）')
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()

# 圖二：各版位導流轉換率比較
plt.figure(figsize=(10, 5))
plt.bar(df['版位'], df['導流轉換率'], color=['steelblue']*3 + ['coral']*3, edgecolor='black')
plt.title('各版位導流轉換率比較')
plt.xlabel('版位')
plt.ylabel('導流轉換率（%）')
plt.xticks(rotation=15)
plt.ylim(0, 100)
plt.tight_layout()
plt.show()