#titanic 初学時実行pyファイル
#参考：https://www.codexa.net/kaggle-titanic-beginner/
#まずは？.....................................................今回NumpyとPandasを使います。インポートして、先ほどダウンロードしたtrain.csvとtest.csvをデータフレーム形式で読み込みましょう。
import pandas as pd
import numpy as np
#/(指定する)/exec/test.csv
train = pd.read_csv("(指定する)")
test = pd.read_csv("(指定する)")
#次は？.....................................................Pandasのhead()を使うと、データフレームの最上部5段がデフォルトで表示されます。
print("次は？--train.head()")
train_h = train.head()
print(train_h)
#~~~~
#    PassengerId  Survived  Pclass                                               Name     Sex   Age  SibSp  Parch            Ticket     Fare Cabin Embarked
# 0            1         0       3                            Braund, Mr. Owen Harris    male  22.0      1      0         A/5 21171   7.2500   NaN        S
# 1            2         1       1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1      0          PC 17599  71.2833   C85        C
# 2            3         1       3                             Heikkinen, Miss. Laina  female  26.0      0      0  STON/O2. 3101282   7.9250   NaN        S
# 3            4         1       1       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1      0            113803  53.1000  C123        S
# 4            5         0       3                           Allen, Mr. William Henry    male  35.0      0      0            373450   8.0500   NaN        S
#~~~~
#-----------------
#PassengerId – 乗客識別ユニークID
# Survived – 生存フラグ（0=死亡、1=生存）
# Pclass – チケットクラス
# Name – 乗客の名前
# Sex – 性別（male=男性、female＝女性）
# Age – 年齢
# SibSp – タイタニックに同乗している兄弟/配偶者の数
# parch – タイタニックに同乗している親/子供の数
# ticket – チケット番号
# fare – 料金
# cabin – 客室番号
# Embarked – 出港地（タイタニックへ乗った港）
#pclass = チケットクラス
# 1 = 上層クラス（お金持ち）
# 2 = 中級クラス（一般階級）
# 3 = 下層クラス（労働階級）
# Embarked = 各変数の定義は下記の通り
# C = Cherbourg
# Q = Queenstown
# S = Southampton
#以上が訓練データとして提供されている項目となります。さらに各変数の簡単な説明も記載をしておきます。
#-----------------
# 次は？..................................................... test.csv も内容を簡単に確認してみましょう。
#-----------------0
test_h = test.head()
print("次は？--test.head()")
print(test_h)
#~~~~
#    PassengerId  Pclass                                          Name     Sex   Age  SibSp  Parch   Ticket     Fare Cabin Embarked
# 0          892       3                              Kelly, Mr. James    male  34.5      0      0   330911   7.8292   NaN        Q
# 1          893       3              Wilkes, Mrs. James (Ellen Needs)  female  47.0      1      0   363272   7.0000   NaN        S
# 2          894       2                     Myles, Mr. Thomas Francis    male  62.0      0      0   240276   9.6875   NaN        Q
# 3          895       3                              Wirz, Mr. Albert    male  27.0      0      0   315154   8.6625   NaN        S
# 4          896       3  Hirvonen, Mrs. Alexander (Helga E Lindqvist)  female  22.0      1      1  3101298  12.2875   NaN        S
#~~~~

#こちらの test には、Survivedのカラムが無いのが確認できます。他のカラムは train と同様です。つまり、 train の乗客の情報と「Survived（生存したかどうか）」の答えを機械学習して、 test で提供されている乗客情報を元に、生存したか死亡したかの予測を作るのが課題ということです。
#-----------------
#次は？.....................................................train と test の簡単な統計情報とサイズも確認しておきましょう。
test_shape = test.shape
train_shape = train.shape
print("次は？--test.shape")
print(test_shape)
#~~~~
# (418, 11)
#~~~~
print("次は？--train.shape")
print(train_shape)
#~~~~
# (891, 12)
#~~~~
#次は？.....................................................pandasのdescribe()を使って、各データセットの基本統計量も確認しておきましょう。

