# やりたいこと
- mackerel-agentを利用して、Mackerelのダッシュボードに独自 ( カスタム )メトリクスを投稿してグラフ描画する。
  - awsアカウントのEC2インスタンスの起動中・停止中の台数をグラフ化してみる。

- 環境
  - Ubuntu16.04
    - IAMロールを付与
    - mackerel-agent
    - Python3
    - boto3 

- Mackerel公式サイトのカスタムメトリクスを投稿する場合について
  - https://mackerel.io/ja/docs/entry/advanced/custom-metrics

# mackerel-agentの設定

- `/etc/mackerel-agent/mackerel-agent.conf`

```
apikey = "XXXXX"
include = "/etc/mackerel-agent/*"
```

- `/etc/mackerel-agent/get_instance_num`

```
[plugin.metrics.ec2num]
command = 'python3 /usr/local/yhidetoshi/get_instance_num.py'
```

# 結果
- 起動中のインスタンス数が1, 停止中のインスタンス数が0というグラフを作成することができた。 

![Alt Text](https://github.com/yhidetoshi/Pictures/raw/master/Blog/mackerel-custommetrics-instance.png)

