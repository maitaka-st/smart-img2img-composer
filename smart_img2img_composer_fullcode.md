## README.md

`markdown
# 🎲 Smart Img2Img Composer v1.1.2 Stable

[日本語版 (README_ja.md)](README_ja.md)

![Smart Img2Img Composer Overview](docs/images/1en.png)

## Overview
**Smart Img2Img Composer** is an advanced prompt construction and asset management architecture for the AUTOMATIC1111 Stable Diffusion WebUI, designed to control and deeply automate your img2img workflows.

Equipped with autonomous tag analysis from reference images, memo file synchronization, a unique lottery system for LoRAs and wildcards (Inventory feature), and model-specific prompt optimization. It fully automates tedious batch processing and prompt building, drastically improving creative efficiency and generation quality.

---

## 📥 Installation

1. Open the `Extensions` tab in your AUTOMATIC1111 WebUI.
2. Select the `Install from URL` tab.
3. Paste the following **Repository URL** into the URL field:
   ```text
   https://github.com/MaxwelI-st/smart-img2img-composer
   ```
4. Click the `Install` button.
5. After installation succeeds, go to the `Installed` tab and click `Apply and restart UI`.

*(Note: To use the Auto-Prompt Generator feature, the "WD14 Tagger" extension must be installed and active beforehand.)*

---

## ✨ Full Features of v1.1.2

### 🧠 Autonomous Analysis & Prompt Generator (Tagger Analyzer)
![Tag Analysis and Auto Prompt Gen](docs/images/2en.png)
*   **Auto Tag Extraction**: In the `Prompt Generator` tab, it integrates with WD14 Tagger to extract high-precision tags from uploaded images using deep learning.
*   **Category Controls**: Individual sliders for categories (Composition, Background, Character, NSFW, etc.) allow fine-tuned control over "Confidence Thresholds," giving you only the tags you want.
*   **Mosaic Auto-Detection**: Automatically detects mosaic/censored attributes in images and injects corresponding protective tags (e.g., `censored`).
*   **🚀 1-Click Warp**: Once you are satisfied with your extracted prompt, click the dedicated button to **warp directly to the img2img tab** with all prompt data and images fully intact, enabling an immediate start to your generation.

### 🔗 Filename-Driven Automatic Prompt Synchronization (Memo Sync)
*   **Auto Matching**: Automatically matches filenames in the `Reference Image Folder` with manually written section tags (e.g., `[image_01]`) in your `Memo File` (.txt).
*   **Match Threshold**: The UI slider allows for flexible fuzzy-matching, ensuring seamless application of image-specific unique prompts even during massive bulk generation runs.

### 🛡️ Model-Specific Prompt Optimization (Smart Negative & Polish)
![Smart Negative Feature](docs/images/3en.png)
*   **Smart Negative**: By selecting your target model architecture (SDXL, Pony, Illustrious, Animagine, etc.) from the `Active Profile`, the system automatically injects or overwrites the absolute optimal negative prompts to maximize that model's potential.
*   **Prompt Order Optimization**: Automatically sorts the generated tags based on your selected profile. For Pony lineages, critical quality items like `score_9, score_8_up...` are forced to the front.
*   **Prompt Polish**: Effortlessly cleans up syntax errors right before generation, such as duplicate tags, trailing spaces, and double commas (`, , `), while completely protecting your intentional LoRA weights.

### 📦 Bias-Prevention Autonomous Inventory Control (Inventory Logic)
![Inventory Control System](docs/images/4en.png)
*   **Asset Management**: Manage custom lists of Character LoRAs, Situation LoRAs, and Wildcards directly from the WebUI inside the `Asset Lists` tab.
*   **Inventory Control**: The robust lottery logic remembers the "usage history" of assets during randomized generation. It heavily prioritizes **"assets that have never been used"** or **"assets with the lowest usage counts."** This entirely eliminates repetitive "LoRA fatigue" during mass productions.

### 🪄 Auto-Syntax Repair & Custom Dictionary
*   Setup simple shortcuts like `night, city > cyberpunk cityscape, neon lights...` in the Custom Dictionary. Short memo keywords will be beautifully expanded into rich, descriptive prompts automatically.

### 🎛️ Output Organization & High-Density UI
![Streamlined Professional UI Design](docs/images/5en.png)
*   **Health Check (Fail-Safe)**: Real-time path validation for folders and text files with ✅ / ❌ indicators on the UI to prevent silly execution crashes.
*   **Auto-Filename**: Automatically renames output images (e.g., `masterpiece-1girl-smile_0001.png`) by combining the core extracted prompt tags.
*   **Smart Output Sorting**: Change the `Sort Mode` to automatically create clean subfolders organized by "Preset Name," "Section Name," or "Date" without breaking standard save settings.

---

## 📖 Quick Start Usage

1. **Global Settings**: In the `Smart Img2Img Composer` tab under `Settings & Preview`, enter your `Reference Image Folder` and (optional) `Memo File` path.
2. **Options**: Check `Auto-Optimize Prompt` and `Smart Negative`, then select your `Active Profile`.
3. **Save Preset**: Once configured, type a name and click "Save Settings" to store your Preset.
4. **Execute**: Open the `img2img` tab, expand the accordion, check `Enable`, and hit "Generate." The extension will automatically batch-process everything in the folder using your synced memos, optimized prompts, and random inventories!

---
*Developed by Antigravity*

`

## README_ja.md

`markdown
# 🎲 Smart Img2Img Composer v1.1.2 Stable

[English Version (README.md)](README.md)

![Smart Img2Img Composer 全体概要](docs/images/1ja.png)

## 概要 (Overview)
**Smart Img2Img Composer** は、AUTOMATIC1111 Stable Diffusion WebUI 向けの、img2imgワークフローを統合的に制御・自動化するための高度な拡張機能です。

参照画像の自律タグ解析、メモファイルとのプロンプト同期、LoRAやワイルドカードの独自の抽選システム（インベントリ機能）、そしてモデル固有のプロンプト最適化機能を備えています。煩雑なimg2imgの大量バッチ処理やプロンプト構築作業を全自動化し、作業効率と生成品質を飛躍的に向上させます。

---

## 📥 インストール方法 (Installation)

1. AUTOMATIC1111 WebUIの `Extensions` タブを開きます。
2. `Install from URL` タブを選択します。
3. 以下の**リポジトリURL**を入力欄にペーストします：
   ```text
   https://github.com/MaxwelI-st/smart-img2img-composer
   ```
4. `Install` ボタンをクリックします。
5. インストール完了後、`Installed` タブへ移動し `Apply and restart UI` をクリックしてWebUIを再起動してください。

*(※タグ解析機能を使用する場合、あらかじめ「WD14 Tagger」拡張機能がインストールされ有効になっている必要があります。)*

---

## ✨ v1.1.2 の全機能紹介 (Full Features)

### 🧠 参照画像の自律解析とプロンプト構築 (Tagger Analyzer)
![タグ解析とプロンプト自動生成](docs/images/2ja.png)
* **自動タグ抽出**: `Prompt Generator` タブにて、WD14 Taggerと連携し、深層学習を用いてアップロードされた画像から高精度なタグを抽出します。
* **カテゴリ別コントロール**: 構図、背景、人物、NSFW要素など、細分化されたカテゴリごとに「信頼度（Confidence）のしきい値」を個別に設定し、必要なタグだけを厳選できます。
* **モザイク自動検知**: 画像からモザイク・検閲属性を検知し、適切なタグ（`censored` 等）を自動で付与します。
* **🚀 1クリック・ワープ**: 納得のいくプロンプトが抽出できたら、専用ボタンを押すだけで**プロンプトと画像を保持したまま自動的に img2img タブへ画面遷移**し、即座に生成を開始できます。

### 🔗 ファイル名駆動型のプロンプト自動同期 (Memo Sync)
* **自動紐付け**: `Reference Image Folder`（参照画像フォルダ）内のファイル名と、`Memo File`（.txt）内に記述したセクション名（例：`[image_01]`）を自動でマッチングします。
* **Match Threshold（一致度設定）**: スライダーを設定することで、完全一致でなくても柔軟に紐付けることができ、大量のバッチ処理時にも「画像ごとの固有プロンプト」をシームレスに適用します。

### 🛡️ モデル別プロンプト自動最適化 (Smart Negative & Polish)
![スマート・ネガティブ機能](docs/images/3ja.png)
* **Smart Negative（ネガティブ補強）**: `Active Profile` から使用するモデル体系（SDXL, Pony, Illustrious, Animagineなど）を選択すると、そのモデルのポテンシャルを最大限に引き出す必須ネガティブプロンプトが自動で追加・上書きされます。
* **プロンプト並び順の最適化**: 選択したプロファイルに合わせてプロンプトの順序をソートします。例えばPony系なら `score_9, score_8_up...` 等の品質タグを自動で最前列へ移動させます。
* **Prompt Polish（プロンプト整形）**: 重複した不要なタグや、連続するカンマ（`, , `）、無駄な空白を生成直前に完璧にクリーンアップします。（※意図的なLoRAウェイトは保護されます）

### 📦 資産の偏りを防ぐ自律型インベントリ制御 (Inventory Logic)
![インベントリ制御システム](docs/images/4ja.png)
* **アセット管理**: `Asset Lists` タブで、ランダム生成に使用するキャラクターLoRA、シチュエーションLoRA、ワイルドカードのリストをWebUI上から直接管理できます。
* **Inventory Control（在庫管理）**: ランダム生成時にアイテムの「使用回数履歴」を記憶し、**「まだ一度も使われていないアセット」や「使用回数が少ないアセット」を優先的に高確率で選出**する独自の抽選ロジックが働きます。これにより「同じLoRAばかりが選ばれる」マンネリ化を完全に防止します。

### 🪄 独自辞書によるタグ展開 (Custom Dictionary)
* `night, city > cyberpunk cityscape, neon lights...` のように辞書登録しておくことで、短いメモ書きをリッチな長文プロンプトへ全自動で変換・展開します。

### 🎛️ 出力整理と高密度UI設計 (Output Organization & UI)
![操作を快適にする洗練された設計](docs/images/5ja.png)
* **Health Check（フェイルセーフ）**: 設定したフォルダやテキストファイルのパスが存在するかをリアルタイムに検証し、UI上に ✅ / ❌ で表示します。
* **Auto-Filename（自動命名）**: 抽出された重要なプロンプトタグを組み合わせて、出力画像ファイルの名前（例：`masterpiece-1girl-smile_0001.png`）を自動生成します。
* **Smart Output Sorting**: 保存先サブフォルダを「指定したプリセット名」や「セクション名」「日付」ごとに自動作成・仕分けし、出力結果を綺麗に整理できます。

---

## 📖 使い方 (Quick Start)

1. **基本設定**: `Smart Img2Img Composer` タブの `Settings & Preview` で、画像の入ったフォルダとメモファイル（任意）のパスを指定します。
2. **生成オプション**: `Auto-Optimize Prompt` や `Smart Negative` にチェックを入れ、プロファイルを指定します。
3. **プリセット保存**: 設定が完了したら名前を付けて「Save Settings」でプリセットとして保存します。
4. **img2img の実行**: `img2img` タブを開き、アコーディオン内の `Enable` にチェックを入れて「Generate」ボタンを押すと、フォルダ内の画像に対して自動でプロンプト処理と画像生成が連続実行されます！

---
*Developed by Antigravity*

`

## sc_composer/__init__.py

`python
# -*- coding: utf-8 -*-
# Marker for sc_composer package

`

## sc_composer/constants.py