test_d = test.describe()
train_d = train.describe()
print("次は？--test.describe()")
print(test_d)
#~~~~
#       PassengerId      Pclass         Age       SibSp       Parch        Fare
# count   418.000000  418.000000  332.000000  418.000000  418.000000  417.000000
# mean   1100.500000    2.265550   30.272590    0.447368    0.392344   35.627188
# std     120.810458    0.841838   14.181209    0.896760    0.981429   55.907576
# min     892.000000    1.000000    0.170000    0.000000    0.000000    0.000000
# 25%     996.250000    1.000000   21.000000    0.000000    0.000000    7.895800
# 50%    1100.500000    3.000000   27.000000    0.000000    0.000000   14.454200
# 75%    1204.750000    3.000000   39.000000    1.000000    0.000000   31.500000
# max    1309.000000    3.000000   76.000000    8.000000    9.000000  512.329200
#~~~~
print("次は？--train.describe()")
print(train_d)
#~~~~
#        PassengerId    Survived      Pclass         Age       SibSp       Parch        Fare
# count   891.000000  891.000000  891.000000  714.000000  891.000000  891.000000  891.000000
# mean    446.000000    0.383838    2.308642   29.699118    0.523008    0.381594   32.204208
# std     257.353842    0.486592    0.836071   14.526497    1.102743    0.806057   49.693429
# min       1.000000    0.000000    1.000000    0.420000    0.000000    0.000000    0.000000
# 25%     223.500000    0.000000    2.000000   20.125000    0.000000    0.000000    7.910400
# 50%     446.000000    0.000000    3.000000   28.000000    0.000000    0.000000   14.454200
# 75%     668.500000    1.000000    3.000000   38.000000    1.000000    0.000000   31.000000
# max     891.000000    1.000000    3.000000   80.000000    8.000000    6.000000  512.329200
#~~~~
#上記表の上が train で下が test の統計量情報となります。
#--各データのshapeを確認した通り、両データ共に「PassengerId」はTrain=891カウント、test＝418カウントと一致していますね。
#--どうやら「Age」など一部のカラムでカウント数が少ない＝つまり欠損データがあるようです。
#------------------
#次は？.....................................................両データセットの欠損データを確認していきましょう。
def kesson_table(df): 
#データセットを指定して呼び出す
        null_val = df.isnull().sum()
        #欠損値の件数を取得
        percent = 100 * df.isnull().sum()/len(df)
        #100% * 欠損値の件数 / 全体の件数 
        kesson_table = pd.concat([null_val, percent], axis=1)
        #欠損割合をconcat
        kesson_table_ren_columns = kesson_table.rename(
        columns = {0 : '欠損数', 1 : '%'})
        #列名を欠損数へリネーム
        return kesson_table_ren_columns     
# kesson_table(train)
# kesson_table(test)
print("次は？--train.kesson_table(--)")
print(kesson_table(train))
#~~~~
#            欠損数          %
# PassengerId    0   0.000000
# Survived       0   0.000000
# Pclass         0   0.000000
# Name           0   0.000000
# Sex            0   0.000000
# Age          177  19.865320
# SibSp          0   0.000000
# Parch          0   0.000000
# Ticket         0   0.000000
# Fare           0   0.000000
# Cabin        687  77.104377
# Embarked       2   0.224467
#~~~~
print("次は？--test.kesson_table(--)")
print(kesson_table(test))
#~~~~
#            欠損数          %
# PassengerId    0   0.000000
# Pclass         0   0.000000
# Name           0   0.000000
# Sex            0   0.000000
# Age           86  20.574163
# SibSp          0   0.000000
# Parch          0   0.000000
# Ticket         0   0.000000
# Fare           1   0.239234
# Cabin        327  78.229665
# Embarked       0   0.000000
#~~~~
#わかったことは？ --------------- 思ったよりもしっかりとしたデータではありますが、特に「Age」と「Cabin」の2つの項目で欠損が多いですね。
#次は？ ----------------------- 欠損データを含めたデータの事前処理を次は行なっていきましょう！ 
#今回はあくまでKaggle初心者向けチュートリアルですので、基本的なことを行なっていきます。このチュートリアルで行う内容としては・・
#(1) 欠損データを代理データに入れ替える
# (2) 文字列カテゴリカルデータを数字へ変換
#まずは train から綺麗にしていきましょう。先に確認しましたが、 train では「Age」「Embarked」「Cabin」の3カラムに欠損データがありましたね。
#「Cabin」は予測モデルで使わないので、「Age」と「Embarked」の2つの欠損データを綺麗にしていきましょう。


