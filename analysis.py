import pandas as pd

df = pd.read_csv('mobile_game_inapp_purchases.csv')
print(df.shape)
print(df.head())
# 第一個分析：哪種玩家最容易付費？

# 1. 按年齡分組分析
print("=== 年齡 vs 平均付費金額 ===")
df['AgeGroup'] = pd.cut(df['Age'], bins=[0, 18, 25, 35, 50, 100], 
                         labels=['18以下', '18-25', '25-35', '35-50', '50以上'])
age_analysis = df.groupby('AgeGroup')['InAppPurchaseAmount'].mean().round(2)
print(age_analysis)

# 2. 按性別分析
print("\n=== 性別 vs 平均付費金額 ===")
gender_analysis = df.groupby('Gender')['InAppPurchaseAmount'].mean().round(2)
print(gender_analysis)

# 3. 按國家分析 TOP 5
print("\n=== 前5名付費最高的國家 ===")
country_analysis = df.groupby('Country')['InAppPurchaseAmount'].mean().round(2).sort_values(ascending=False).head(5)
print(country_analysis)

# 確認各國樣本數
print("\n=== 各國樣本數 ===")
print(df.groupby('Country')['InAppPurchaseAmount'].count().sort_values(ascending=False).head(10))

# 第二個分析：哪個遊戲類型最賺錢？
print("=== 遊戲類型 vs 平均付費金額 ===")
genre_analysis = df.groupby('GameGenre')['InAppPurchaseAmount'].agg(['mean', 'count']).round(2)
genre_analysis.columns = ['平均付費', '玩家數']
genre_analysis = genre_analysis.sort_values('平均付費', ascending=False)
print(genre_analysis)

# 第三個分析：玩家多久會付費？
print("=== 付費快慢 vs 付費金額 ===")
df['PurchaseSpeed'] = pd.cut(df['FirstPurchaseDaysAfterInstall'], 
                              bins=[-1, 7, 15, 30],
                              labels=['7天內', '8-15天', '16-30天'])
speed_analysis = df.groupby('PurchaseSpeed')['InAppPurchaseAmount'].mean().round(2)
print(speed_analysis)

print(df['FirstPurchaseDaysAfterInstall'].describe())
print("\n最大值:", df['FirstPurchaseDaysAfterInstall'].max())