`python
# -*- coding: utf-8 -*-
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONFIG_PATH = os.path.join(BASE_DIR, "config.json")
LORA_CHAR_PATH = os.path.join(BASE_DIR, "lora_char.txt")
LORA_SIT_PATH = os.path.join(BASE_DIR, "lora_sit.txt")
WILD_1_PATH = os.path.join(BASE_DIR, "wildcard_1.txt")
WILD_2_PATH = os.path.join(BASE_DIR, "wildcard_2.txt")
WILD_3_PATH = os.path.join(BASE_DIR, "wildcard_3.txt")
INVENTORY_PATH = os.path.join(BASE_DIR, "inventory.json")

DEFAULT_CONFIG = {
    "language": "ja",
    "image_folder": "",
    "memo_file": "",
    "match_threshold": 0.3,
    "generation_count": 1,
    "gen_conf_base": 0.35,
    "gen_conf_char": 0.35,
    "gen_conf_nsfw": 0.35,
    "gen_confidence": 0.35,
    "gen_positive": "(masterpiece:1.1), (best quality:1.0), ",
    "gen_negative": "lowres, blurry, artifact, bad anatomy, worst quality, low quality, jpeg artifacts",
    "gen_custom_dict": (
        "night, city > cyberpunk cityscape, neon lights, cinematic lighting, rain reflections, highly detailed\n"
        "sunset, skyline > golden hour lighting, dramatic sky colors, atmospheric perspective\n"
        "indoor, room > detailed background, interior design"
    ),
    "wildcard_1_path": WILD_1_PATH,
    "wildcard_2_path": WILD_2_PATH,
    "wildcard_3_path": WILD_3_PATH,
    "fallback_enabled": True,
    "auto_lora_enabled": True,
    "lora_offset": 0.0,
    "output_sort_mode": "None",
    "presets": {},
    "gen_categories": None,
    "custom_base_tags": "masterpiece, best quality, 1girl, solo",
    "auto_optimize_prompt": False,
    "active_profile": "Standard / SDXL",
    "auto_filename": False,
    "prompt_polish": False,
    "smart_negative": False,
    "smart_negative_mode": "append",
    "inventory_mode": False,
    "gen_mosaic_auto": False,
    "gen_mosaic_level": "Mosaic Med",
    "gen_custom_dict_enabled": False,
    "limit_base": 10,
    "limit_char": 10,
    "limit_nsfw": 15,
    "debug": False,
}

IMAGE_EXTENSIONS = [".png", ".jpg", ".jpeg", ".webp", ".bmp", ".gif"]

# ▼ 詳細なタグ定義 (AIによる機能性維持のための温存)
_TAG_CATEGORIES = {
    "cat_composition": ["re:.*_view", "re:.*_shot", "re:.*_perspective", "portrait", "upper_body", "lower_body", "full_body", "wide_shot", "from_above", "from_below", "from_side", "from_behind"],
    "cat_pose": ["re:.*_standing", "re:.*_sitting", "re:.*_lying", "re:.*_leaning", "re:.*_kneeling", "arm_up", "arms_behind_back", "arms_behind_head", "hand_on_hip", "hand_to_mouth", "leg_up"],
    "cat_background": ["re:.*_background", "indoor", "outdoor", "room", "bedroom", "bathroom", "kitchen", "classroom", "forest", "beach", "cityscape", "ocean", "street", "park"],
    "cat_nature": ["re:sky", "re:cloud", "re:sun", "re:rain", "re:snow", "flower", "tree", "grass", "mountain", "river", "sea", "forest"],
    "cat_lighting": ["re:.*_lighting", "sunlight", "moonlight", "backlighting", "rim_lighting", "soft_lighting", "cinematic_lighting", "neon_lights"],
    "cat_atmosphere": ["moody", "calm", "vibrant", "dark", "light", "colorful", "monochrome", "sepia"],
    "cat_meta": ["masterpiece", "best_quality", "highres", "absurdres", "quality", "solo", "1girl", "1boy"],
    "cat_char_base": ["re:skin", "re:body", "re:age", "small_breasts", "medium_breasts", "large_breasts", "huge_breasts", "flat_chest", "curvy", "slim", "muscular"],
    "cat_char_hair": ["re:.*_hair", "short_hair", "medium_hair", "long_hair", "very_long_hair", "ponytail", "twintails", "braid", "bob_cut", "blunt_bangs"],
    "cat_char_eyes": ["re:.*_eyes", "blue_eyes", "red_eyes", "green_eyes", "yellow_eyes", "brown_eyes", "purple_eyes", "pink_eyes", "heterochromia"],
    "cat_char_face": ["re:.*_smile", "re:expression", "blush", "open_mouth", "closed_eyes", "tsundere", "kuudere", "yandere"],
    "cat_char_clothes": ["re:.*_wear", "re:.*_outfit", "dress", "skirt", "shirt", "pants", "shorts", "swimsuit", "bikini", "uniform", "school_uniform", "maid_outfit"],
    "cat_char_male": ["1boy", "male_focus", "guy", "man", "muscular_male", "beard", "abs"],
    "cat_nsfw_action": ["re:.*_sex", "re:.*_position", "blowjob", "cunnilingus", "handjob", "footjob", "paizuri", "penetration", "vaginal", "anal", "group_sex", "irrumatio", "fellatio", "oral_sex", "deep_throat", "mutual_masturbation", "public_sex", "outdoor_sex", "public_intimacy", "al_fresco", "shibari", "spanking", "flogging", "impact_play", "sensory_play", "role_play"],
    "cat_nsfw_creature": ["tentacles", "monster", "demon", "orc", "goblin", "beast", "creature", "tentacle_play", "monster_sex", "tentacle_sex"],
    "cat_nsfw_item": ["vibrator", "dildo", "sex_toy", "handcuffs", "blindfold", "gag", "rope", "bondage", "milking_machine", "breast_pump", "lactation", "sybian", "automaton", "mechanical_arm", "bondage_machine", "fucking_machine", "spanking_machine", "whip", "collar", "chain", "harness", "chastity_belt", "straitjacket", "leash", "muzzle", "bit_gag", "ball_gag"],
    "cat_nsfw_focus": ["re:.*_focus", "ass_focus", "breast_focus", "pussy_focus", "penis_focus", "crotch_focus", "feet_focus", "armpit_focus", "navel_focus", "thigh_focus"],
    "cat_nsfw_fluids": ["cum", "cum_on_body", "cum_on_face", "cum_in_pussy", "cum_in_mouth", "precum", "sweat", "saliva", "urine", "body_fluids", "cum_all_over", "squirt", "splash", "gush", "spurt"],
    "cat_nsfw_fetish": ["re:.*_fingering", "re:.*_fisting", "ahegao", "tongue_out", "eyes_rolled_back", "drool", "foot_fetish", "armpit_fetish", "toe_sucking", "foot_worship", "sole_licking", "foot_trample", "pedal_play", "corruption", "fall", "descent", "decay", "malevolence", "depravity", "sinister", "nefarious", "shame", "embarrassment", "humiliation", "degradation", "dishonor"],
    "cat_nsfw_clothes_mess": ["re:.*_lift", "re:.*_pull", "re:.*_removal", "undressing", "clotheless", "naked", "topless", "bottomless", "exhibitionism", "public_exposure", "flashing", "undressing_self", "clothing_around_ankles"],
    "cat_nsfw_genitals": ["pussy", "penis", "testicles", "anus", "nipples", "erection", "clitoris", "genitals", "labia", "scrotum", "large_clitoris", "huge_penis"],
}

_CAT_BASE_KEYS = ["cat_composition", "cat_pose", "cat_background", "cat_nature", "cat_lighting", "cat_atmosphere", "cat_meta"]
_CAT_CHAR_KEYS = ["cat_char_base", "cat_char_hair", "cat_char_eyes", "cat_char_face", "cat_char_clothes", "cat_char_male"]
_CAT_NSFW_KEYS = ["cat_nsfw_action", "cat_nsfw_creature", "cat_nsfw_item", "cat_nsfw_focus", "cat_nsfw_fluids", "cat_nsfw_fetish", "cat_nsfw_clothes_mess", "cat_nsfw_genitals"]

LORA_CHAR_TEMPLATE = """# Character LoRA or Tags
# Usage:
# <lora:name:1.0>
# <lora:name:0.8>, character_tag, series_tag
#
# List your assets below:
"""

LORA_SIT_TEMPLATE = """# Situation LoRA or Tags
# Usage:
# <lora:name:1.0>
# <lora:name:0.8>, sitting, indoors
#
# List your assets below:
"""

# ▼ 復元されたプロファイル本体
PROMPT_PROFILES = {
    "Standard / SDXL": {
        "order": ["subject", "environment", "lighting", "camera", "style"],
        "ref": "(masterpiece:1.2), best quality, highres, highly detailed",
        "neg": "worst quality, low quality, bad anatomy, bad hands, missing fingers, extra digit, fewer digits, ugly, watermark, signature"
    },
    "Pony Diffusion V6 XL": {
        "order": ["score", "rating", "subject", "environment", "lighting", "camera", "style"],
        "ref": "score_9, score_8_up, score_7_up, score_6_up, source_anime, masterpiece, best quality",
        "neg": "score_4, score_5, score_6, source_pony, source_furry, source_cartoon, 3d"
    },
    "Illustrious XL": {
        "order": ["quality", "rating", "subject", "environment", "lighting", "camera", "style"],
        "ref": "masterpiece, best quality, very aesthetic, absurdres, highres, extremely detailed",
        "neg": "worst quality, bad quality, low quality, displeasing, very displeasing, chromatic aberration, abstract"
    },
    "Animagine XL 3.x": {
        "order": ["quality", "rating", "subject", "environment", "lighting", "camera", "style"],
        "ref": "masterpiece, best quality, very aesthetic, absurdres, highres",
        "neg": "lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry"
    },
    "SD 1.5 (Anime / Danbooru)": {
        "order": ["quality", "subject", "clothing", "environment", "lighting", "camera", "style"],
        "ref": "masterpiece, best quality, ultra-detailed, highres, illustration",
        "neg": "worst quality, low quality, bad anatomy, bad hands, missing fingers, extra digit, fewer digits, ugly, watermark, signature"
    }
}

`

## sc_composer/core.py

