# portfolio_project

# Git ブランチ名の命名規則

Git のブランチ名には、開発作業の内容を分かりやすく示すための命名規則があります。以下は、一般的に使われるブランチ名の命名パターンです。

## 1. `feature/` プレフィックス
新しい機能を開発するためのブランチに使います。
例:
- `feature/user-authentication`
- `feature/payment-integration`

## 2. `bugfix/` プレフィックス
バグを修正するためのブランチに使います。
例:
- `bugfix/login-error`
- `bugfix/fix-crash-on-startup`

## 3. `hotfix/` プレフィックス
本番環境で発生した緊急のバグ修正に使います。
例:
- `hotfix/critical-issue`
- `hotfix/fix-payment-bug`

## 4. `chore/` プレフィックス
機能追加ではなく、コードの整理や環境設定の変更などを行う場合に使います。
例:
- `chore/update-dependencies`
- `chore/refactor-api`

## 5. `docs/` プレフィックス
ドキュメントの更新や追加を行うブランチに使います。
例:
- `docs/update-readme`
- `docs/add-api-docs`

---

## 命名のポイント
- **わかりやすく**: 他の開発者が見ても、何をしているのか分かるように名前を付ける。
- **短く簡潔に**: ブランチ名が長すぎないように心掛ける。
- **スラングを避ける**: なるべく一般的で理解しやすい言葉を使う。

## 📦 使用技術
- Python 3.13.2
- Django 5.2
- HTML/CSS
- etc...

## 🚀 開発ルール

### 🛠️ コーディングルール
- **ファイル命名規則**：
  - Pythonファイル：`snake_case.py`
  - HTMLテンプレート：`snake_case.html`
- **関数名・変数名**：`snake_case` を使用
- **クラス名**：`PascalCase`
- **1ファイル1責務**を意識（関数が多くなりすぎないよう分割）
- **マジックナンバーは禁止**（定数化）
- **コメントは日本語でOK／docstringは英語で書く**

### 🧱 フォルダ構成ルール（Django向け）
- アプリごとに `/templates/` `/static/` を配置
- 共通テンプレートは `base.html` を作成し継承で管理
- URLはアプリごとに `urls.py` を持ち、プロジェクト直下で `include()` を使用

### 🔁 Git運用ルール
- **ブランチ戦略**（個人開発でも使ってOK）：
  - `main`：本番に出すコード（デプロイ対象）
  - `dev`：開発用（デフォルトブランチ）
  - `feature/xxx`：機能ごとの作業ブランチ

- **PR（プルリク）ルール**：
  - 個人開発でもPRを通して変更を見直す癖をつける
  - PR名は `feat: 機能追加`, `fix: バグ修正`, `refactor: リファクタ` 等のPrefixを付ける

### 📝 コミットメッセージルール（厳選版）
コミットメッセージは**目的が一発でわかるように**。  
以下のフォーマットをベースに使おう：


#### 代表的なタイプ一覧（使い回せるやつ）

| タイプ     | 内容                     |
|------------|--------------------------|
| `feat`     | 新機能の追加             |
| `fix`      | バグ修正                 |
| `docs`     | ドキュメントの変更       |
| `style`    | フォーマットの変更のみ   |
| `refactor` | リファクタ（挙動変更なし）|
| `test`     | テストの追加・修正       |
| `chore`    | ビルド・依存など雑多系   |

#### 例：

 - feat: helloページのルーティングを追加
 - /hello/ にアクセス時に hello_view を返す処理を追加。