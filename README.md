## NuxtJs概要
* nuxtjsとは  
　→nextjs(react)をリスペクトして生まれた最近話題のFW  
　→Vueの主要ライブラリを内包したフルスタックフレームワーク  
　→SSRできる！
* https://ja.nuxtjs.org/
* https://ssr.vuejs.org/ja/

## 特徴・機能

* SEOバッチリ

* head・metaタグをnuxt.config.jsでデフォルト設定

* ビルドプロセス隠蔽
　→煩雑だったwebpackやらテンプレートコンパイルやらその他プラグインをいい感じにしてくれる

* Vue(Router Vuex Server Renderer vue-meta)が内包されている

* 独自レイヤの実装(nuxtjs自体が裏にサーバー・その他ミドルウェアを持っている)
　→SSRはもちろん、301/302リダイレクト・描画前にVuex等に必要なデータを格納しておける  

* 規約を守って開発するFW
　→具体例は後述。規約を守るとルーティングとかいい感じにやってくれて高速開発できる

* pwa公式対応

## サンプルコード入手
実際に一から開発する際は「$ npx create-nuxt-app [project-name]」でいける。  

```$ git clone git@github.com:ishizukayusuke/nuxt-docker-sample.git```

## 動かす
docker-compose  
```
$ docker-compose up 
```

docker
```
ビルド
$ docker image build -t nuxt-app:latest .
動かす
$ docker run -d -p 3000:3000 --name nuxt-app nuxt-app:latest 

```

もしくは(ホットリロード可)
```
 $ brew install node  
 $ brew install yarn
 $ cd nuxt-docker-sample
 $ yarn
 $ yarn dev
```

## ルーティングを試してみる
他にも実装で試してみたいものたくさんありますが、すいませんまたの機会に。。。

* 「pages/wedding/index.vue」作成
```
<template>
  <div>
    <p>
      こんにちは
      /wedding/index.vue
      です
    </p>
  </div>
</template>
```
* http://localhost:3000/wedding/ にアクセス
* .nuxt/router.js に/weddingのルーティング定義が追加されている

## 描画の流れ(多分)
* http://localhost:3000/ にアクセス
* 該当するテンプレート「pages/index.vue」が呼ばれる？
* scriptタグないの処理が走る「fetchItems」（store/index.js）される？
* store/index.js「fetchItems」が呼ばれ（qiitaのapi叩いてます）結果がstoreにコミットされる？  
　※ ajaxではない。axios(nodejs側でapi叩いてる)
* 「pages/index.vue」のテンプレートタグないの内容がstoreの内容をもとに決まり、描画される。  
ここまで全てサーバーサイド。

## デプロイ
nuxtjsでssrする場合サーバーサイドのモジュールも成果物に含まれるので、  
index.htmlとかにしてs3に配置、、はできない。  

[公式](https://nuxtjs.org/faq/deployment-aws-s3-cloudfront)みた感じawsで上手いことやってる解説はなし。


調べた感じの代案。とりあえずnodejsが動けばnuxtjsの実行環境としては良いらしい。  
サーバーサイドのAPIに関しても今まで通りjson返却すればよし(API側でhtml返さなきゃいけないのかと思ってた。。。。)。

* docker化  
　→SSRサーバーもろともDokcerコンテナ化してecsなりeksなりでデプロイ  
　→やってみたのですがメモリの割り当て128Mとかだと起動に失敗する

* api gatway + lamda  
　→あんまよくわかってないですが、apigateway結構あまりどころが多いらしい。

* Google App Engine  
　→nodejsの実行環境を公式にサポートしているのでawsにこだわらないのであればこちらが無難らしい。

* firebase

## ちなみに

SSR以外にも対応したモードがある。「npx create-nuxt-app [project-name]」やった時に選択可能。  


* Universalモード  
　→デフォルト。SSRをサポートしたモード
* Generateモード  
　→全てのSSRルートをレンダリングしてから、静的ページとしてindex.htmlを吐き出すモード  
　→静的ページだがSEOメタなどのメタ情報を十分に含んだページが作成可能。nuxtjsの高機能・高速開発はそのままできる。
* SPAモード
　→従来通りのSPAページ作成。nuxtjsの高機能・高速開発はそのままできる。

静的なページの作成も非常に効率的に行える。