`python
import os
import json
import random
import re
from .constants import CONFIG_PATH, DEFAULT_CONFIG, INVENTORY_PATH, IMAGE_EXTENSIONS
from .utils import _clean_path, _polish_prompt, get_image_files
from .i18n import t, invalidate_lang_cache

# config キャッシュ（ディスク I/O 削減用）
_config_cache = None
_config_mtime = 0.0

def load_config() -> dict:
    global _config_cache, _config_mtime
    if os.path.exists(CONFIG_PATH):
        try:
            mtime = os.path.getmtime(CONFIG_PATH)
            if _config_cache is not None and mtime == _config_mtime:
                return dict(_config_cache)
            with open(CONFIG_PATH, "r", encoding="utf-8") as f:
                config = {**DEFAULT_CONFIG, **json.load(f)}
                for k in ["image_folder", "memo_file", "wildcard_1_path", "wildcard_2_path", "wildcard_3_path"]:
                    if k in config and isinstance(config[k], str):
                        config[k] = _clean_path(config[k])
                _config_cache = dict(config)
                _config_mtime = mtime
                return config
        except Exception as e:
            print(f"[Smart Composer] config.json 読み込みエラー: {e}")
    return dict(DEFAULT_CONFIG)

def save_config(config: dict) -> str:
    global _config_cache, _config_mtime
    try:
        old_lang = (_config_cache or {}).get("language")
        dir_path = os.path.dirname(CONFIG_PATH)
        if dir_path: os.makedirs(dir_path, exist_ok=True)
        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4, ensure_ascii=False)
        _config_cache = dict(config)
        _config_mtime = os.path.getmtime(CONFIG_PATH)
        if config.get("language") != old_lang:
            invalidate_lang_cache()
        return t("msg_settings_saved")
    except IOError as e:
        return f"{t('msg_settings_err')} {e}"

def load_inventory():
    if not os.path.exists(INVENTORY_PATH): return {}
    try:
        with open(INVENTORY_PATH, "r", encoding="utf-8") as f: return json.load(f)
    except Exception as e:
        print(f"[Smart Composer] inventory.json 読み込みエラー: {e}")
        return {}

def save_inventory(data):
    try:
        with open(INVENTORY_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"[Smart Composer] inventory.json 書き込みエラー: {e}")

def get_inventory_weighted_choice(item_list, category_key):
    if not item_list: return None
    inventory = load_inventory()
    old_hist = dict(inventory.get(category_key, {}))
    # 現在の item_list に存在するものだけ残す（削除済みアイテムの肥大化防止）
    cat_hist = {item: old_hist.get(item, 0) for item in item_list}
    weights = [1.0 / (float(cat_hist[item]) + 1.0) for item in item_list]
    choice = random.choices(item_list, weights=weights, k=1)[0]
    cat_hist[choice] += 1
    inventory[category_key] = cat_hist
    save_inventory(inventory)
    return choice

def parse_memo_file(memo_path: str) -> dict:
    memo_path = _clean_path(memo_path)
    sections = {}
    if not memo_path or not os.path.isfile(memo_path): return sections
    try:
        content = ""
        for enc in ("utf-8", "utf-8-sig", "cp932"):
            try:
                with open(memo_path, "r", encoding=enc) as f: content = f.read()
                break
            except Exception: continue
        if not content: return sections
        cur_key, cur_data, mode = None, {"positive": [], "negative": [], "lora": []}, "positive"
        def _save():
            if cur_key:
                sections[cur_key] = {
                    "positive": ", ".join(cur_data["positive"]),
                    "negative": ", ".join(cur_data["negative"]),
                    "lora": cur_data["lora"]
                }
        for line in content.splitlines():
            s_raw = line.strip()
            if not s_raw or s_raw.startswith("#"): continue
            m = re.match(r"^\[(.+)\]$", s_raw)
            if m:
                _save(); cur_key = m.group(1).strip().lower()
                cur_data, mode = {"positive": [], "negative": [], "lora": []}, "positive"
                continue
            
            # P2: "positive:" と "positive" 両方を受け付ける
            s_low = s_raw.lower().rstrip(":").strip()
            if s_low in ("positive", "negative", "lora"):
                mode = s_low; continue
            if cur_key: cur_data[mode].append(s_raw)
        _save()
    except Exception as e:
        print(f"[Smart Composer] メモファイル解析エラー: {e}")
    return sections

def compose_prompt(folder, memo, threshold, fallback=True, auto_l=True, l_off=0.0, w1="", w2="", w3="", prof_name="Standard / SDXL", inv_mode=False, selection_mode="random"):
    """5タプル (img_path, pos, neg, log, section_name) を返す共通関数。
    UI プレビュー用には compose_prompt_preview() を使うこと。"""
    config = load_config()
    _dbg = config.get("debug", False)
    if _dbg:
        print(f"[SC_DEBUG] compose_prompt: folder={folder}, memo={memo}, threshold={threshold}, mode={selection_mode}")
    if folder and not os.path.isdir(folder):
        raise ValueError(f"画像フォルダが存在しません: {folder}")
    if memo and not os.path.isfile(memo):
        print(f"[Smart Composer] 警告: メモファイルが存在しません: {memo}")
    return _compose_core(folder, memo, threshold, selection_mode=selection_mode, _dbg=_dbg)

def compose_prompt_preview(folder, memo, threshold, fallback=True, auto_l=True, l_off=0.0, w1="", w2="", w3="", prof_name="Standard / SDXL", inv_mode=False):
    """設定タブの「構成テスト」ボタン用: プレビュー文字列を返す。"""
    img, pos, neg, log, sec = _compose_core(folder, memo, threshold)
    if not img: return log
    from .constants import PROMPT_PROFILES
    profile = PROMPT_PROFILES.get(prof_name, next(iter(PROMPT_PROFILES.values())))
    p_neg = profile.get("neg", "")
    return f"--- PREVIEW ---\nSection: [{sec}]\nImage: {os.path.basename(img)}\n\nPositive:\n{pos}\n\nNegative:\n{neg}\n(Profile Neg: {p_neg})\n\nLog:\n{log}"

def _compose_core(folder, memo, threshold, selection_mode="random", _dbg=False):
    from .utils import get_image_files, _clean_path
    folder_clean = _clean_path(folder)
    memo_clean = _clean_path(memo)
    files = get_image_files(folder_clean)
    if not files:
        if _dbg: print(f"[SC_DEBUG] _compose_core: 画像なし (folder={folder_clean})")
        return None, "", "", t("no_images"), ""
    config = load_config()
    if selection_mode == "sequential":
        idx = config.get("last_sequential_index", 0) % len(files)
        sel = files[idx]; config["last_sequential_index"] = idx + 1; save_config(config)
    else: sel = random.choice(files)
    if _dbg: print(f"[SC_DEBUG] _compose_core: 選択画像={os.path.basename(sel)}, mode={selection_mode}")
    sections = parse_memo_file(memo_clean)
    if not sections:
        if _dbg: print(f"[SC_DEBUG] _compose_core: セクションなし")
        return sel, "", "", t("log_no_sections"), ""
    from difflib import SequenceMatcher
    fname = os.path.splitext(os.path.basename(sel))[0].lower()
    best_score, best_sec = -1.0, None
    for k in sections:
        if k == "default": continue
        sc = SequenceMatcher(None, fname, k).ratio()
        if _dbg: print(f"[SC_DEBUG]   match: '{fname}' vs '{k}' = {sc:.3f}")
        if sc >= threshold and sc > best_score: best_score, best_sec = sc, k
    if not best_sec:
        if "default" in sections: best_sec = "default"
        else: return sel, "", "", t("log_no_match"), ""
    
    data = sections[best_sec]
    pos = data.get("positive", "")
    neg = data.get("negative", "")
    loras = data.get("lora", [])
    if loras:
        pos = ", ".join([pos] + loras) if pos else ", ".join(loras)
    if _dbg: print(f"[SC_DEBUG] _compose_core: sec={best_sec}, score={best_score:.3f}, pos_len={len(pos)}, neg_len={len(neg)}, loras={len(loras)}")
    return sel, pos, neg, f"Matched: {best_sec} ({best_score:.2f})", best_sec

def apply_lora_offset(prompt: str, offset: float) -> str:
    if offset == 0.0: return prompt
    def repl(m):
        base, val = m.group(1), float(m.group(2))
        new_val = max(0.0, min(2.0, val + offset))
        return f"<lora:{base}:{new_val:.2f}>"
    return re.sub(r'<lora:([^:]+):([-+]?\d*\.?\d+)>', repl, prompt)

def save_all_settings(lang, img_f, memo, threshold, count, fallback, auto_l, confidence, pos, neg, c_dict, c_base, c_char, c_nsfw, w1, w2, w3, offset, mosaic_auto, mosaic_level, c_dict_enabled, auto_opt, custom_tags, active_prof, polish, smart_neg, smart_neg_mode, inventory_mode, limit_base, limit_char, limit_nsfw, c_mosaic, conf_base, conf_char, conf_nsfw, use_global_conf, sort_mode="None", auto_file=False):
    config = load_config()
    config.update({
        "language": lang, "image_folder": _clean_path(img_f), "memo_file": _clean_path(memo),
        "match_threshold": threshold, "generation_count": count, "fallback_enabled": fallback,
        "auto_lora_enabled": auto_l, "gen_confidence": confidence, "gen_positive": pos,
        "gen_negative": neg, "gen_custom_dict": c_dict, "gen_categories": list(c_base) + list(c_char) + list(c_nsfw),
        "wildcard_1_path": _clean_path(w1), "wildcard_2_path": _clean_path(w2), "wildcard_3_path": _clean_path(w3),
        "lora_offset": offset, "output_sort_mode": sort_mode, "auto_filename": auto_file, "gen_mosaic_auto": mosaic_auto, "gen_mosaic_level": mosaic_level,
        "gen_custom_dict_enabled": c_dict_enabled, "auto_optimize_prompt": auto_opt, "custom_base_tags": custom_tags,
        "active_profile": active_prof, "prompt_polish": polish, "smart_negative": smart_neg,
        "smart_negative_mode": smart_neg_mode, "inventory_mode": inventory_mode,
        "limit_base": limit_base, "limit_char": limit_char, "limit_nsfw": limit_nsfw, "gen_cat_mosaic": list(c_mosaic),
        "gen_conf_base": conf_base, "gen_conf_char": conf_char, "gen_conf_nsfw": conf_nsfw,
        "use_global_conf": use_global_conf
    })
    save_config(config)
    return f"\u2705 {t('msg_all_saved')}"

def handle_load_preset(name):
    config = load_config(); presets = config.get("presets", {}); p = presets.get(name)
    if not p: return (
        "", "", 0.3, 1,           # image_folder, memo_file, threshold, count
        True, True,               # fallback, auto_lora
        0.35, "", "", "",         # confidence, pos, neg, custom_dict
        "", "", "",               # w1, w2, w3
        0.0, False, "Med", True,  # lora_offset, mosaic_auto, mosaic_level, custom_dict_enabled
        False, "", "Standard / SDXL",  # auto_opt, custom_tags, profile
        False, False, "append",   # polish, smart_neg, sn_mode
        False, 10, 10, 15,        # inventory_mode, limit_base, limit_char, limit_nsfw
        [], [], [],               # c_base, c_char, c_nsfw (CheckboxGroup は [] が正しい)
        0.35, 0.35, 0.35,         # conf_base, conf_char, conf_nsfw
        True                      # use_global_conf
    )
    config["last_preset"] = name; save_config(config)
    all_cats = p.get("gen_categories", [])
    from .constants import _CAT_BASE_KEYS, _CAT_CHAR_KEYS, _CAT_NSFW_KEYS, WILD_1_PATH, WILD_2_PATH, WILD_3_PATH
    c_base = [k for k in all_cats if k in _CAT_BASE_KEYS]
    c_char = [k for k in all_cats if k in _CAT_CHAR_KEYS]
    c_nsfw = [k for k in all_cats if k in _CAT_NSFW_KEYS]
    return (
        p.get("image_folder", ""), p.get("memo_file", ""), p.get("match_threshold", 0.3), p.get("generation_count", 1),
        p.get("fallback_enabled", True), p.get("auto_lora_enabled", True),
        p.get("gen_confidence", 0.35), p.get("gen_positive", ""), p.get("gen_negative", ""),
        p.get("gen_custom_dict", ""), 
        p.get("wildcard_1_path", WILD_1_PATH), p.get("wildcard_2_path", WILD_2_PATH), p.get("wildcard_3_path", WILD_3_PATH),
        p.get("lora_offset", 0.0), p.get("gen_mosaic_auto", False), p.get("gen_mosaic_level", "Med"),
        p.get("gen_custom_dict_enabled", True),
        p.get("auto_optimize_prompt", False), p.get("custom_base_tags", ""), p.get("active_profile", "Standard / SDXL"),
        p.get("prompt_polish", False), p.get("smart_negative", False), p.get("smart_negative_mode", "append"),
        p.get("inventory_mode", False), p.get("limit_base", 10),
        p.get("limit_char", 10), p.get("limit_nsfw", 15),
        c_base, c_char, c_nsfw,
        p.get("conf_base", 0.35), p.get("conf_char", 0.35), p.get("conf_nsfw", 0.35),
        p.get("use_global_conf", True)
    )

def handle_save_preset(name, *args):
    if not name or not name.strip(): return "Error: Name empty", None
    config = load_config(); presets = config.get("presets", {})
    # args: [0:img, 1:memo, 2:thr, 3:cnt, 4:fall, 5:al, 6:g_conf, 7:g_pos, 8:g_neg, 9:g_cust, 10:w1, 11:w2, 12:w3, 13:l_off, 14:m_auto, 15:m_lvl, 16:c_en, 17:a_opt, 18:c_tags, 19:prof, 20:p_pol, 21:s_neg, 22:s_neg_mode, 23:inv_m, 24:l_base, 25:l_char, 26:l_nsfw, 27:c_base, 28:c_char, 29:c_nsfw, 30:conf_b, 31:conf_c, 32:conf_n, 33:ug_conf]
    presets[name.strip()] = {
        "image_folder": args[0], "memo_file": args[1], "match_threshold": args[2],
        "generation_count": args[3], "fallback_enabled": args[4], "auto_lora_enabled": args[5],
        "gen_confidence": args[6], "gen_positive": args[7], "gen_negative": args[8],
        "gen_custom_dict": args[9], "wildcard_1_path": args[10], "wildcard_2_path": args[11],
        "wildcard_3_path": args[12], "lora_offset": args[13], "gen_mosaic_auto": args[14],
        "gen_mosaic_level": args[15], "gen_custom_dict_enabled": args[16],
        "auto_optimize_prompt": args[17], "custom_base_tags": args[18], "active_profile": args[19],
        "prompt_polish": args[20], "smart_negative": args[21], "smart_negative_mode": args[22],
        "inventory_mode": args[23], "limit_base": args[24], "limit_char": args[25],
        "limit_nsfw": args[26], "gen_categories": list(args[27]) + list(args[28]) + list(args[29]),
        "conf_base": args[30], "conf_char": args[31], "conf_nsfw": args[32], "use_global_conf": args[33]
    }
    config["presets"] = presets; config["last_preset"] = name.strip(); save_config(config)
    import gradio as gr
    return f"\u2705 Saved: {name}", gr.update(choices=["Default"] + list(presets.keys()))

def handle_delete_preset(name):
    if not name or name == "Default": return "Cannot delete Default", None
    config = load_config(); presets = config.get("presets", {})
    if name in presets: del presets[name]
    config["presets"] = presets; save_config(config)
    import gradio as gr
    return f"\U0001f5d1\ufe0f Deleted: {name}", gr.update(choices=["Default"] + list(presets.keys()))

def get_inventory_status():
    inventory = load_inventory()
    if not inventory: return t("msg_no_tags_err")
    lines = []
    for cat, items in inventory.items():
        lines.append(f"### {cat}")
        sorted_items = sorted(items.items(), key=lambda x: x[1], reverse=True)
        for item, count in sorted_items: lines.append(f"- {item}: {count}")
    return "\n".join(lines)

def reset_inventory_global():
    save_inventory({})
    return t("msg_inventory_reset")

def reset_inventory_lora():
    inventory = load_inventory()
    new_inventory = {k: v for k, v in inventory.items() if not k.startswith("lora_") and not k.startswith("slot_")}
    save_inventory(new_inventory)
    return t("msg_inventory_reset")

def append_to_memo(memo_path, entry):
    if not memo_path or not entry: return t("msg_memo_err")
    try:
        memo_path = _clean_path(memo_path)
        dir_path = os.path.dirname(memo_path)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)
        with open(memo_path, "a", encoding="utf-8") as f: f.write("\n\n" + entry.strip() + "\n")
        return t("msg_memo_appended")
    except Exception as e: return f"Error: {e}"

def pick_random_assets(en_char, en_sit, en_w1, en_w2, en_w3, inventory_mode=False):
    from .lora_mgr import load_lora_list
    config = load_config()
    _dbg = config.get("debug", False)
    res = {"char": None, "sit": None, "w1": None, "w2": None, "w3": None}
    def _p(l, k):
        items = [i.strip() for i in load_lora_list(l).splitlines() if i.strip() and not i.strip().startswith('#')]
        if not items: return None
        choice = get_inventory_weighted_choice(items, k) if inventory_mode else random.choice(items)
        if _dbg: print(f"[SC_DEBUG] pick_random: slot={k}, items={len(items)}, choice={choice}, inv={inventory_mode}")
        return choice
    if en_char: res["char"] = _p(t("lora_type_char"), "slot_char")
    if en_sit: res["sit"] = _p(t("lora_type_sit"), "slot_sit")
    if en_w1: res["w1"] = _p(t("wildcard_1"), "slot_w1")
    if en_w2: res["w2"] = _p(t("wildcard_2"), "slot_w2")
    if en_w3: res["w3"] = _p(t("wildcard_3"), "slot_w3")
    return res

`

## sc_composer/i18n.py