#まず「Age」ですが、シンプルに train の全データの中央値（Median）を代理として使いましょう。
train["Age"] = train["Age"].fillna(train["Age"].median())
# （代理データで何を使うか、どのような処理を加えるかは非常に重要かつ大きな議論ではありますが、ここはシンプルに考えて進めます）
#次に「Embarked」（出港地）ですが、こちらも2つだけ欠損データが train に含まれています。他のデータを確認すると「S」が一番多い値でしたので、代理データとして「S」を使いましょう。
#各カラムでfillna()を使って代理となるデータを入れておきましょう
train["Embarked"] = train["Embarked"].fillna("S")
print('まず「Age」ですが、シンプルに train の全データの中央値（Median）を代理として使いましょう。')
print('次に「Embarked」（出港地）ですが、こちらも2つだけ欠損データが train に含まれています。他のデータを確認すると「S」が一番多い値でしたので、代理データとして「S」を使いましょう。')
#print('')
print('??kesson_table(train))')
print(kesson_table(train))
#欠損データの処理が終わりました!
#次は？ーーーーーーーーーーーーーーーーーーーーーーーーカテゴリカルデータの文字列を数字に変換しましょう。
# 今回の予想で使う項目で文字列を値として持っているカラムは「Sex」と「Embarked」の2種類となります。
# Sexは「male」「female」の2つのカテゴリー文字列、Embarkedはは「S」「C」「Q」の3つの文字列となります。
# ーーーーーーーーーーーーーーーーーーーーーーーーーーーこれらを数字に変換しましょう。
train["Sex"][train["Sex"] == "male"] = 0
train["Sex"][train["Sex"] == "female"] = 1
train["Embarked"][train["Embarked"] == "S" ] = 0
train["Embarked"][train["Embarked"] == "C" ] = 1
train["Embarked"][train["Embarked"] == "Q"] = 2
print('''
#次は？ーーーーーーーーーーーーーーーーーーーーーーーーカテゴリカルデータの文字列を数字に変換しましょう。\n
# 今回の予想で使う項目で文字列を値として持っているカラムは「Sex」と「Embarked」の2種類となります。\n
# Sexは「male」「female」の2つのカテゴリー文字列、Embarkedはは「S」「C」「Q」の3つの文字列となります。\n
# ーーーーーーーーーーーーーーーーーーーーーーーーーーーこれらを数字に変換しましょう。\n
''')
#確認
print(train.head(10))
#上記の通り、SexとEmbarkedに入っていた文字列の値が、数字へ変換されていることが確認できます。
print('''
上記の通り、SexとEmbarkedに入っていた文字列の値が、数字へ変換されていることが確認できます。\n
''')
#次は？ーーーーーーーーーーーーーーーーーーーーーーーー次は test も同様の処理を行わないといけません。
print('''
#次は？ーーーーーーーーーーーーーーーーーーーーーーーー次は test も同様の処理を行わないといけません。\n
''')
test["Age"] = test["Age"].fillna(test["Age"].median())
test["Sex"][test["Sex"] == "male"] = 0
#^^ SettingWithCopyWarning: A value is trying to be set on a copy of a slice from a DataFrame
test["Sex"][test["Sex"] == "female"] = 1
#^^ SettingWithCopyWarning: A value is trying to be set on a copy of a slice from a DataFrame
test["Embarked"][test["Embarked"] == "S"] = 0
test["Embarked"][test["Embarked"] == "C"] = 1
test["Embarked"][test["Embarked"] == "Q"] = 2
test.Fare[152] = test.Fare.median()
print(test.head(10))
#同様に「Age」へは中央値（Median）の代入、また文字列の値（AgeとEmbarked）は数字に変換しました。
#さらに、 test では、「Fare」に一つだけ欠損がありましたので、こちらも年齢と同様に中央値（Median）を代理で入れています。念のためhead()でデータの中身も確認をしておきましょう。
print('''
#同様に「Age」へは中央値（Median）の代入、また文字列の値（AgeとEmbarked）は数字に変換しました。\n
#さらに、 test では、「Fare」に一つだけ欠損がありましたので、こちらも年齢と同様に中央値（Median）を代理で入れています。念のためhead()でデータの中身も確認をしておきましょう。\n
''')


