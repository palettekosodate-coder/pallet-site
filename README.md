# 子育て応援隊ぱれっと - ウェブサイト

東京都世田谷区の子育て支援団体「子育て応援隊ぱれっと」の公式ウェブサイトです。

## ファイル構成

```
palette-site/
├── index.html      … トップページ
├── shokuiku.html   … 食育＆学習支援
├── workshop.html   … 季節のワークショップ
├── sawakai.html    … 茶話会
├── privacy.html    … プライバシーポリシー
├── palette-logo.png … ロゴ画像
├── styles.css      … 共通スタイルシート
├── images/         … イラスト画像（SVG）
└── README.md       … このファイル
```

## デプロイ方法

静的HTMLサイトなので、以下のサービスで無料ホスティングできます。

### Cloudflare Pages（推奨）

1. [Cloudflare](https://dash.cloudflare.com/) にアカウント登録
2. 「Pages」→「Create a project」→「Direct Upload」を選択
3. `palette-site` フォルダをドラッグ＆ドロップでアップロード
4. プロジェクト名を入力して「Deploy」

### Netlify

1. [Netlify](https://app.netlify.com/) にアカウント登録
2. トップページ下部の「Deploy manually」エリアに `palette-site` フォルダをドロップ
3. 自動でデプロイされます

## 独自ドメインの接続

1. お名前.com / ムームードメイン等でドメインを取得
2. Cloudflare Pages / Netlify の管理画面で「Custom domains」を設定
3. ドメイン管理画面でDNSレコード（CNAMEまたはAレコード）を設定
4. SSL証明書は自動で発行されます

## コンテンツの更新方法

HTMLファイルをテキストエディタで開いて編集します。

### テキストの変更
該当するHTMLファイル内のテキストを直接書き換えてください。

### 画像の追加
1. 画像ファイルを `palette-site` フォルダ内に配置
2. HTMLファイル内で `<img src="ファイル名.jpg" alt="説明">` として参照

### ロゴの差し替え
`palette-logo.png` ファイルを差し替えてください。ヘッダーで `<img src="palette-logo.png">` として参照しています

## 差し替えが必要な箇所（TODO）

HTMLファイル内に `<!-- TODO: ... -->` コメントで目印をつけています。以下を実際の情報に差し替えてください。

- **メールアドレス**: `info@example.com` → 実際のアドレスに
- **Instagramアカウント**: `@palette_setagaya` → 実際のアカウントに
- **利用者の声**: プレースホルダーテキストを実際の感想に
- **定員**: `○名` を実際の人数に
- **寄付方法**: 振込先やオンライン決済リンクを追記

## Google Search Console への登録

1. [Google Search Console](https://search.google.com/search-console/) にアクセス
2. 「プロパティを追加」→「URLプレフィックス」で自分のサイトURLを入力
3. 表示される確認用HTMLファイルを `palette-site` フォルダに追加してデプロイ
4. Search Console上で「確認」ボタンを押す
5. 「サイトマップ」→ `sitemap.xml` のURLを送信（必要に応じて作成）