`python
# -*- coding: utf-8 -*-
import os
import json
from .constants import CONFIG_PATH

_I18N = {
    "tab_header": {"en": "Smart Img2Img Composer Settings", "ja": "スマート・img2imgコンポーザー 設定"},
    "tab_settings": {"en": "⚙️ Settings & Preview", "ja": "⚙️ 設定 & プレビュー"},
    "h_settings": {"en": "⚙️ Global Settings", "ja": "⚙️ 全般設定"},
    "h_preview": {"en": "👀 Generation Preview", "ja": "👀 生成プレビュー"},
    "language_label": {"en": "UI Language", "ja": "表示言語"},
    "image_folder": {"en": "Reference Image Folder", "ja": "参照画像フォルダ"},
    "memo_file": {"en": "Memo File (.txt)", "ja": "メモファイル (.txt)"},
    "match_threshold": {"en": "Match Threshold", "ja": "ファイル名一致しきい値"},
    "generation_count": {"en": "Batch Count", "ja": "生成枚数"},
    "lora_offset": {"en": "LoRA Offset", "ja": "LoRA 強度オフセット"},
    "btn_save": {"en": "💾 Save All Settings", "ja": "💾 全ての設定を保存"},
    "btn_preview": {"en": "🔎 Test Composition", "ja": "🔎 構成テスト"},
    "positive_prompt": {"en": "Positive Prompt", "ja": "生成ポジティブ"},
    "negative_prompt": {"en": "Negative Prompt", "ja": "生成ネガティブ"},
    "log": {"en": "Log", "ja": "ログ"},
    "tab_prompt_gen": {"en": "🏷️Auto-Prompt Gen", "ja": "🏷️タグ解析＋メモ生成"},
    "tab_lora_manager": {"en": "📦Asset Lists", "ja": "📦アセットリスト管理"},
    "tab_inventory": {"en": "⚖️ Inventory Control", "ja": "⚖️ 在庫管理"},
    "tab_usage": {"en": "📖 Manual", "ja": "📖 使い方"},
    "selected_image": {"en": "Selected Image", "ja": "選択された画像"},
    
    # Preset
    "preset_label": {"en": "Load Preset", "ja": "プリセット一覧"},
    "preset_ph": {"en": "New Preset Name", "ja": "新しいプリセット名"},
    
    # Logic Settings
    "auto_optimize_prompt": {"en": "✨ Auto-Optimize Prompt", "ja": "✨ プロンプト自動最適化"},
    "prompt_polish": {"en": "🪄 Prompt Polish", "ja": "🪄 プロンプト洗練"},
    "active_profile": {"en": "🎨 Profile", "ja": "🎨 最適化プロファイル"},
    "custom_base_tags": {"en": "Base Tags", "ja": "基本タグ"},
    "smart_negative": {"en": "🚫 Smart Negative", "ja": "🚫 ネガティブ補強"},
    "sn_mode_add": {"en": "Append", "ja": "追加"},
    "sn_mode_overwrite": {"en": "Overwrite", "ja": "上書き"},
    "smart_negative_mode": {"en": "Mode", "ja": "ネガティブ挿入モード"},
    "auto_lora_enabled":        {"en": "Auto LoRA Apply",          "ja": "LoRA 自動適用"},
    "preview_output":            {"en": "Preview Output",            "ja": "プレビュー出力"},
    "fallback_enabled": {"en": "Fallback Section", "ja": "一致しない場合は [default] セクションを使用"},
    "output_settings": {"en": "Output Management", "ja": "出力設定"},
    "sort_mode": {"en": "Sort Subfolders", "ja": "サブフォルダ分け"},
    "sort_none": {"en": "None", "ja": "なし"},
    "sort_preset": {"en": "By Preset", "ja": "プリセット別"},
    "sort_section": {"en": "By Section", "ja": "セクション別"},
    "sort_date": {"en": "By Date", "ja": "日付別"},
    "auto_filename": {"en": "🏷️ Auto-Filename", "ja": "🏷️ 自動命名"},
    
    # Tab 2: Gen
    "prompt_gen_desc": {"en": "Analyze images and create memo entries.", "ja": "画像を解析してメモ用のエントリを自動生成します。"},
    "target_image": {"en": "Target Image", "ja": "📸 解析する画像"},
    "section_name": {"en": "Section Name", "ja": "📌 セクション名 (Memo Key)"},
    "section_ph": {"en": "e.g. Character A", "ja": "例: タイトル1"},
    "section_info": {"en": "Matches image filename in img2img.", "ja": "img2img 生成時のファイル名一致に使用します。"},
    "h_extracted_tags": {"en": "Extracted Tags (Current)", "ja": "抽出タグ"},
    "gen_tags_only": {"en": "Tags Only Mode", "ja": "タグのみ出力"},
    "gen_tags_only_info": {"en": "Do not compose with template.", "ja": "メモテンプレートを使わず、タグのみを出力します。"},
    "btn_gen_tags": {"en": "🏷️ Generate Tags", "ja": "🏷️ タグ解析＆生成"},
    "h_categories": {"en": "Categories (Extract checked types)", "ja": "🏷️ 抽出するタグの種類（チェックした種類のタグだけを抽出します）"},
    "btn_toggle_cat_all": {"en": "🔄 Select/Deselect All", "ja": "🔄 全選択/解除"},
    "cat_base": {"en": "Base Categories", "ja": "基本カテゴリ (構図・背景など)"},
    "cat_char": {"en": "Character Categories", "ja": "人物・詳細カテゴリ (髪型・服装・性別など)"},
    "cat_nsfw": {"en": "NSFW Categories", "ja": "特殊・NSFWカテゴリ (行為・局部・アイテム等)"},
    
    # Detailed Categories
    "cat_composition": {"en": "Composition", "ja": "構図・画角"},
    "cat_pose": {"en": "Pose / Action", "ja": "ポーズ・動作"},
    "cat_background": {"en": "Background", "ja": "背景・場所"},
    "cat_nature": {"en": "Nature / Environment", "ja": "自然・環境"},
    "cat_lighting": {"en": "Lighting", "ja": "照明・ライティング"},
    "cat_atmosphere": {"en": "Atmosphere / Mood", "ja": "雰囲気・ムード"},
    "cat_meta": {"en": "Meta / Quality", "ja": "品質・メタタグ"},
    "cat_char_base": {"en": "Body Type", "ja": "体型・ボディ"},
    "cat_char_hair": {"en": "Hair Style", "ja": "髪型・ヘア"},
    "cat_char_eyes": {"en": "Eyes", "ja": "瞳・目元"},
    "cat_char_face": {"en": "Face / Expression", "ja": "顔・表情"},
    "cat_char_clothes": {"en": "Outfits", "ja": "服装・衣装"},
    "cat_char_male": {"en": "Male Specific", "ja": "男性要素"},

    "cat_nsfw_action": {"en": "Sex Actions", "ja": "性行為内容"},
    "cat_nsfw_creature": {"en": "Creatures", "ja": "人外・触手等"},
    "cat_nsfw_item": {"en": "Toys / Items", "ja": "道具・アイテム"},
    "cat_nsfw_focus": {"en": "Body Part Focus", "ja": "部位フォーカス"},
    "cat_nsfw_fluids": {"en": "Body Fluids", "ja": "体液・汁"},
    "cat_nsfw_fetish": {"en": "Fetish / Kink", "ja": "フェティッシュ"},
    "cat_nsfw_clothes_mess": {"en": "Undressing", "ja": "着衣乱れ・露出"},
    "cat_nsfw_genitals": {"en": "Genitals", "ja": "局部・性器"},
    "cat_nsfw_scenario": {"en": "Scenarios", "ja": "シチュエーション・特殊"},
    "btn_toggle_cat": {"en": "Select All / Deselect All", "ja": "全選択 / 解除"},
    
    "h_tag_analysis_settings": {"en": "⚙️ Tag Analysis Settings", "ja": "⚙️ タグ解析・設定"},
    "conf_base": {"en": "Base Group (BG, etc.)", "ja": "基本グループ (背景等)"},
    "conf_char": {"en": "Character Group (Face, Clothes)", "ja": "人物グループ (顔・服)"},
    "conf_nsfw": {"en": "NSFW Group (Genitals, Actions)", "ja": "NSFWグループ (局部・行為)"},
    "conf_total": {"en": "Tag Confidence (Total)", "ja": "タグ信頼性 (共通)"},
    
    "gen_custom_dict_enabled_label": {"en": "Enable Custom Dictionary", "ja": "カスタム読替え辞書を有効にする"},
    "h_mosaic_settings": {"en": "🧱 Mosaic Auto-Prompt Settings", "ja": "🧱 モザイクプロンプト自動付与設定"},
    "gen_mosaic_auto": {"en": "Auto Detect", "ja": "自動検知"},
    "gen_mosaic_level": {"en": "Level", "ja": "モザイクの濃さ"},
    "mosaic_layer_1": {"en": "Mosaic Layer 1", "ja": "モザイク一層目"},
    "mosaic_low": {"en": "Thin", "ja": "薄い"},
    "mosaic_med": {"en": "Med", "ja": "普通"},
    "mosaic_high": {"en": "Thick", "ja": "厚い"},
    "cat_nsfw_mosaic": {"en": "Categories", "ja": "検知タイプ"},
    "h_pickup_limits": {"en": "Pickup Limits", "ja": "📏 抽出本数上限"},
    "limit_base_label": {"en": "Base", "ja": "基本グループ（背景等）"},
    "limit_char_label": {"en": "Char", "ja": "人物グループ（顔・服）"},
    "limit_nsfw_label": {"en": "NSFW", "ja": "NSFWグループ（局部・行為）"},
    "default_positive": {"en": "Positive Template", "ja": "✨ デフォルトポジティブ"},
    "default_negative": {"en": "Negative Template", "ja": "🚫 デフォルトネガティブ"},
    "custom_dict": {"en": "Custom Dictionary", "ja": "カスタム読替え辞書"},
    "generated_entry": {"en": "📋 Generated Entry (editable)", "ja": "📋 生成されたエントリ（編集可能）"},
    "generated_entry_info": {"en": "Paste this to memo file.", "ja": "これをメモファイルに貼り付けてください。"},
    "btn_append_memo": {"en": "📝 Append to Memo", "ja": "📝 メモファイルに追記"},
    "btn_send_img2img": {"en": "🚀 img2img Transfer", "ja": "🚀 img2imgへ送信"},
    "analysis_log": {"en": "Analysis Log", "ja": "解析ログ"},
    "btn_save_settings": {"en": "💾 Save Settings", "ja": "💾 設定を保存"},
    "append_status": {"en": "Append Status", "ja": "追記ステータス"},
    
    # Tab 3: LoRA
    "lora_manager_desc": {"en": "Manage asset lists.", "ja": "ランダムアセットのリストを管理します。"},
    "lora_type": {"en": "Target Slot", "ja": "対象スロット"},
    "lora_type_char": {"en": "Char LoRA", "ja": "キャラ LoRA"},
    "lora_type_sit": {"en": "Sit LoRA", "ja": "シチュ LoRA"},
    "wildcard_1": {"en": "W1", "ja": "ワイルド1"},
    "wildcard_2": {"en": "W2", "ja": "ワイルド2"},
    "wildcard_3": {"en": "W3", "ja": "ワイルド3"},
    "lora_list_label": {"en": "List Content", "ja": "リスト内容"},
    "lora_mgr_placeholder": {"en": "Enter items...", "ja": "1行ごとに入力してください。"},
    "btn_save_lora_list": {"en": "Save List", "ja": "リストを保存"},
    "lora_input_label": {"en": "Quick Add", "ja": "クイック追加"},
    "btn_append_lora": {"en": "Add", "ja": "追加"},
    
    # Tab 4: Inventory
    "inventory_desc": {"en": "Manage usage statistics.", "ja": "アセットの使用回数を管理します。"},
    "inventory_mode": {"en": "Enable Inventory Logic", "ja": "在庫管理ロジックを有効にする"},
    "inventory_mode_info": {"en": "Prioritizes lower usage items.", "ja": "使用回数が少ない項目を優先します。"},
    "btn_check_stock": {"en": "View Stats", "ja": "使用統計を表示"},
    "btn_lora_reset": {"en": "Reset Usage", "ja": "使用履歴リセット"},
    "btn_global_reset": {"en": "Reset All", "ja": "全データリセット"},
    "inventory_status_label": {"en": "Status", "ja": "ステータス"},
    
    # Manual
    "usage_md": {
        "en": """
### 🎲 How to Use Smart Img2Img Composer v1.1.2

This extension is a powerful tool to synchronize your image metadata with your prompt generation workflow.

#### 1. ⚙️ Settings & Preview
- **Reference Image Folder**: The directory where your source images are stored.
- **Memo File**: A .txt file containing prompt entries for each image name.
- **Health Check (✅/❌)**: Real-time validation of your paths.
- **Preset Management**: Save and load different configurations easily.

#### 2. 🏷️ Tag Analysis (Tagger)
- **Auto-Prompt Gen**: Uses deep learning to analyze your uploaded image and generate tags.
- **Category Sliders**: Fine-tune confidence thresholds for different types of tags.
- **Mosaic Auto-Prompt**: Automatically adds NSFW/Mosaic-safe tags based on visual analysis.

#### 3. 📦 Asset Lists (LoRA/Wildcards)
- Manage your LoRA and Wildcard lists globally. These are used when 'Inventory Logic' is enabled.

#### 4. ⚖️ Inventory Logic
- Prevents repetition by tracking which assets have been used and prioritizing unused ones.

---
*Created by Antigravity Team*
        """,
        "ja": """
### 🎲 Smart Img2Img Composer v1.1.2 マニュアル

本拡張機能は、参照画像のファイル名とメモファイルを紐付け、複雑な img2img 構成を自動化するプロフェッショナルツールです。

#### 1. ⚙️ 設定 & プレビュー (基本操作)
- **参照画像フォルダ**: img2img で読み込む画像の保存先を指定します。
- **メモファイル**: ファイル名に基づいたプロンプト（LoRAやタグ）を記述した .txt ファイルです。
- **ヘルスチェック (✅/❌)**: パスが正しいかリアルタイムで判定します。
- **プリセット**: 「SDXL用」「Pony用」など、設定をまるごと保存・読込できます。

#### 2. 🏷️ タグ解析＋メモ生成 (Tagger)
- **タグ抽出**: アップロードした画像をAIが解析し、全自動でプロンプトを生成します。
- **カテゴリ別信頼性**: 背景、衣装、行為などのグループごとに抽出の厳しさを調整可能。
- **モザイク自動付与**: 画像からモザイク属性を検知し、適切なタグを自動挿入します。

#### 3. 📦 アセットリスト管理
- ランダムに使用する LoRA やワイルドカードのリストを一括管理できます。

#### 4. ⚖️ 在庫管理 (Inventory Logic)
- **使用回数カウント**: 同じ LoRA ばかりが出ないよう、使用回数が少ない順に優先して抽選します。

---
*Developed by Antigravity*
        """
    },
    
    # msgs
    "msg_all_saved": {"en": "Saved", "ja": "保存しました"},
    "msg_inventory_reset": {"en": "Reset done", "ja": "リセット完了"},
    "msg_memo_appended": {"en": "Appended", "ja": "追記完了"},
    "msg_memo_err": {"en": "Error", "ja": "エラー"},
    "msg_lora_saved": {"en": "List saved", "ja": "リストを保存しました"},
    "no_images": {"en": "No images", "ja": "画像なし"},
    "log_no_sections": {"en": "No sections", "ja": "セクションなし"},
    "log_no_match": {"en": "No match", "ja": "一致なし"},
    "msg_tagger_not_found": {"en": "Tagger missing", "ja": "タガーが見つかりません"},
    "msg_tag_fetch_err": {"en": "Tag error", "ja": "タグ解析エラー"},
    "msg_no_upload_err": {"en": "Upload first", "ja": "画像をアップロードしてください"},
    "msg_no_section_err": {"en": "Name section", "ja": "セクション名を入力してください"},
    "log_all_tags": {"en": "{count} tags found", "ja": "{count} 個のタグを検出"},
    "log_filtered_tags": {"en": "{count} tags picked", "ja": "{count} 個のタグを抽出"},
    "log_custom_match": {"en": "Rule hit: {cond} -> {prompt}", "ja": "カスタムルール一致: {cond} -> {prompt}"},

    # --- 欠損していたキー群の追加 ---
    "pos_label": {"en": "Injection Position", "ja": "挿入位置"},
    "resize_slider": {"en": "Slider Value", "ja": "スライダー値"},

    "accordion_desc": {"en": "Description", "ja": "説明"},
    "enable": {"en": "Enable", "ja": "有効化"},
    "accordion_assets": {"en": "Assets", "ja": "アセット"},
    "pos_front": {"en": "Front", "ja": "前"},
    "pos_back": {"en": "Back", "ja": "後"},
    "pos_smart": {"en": "Smart", "ja": "スマート"},
    "enable_random_char": {"en": "Random Char", "ja": "ランダムキャラ"},
    "enable_random_sit": {"en": "Random Situation", "ja": "ランダムシチュ"},
    "selection_mode": {"en": "Selection Mode", "ja": "選択モード"},
    "sel_random": {"en": "Random", "ja": "ランダム"},
    "sel_sequential": {"en": "Sequential", "ja": "順番"},
    "overwrite_prompt": {"en": "Overwrite Prompt", "ja": "プロンプト上書き"},
    "resize_mode": {"en": "Resize Mode", "ja": "リサイズモード"},
    "resize_none": {"en": "None", "ja": "なし"},
    "resize_slider_base": {"en": "Slider (Base Res)", "ja": "スライダー指定"}, # キー重複を避けるため変更
    "resize_512": {"en": "512-1024", "ja": "512-1024"},
    "resize_1024": {"en": "1024-1536", "ja": "1024-1536"},
    "resize_1536": {"en": "1536-1792", "ja": "1536-1792"},
    "base_resolution": {"en": "Base Res", "ja": "基本解像度"},
    "msg_settings_saved": {"en": "Settings Saved", "ja": "設定を保存しました"},
    "msg_settings_err": {"en": "Save Error", "ja": "保存エラー"},
    "msg_no_tags_err": {"en": "No Tags", "ja": "タグがありません"},
    "use_global_conf": {"en": "Prioritize Global Confidence", "ja": "タグ信頼性(共通)を優先する"},
    "use_global_conf_info": {"en": "* If unchecked, individual category values will be prioritized.", "ja": "※チェックを外すと、各カテゴリ（基本・キャラ・NSFW）の個別数値が優先されます。"},
    "health_check_ok": {"en": "✅ Ready", "ja": "✅ 正常"},
    "health_check_err": {"en": "❌ Not Found", "ja": "❌ 異常"},
}

_lang_cache = None

def _get_lang() -> str:
    global _lang_cache
    if _lang_cache is not None: return _lang_cache
    try:
        if os.path.exists(CONFIG_PATH):
            with open(CONFIG_PATH, "r", encoding="utf-8") as f:
                _lang_cache = json.load(f).get("language", "ja")
                return _lang_cache
    except Exception: pass
    return "ja"

def invalidate_lang_cache():
    global _lang_cache
    _lang_cache = None

def t(key: str) -> str:
    lang = _get_lang()
    entry = _I18N.get(key, {})
    return entry.get(lang, entry.get("en", key))

`

## sc_composer/lora_mgr.py

`python
# -*- coding: utf-8 -*-
import os
from .i18n import t
from .core import load_config
from .constants import LORA_CHAR_PATH, LORA_SIT_PATH, WILD_1_PATH, WILD_2_PATH, WILD_3_PATH

def get_mgr_path(mgr_label):
    config = load_config()
    label_to_key = {
        t("lora_type_char"): "char",
        t("lora_type_sit"): "sit",
        t("wildcard_1"): "w1",
        t("wildcard_2"): "w2",
        t("wildcard_3"): "w3",
    }
    mgr_key = label_to_key.get(mgr_label, "char")
    mapping = {
        "char": LORA_CHAR_PATH,
        "sit": LORA_SIT_PATH,
        "w1": config.get("wildcard_1_path") or WILD_1_PATH,
        "w2": config.get("wildcard_2_path") or WILD_2_PATH,
        "w3": config.get("wildcard_3_path") or WILD_3_PATH,
    }
    return mapping.get(mgr_key)

def _ensure_dir(path):
    if not path: return
    d = os.path.dirname(path)
    if d: os.makedirs(d, exist_ok=True)

def load_lora_list(mgr_label):
    if mgr_label is None: return ""
    path = get_mgr_path(mgr_label)
    if path and os.path.exists(path):
        for enc in ("utf-8", "utf-8-sig", "cp932"):
            try:
                with open(path, "r", encoding=enc, errors=("ignore" if enc == "cp932" else "strict")) as f:
                    return f.read()
            except Exception: continue
    return ""

def save_lora_list(mgr_label, content):
    path = get_mgr_path(mgr_label)
    if path:
        _ensure_dir(path)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return t("msg_lora_saved"), content
    return "Error", content

def append_lora_list(mgr_label, input_text):
    if not input_text or not input_text.strip():
        return load_lora_list(mgr_label), ""
    
    path = get_mgr_path(mgr_label)
    if not path: return "Error: Path not found", ""

    current = load_lora_list(mgr_label)
    new_line = input_text.strip()
    if current and not current.endswith("\n"):
        current += "\n"
    current += new_line + "\n"

    _ensure_dir(path)
    with open(path, "w", encoding="utf-8") as f:
        f.write(current)
    return current, ""

`

