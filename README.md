# 子育て応援隊ぱれっと - 公式Webサイト

東京都世田谷区の子育て支援団体「子育て応援隊ぱれっと」の公式Webサイトです。

🌐 **https://palette-kosodate.jp**

## 概要

食育・学習支援、季節のワークショップ、発達に関する茶話会を通じて、子どもも保護者も安心して過ごせる場をつくっています。

## 技術スタック

- HTML / CSS（静的サイト、フレームワーク不使用）
- Google Fonts（Zen Maru Gothic）
- Cloudflare Pages（ホスティング）
- 独自ドメイン：palette-kosodate.jp（お名前.com）
- メール：Google Workspace

## ファイル構成

```
palette-site/
├── index.html              … トップページ
├── shokuiku.html           … 食育＆学習支援
├── workshop.html           … 季節のワークショップ
├── sawakai.html            … 茶話会
├── privacy.html            … プライバシーポリシー
├── styles.css              … 共通スタイルシート
├── favicon.ico             … ファビコン
├── events/                 … イベントLP
│   ├── shokuiku-01.html    … 春のおにぎりパーティー＆学習会
│   ├── shokuiku-02.html    … 旬の野菜で作ろう！カレー教室
│   ├── workshop-01.html    … 春のお花見ピクニック＆工作会
│   ├── workshop-02.html    … こいのぼり工作＆春の自然観察
│   ├── sawakai-01.html     … 3月の茶話会
│   └── sawakai-02.html     … 4月の茶話会
├── images/
│   ├── palette-logo.png    … ロゴ画像
│   ├── palette-hero.mp4    … ヒーロー動画
│   ├── apple-touch-icon.png … Apple Touch Icon
│   ├── shokuiku.svg        … 食育イラスト
│   ├── workshop.svg        … ワークショップイラスト
│   ├── sawakai.svg         … 茶話会イラスト
│   ├── hero-illustration.svg
│   ├── fincscreateaccount.png
│   └── ogp/                … OGP画像（各ページ用）
│       ├── ogp-index.png
│       ├── ogp-shokuiku.png
│       ├── ogp-workshop.png
│       ├── ogp-sawakai.png
│       ├── ogp-privacy.png
│       └── ogp-event-*.png
└── README.md
```

## デプロイ

Cloudflare PagesでGitHub連携済み。mainブランチへのpushで自動デプロイされます。

```bash
git add .
git commit -m "変更内容の説明"
git push
```

## ドメイン・DNS設定

| 項目 | 設定 |
|---|---|
| ドメイン | palette-kosodate.jp（お名前.com） |
| DNS | Cloudflare |
| SSL | Cloudflare（自動発行） |
| メール | Google Workspace（MXレコード設定済み） |

## 差し替えが必要な箇所（TODO）

HTML内の `<!-- TODO: ... -->` コメントで目印あり。

- メールアドレス：`info@example.com` → 実際のアドレス
- Instagramアカウント：`@palette_setagaya` → 実際のアカウント
- 利用者の声：プレースホルダーを実際の感想に
- Fincs登録URL：モーダル内のリンク先
- イベントLP内の申し込みリンク

## ライセンス

© 2023-2026 子育て応援隊ぱれっと All Rights Reserved.