#次は？ーーーーーーーーーーーーーーーーーーーーーーーーとうとう本題の予測モデルを作って、実際に予測をしてみましょう！本記事では予測モデル「決定木」を異なるデータで訓練して、結果を比較してみようと思います。

print('''
#次は？ーーーーーーーーーーーーーーーーーーーーーーーーとうとう本題の予測モデルを作って、実際に予測をしてみましょう！本記事では予測モデル「決定木」を異なるデータで訓練して、結果を比較してみようと思います。
# ''')
print('''
# まず決定木で使うTargetとFeatureの値を train から取得して格納しておきます。\n
# 次にscikit-learnの「DecisionTreeClassifier（）」を使って「my_tree_one」という決定木モデルを作成しました。\n
# 最後に事前に綺麗に処理をしておいた test から train で使ったFeatureと同様の項目の値を「test_features」へ入れて、predict()を使って予測をしました。\n
# 予測されたデータを確認してみましょう。\n
#  my_prediction.shape --サイズ確認 ??(418,)
 ''')

# scikit-learnのインポートをします
from sklearn import tree
# 「train」の目的変数と説明変数の値を取得
target = train["Survived"].values
features_one = train[["Pclass", "Sex", "Age", "Fare"]].values
# 決定木の作成
my_tree_one = tree.DecisionTreeClassifier()
my_tree_one = my_tree_one.fit(features_one, target)
# 「test」の説明変数の値を取得
test_features = test[["Pclass", "Sex", "Age", "Fare"]].values
# 「test」の説明変数を使って「my_tree_one」のモデルで予測
my_prediction = my_tree_one.predict(test_features)
print(my_prediction.shape)
print('''
# 次は？---------------------------------------------早速、予測データの中身を確認 --print(my_prediction)
 ''')
print(my_prediction)

print('''
# 予測をしなくてはいけないデータ数、つまり test のデータ数は418個でしたが、\n
# 上記の通りmy_predictionも同じ数の予測数が結果として出力されていますね。\n
# 今回の予測は「0か1（生存か死亡）」でしたが、念のため中身も確認してみると0と1で構成されているのが確認できます。\n
 ''')




print('''
# 次は？ ----------------------------------------------では、この予測データをCSVへ書き出してKaggleへ早速投稿してみましょう！下記のコードでPassengerIdと予測値を取得してCSVファイルを書き出します。
 ''')