## sc_composer/tagger.py

`python
# -*- coding: utf-8 -*-
import os
import re
import sys
import traceback
from .i18n import t
from .constants import _TAG_CATEGORIES, _CAT_BASE_KEYS, _CAT_CHAR_KEYS, _CAT_NSFW_KEYS, BASE_DIR

_compiled_cat_patterns = {}

def _get_easy_prompt_tags():
    # yamlの動的インポート (競合回避のため個別関数内)
    try:
        import yaml
    except ImportError:
        return set()

    tags = set()
    extensions_root = os.path.dirname(BASE_DIR)
    _CANDIDATES = [
        ("sdweb-easy-prompt-selector", "tags"),
        ("easy-prompt-selector",       "tags"),
        ("a1111-sd-webui-tagcomplete", "tags"),
        ("sd-webui-tagcomplete",       "tags"),
    ]

    installed = os.listdir(extensions_root) if os.path.isdir(extensions_root) else []
    found_dirs = []
    for ext_name, sub in _CANDIDATES:
        candidate = os.path.join(extensions_root, ext_name, sub)
        if os.path.isdir(candidate):
            found_dirs.append(candidate)
        for name in installed:
            if name.startswith(ext_name):
                c2 = os.path.join(extensions_root, name, sub)
                if os.path.isdir(c2) and c2 not in found_dirs:
                    found_dirs.append(c2)

    def _extract(d):
        for v in d.values():
            if isinstance(v, list):
                for item in v:
                    if isinstance(item, str) and not item.startswith(("<lora:", "__")):
                        tags.add(item.strip().lower().replace(" ", "_"))
            elif isinstance(v, dict):
                _extract(v)

    for d in found_dirs:
        try:
            for root, _, files in os.walk(d):
                for f in files:
                    if f.endswith((".yml", ".yaml")):
                        with open(os.path.join(root, f), "r", encoding="utf-8") as file:
                            data = yaml.safe_load(file)
                        if isinstance(data, dict):
                            _extract(data)
        except Exception:
            continue
    return tags

def _filter_tags(tags: dict, confidence_dict: dict, selected_cats=None, protect_easy=True, limits=None):
    global _compiled_cat_patterns
    if not selected_cats:
        selected_cats = list(_TAG_CATEGORIES.keys())

    filtered = {}
    easy_tags = _get_easy_prompt_tags() if protect_easy else set()
    
    cache_key = tuple(sorted(selected_cats))
    if cache_key in _compiled_cat_patterns:
        allowed_tags, allowed_patterns = _compiled_cat_patterns[cache_key]
    else:
        allowed_tags = set()
        allowed_patterns = []
        for cat in selected_cats:
            if cat in _TAG_CATEGORIES:
                for item in _TAG_CATEGORIES[cat]:
                    if item.startswith("re:"):
                        try:
                            allowed_patterns.append((cat, re.compile(item[3:])))
                        except Exception: pass
                    else:
                        allowed_tags.add((item, cat))
        _compiled_cat_patterns[cache_key] = (allowed_tags, allowed_patterns)

    if limits is None:
        limits = {"base": 10, "char": 10, "nsfw": 15}

    cat_matches = {cat: [] for cat in selected_cats}
    easy_protected = {}

    # グローバルしきい値の優先判定
    use_global = confidence_dict.get("_use_global", True)
    global_conf = confidence_dict.get("_global", 0.35)

    for tag, score in tags.items():
        tag_clean = tag.strip().lower().replace(" ", "_")
        
        # Easy Prompt Selector 保護
        if protect_easy and tag_clean in easy_tags:
            if score >= global_conf:
                easy_protected[tag_clean] = score
            continue

        matched_cat = None
        # 高速マッチング: 直接指定
        for item, cat in allowed_tags:
            if item == tag_clean:
                matched_cat = cat; break
        
        # 正規表現マッチング
        if not matched_cat:
            for cat, p in allowed_patterns:
                if p.search(tag_clean):
                    matched_cat = cat; break

        if matched_cat:
            # しきい値判定 (個別 or グローバル)
            conf = global_conf if use_global else confidence_dict.get(matched_cat, global_conf)
            if score >= conf:
                cat_matches[matched_cat].append((tag_clean, score))

    for cat in selected_cats:
        matches = cat_matches.get(cat, [])
        limit = 999
        if cat in _CAT_BASE_KEYS: limit = int(limits.get("base", 10))
        elif cat in _CAT_CHAR_KEYS: limit = int(limits.get("char", 10))
        elif cat in _CAT_NSFW_KEYS: limit = int(limits.get("nsfw", 15))
        
        sorted_m = sorted(matches, key=lambda x: x[1], reverse=True)
        for t_c, s in sorted_m[:limit]:
            if t_c not in filtered:
                filtered[t_c] = s

    filtered.update(easy_protected)
    return filtered

def _find_tagger():
    # 旧版の安定した検索ロジックを復元
    try:
        from tagger import interrogator as tagger_mod
        return tagger_mod, None
    except ImportError:
        pass
    try:
        ext_dir = os.path.dirname(BASE_DIR)
        if os.path.isdir(ext_dir):
            for d in os.listdir(ext_dir):
                if "tagger" in d.lower() or "wd14" in d.lower():
                    tp = os.path.join(ext_dir, d)
                    if tp not in sys.path: sys.path.insert(0, tp)
            from tagger import interrogator as tagger_mod
            return tagger_mod, None
    except Exception:
        pass
    return None, t("msg_tagger_not_found")

def _interrogate_image(image, confidence_dict: dict, selected_cats=None, limits=None):
    tagger_mod, err = _find_tagger()
    if tagger_mod is None: return {}, {}, err
    try:
        all_tags = {}
        success = False
        internal_error = ""

        # 旧版のシンプルかつ安定した呼び出し方式
        try:
            from tagger import utils as tu
            if hasattr(tu, "interrogators") and tu.interrogators:
                # ドットありを優先試行 (旧版の挙動)
                if not tu.interrogators: return None # guard against empty interrogators
                # Handle empty dict next(iter(...)) StopIteration
                obj = (tu.interrogators.get("wd14-convnext.v2") or
                       tu.interrogators.get("wd14-convnextv2") or
                       (next(iter(tu.interrogators.values())) if tu.interrogators else None))
                if obj is None:
                    raise RuntimeError("No interrogators loaded")
                
                # 画像をRGB PILに固定 (DLLエラーとは無関係だが安定のため)
                if hasattr(image, "convert"): image = image.convert("RGB")
                
                res = obj.interrogate(image)
                if isinstance(res, tuple) and len(res) >= 2:
                    all_tags = res[1] if isinstance(res[1], dict) else {}
                    success = True
                elif isinstance(res, dict):
                    all_tags = res; success = True
        except Exception as e:
            internal_error = f"Utils error: {e}"

        if not success:
            try:
                import tagger.api as ta
                res = ta.interrogate(image)
                if isinstance(res, dict):
                    all_tags = res.get("caption") or res
                    success = True
            except Exception as e:
                internal_error += f" | API error: {e}"

        if not success: 
            return {}, {}, f"{t('msg_tagger_not_found')}\n({internal_error})"

        return _filter_tags(all_tags, confidence_dict, selected_cats, limits=limits), all_tags, None
    except Exception as e:
        return {}, {}, f"{t('msg_tag_fetch_err')} {e}"

def autogen_prompt(image, section_name, confidence, pos, neg, cat_base, cat_char, cat_nsfw, custom_dict, gen_mosaic=False, mosaic_level="Mosaic Med", custom_enabled=True, limit_base=10, limit_char=10, limit_nsfw=15, cat_mosaic=None, conf_base=0.35, conf_char=0.35, conf_nsfw=0.35, use_global_conf=True):
    # confidence_dict を個別引数から構築
    conf_dict = {
        "_global": confidence,
        "_use_global": use_global_conf,
        **{k: conf_base for k in _CAT_BASE_KEYS},
        **{k: conf_char for k in _CAT_CHAR_KEYS},
        **{k: conf_nsfw for k in _CAT_NSFW_KEYS}
    }

    cats = list(cat_base) + list(cat_char) + list(cat_nsfw)
    if cat_mosaic: cats += list(cat_mosaic)
    
    if image is None: return "", t("msg_no_upload_err"), ""
    if not section_name or not section_name.strip(): return "", t("msg_no_section_err"), ""

    try:
        # gr.Number returns float, cast to int for slice indexing
        limits = {"base": int(limit_base), "char": int(limit_char), "nsfw": int(limit_nsfw)}
        filtered, all_tags, err = _interrogate_image(image, conf_dict, cats, limits=limits)
        if err: return "", err, ""

        log = [t("log_all_tags").format(count=len(all_tags)), t("log_filtered_tags").format(count=len(filtered))]
        
        mosaic_extra = []
        if gen_mosaic:
            l_val = str(mosaic_level)
            # 全タグからモザイク検知
            if any(tag in all_tags for tag in ["mosaic_censoring", "censored", "bar_censor"]):
                if "Low" in l_val or "薄" in l_val:
                    mosaic_extra = ["(mosaic_censoring:0.8)", "(light_mosaic:1.1)"]
                elif "High" in l_val or "厚" in l_val:
                    mosaic_extra = ["(mosaic_censoring:1.4)", "(thick_mosaic:1.2)"]
                else:
                    mosaic_extra = ["(mosaic_censoring:1.1)", "(detailed_mosaic:1.0)"]
                log.append(f"🧱 Mosaic Auto-Prompt added ({mosaic_level})")

        matched_custom = []
        if custom_enabled and custom_dict:
            for line in custom_dict.splitlines():
                if not line or line.startswith("#"): continue
                sep = "=>" if "=>" in line else "->" if "->" in line else ">" if ">" in line else None
                if not sep: continue
                l, r = line.split(sep, 1)
                conds = [ct.strip().lower().replace(" ", "_") for ct in l.split(",")]
                if all(c in all_tags for c in conds):
                    matched_custom.append(r.strip())
                    log.append(t("log_custom_match").format(cond=l, prompt=r.strip()))

        gen_tags = ", ".join(tag.replace("_", " ") for tag in filtered.keys())
        parts = [pos.strip()] if pos else []
        parts.extend(mosaic_extra)
        parts.extend(matched_custom)
        if gen_tags: parts.append(gen_tags)
        
        final_pos = ", ".join(parts)
        entry = f"[{section_name.strip()}]\npositive:\n{final_pos}\n\nnegative:\n{neg}\n"
        return entry, "\n".join(log), ", ".join(filtered.keys())
    except Exception as e:
        return "", f"❌ Error: {e}\n{traceback.format_exc()}", ""

`

## sc_composer/ui_common.py

`python
# -*- coding: utf-8 -*-
import os

def update_ref_tags(profile_name: str):
    from .constants import PROMPT_PROFILES
    profile = PROMPT_PROFILES.get(profile_name, PROMPT_PROFILES["Standard / SDXL"])
    return profile["ref"], profile["neg"]

def _ensure_lora_files():
    from .constants import LORA_CHAR_PATH, LORA_SIT_PATH, LORA_CHAR_TEMPLATE, LORA_SIT_TEMPLATE
    for p, tmp in [(LORA_CHAR_PATH, LORA_CHAR_TEMPLATE), (LORA_SIT_PATH, LORA_SIT_TEMPLATE)]:
        if not os.path.exists(p):
            with open(p, "w", encoding="utf-8") as f:
                f.write(tmp)

`

## sc_composer/ui_img2img.py

`python
# -*- coding: utf-8 -*-
import gradio as gr
from .i18n import t
from .core import load_config
from .constants import PROMPT_PROFILES

def on_ui_img2img():
    config = load_config()

    with gr.Accordion("\U0001F3B2 Smart Img2Img Composer", open=False, elem_id="smart_composer_accordion"):
        gr.Markdown(t("accordion_desc"))
        
        enabled = gr.Checkbox(
            label=t("enable"),
            value=False,
            elem_id="smart_composer_enabled",
        )

        # Assets
        with gr.Accordion(t("accordion_assets"), open=False):
            with gr.Row():
                gr.Markdown(f"<div style='text-align: right; padding-right: 15px;'><b>{t('pos_label')}</b></div>")
            
            _pos_choices = [t("pos_front"), t("pos_back"), t("pos_smart")]

            with gr.Row():
                en_char = gr.Checkbox(label=t("enable_random_char"), value=False, scale=8)
                pos_char = gr.Radio(choices=_pos_choices, value=t("pos_back"), show_label=False, scale=2, min_width=180)
            
            with gr.Row():
                en_sit = gr.Checkbox(label=t("enable_random_sit"), value=False, scale=8)
                pos_sit = gr.Radio(choices=_pos_choices, value=t("pos_back"), show_label=False, scale=2, min_width=180)
            
            with gr.Row():
                en_w1 = gr.Checkbox(label=t("wildcard_1"), value=False, scale=8)
                pos_w1 = gr.Radio(choices=_pos_choices, value=t("pos_back"), show_label=False, scale=2, min_width=180)
            
            with gr.Row():
                en_w2 = gr.Checkbox(label=t("wildcard_2"), value=False, scale=8)
                pos_w2 = gr.Radio(choices=_pos_choices, value=t("pos_back"), show_label=False, scale=2, min_width=180)
            
            with gr.Row():
                en_w3 = gr.Checkbox(label=t("wildcard_3"), value=False, scale=8)
                pos_w3 = gr.Radio(choices=_pos_choices, value=t("pos_back"), show_label=False, scale=2, min_width=180)

        with gr.Row():
            selection_mode = gr.Radio(
                label=t("selection_mode"),
                choices=[(t("sel_random"), "random"), (t("sel_sequential"), "sequential")],
                value="random",
            )
            override_prompt = gr.Checkbox(
                label=t("overwrite_prompt"),
                value=True,
            )

        active_profile = gr.Dropdown(
            label=t("active_profile"),
            choices=list(PROMPT_PROFILES.keys()),
            value=lambda: load_config().get("active_profile", "Standard / SDXL"),
            visible=False
        )
        custom_base_tags = gr.Textbox(
            label=t("custom_base_tags"),
            value=lambda: load_config().get("custom_base_tags", "masterpiece, best quality, 1girl, solo"),
            visible=False
        )

        with gr.Row():
            auto_optimize = gr.Checkbox(
                label=t("auto_optimize_prompt"),
                value=lambda: load_config().get("auto_optimize_prompt", False),
            )
            prompt_polish = gr.Checkbox(
                label=t("prompt_polish"),
                value=lambda: load_config().get("prompt_polish", False),
            )

        with gr.Row():
            _resize_choices = [t("resize_none"), t("resize_slider_base"), t("resize_512"), t("resize_1024"), t("resize_1536")]
            resize_mode = gr.Dropdown(
                label=t("resize_mode"),
                choices=_resize_choices,
                value=_resize_choices[0],
            )
            base_resolution = gr.Slider(
                label=t("base_resolution"),
                minimum=512, maximum=2048, step=64,
                value=1024,
            )

        with gr.Accordion(t("output_settings"), open=False):
            output_sort_mode = gr.Dropdown(
                label=t("sort_mode"),
                # Internal keys: "None", "By Preset", "By Section", "By Date"
                choices=[(t("sort_none"), "None"), (t("sort_preset"), "By Preset"), (t("sort_section"), "By Section"), (t("sort_date"), "By Date")],
                value="None"
            )
            auto_filename_chk = gr.Checkbox(
                label=t("auto_filename"),
                value=lambda: load_config().get("auto_filename", False),
            )

    return [
        enabled, override_prompt, resize_mode, base_resolution, selection_mode,
        en_char, pos_char, en_sit, pos_sit, en_w1, pos_w1, en_w2, pos_w2, en_w3, pos_w3,
        output_sort_mode, auto_optimize, custom_base_tags, active_profile, prompt_polish, auto_filename_chk
    ]

`

