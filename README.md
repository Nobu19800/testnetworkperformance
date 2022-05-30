# testnetworkperformance

## test_jitter_all.ps1
pingコマンドを連続して実行するスクリプト

PowerShell上で実行する。

```
.\test_jitter_all.ps1
```

スクリプト内の変数を変更することでパケットサイズや試行回数を変更できる。

|変数名|意味|
| ------------- | ------------- |
|`MIN_SIZE`|パケット最小サイズ|
|`MAX_SIZE`|パケット最大サイズ|
|`STEP_SIZE`|パケットの最小サイズから最大サイズまで徐々にサイズを増加させて計測するが、増加のステップサイズを指定する|
|`ONLY_ONCE`|trueの時はパケット最小サイズで1回だけ実行する|
|`IP_ADDRESS`|相手のIPアドレス|
|`PING_MAX_COUNT`|あるパケットサイズでの試行回数|
|`LOG_DIR`|ログファイルの出力先|


## analyze_jitter.py

`test_jitter_all.ps1`が出力したログファイルから時間だけ取り出すスクリプト。
ログを保存したフォルダを指定して実行する。

```
.\analyze_jitter.py test_${IP_ADDRESS}_${MIN_SIZE}_${MAX_SIZE}_${STEP_SIZE}
```

この時、ログファイルのフォルダは以下の形式のファイル名になっている必要がある。
`***`は`_`を含まない文字列。

```
****_${IP_ADDRESS}_${MIN_SIZE}_${MAX_SIZE}_${STEP_SIZE}
```

ログファイルは以下の形式のファイル名で保存されている必要がある。

```
****_${IP_ADDRESS}_${MIN_SIZE}_${MAX_SIZE}_${STEP_SIZE}_${DATA_SIZE}.log
```

出力ファイル名は以下のようになっている。

```
#最小値、最大値、平均値を出力
****_${IP_ADDRESS}_${MIN_SIZE}_${MAX_SIZE}_${STEP_SIZE}.txt
#抽出したデータのリストを出力
****_${IP_ADDRESS}_${MIN_SIZE}_${MAX_SIZE}_${STEP_SIZE}_datalist.txt
```