# PassengerIdを取得
PassengerId = np.array(test["PassengerId"]).astype(int)
# my_prediction(予測データ）とPassengerIdをデータフレームへ落とし込む
my_solution = pd.DataFrame(my_prediction, PassengerId, columns = ["Survived"])
# my_tree_one.csvとして書き出し
my_solution.to_csv("(指定する)/exec/output/my_tree_one.csv", index_label = ["PassengerId"])
#ファイルがKaggleの投稿基準を満たしていると、即座にスコアを計算して表示してくれます。\n
# 「my_tree_one」は「チケットクラス（社会経済的地位）」「性別」「年齢」「料金」の4つのデータを用いて「決定木」のモデルを使い予測を行いましたが、結果として「0.71770」のスコアが獲得できました。
# Kaggleのスコアはコンペにより異なります。各コンペの「Evaluation」のページに詳細が記載されています。\n
# 今回予測を行なったタイタニックのコンペでは予測スコアは単純に「Accuracy（正解率）」が使われていますので、今作った「my_tree_one」は約71.8%の確率で正解を予測できましたということになります。
#参考までにですが、Kaggleタイタニックのランキングを見てみると「0.71770」のスコアですと、約8600位前後となります。\n
# （＊このタイタニックの予測課題ですが、実は100%（つまりスコア1.0）を叩き出している強者データサイエンティストもいます。\n
# インターネットにその手法も公開されています。）


# 次は?----------------------------------------------この71.8%のスコアよりももう少し正確なモデルを作って見ましょう！\n

print('''
# 次は?----------------------------------------------この71.8%のスコアよりももう少し正確なモデルを作って見ましょう！\n
# 予測モデル その2 「決定木 + 7つの説明変数」を進めていきます。\n
# さて、予測モデルその1では「タイタニックに乗船していた客の「チケットクラス」「性別」「年齢」「料金」のデータを元に生存したか死亡したかを予測」しました。Kaggleで答え合わせをすると「約71.8%」の正解率でした。\n
# では・・この正解率を上げるためにはどうすれば良いでしょうか？\n
# 少し考えて見てください\n
# ・・・
# ・・・
# 色々と試せることはあるかと思いますが、パッと思いつく限りだと、予測モデルの訓練で使うデータに他の変数も加味してみてはどうだろう？！と考えれますよね。\n
# では、「その1」では4つのデータしか予測モデルに反映しませんでしがが、他で使えそうなデータも予測モデルに使って見ましょう！\n
# 映画「タイタニック」でも家族や子供と一緒に船から脱出を試みるシーンがあったように記憶してますが、これは恐らく生存確率に影響をしそうですよね。\n
# また出発港も3つのカテゴリしかありませんが、生存確率に何かしらの影響はあるのでは？と睨んで追加をしてみましょう。\n
# まずはtrainのデータセットから今回追加になった項目の値も追加して「features_two」に取り出しましょう。\n
# また、予測モデルその2では、簡単ではありますが「過学習（Overfitting）」についても考えて見ましょう。\n
# その1で作成した決定木のモデルではmax_depthとmin_samples_slitのアーギュメントを指定しませんでしたが、その2のモデルではアーギュメントを設定してみましょう。\n
# さて、モデルの作成もできましたので、実際に「my_tree_two」を使って予測をしてみましょう。\n
# 上記のコードを正しく打ち込んでいれば、「my_tree_two.csv」として新しく作成した決定木による予測のCSVファイルが書き出されているはずです。\n
# では、早速、Kaggleへ戻って結果をアップロードしてみましょう。\n
# 結果は・・スコア「0.76076」でした！つまり、正解確率が約76.0%とすこ〜しだけ改善されています。その１では正解率が約71.8%でしたので、訓練データを増やしたことにより約4%の改善ができました。\n
 ''')

 print('''
# まとめ\n
# 今回の記事ではKaggle初心者編として、タイタニック号の乗客リストを使った生存予測を行ってみました。簡単な事前データ処理とScikit-learnの決定木を使うことで、思ったよりも簡単に機械学習に触れることが可能です。\n
# 英語ばかりで慣れないKaggleではありますが、機械学習を学ぶ人にとっては避けて通れないほど魅力が詰まっています。是非、これを機械にKaggleへの参加をしてみましょう。\n
# codexaでは、機械学習初心者向けのチュートリアルや無料講座や有料チュートリアルも配信しています。Kaggleへ参加される前にPythonの機械学習系ライブラリの操作方法などを身につけてみましょう。\n
  ''')



print('''
#以上です。
# ''')

#以上です。