## sc_composer/ui_tabs.py

`python
# -*- coding: utf-8 -*-
import gradio as gr
import os
import traceback
from .i18n import t
from .core import load_config, save_all_settings, handle_load_preset, handle_save_preset, handle_delete_preset, compose_prompt, compose_prompt_preview, append_to_memo
from .utils import _clean_path, check_individual_health
from .constants import WILD_1_PATH, WILD_2_PATH, WILD_3_PATH, PROMPT_PROFILES

def on_ui_tabs():
    try:
        from .ui_tabs_gen import on_tab_prompt_gen
        from .ui_tabs_lora import on_tab_lora_manager

        config = load_config()

        # 旧版に倣い、Block内部で丁寧に構築
        with gr.Blocks(analytics_enabled=False) as tab_interface:
            gr.Markdown(f"# 🎲 Smart Img2Img Composer v1.1.2 Stable\n{t('tab_header')}")

            with gr.Tabs() as tabs_root:
                # --- Tab 1: Settings & Preview ---
                with gr.Tab(t("tab_settings")):
                    with gr.Row():
                        with gr.Column(scale=1):
                            gr.Markdown(t("h_settings"))
                            with gr.Group():
                                with gr.Row():
                                    preset_dropdown = gr.Dropdown(
                                        label=t("preset_label"),
                                        choices=["Default"] + list(load_config().get("presets", {}).keys()),
                                        value="Default",
                                    )
                                with gr.Row():
                                    preset_name_input = gr.Textbox(placeholder=t("preset_ph"), label=None, scale=10)
                                    save_preset_btn = gr.Button("💾", variant="secondary", scale=1, min_width=40)
                                    delete_preset_btn = gr.Button("🗑️", variant="stop", scale=1, min_width=40)

                            with gr.Group():
                                with gr.Row():
                                    image_folder = gr.Textbox(label=t("image_folder"), value=lambda: load_config().get("image_folder", ""), lines=1, scale=8)
                                    with gr.Column(scale=1, min_width=120):
                                        status_img = gr.HTML("")
                                with gr.Row():
                                    memo_file = gr.Textbox(label=t("memo_file"), value=lambda: load_config().get("memo_file", ""), lines=1, scale=8)
                                    with gr.Column(scale=1, min_width=120):
                                        status_memo = gr.HTML("")
                                
                                match_threshold = gr.Slider(label=t("match_threshold"), minimum=0.0, maximum=1.0, step=0.05, value=lambda: load_config().get("match_threshold", 0.3))
                                generation_count = gr.Slider(label=t("generation_count"), minimum=1, maximum=100, step=1, value=lambda: load_config().get("generation_count", 1))

                            with gr.Group():
                                lora_offset = gr.Slider(label=t("lora_offset"), minimum=-1.0, maximum=1.0, step=0.05, value=lambda: load_config().get("lora_offset", 0.0))
                                with gr.Row():
                                    wildcard_1_path = gr.Textbox(label=t("wildcard_1"), value=lambda: load_config().get("wildcard_1_path", WILD_1_PATH), lines=1, scale=8)
                                    with gr.Column(scale=1, min_width=120):
                                        status_w1 = gr.HTML("")
                                with gr.Row():
                                    wildcard_2_path = gr.Textbox(label=t("wildcard_2"), value=lambda: load_config().get("wildcard_2_path", WILD_2_PATH), lines=1, scale=8)
                                    with gr.Column(scale=1, min_width=120):
                                        status_w2 = gr.HTML("")
                                with gr.Row():
                                    wildcard_3_path = gr.Textbox(label=t("wildcard_3"), value=lambda: load_config().get("wildcard_3_path", WILD_3_PATH), lines=1, scale=8)
                                    with gr.Column(scale=1, min_width=120):
                                        status_w3 = gr.HTML("")

                            with gr.Group():
                                fallback_enabled = gr.Checkbox(label=t("fallback_enabled"), value=lambda: load_config().get("fallback_enabled", True))
                                auto_lora_enabled = gr.Checkbox(label=t("auto_lora_enabled"), value=lambda: load_config().get("auto_lora_enabled", True))
                                inventory_mode = gr.Checkbox(label=t("inventory_mode"), value=lambda: load_config().get("inventory_mode", False))
                            
                            with gr.Group():
                                auto_optimize_prompt = gr.Checkbox(label=t("auto_optimize_prompt"), value=lambda: load_config().get("auto_optimize_prompt", False))
                                active_profile = gr.Dropdown(label=t("active_profile"), choices=list(PROMPT_PROFILES.keys()), value=lambda: load_config().get("active_profile", "Standard / SDXL"))
                                custom_base_tags = gr.Textbox(label=t("custom_base_tags"), value=lambda: load_config().get("custom_base_tags", ""), lines=2)
                            
                            with gr.Group():
                                prompt_polish = gr.Checkbox(label=t("prompt_polish"), value=lambda: load_config().get("prompt_polish", False))
                                smart_negative = gr.Checkbox(label=t("smart_negative"), value=lambda: load_config().get("smart_negative", False))
                                smart_negative_mode = gr.Radio(label=t("smart_negative_mode"), choices=[(t("sn_mode_add"), "append"), (t("sn_mode_overwrite"), "overwrite")], value=lambda: load_config().get("smart_negative_mode", "append"))

                        with gr.Column(scale=1):
                            gr.Markdown(t("h_preview"))
                            preview_output = gr.Textbox(label=t("preview_output"), lines=8, interactive=False)
                            test_btn = gr.Button(t("btn_preview"), variant="primary")
                            
                            gr.Markdown(t("language_label"))
                            lang_dropdown = gr.Dropdown(choices=["ja", "en"], value=lambda: load_config().get("language", "ja"), show_label=False)
                            save_btn = gr.Button(t("btn_save"), variant="primary")
                            status = gr.Markdown("")

                            # P3: output_sort_mode / auto_filename を設定タブから保存できるよう hidden コンポーネントとして追加
                            output_sort_hidden = gr.Textbox(
                                value=lambda: load_config().get("output_sort_mode", "None"),
                                visible=False, label="output_sort_mode_hidden"
                            )
                            auto_filename_hidden = gr.Checkbox(
                                value=lambda: load_config().get("auto_filename", False),
                                visible=False, label="auto_filename_hidden"
                            )

                # --- Tab 2: Prompt Generator ---
                with gr.Tab(t("tab_prompt_gen")):
                    gen_comps = on_tab_prompt_gen()
                    # 展開 (ui_tabs_gen.py の戻り値に合わせる)
                    (
                        gen_image, gen_section, gen_confidence, gen_positive, gen_negative, gen_custom_dict,
                        gen_cat_base, gen_cat_char, gen_cat_nsfw, gen_mosaic_auto, gen_mosaic_level, gen_custom_dict_enabled,
                        limit_base, limit_char, limit_nsfw, gen_cat_mosaic,
                        gen_btn, gen_output, gen_log, gen_tags_only, gen_save_btn, append_btn, append_status, send_img2img_btn,
                        conf_base_val, conf_char_val, conf_nsfw_val, use_global_conf
                    ) = gen_comps

                # --- Tab 3: LoRA/Wildcard Manager ---
                with gr.Tab(t("tab_lora_manager")):
                    on_tab_lora_manager()

                # --- Tab 4: Manual ---
                with gr.Tab(t("tab_usage")):
                    gr.Markdown(t("usage_md"))

            # --- Wiring ---
            preset_args_list = [
                image_folder, memo_file, match_threshold, generation_count,
                fallback_enabled, auto_lora_enabled,
                gen_confidence, gen_positive, gen_negative, gen_custom_dict,
                wildcard_1_path, wildcard_2_path, wildcard_3_path,
                lora_offset,
                gen_mosaic_auto, gen_mosaic_level, gen_custom_dict_enabled,
                auto_optimize_prompt, custom_base_tags, active_profile, 
                prompt_polish, smart_negative, smart_negative_mode,
                inventory_mode, limit_base, limit_char, limit_nsfw,
                gen_cat_base, gen_cat_char, gen_cat_nsfw,
                conf_base_val, conf_char_val, conf_nsfw_val,
                use_global_conf
            ]

            preset_dropdown.change(fn=handle_load_preset, inputs=[preset_dropdown], outputs=preset_args_list)
            save_preset_btn.interactive = False

            def _toggle_save_preset_btn(name):
                return gr.update(interactive=bool(name and name.strip()))

            preset_name_input.input(
                fn=_toggle_save_preset_btn,
                inputs=[preset_name_input],
                outputs=[save_preset_btn]
            )

            save_preset_btn.click(
                fn=handle_save_preset,
                inputs=[preset_name_input] + preset_args_list,
                outputs=[status, preset_dropdown]
            )
            delete_preset_btn.click(fn=handle_delete_preset, inputs=[preset_dropdown], outputs=[status, preset_dropdown])

            def _save_all(
                lang, img_f, memo, threshold, count, fallback, auto_l, confidence, pos, neg, c_dict, 
                c_base, c_char, c_nsfw, w1, w2, w3, offset, mosaic_auto, mosaic_level, c_dict_enabled, 
                auto_opt, custom_tags, active_prof, polish, smart_neg, smart_neg_mode, inventory_mode, 
                limit_base, limit_char, limit_nsfw, c_mosaic, conf_base, conf_char, conf_nsfw, ug_conf,
                sort_mode="None", auto_file=False
            ):
                return save_all_settings(
                    lang, img_f, memo, threshold, count, fallback, auto_l, confidence, pos, neg, c_dict, 
                    c_base, c_char, c_nsfw, w1, w2, w3, offset, mosaic_auto, mosaic_level, c_dict_enabled, 
                    auto_opt, custom_tags, active_prof, polish, smart_neg, smart_neg_mode, inventory_mode, 
                    limit_base, limit_char, limit_nsfw, c_mosaic, conf_base, conf_char, conf_nsfw, ug_conf,
                    sort_mode, auto_file
                )

            all_settings_inputs = [
                lang_dropdown, image_folder, memo_file, match_threshold, generation_count,
                fallback_enabled, auto_lora_enabled,
                gen_confidence, gen_positive, gen_negative, gen_custom_dict,
                gen_cat_base, gen_cat_char, gen_cat_nsfw,
                wildcard_1_path, wildcard_2_path, wildcard_3_path, lora_offset,
                gen_mosaic_auto, gen_mosaic_level, gen_custom_dict_enabled, 
                auto_optimize_prompt, custom_base_tags, active_profile, 
                prompt_polish, smart_negative, smart_negative_mode, inventory_mode,
                limit_base, limit_char, limit_nsfw, gen_cat_mosaic,
                conf_base_val, conf_char_val, conf_nsfw_val, use_global_conf,
                output_sort_hidden, auto_filename_hidden  # P3: sort_mode / auto_file を保存に含める
            ]
            
            save_btn.click(fn=_save_all, inputs=all_settings_inputs, outputs=[status])
            gen_save_btn.click(fn=_save_all, inputs=all_settings_inputs, outputs=[append_status])

            test_btn.click(fn=compose_prompt_preview, inputs=[
                image_folder, memo_file, match_threshold, fallback_enabled, auto_lora_enabled, lora_offset, wildcard_1_path, wildcard_2_path, wildcard_3_path, active_profile, inventory_mode
            ], outputs=[preview_output])

            append_btn.click(fn=append_to_memo, inputs=[memo_file, gen_output], outputs=[append_status])

            # --- HEALTH CHECK WIRING ---
            health_inputs = [image_folder, memo_file, wildcard_1_path, wildcard_2_path, wildcard_3_path]
            health_outputs = [status_img, status_memo, status_w1, status_w2, status_w3]

            def _init_health():
                c = load_config()
                return check_individual_health(
                    c.get("image_folder", ""),
                    c.get("memo_file", ""),
                    c.get("wildcard_1_path", WILD_1_PATH),
                    c.get("wildcard_2_path", WILD_2_PATH),
                    c.get("wildcard_3_path", WILD_3_PATH)
                )

            for comp in health_inputs:
                comp.change(fn=check_individual_health, inputs=health_inputs, outputs=health_outputs)
            
            # 旧版で実績のある tab.load による初期化手順の復元
            tab_interface.load(fn=_init_health, outputs=health_outputs)

        # Tab ID を旧版と同じ "smart_composer_tabs_root" に差し戻し
        return [(tab_interface, "Smart Img2Img Composer", "smart_composer_tabs_root")]

    except Exception as e:
        err_f = traceback.format_exc()
        print(f"[Smart Img2Img Composer] FATAL: {e}")
        with gr.Blocks() as err_ui:
            gr.Markdown(f"## ❌ Smart Img2Img Composer: Load Error\n```{err_f}```")
        return [(err_ui, "Composer Error", "sc_error_tab")]

`

## sc_composer/ui_tabs_gen.py

`python
# -*- coding: utf-8 -*-
import gradio as gr
from .i18n import t
from .core import load_config, append_to_memo
from .tagger import autogen_prompt
from .constants import _CAT_BASE_KEYS, _CAT_CHAR_KEYS, _CAT_NSFW_KEYS

def on_tab_prompt_gen():
    config = load_config()

    with gr.Row():
        # Left Side (Settings)
        with gr.Column(scale=2):
            with gr.Row():
                with gr.Column(scale=1):
                    gen_image = gr.Image(label=t("target_image"), type="pil")
                with gr.Column(scale=1):
                    gen_section = gr.Textbox(label=t("section_name"), placeholder=t("section_ph"), info=t("section_info"))
            
            gr.Markdown(t("h_categories"))
            btn_toggle_cat_all = gr.Button(t("btn_toggle_cat_all"), variant="primary")
            
            # ▼ 究極のスリム化： [🔄] [0.35] [チェックボックス群] の完全1行配置 ▼
            with gr.Accordion(t("cat_base"), open=True):
                with gr.Row(equal_height=True):
                    btn_toggle_cat_base = gr.Button("🔄", variant="secondary", size="sm", min_width=40, scale=0)
                    conf_base = gr.Number(value=0.35, minimum=0.0, maximum=1.0, step=0.01, show_label=False, container=False, min_width=80, scale=0)
                    gen_cat_base = gr.CheckboxGroup(
                        choices=[(t(c), c) for c in _CAT_BASE_KEYS],
                        value=["cat_composition", "cat_pose", "cat_background", "cat_atmosphere"],
                        show_label=False,
                        scale=1
                    )
            
            with gr.Accordion(t("cat_char"), open=False):
                with gr.Row(equal_height=True):
                    btn_toggle_cat_char = gr.Button("🔄", variant="secondary", size="sm", min_width=40, scale=0)
                    conf_char = gr.Number(value=0.35, minimum=0.0, maximum=1.0, step=0.01, show_label=False, container=False, min_width=80, scale=0)
                    gen_cat_char = gr.CheckboxGroup(
                        choices=[(t(c), c) for c in _CAT_CHAR_KEYS],
                        value=["cat_char_face", "cat_char_male"],
                        show_label=False,
                        scale=1
                    )
            
            with gr.Accordion(t("cat_nsfw"), open=False):
                with gr.Row(equal_height=True):
                    btn_toggle_cat_nsfw = gr.Button("🔄", variant="secondary", size="sm", min_width=40, scale=0)
                    conf_nsfw = gr.Number(value=0.35, minimum=0.0, maximum=1.0, step=0.01, show_label=False, container=False, min_width=80, scale=0)
                    gen_cat_nsfw = gr.CheckboxGroup(
                        choices=[(t(c), c) for c in _CAT_NSFW_KEYS],
                        value=[k for k in _CAT_NSFW_KEYS if k != "cat_nsfw_clothes_mess"],
                        show_label=False,
                        scale=1
                    )

            with gr.Accordion(t("h_pickup_limits"), open=False):
                with gr.Row():
                    limit_base = gr.Number(label=t('limit_base_label'), minimum=1, maximum=50, step=1, value=10, min_width=80)
                    limit_char = gr.Number(label=t('limit_char_label'), minimum=1, maximum=50, step=1, value=10, min_width=80)
                    limit_nsfw = gr.Number(label=t('limit_nsfw_label'), minimum=1, maximum=50, step=1, value=15, min_width=80)

            # ▼ 新規追加：共通信頼性の優先チェックボックスと説明文 ▼
            with gr.Group():
                with gr.Row(equal_height=True):
                    use_global_conf = gr.Checkbox(label=t("use_global_conf"), value=True, min_width=0)
                    gr.HTML(f"<span style='font-size: 0.85em; color: gray; margin-left: 10px; white-space: nowrap;'>{t('use_global_conf_info')}</span>")
                gen_confidence = gr.Slider(label=t('conf_total'), minimum=0.0, maximum=1.0, step=0.05, value=0.35)

            gen_positive = gr.Textbox(label=t("default_positive"), placeholder="masterpiece, 1girl...", lines=2, value=lambda: load_config().get("gen_positive", ""))
            gen_negative = gr.Textbox(label=t("default_negative"), placeholder="lowres, bad anatomy...", lines=2, value=lambda: load_config().get("gen_negative", ""))

            with gr.Accordion(t("gen_custom_dict_enabled_label"), open=False):
                gen_custom_dict_enabled = gr.Checkbox(label=t("gen_custom_dict_enabled_label"), value=False, show_label=False)
                gen_custom_dict = gr.Textbox(label=t("custom_dict"), placeholder="night > neon lights...", lines=3, value=lambda: load_config().get("gen_custom_dict", ""))

            with gr.Accordion(t("h_mosaic_settings"), open=False):
                gen_mosaic_auto = gr.Checkbox(label=t("gen_mosaic_auto"), value=False)
                gen_mosaic_level = gr.Radio(label=t("gen_mosaic_level"), choices=[t("mosaic_low"), t("mosaic_med"), t("mosaic_high")], value=t("mosaic_med"))
                gr.Markdown(t("mosaic_layer_1"))
                gen_cat_mosaic = gr.CheckboxGroup(
                    choices=[("mosaic_censoring", "mosaic_censoring"), ("bar_censor", "bar_censor"), ("censored", "censored"), ("uncensored", "uncensored"), ("detailed_mosaic", "detailed_mosaic")],
                    value=["mosaic_censoring", "bar_censor", "censored"],
                    show_label=False
                )

            with gr.Row():
                gen_btn = gr.Button(t("btn_gen_tags"), variant="primary", scale=2)
                append_btn = gr.Button(t("btn_append_memo"), variant="secondary", scale=1)
                gen_save_btn = gr.Button(t("btn_save_settings"), variant="secondary", scale=1)

        # Right Side (Output)
        with gr.Column(scale=1):
            send_img2img_btn = gr.Button(t("btn_send_img2img"), variant="primary")
            gen_output = gr.Textbox(label=t("generated_entry"), lines=12, interactive=True)
            gen_tags_only = gr.Textbox(label=t("gen_tags_only"), lines=6, interactive=True)
            gen_log = gr.Textbox(label=t("analysis_log"), lines=8, interactive=False)
            append_status = gr.Textbox(label=t("append_status"), interactive=False)

    # --- Category Toggle Helpers ---
    def toggle_group(current, keys):
        if len(current) > 0: return gr.update(value=[])
        return gr.update(value=keys)

    def toggle_all(b, c, n):
        if b or c or n: return gr.update(value=[]), gr.update(value=[]), gr.update(value=[])
        return gr.update(value=_CAT_BASE_KEYS), gr.update(value=_CAT_CHAR_KEYS), gr.update(value=_CAT_NSFW_KEYS)

    btn_toggle_cat_all.click(fn=toggle_all, inputs=[gen_cat_base, gen_cat_char, gen_cat_nsfw], outputs=[gen_cat_base, gen_cat_char, gen_cat_nsfw])
    btn_toggle_cat_base.click(fn=lambda v: toggle_group(v, _CAT_BASE_KEYS), inputs=[gen_cat_base], outputs=[gen_cat_base])
    btn_toggle_cat_char.click(fn=lambda v: toggle_group(v, _CAT_CHAR_KEYS), inputs=[gen_cat_char], outputs=[gen_cat_char])
    btn_toggle_cat_nsfw.click(fn=lambda v: toggle_group(v, _CAT_NSFW_KEYS), inputs=[gen_cat_nsfw], outputs=[gen_cat_nsfw])

    # --- Event Wiring ---
    gen_btn.click(
        fn=autogen_prompt,
        inputs=[
            gen_image, gen_section, gen_confidence, gen_positive, gen_negative, 
            gen_cat_base, gen_cat_char, gen_cat_nsfw, gen_custom_dict, 
            gen_mosaic_auto, gen_mosaic_level, gen_custom_dict_enabled, 
            limit_base, limit_char, limit_nsfw, gen_cat_mosaic,
            conf_base, conf_char, conf_nsfw, use_global_conf
        ],
        outputs=[gen_output, gen_log, gen_tags_only]
    )

    # JS Fix: scSendToImg2img は smart_img2img_composer.js で定義
    # タブ切り替えを 250ms 遅延させることで Gradio の _js 後処理との競合を回避
    send_img2img_btn.click(
        fn=None,
        _js="scSendToImg2img",
        inputs=[gen_image, gen_output, gen_negative],
        outputs=None
    )

    return (
        gen_image, gen_section, gen_confidence, gen_positive, gen_negative, gen_custom_dict,
        gen_cat_base, gen_cat_char, gen_cat_nsfw, gen_mosaic_auto, gen_mosaic_level, gen_custom_dict_enabled,
        limit_base, limit_char, limit_nsfw, gen_cat_mosaic,
        gen_btn, gen_output, gen_log, gen_tags_only, gen_save_btn, append_btn, append_status, send_img2img_btn,
        conf_base, conf_char, conf_nsfw, use_global_conf
    )

`

## sc_composer/ui_tabs_inventory.py

`python
# -*- coding: utf-8 -*-
import gradio as gr
from .i18n import t
from .core import load_config, get_inventory_status, reset_inventory_global, reset_inventory_lora

def on_tab_inventory():
    config = load_config()
    
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown(t("inventory_desc"))
            inventory_mode_chk = gr.Checkbox(
                label=t("inventory_mode"),
                value=lambda: load_config().get("inventory_mode", False),
                info=t("inventory_mode_info")
            )
            
            with gr.Row():
                check_btn = gr.Button(t("btn_check_stock"), variant="primary")
                reset_lora_btn = gr.Button(t("btn_lora_reset"), variant="secondary")
                reset_all_btn = gr.Button(t("btn_global_reset"), variant="secondary")
            
            status_msg = gr.Markdown("")
            
        with gr.Column(scale=1):
            gr.Markdown(f"### {t('inventory_status_label')}")
            inventory_display = gr.Textbox(label=None, lines=20, interactive=False)

    # Events
    check_btn.click(fn=get_inventory_status, outputs=[inventory_display])
    reset_lora_btn.click(fn=reset_inventory_lora, outputs=[status_msg])
    reset_all_btn.click(fn=reset_inventory_global, outputs=[status_msg])

    return inventory_mode_chk

`

## sc_composer/ui_tabs_lora.py

`python
# -*- coding: utf-8 -*-
import gradio as gr
from .i18n import t
from .lora_mgr import load_lora_list, save_lora_list, append_lora_list

def on_tab_lora_manager():
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown(t("lora_manager_desc"))
            lora_type = gr.Radio(
                label=t("lora_type"),
                choices=[t("lora_type_char"), t("lora_type_sit"), t("wildcard_1"), t("wildcard_2"), t("wildcard_3")],
                value=t("lora_type_char")
            )
            lora_list = gr.Textbox(label=t("lora_list_label"), lines=15, placeholder=t("lora_mgr_placeholder"))
            
            with gr.Row():
                save_btn = gr.Button(t("btn_save_lora_list"), variant="primary")
                status = gr.Markdown("")
        
        with gr.Column(scale=1):
            gr.Markdown("### \u2795 Quick Append")
            lora_input = gr.Textbox(label=t("lora_input_label"), placeholder="<lora:name:1.0> or tag")
            append_btn = gr.Button(t("btn_append_lora"), variant="secondary")

    # Events
    lora_type.change(fn=load_lora_list, inputs=[lora_type], outputs=[lora_list])
    
    # Matching save_lora_list return values
    def _do_save(label, content):
        msg, new_content = save_lora_list(label, content)
        return msg

    save_btn.click(fn=_do_save, inputs=[lora_type, lora_list], outputs=[status])
    
    def _do_append(label, input_text):
        # Append logic: return updated list and clear input box
        new_list, _ = append_lora_list(label, input_text)
        return new_list, ""

    append_btn.click(fn=_do_append, inputs=[lora_type, lora_input], outputs=[lora_list, lora_input])

    return lora_list

`

## sc_composer/utils.py

`python
import re
import os
from .constants import PROMPT_PROFILES, IMAGE_EXTENSIONS

def _clean_path(path: str) -> str:
    if not path or not isinstance(path, str): return ""
    return path.strip().strip('"').strip("'").strip()

def _polish_prompt(prompt_str: str) -> str:
    if not prompt_str: return ""
    res = re.sub(r',[\s,]+', ', ', prompt_str)
    res = re.sub(r',\s*\)', ')', res)
    res = re.sub(r',\s*\]', ']', res)
    res = re.sub(r'\s+', ' ', res)
    res = res.strip(", ")
    
    parts = [p.strip() for p in res.split(',')]
    seen = set()
    unique_parts = []
    for p in parts:
        if not p: continue
        # LoRA タグやウェイト付きタグは重複除去しない（意図的な違いがある）
        if "<lora:" in p or (p.startswith("(") and ":" in p):
            unique_parts.append(p)
            continue
        
        lower_p = p.lower()
        if lower_p not in seen:
            seen.add(lower_p)
            unique_parts.append(p)
            
    return ", ".join(unique_parts)

_EXT_SET = {ext.lower() for ext in IMAGE_EXTENSIONS}

def get_image_files(folder: str) -> list:
    folder = _clean_path(folder)
    if not folder or not os.path.isdir(folder): return []
    res = []
    for f in os.listdir(folder):
        ext = os.path.splitext(f)[1].lower()
        if ext in _EXT_SET:
            res.append(os.path.join(folder, f))
    return sorted(res)

def get_stable_dimensions(img, mode, base_res=1024):
    if not img: return None, None
    w, h = img.size
    if "slider" in mode.lower() or "\u30b9\u30e9\u30a4\u30c0\u30fc" in mode:
        if w > h:
            nw = base_res; nh = int(h * (base_res / w))
        else:
            nh = base_res; nw = int(w * (base_res / h))
        return nw, nh
    mi, mx = 512, 1024
    if "512" in mode: mi, mx = 512, 1024
    elif "1024" in mode: mi, mx = 1024, 1536
    elif "1536" in mode: mi, mx = 1536, 1792
    else: return w, h
    long_edge = max(w, h)
    if long_edge <= mi: scale = mi / long_edge
    elif long_edge >= mx: scale = mx / long_edge
    else: return (w // 64 * 64), (h // 64 * 64)
    return (int(w * scale) // 64 * 64), (int(h * scale) // 64 * 64)


# P3: カテゴリ分類キーワード辞書
# PROMPT_PROFILES の order に登場するカテゴリに対してキーワードで仕分ける
_CAT_KEYWORDS = {
    # quality / score / rating 系
    "quality":  {"masterpiece", "best quality", "ultra-detailed", "highres", "highly detailed",
                 "very aesthetic", "absurdres", "illustration"},
    "score":    {"score_9", "score_8_up", "score_7_up", "score_6_up", "score_5_up",
                 "score_4_up", "score_4", "score_5", "score_6"},
    "rating":   {"source_anime", "source_pony", "source_furry", "source_cartoon",
                 "rating_safe", "rating_questionable", "rating_explicit",
                 "general", "sensitive", "nsfw"},
    # subject 系（人物描写）
    "subject":  {"1girl", "1boy", "2girls", "2boys", "multiple girls", "multiple boys",
                 "solo", "duo", "group", "standing", "sitting", "lying", "smile", "closed eyes",
                 "looking at viewer", "long hair", "short hair", "blonde hair", "black hair",
                 "blue eyes", "brown eyes"},
    # clothing 系
    "clothing": {"dress", "shirt", "skirt", "jacket", "coat", "uniform", "bikini",
                 "swimsuit", "naked", "nude", "topless", "bottomless", "underwear",
                 "lingerie", "pantyhose", "thighhighs", "socks", "shoes", "boots"},
    # environment / background 系
    "environment": {"outdoors", "indoors", "background", "sky", "cloud", "forest", "city",
                    "ocean", "beach", "room", "classroom", "garden", "street", "night",
                    "day", "sunset", "sunrise", "rain", "snow", "nature", "urban"},
    # lighting 系
    "lighting": {"light", "shadow", "bright", "dark", "backlight", "rim light",
                 "soft lighting", "hard lighting", "dramatic lighting", "bloom",
                 "glow", "neon", "sunlight", "moonlight", "candlelight"},
    # camera / composition 系
    "camera":   {"close-up", "close up", "full body", "upper body", "cowboy shot",
                 "portrait", "from above", "from below", "from behind", "side view",
                 "wide shot", "medium shot", "dutch angle", "fisheye", "bokeh",
                 "depth of field", "motion blur"},
    # style 系
    "style":    {"anime", "manga", "realistic", "3d", "digital art", "watercolor",
                 "oil painting", "sketch", "line art", "flat color", "cel shading",
                 "photorealistic", "hyperrealistic", "painterly"},
}

def _classify_tag(tag: str, categorized: dict) -> str | None:
    """タグを categorized のキーにマッピングして返す。マッチしなければ None。"""
    lower = tag.lower()
    for cat, keywords in _CAT_KEYWORDS.items():
        if cat not in categorized: continue
        for kw in keywords:
            if " " in kw:
                # 複数語キーワード: 部分一致（"soft lighting" in "beautiful soft lighting"）
                if kw in lower:
                    return cat
            else:
                # 単語キーワード: 完全一致のみ（"dark" != "dark elf"）
                if lower == kw:
                    return cat
    return None

def optimize_prompt_order(prompt: str, profile: str = "Standard / SDXL") -> str:
    if profile not in PROMPT_PROFILES: return prompt
    order = PROMPT_PROFILES[profile]["order"]
    tags = [tag.strip() for tag in prompt.split(",") if tag.strip()]
    categorized = {cat: [] for cat in order}
    others = []
    for tag in tags:
        lower = tag.lower()
        # LoRA / wildcard は専用処理
        if "<lora:" in lower:
            if "lora" in categorized: categorized["lora"].append(tag)
            else: others.append(tag)
            continue
        if "__" in tag and tag.startswith("__") and tag.endswith("__"):
            if "wildcard" in categorized: categorized["wildcard"].append(tag)
            else: others.append(tag)
            continue
        # キーワード辞書でカテゴリ分類
        cat = _classify_tag(tag, categorized)
        if cat:
            categorized[cat].append(tag)
        else:
            others.append(tag)
    # カテゴリ順に並べ、未分類タグは末尾に配置
    # （Pony等でスコアタグの間に割り込むのを防止）
    result = []
    for cat in order:
        result.extend(categorized.get(cat, []))
    return ", ".join(result + others)

def check_individual_health(image_folder, memo_file, w1, w2, w3):
    from .i18n import t
    def check(p, is_file=False):
        if not p: 
            msg = t("health_check_ok")
        else:
            p_clean = _clean_path(p)
            exists = os.path.isfile(p_clean) if is_file else os.path.isdir(p_clean)
            msg = t("health_check_ok") if exists else "❌ " + t("health_check_err").format(path=os.path.basename(p_clean) or "Invalid")
        
        # ▼ Gradioに押し潰されないための「強制CSS化」▼
        return f"<div style='margin-top: 36px; font-weight: bold; white-space: nowrap;'>{msg}</div>"
    
    return (
        check(image_folder, False),
        check(memo_file, True),
        check(w1, True),
        check(w2, True),
        check(w3, True)
    )

`

## scripts/random_composer.py

`python
# -*- coding: utf-8 -*-
import os
import sys
import random
from pathlib import Path

# --- Ensure path for sc_composer (from root) ---
ext_root = str(Path(__file__).parent.parent)
if ext_root not in sys.path:
    sys.path.insert(0, ext_root)  # insert(0) で優先順位を上げる
print(f"[Smart Img2Img Composer] ext_root={ext_root}")

import gradio as gr
from modules import scripts

from sc_composer.constants import PROMPT_PROFILES
from sc_composer.i18n import t
from sc_composer.utils import _clean_path, _polish_prompt, get_stable_dimensions
from sc_composer.core import load_config, compose_prompt, pick_random_assets

class RandomComposerScript(scripts.Script):
    def title(self):
        return "Smart Img2Img Composer v1.1.2"

    def show(self, is_img2img):
        return scripts.AlwaysVisible if is_img2img else False

    def ui(self, is_img2img):
        if not is_img2img: return []
        from sc_composer.ui_img2img import on_ui_img2img
        return on_ui_img2img()

    def before_process(self, p, *args):
        if not args or not args[0]:
            return  # Early return if not enabled
        if getattr(p, "_sc_processed", False):
            return  # Prevent double processing
        setattr(p, "_sc_processed", True)

        config = load_config()
        p.n_iter = config.get("generation_count", 1)

        try:
            overwrite_prompt = args[1]
            resize_mode = args[2]
            base_res = args[3]
            selection_mode = args[4]
            en_char = args[5]
            pos_char_mode = args[6]
            en_sit = args[7]
            pos_sit_mode = args[8]
            en_w1 = args[9]
            pos_w1_mode = args[10]
            en_w2 = args[11]
            pos_w2_mode = args[12]
            en_w3 = args[13]
            pos_w3_mode = args[14]
            output_sort_mode = args[15]
            auto_optimize = args[16]
            custom_base_tags = args[17]
            active_profile = args[18]
            prompt_polish = args[19]
            auto_filename = args[20]
        except IndexError:
            print("[Smart Img2Img Composer] UI components count mismatch.")
            return
        
        actual_preset_name = config.get("last_preset", "Default")
        image_folder = config.get("image_folder", ""); memo_file = config.get("memo_file", "")
        match_threshold = config.get("match_threshold", 0.3); inventory_mode = config.get("inventory_mode", False)

        sel_mode_str = "sequential" if "sequential" in str(selection_mode).lower() else "random"
        img_path, pos, neg, log, section_name = compose_prompt(image_folder, memo_file, match_threshold, selection_mode=sel_mode_str)
        if not img_path: return

        from PIL import Image
        image = Image.open(img_path); p.init_images = [image]
        assets = pick_random_assets(en_char, en_sit, en_w1, en_w2, en_w3, inventory_mode=inventory_mode)
        
        def _inject(prompt, asset, pos_mode, is_lora=True):
            if not asset: return prompt
            item = f"<lora:{asset}:1.0>" if is_lora else f"__{asset}__"
            if pos_mode == t("pos_front"): return f"{item}, {prompt}"
            elif pos_mode == t("pos_back"): return f"{prompt}, {item}"
            else:
                base_tags = [bt.strip().lower() for bt in custom_base_tags.split(",") if bt.strip()]
                tags = [tag.strip() for tag in prompt.split(",") if tag.strip()]
                last_idx = -1
                for i, tag in enumerate(tags):
                    if any(bt in tag.lower() for bt in base_tags): last_idx = i
                if last_idx != -1:
                    tags.insert(last_idx + 1, item)
                    return ", ".join(tags)
                # base_tags が空/一致なしの場合は Back にフォールバック
                return f"{prompt}, {item}"

        pos = _inject(pos, assets["char"], pos_char_mode, True)
        pos = _inject(pos, assets["sit"], pos_sit_mode, True)
        pos = _inject(pos, assets["w1"], pos_w1_mode, False)
        pos = _inject(pos, assets["w2"], pos_w2_mode, False)
        pos = _inject(pos, assets["w3"], pos_w3_mode, False)

        if resize_mode != t("resize_none"):
            new_w, new_h = get_stable_dimensions(image, mode=resize_mode, base_res=base_res)
            if new_w: p.width, p.height = new_w, new_h

        full_pos = pos; full_neg = neg
        if not overwrite_prompt:
            full_pos = f"{p.prompt}, {pos}"; full_neg = f"{p.negative_prompt}, {neg}"

        if config.get("smart_negative", False):
            profile = PROMPT_PROFILES.get(active_profile, next(iter(PROMPT_PROFILES.values())))
            profile_neg = profile.get("neg", "")
            if config.get("smart_negative_mode", "append") == "overwrite": full_neg = profile_neg
            else: full_neg = f"{full_neg}, {profile_neg}"

        lora_offset = config.get("lora_offset", 0.0)
        if lora_offset != 0.0:
            from sc_composer.core import apply_lora_offset
            full_pos = apply_lora_offset(full_pos, lora_offset)

        if prompt_polish:
            full_pos = _polish_prompt(full_pos); full_neg = _polish_prompt(full_neg)
        if auto_optimize:
            from sc_composer.utils import optimize_prompt_order
            full_pos = optimize_prompt_order(full_pos, active_profile)

        p.prompt = full_pos; p.negative_prompt = full_neg
        # Ensure extra_generation_params is a dict (handles None or non-dict)
        if not hasattr(p, 'extra_generation_params') or not isinstance(p.extra_generation_params, dict):
            p.extra_generation_params = {}
        p.extra_generation_params["SC_Section"] = section_name
        p.extra_generation_params["SC_Preset"] = actual_preset_name
        p.extra_generation_params["SC_AutoFilename"] = auto_filename
        p.extra_generation_params["SC_SortMode"] = output_sort_mode

def on_before_image_saved(params):
    p = params.p
    if not p or not hasattr(p, 'extra_generation_params') or p.extra_generation_params is None: return # B6: guard
    egp = p.extra_generation_params
    auto_filename = egp.get("SC_AutoFilename", False)
    sort_mode = egp.get("SC_SortMode", "None")
    section = egp.get("SC_Section", "Default")
    preset = egp.get("SC_Preset", "Default")

    # 元の保存先ディレクトリ（outputs等）を必ず確保する
    orig_dir = os.path.dirname(params.filename)
    new_basename = os.path.basename(params.filename)

    subfolder = ""
    if sort_mode == "By Preset": subfolder = preset
    elif sort_mode == "By Section": subfolder = section
    elif sort_mode == "By Date":
        from datetime import datetime
        subfolder = datetime.now().strftime("%Y-%m-%d")
    
    # フォルダパスの安全な結合（元のパスを絶対に消さない）
    if subfolder:
        subfolder = "".join(c for c in subfolder if c.isalnum() or c in (" ", "-", "_")).strip()
        if subfolder:
            orig_dir = os.path.join(orig_dir, subfolder)
            os.makedirs(orig_dir, exist_ok=True)

    # 自動ファイル名生成
    if auto_filename and hasattr(p, 'prompt') and p.prompt:
        tags = [tok.strip() for tok in p.prompt.split(",") if tok.strip() and ":" not in tok and "<" not in tok]
        naming = "-".join(tags[:3]).replace(" ", "_")
        if naming:
            new_basename = f"{naming}_{new_basename}"

    # 最終決定したパスをセット
    params.filename = os.path.join(orig_dir, new_basename)

from modules import script_callbacks
try:
    from sc_composer.ui_tabs import on_ui_tabs
    script_callbacks.on_ui_tabs(on_ui_tabs)
    script_callbacks.on_before_image_saved(on_before_image_saved)
except Exception as e:
    import traceback
    print(f"[Smart Img2Img Composer] FATAL callback registration error: {e}")
    traceback.print_exc()

`

## javascript/smart_img2img_composer.js

`javascript
/**
 * Smart Img2Img Composer - JavaScript Helper
 *
 * 【初回だけプロンプトが届かない問題の原因と解決策】
 *
 * 旧実装の問題:
 *   プロンプト即時転送 → タブ切り替え(250ms後) の順だったため、
 *   初回は img2img タブが未初期化で textarea が DOM に存在せず空振り。
 *   2回目以降は DOM が既に存在するので届く。
 *
 * 新実装の順序:
 *   250ms後: タブ切り替え（先にDOMを確実に出現させる）+ 画像転送開始
 *   450ms後: プロンプトセット（DOM描画完了を待つ）+ リトライ付き
 */

/** Gradio Shadow DOM / 通常 DOM 両対応 querySelector */
function scApp() {
    if (typeof gradioApp === 'function') return gradioApp();
    return document.querySelector('gradio-app') || document;
}

/** テキストエリアに値をセット + Gradio 変更検知トリガー */
function scSetTextarea(selector, value) {
    var app = scApp();
    var area = app.querySelector(selector + ' textarea');
    if (!area) return false;
    var setter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, 'value').set;
    setter.call(area, value);
    area.dispatchEvent(new Event('input',  { bubbles: true }));
    area.dispatchEvent(new Event('change', { bubbles: true }));
    return true;
}

/** img2img タブへ切り替え（即時） */
function scSwitchToImg2img() {
    if (typeof switch_to_img2img === 'function') {
        try { switch_to_img2img(); return true; } catch(e) {}
    }
    var app = scApp();
    var tabs = app.querySelectorAll('#tabs > div > button');
    var found = false;
    tabs.forEach(function(btn) {
        var txt = (btn.innerText || btn.textContent || '').toLowerCase().trim();
        if (!found && txt.indexOf('img2img') !== -1 && txt.indexOf('settings') === -1) {
            btn.click();
            found = true;
        }
    });
    if (found) return true;
    if (tabs.length > 1) { tabs[1].click(); return true; }
    return false;
}

/**
 * プロンプトセット（リトライ付き）
 * タブ切り替え直後は textarea がまだ描画中のことがあるため
 * 最大 retries 回、100ms 間隔で再試行する
 */
function scSetPromptsWithRetry(pos, neg, delay_ms, retries) {
    setTimeout(function() {
        var ok = scSetTextarea('#img2img_prompt', pos);
        scSetTextarea('#img2img_neg_prompt', neg);
        if (!ok && retries > 1) {
            scSetPromptsWithRetry(pos, neg, 100, retries - 1);
        }
    }, delay_ms);
}

/** 画像を fetch して img2img の file input に流し込む */
function scTransferImage(imgUrl) {
    fetch(imgUrl)
        .then(function(r) { return r.blob(); })
        .then(function(blob) {
            var file = new File([blob], 'sc_image.png', { type: blob.type || 'image/png' });
            var app = scApp();
            [
                app.querySelector('#img2img_image'),
                app.querySelector('#img2img_sketch'),
                app.querySelector('[data-testid="img2img"]'),
            ].forEach(function(c) {
                if (!c) return;
                var inp = c.querySelector('input[type="file"]');
                if (!inp) return;
                var dt = new DataTransfer();
                dt.items.add(file);
                inp.files = dt.files;
                inp.dispatchEvent(new Event('change', { bubbles: true }));
            });
        })
        .catch(function(e) { console.warn('[SC] Image fetch failed:', e); });
}

/**
 * メインハンドラ
 *
 * タイムライン:
 *   0ms    : 関数呼び出し（Gradio _js 後処理待ちのため即時操作はしない）
 *   250ms  : ① タブ切り替え（DOMを出現させる）  ② 画像転送開始
 *   450ms  : ③ プロンプトセット（リトライ最大5回 × 100ms）
 *
 * ポイント: タブを先に切り替えることで初回でも textarea が存在する状態を作る
 */
function scSendToImg2img(img, entry, default_neg) {
    // ── プロンプト解析 ──
    var pos = '';
    var neg = (default_neg && typeof default_neg === 'string') ? default_neg.trim() : '';

    if (entry && typeof entry === 'string') {
        var posMarker = 'positive:\n';
        var negMarker = '\n\nnegative:\n';
        var pi = entry.indexOf(posMarker);
        if (pi !== -1) {
            var after = entry.substring(pi + posMarker.length);
            var ni = after.indexOf(negMarker);
            if (ni !== -1) {
                pos = after.substring(0, ni).trim();
                neg = after.substring(ni + negMarker.length).trim();
            } else {
                pos = after.trim();
            }
        } else {
            pos = entry.trim();
        }
    }

    // ── 画像URL解決 ──
    var imgUrl = null;
    if (img) {
        if (typeof img === 'string' && img.length > 0)        { imgUrl = img; }
        else if (img.data)                                     { imgUrl = img.data; }
        else if (img.path)                                     { imgUrl = img.path; }
        else if (Array.isArray(img) && img[0] && img[0].data) { imgUrl = img[0].data; }
    }

    // ── Step 1 (250ms後): タブ切り替え ＋ 画像転送 ──
    setTimeout(function() {
        scSwitchToImg2img();
        if (imgUrl) scTransferImage(imgUrl);

        // ── Step 2 (さらに200ms後): プロンプトセット ──
        // タブを開いた後 textarea の描画を待ってからセット、最大5回リトライ
        scSetPromptsWithRetry(pos, neg, 200, 5);

    }, 250);
}

`
