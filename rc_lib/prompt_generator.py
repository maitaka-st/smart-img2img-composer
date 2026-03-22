# -*- coding: utf-8 -*-
"""
プロンプト自動生成モジュール
WD14 Tagger と連携して画像からシーン/ポーズ/構図タグのみ抽出する。
服装・人物特徴は除外し、img2imgで元キャラに干渉しないプロンプトを生成。
"""

import os
import sys
import re

# ======================================================================
# 許可タグパターン（これらに一致するタグのみ残す）
# ======================================================================
# img2imgで元画像のキャラクターに干渉しないタグだけを通す

# ── 構図・ショット ──
COMPOSITION_TAGS = {
    "portrait", "upper_body", "lower_body", "full_body",
    "cowboy_shot", "close-up", "wide_shot", "medium_shot",
    "head_shot", "bust_shot", "knee_shot",
    "profile", "three-quarter_view",
}

# ── カメラアングル・視点 ──
CAMERA_TAGS = {
    "from_above", "from_below", "from_behind", "from_side",
    "from_outside", "dutch_angle", "tilted_frame",
    "pov", "first-person_view", "over-shoulder_shot",
    "bird's-eye_view", "worm's-eye_view", "aerial_view",
    "looking_at_viewer", "looking_away", "looking_back",
    "looking_down", "looking_up", "looking_to_the_side",
    "looking_afar", "looking_at_another",
    "facing_away", "facing_viewer",
    "rotated",
}

# ── ポーズ・動作 ──
POSE_TAGS = {
    "standing", "sitting", "lying", "walking", "running",
    "jumping", "crouching", "kneeling", "leaning",
    "leaning_forward", "leaning_back",
    "arms_up", "arms_behind_back", "arms_behind_head",
    "hand_on_hip", "hand_on_own_chest", "hand_on_own_face",
    "hands_on_hips", "hand_up", "hands_up",
    "crossed_arms", "hands_in_pockets",
    "outstretched_arm", "outstretched_arms",
    "reaching", "reaching_out", "pointing", "pointing_at_viewer",
    "spread_arms", "stretching", "waving",
    "v", "peace_sign", "thumbs_up", "double_v",
    "on_back", "on_stomach", "on_side",
    "legs_crossed", "indian_style", "seiza", "wariza",
    "legs_apart", "legs_together",
    "one_knee", "squatting",
    "head_tilt", "head_rest",
    "arched_back", "fetal_position", "hugging_own_legs",
    "lying_on_back", "lying_on_stomach", "lying_on_side",
    "sitting_on_chair", "sitting_on_floor", "sitting_on_bench",
    "standing_on_one_leg", "contrapposto",
    "back-to-back", "arm_support", "chin_rest",
    "holding", "carrying",
    "dancing", "fighting_stance", "battle_stance",
    "action", "dynamic_pose", "floating",
    "falling", "spinning", "twisting",
}

# ── 背景・場所 ──
SCENE_TAGS = {
    "outdoors", "indoors",
    "cityscape", "landscape", "scenery",
    "city", "town", "village", "suburb",
    "sky", "blue_sky", "cloudy_sky", "starry_sky", "night_sky",
    "cloud", "clouds",
    "sunset", "sunrise", "twilight", "dawn", "dusk",
    "night", "day", "evening", "morning", "afternoon",
    "forest", "woods", "jungle",
    "mountain", "hill", "cliff", "valley",
    "ocean", "sea", "beach", "shore", "coast",
    "river", "lake", "pond", "waterfall", "stream",
    "field", "meadow", "grassland", "plains",
    "garden", "park", "playground",
    "street", "road", "path", "alley", "sidewalk",
    "school", "classroom", "library", "gym",
    "office", "workplace", "studio",
    "bedroom", "kitchen", "bathroom", "living_room",
    "dining_room", "hallway", "corridor",
    "rooftop", "balcony", "veranda", "patio", "terrace",
    "window", "door", "doorway",
    "castle", "palace", "mansion",
    "temple", "shrine", "church", "cathedral",
    "ruins", "dungeon", "cave", "cavern",
    "bridge", "stairs", "staircase", "escalator",
    "train", "train_interior", "train_station", "platform",
    "bus", "bus_interior", "bus_stop",
    "car", "car_interior",
    "ship", "boat", "dock", "harbor", "port",
    "airport", "airplane", "airplane_interior",
    "restaurant", "cafe", "bar", "shop", "store",
    "hospital", "prison", "factory",
    "arena", "stadium", "stage", "theater",
    "space", "planet", "moon", "stars",
    "underwater", "floating_island",
    "marketplace", "bazaar", "festival",
    "cemetery", "graveyard",
    "tower", "lighthouse", "windmill",
    "fountain", "statue", "monument",
    "desert", "oasis", "wasteland", "swamp",
    "volcano", "island", "archipelago",
}

# ── 自然・天候 ──
NATURE_TAGS = {
    "snow", "snowing", "rain", "raining", "storm",
    "fog", "mist", "haze",
    "wind", "windy", "breeze",
    "lightning", "thunder",
    "rainbow",
    "cherry_blossoms", "petals", "falling_petals",
    "autumn_leaves", "falling_leaves",
    "flower", "flowers", "bouquet",
    "tree", "trees", "bamboo",
    "grass", "moss", "ivy", "vines",
    "water", "waves", "ripples", "puddle",
    "fire", "flame", "campfire", "bonfire",
    "ice", "icicle", "frost",
    "sunbeam", "light_particles", "sparkle",
    "bubble", "bubbles",
    "feather", "feathers",
    "leaf", "leaves",
    "butterfly", "bird", "birds",
}

# ── 照明 ──
LIGHTING_TAGS = {
    "sunlight", "moonlight", "starlight",
    "backlighting", "backlight",
    "rim_lighting", "rim_light",
    "dramatic_lighting", "soft_lighting",
    "cinematic_lighting", "natural_lighting",
    "volumetric_lighting", "volumetric_light",
    "studio_lighting",
    "light_rays", "crepuscular_rays", "god_rays",
    "lens_flare", "light_leak",
    "shadow", "shadows", "silhouette",
    "reflection", "reflective",
    "glow", "glowing", "neon_lights",
    "candlelight", "firelight", "lamplight",
    "streetlight", "spotlight",
    "warm_lighting", "cool_lighting",
    "ambient_light", "diffused_light",
    "dappled_light", "dappled_sunlight",
    "chiaroscuro", "high_contrast", "low_key",
}

# ── 雰囲気・効果 ──
ATMOSPHERE_TAGS = {
    "depth_of_field", "bokeh", "shallow_depth_of_field",
    "blurry_background", "blurry_foreground",
    "detailed_background", "simple_background",
    "white_background", "black_background", "gradient_background",
    "motion_blur", "speed_lines",
    "chromatic_aberration", "film_grain", "noise",
    "vignette", "bloom",
    "atmospheric_perspective", "hazy",
    "soft_focus",
    "monochrome", "sepia", "desaturated",
    "vibrant", "colorful", "pastel",
    "dark", "bright", "dim",
    "wide_angle", "telephoto", "fisheye",
    "panorama", "split_screen",
}

# すべての許可タグを統合
ALL_ALLOWED_TAGS = (
    COMPOSITION_TAGS
    | CAMERA_TAGS
    | POSE_TAGS
    | SCENE_TAGS
    | NATURE_TAGS
    | LIGHTING_TAGS
    | ATMOSPHERE_TAGS
)

# ── 除外パターン（正規表現）── 許可タグに含まれなかった場合の追加フィルタ
EXCLUDE_PATTERNS = [
    # 人物数・性別
    r"^\d+girl", r"^\d+boy", r"^solo$", r"^duo$", r"^trio$",
    r"^multiple_", r"^couple$", r"^group$",
    # 髪
    r"_hair$", r"^hair_", r"^bangs$", r"^ponytail$", r"^twintails$",
    r"^braid", r"^ahoge$", r"^sidelocks$", r"^bob_cut$",
    r"^hime_cut$", r"^pixie_cut$", r"^drill_hair$",
    r"^long_hair$", r"^short_hair$", r"^medium_hair$", r"^very_long_hair$",
    # 目
    r"_eyes$", r"^heterochromia$", r"^eyelashes$", r"^pupils$",
    # 口・表情
    r"^smile$", r"^grin$", r"^frown$", r"^smirk$",
    r"^blush", r"^open_mouth$", r"^closed_mouth$",
    r"^fang", r"^tears$", r"^crying$", r"^sweatdrop$",
    r"^tongue", r"^pout$", r"^surprised$", r"^angry$",
    r"^embarrassed$", r"^shy$", r"^sad$", r"^happy$",
    r"^expressionless$", r"^serious$",
    # 体の特徴
    r"breast", r"^slim$", r"^muscular", r"^petite$", r"^chubby$",
    r"^thick_thighs$", r"^wide_hips$", r"^narrow_waist$",
    r"^abs$", r"^navel$", r"^midriff$", r"^cleavage$",
    r"^collarbone$", r"^shoulder",
    # 肌・体
    r"_skin$", r"^skin_", r"^pale$", r"^tan$", r"^dark_skin",
    r"^nail", r"^lip", r"^ear$", r"^ears$", r"^nose$",
    r"^mole", r"^scar", r"^tattoo", r"^freckle",
    # 服装（大カテゴリ）
    r"^dress", r"^shirt", r"^skirt", r"^pants$", r"^shorts$",
    r"^uniform", r"^armor", r"^bikini", r"^swimsuit",
    r"^jacket", r"^coat$", r"^cape$", r"^cloak$",
    r"^hoodie", r"^sweater", r"^vest$", r"^cardigan",
    r"^kimono", r"^yukata$", r"^hanfu$",
    r"^maid", r"^apron", r"^suit$", r"^tuxedo",
    r"^robe$", r"^toga$", r"^gown$",
    r"^crop_top", r"^tank_top", r"^t-shirt",
    r"^blouse", r"^tunic", r"^corset",
    r"^overalls", r"^jumpsuit", r"^bodysuit",
    r"^pajamas", r"^nightgown", r"^lingerie",
    r"^underwear", r"^bra$", r"^panties$",
    r"^leotard", r"^one-piece",
    # 靴・靴下
    r"^gloves$", r"^boots$", r"^shoes$", r"^socks$",
    r"^sandals$", r"^sneakers$", r"^heels$", r"^slippers$",
    r"^stockings$", r"^thighhighs$", r"^pantyhose$",
    r"^kneehighs$", r"^ankle_socks$",
    # アクセサリー
    r"^glasses", r"^sunglasses", r"^goggles",
    r"^earring", r"^necklace", r"^ring$", r"^bracelet",
    r"^choker", r"^collar$", r"^scarf$", r"^tie$", r"^necktie",
    r"^bowtie", r"^ribbon", r"^bow$",
    r"^hat$", r"^cap$", r"^crown$", r"^tiara$", r"^headband",
    r"^hairclip", r"^hair_ornament", r"^hair_ribbon",
    r"^hairband", r"^headpiece", r"^headwear",
    r"^bag$", r"^backpack", r"^purse", r"^handbag",
    r"^umbrella", r"^parasol",
    r"^weapon", r"^sword", r"^gun", r"^staff", r"^wand",
    r"^shield", r"^spear", r"^axe$", r"^knife$", r"^dagger",
    r"^mask$", r"^eyepatch",
    r"^wing", r"^tail$", r"^horn", r"^halo$",
    r"^belt$", r"^buckle", r"^strap",
    r"^sleeve", r"^pocket", r"^zipper", r"^button",
    r"^hood$", r"^hooded",
    # メタタグ
    r"^highres$", r"^absurdres$", r"^masterpiece$",
    r"^best_quality$", r"_quality$",
    r"^rating_", r"^score_",
    r"^realistic$", r"^anime$", r"^manga$",
    r"^official_art$", r"^key_visual$",
    r"^traditional_media$", r"^digital_media$",
    # キャラ名・作品名はスコアで自然に低くなるが念のため
    r"^artist:", r"^character:", r"^copyright:",
]

_compiled_excludes = [re.compile(p) for p in EXCLUDE_PATTERNS]


# ======================================================================
# タグフィルタリング
# ======================================================================

def filter_tags(tags: dict, confidence_threshold: float = 0.35) -> dict:
    """
    WD14 Taggerの出力タグをフィルタリングする。
    シーン/ポーズ/構図/照明のみ残し、人物特徴/服装を除外する。

    Args:
        tags: {タグ名: 信頼度スコア} の辞書
        confidence_threshold: この信頼度以上のタグのみ残す

    Returns:
        フィルタリング済みの {タグ名: 信頼度} 辞書
    """
    filtered = {}
    for tag, score in tags.items():
        if score < confidence_threshold:
            continue

        tag_clean = tag.strip().lower().replace(" ", "_")

        # 許可リストにある → 採用
        if tag_clean in ALL_ALLOWED_TAGS:
            filtered[tag_clean] = score
            continue

        # 除外パターンに一致 → 除外
        excluded = False
        for pattern in _compiled_excludes:
            if pattern.search(tag_clean):
                excluded = True
                break
        if excluded:
            continue

        # どちらにも一致しない → 安全のため除外（保守的アプローチ）
        # キャラクター関連タグが漏れるリスクを避ける

    return filtered


def tags_to_prompt(tags: dict) -> str:
    """タグ辞書をプロンプト文字列に変換（信頼度順）"""
    if not tags:
        return ""
    sorted_tags = sorted(tags.items(), key=lambda x: x[1], reverse=True)
    return ", ".join(tag.replace("_", " ") for tag, _ in sorted_tags)


# ======================================================================
# WD14 Tagger 連携
# ======================================================================

def _find_tagger_module():
    """WD14 Tagger モジュールの検索と読み込み"""
    # 方法1: 直接import（SD WebUI が拡張を読み込み済みの場合）
    try:
        from tagger import interrogator as tagger_mod
        return tagger_mod, None
    except ImportError:
        pass

    # 方法2: extensions ディレクトリを手動検索
    try:
        # SD WebUIのルートを推定
        # EXTENSION_DIR は random-img2img-composer のルート
        # → extensions/ → stable-diffusion-webui/
        ext_root = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        )
        extensions_dir = os.path.join(ext_root, "extensions")

        if os.path.isdir(extensions_dir):
            for dirname in os.listdir(extensions_dir):
                if "tagger" in dirname.lower() or "wd14" in dirname.lower():
                    tagger_path = os.path.join(extensions_dir, dirname)
                    if tagger_path not in sys.path:
                        sys.path.insert(0, tagger_path)
            try:
                from tagger import interrogator as tagger_mod
                return tagger_mod, None
            except ImportError:
                pass
    except Exception:
        pass

    return None, (
        "❌ WD14 Tagger が見つかりません。\n"
        "stable-diffusion-webui-wd14-tagger をインストールしてください:\n"
        "https://github.com/toriato/stable-diffusion-webui-wd14-tagger"
    )


def interrogate_image(pil_image, confidence_threshold: float = 0.35):
    """
    画像をWD14 Taggerで解析し、フィルタ済みタグを返す。

    Returns:
        (filtered_tags: dict, all_tags: dict, error: str or None)
        - filtered_tags: フィルタ済みの {タグ: 信頼度}
        - all_tags: フィルタ前の全タグ {タグ: 信頼度}
        - error: エラーメッセージ（成功時は None）
    """
    tagger_mod, error = _find_tagger_module()
    if tagger_mod is None:
        return {}, {}, error

    try:
        # インタロゲーターの取得
        interrogator_obj = None

        # パターン1: Interrogator クラスから取得
        if hasattr(tagger_mod, "Interrogator"):
            cls = tagger_mod.Interrogator
            # 利用可能なインタロゲーター一覧
            if hasattr(cls, "get_interrogators"):
                interrogators = cls.get_interrogators()
                if isinstance(interrogators, dict) and interrogators:
                    interrogator_obj = list(interrogators.values())[0]
            elif hasattr(cls, "interrogators"):
                interrogators = cls.interrogators
                if isinstance(interrogators, dict) and interrogators:
                    interrogator_obj = list(interrogators.values())[0]

        # パターン2: モジュールレベルの関数
        if interrogator_obj is None and hasattr(tagger_mod, "interrogate"):
            result = tagger_mod.interrogate(pil_image)
            if isinstance(result, tuple) and len(result) >= 2:
                all_tags = result[1] if isinstance(result[1], dict) else {}
            elif isinstance(result, dict):
                all_tags = result
            else:
                return {}, {}, "❌ 予期しないタグ形式です"
            filtered = filter_tags(all_tags, confidence_threshold)
            return filtered, all_tags, None

        if interrogator_obj is None:
            return {}, {}, "❌ 対応するインタロゲーターが見つかりません"

        # モデル読み込み
        if hasattr(interrogator_obj, "load"):
            interrogator_obj.load()

        # 解析実行
        result = interrogator_obj.interrogate(pil_image)

        if isinstance(result, tuple) and len(result) >= 2:
            all_tags = result[1] if isinstance(result[1], dict) else {}
        elif isinstance(result, dict):
            all_tags = result
        else:
            return {}, {}, "❌ 予期しないタグ形式です"

        filtered = filter_tags(all_tags, confidence_threshold)
        return filtered, all_tags, None

    except Exception as e:
        return {}, {}, f"❌ タグ取得エラー: {e}"


def generate_memo_entry(
    section_name: str,
    pil_image,
    confidence_threshold: float = 0.35,
    negative_prompt: str = "lowres, blurry, artifact, bad anatomy, worst quality, low quality, jpeg artifacts",
) -> tuple:
    """
    画像を解析してメモファイル用のエントリを生成する。

    Returns:
        (memo_entry: str, log: str)
    """
    log_lines = []

    filtered, all_tags, error = interrogate_image(pil_image, confidence_threshold)

    if error:
        return "", error

    log_lines.append(f"📊 全タグ数: {len(all_tags)}")
    log_lines.append(f"✅ フィルタ後: {len(filtered)}")

    if not filtered:
        log_lines.append("⚠️ シーン/構図/ポーズのタグが見つかりませんでした")
        # タグがない場合でもセクションは作る
        entry = f"[{section_name}]\npositive:\n\n\nnegative:\n{negative_prompt}\n"
        return entry, "\n".join(log_lines)

    positive = tags_to_prompt(filtered)
    log_lines.append(f"📝 Positive: {positive}")
    log_lines.append(f"🚫 Negative: {negative_prompt}")

    # 除外されたタグも表示（参考用）
    excluded_count = len(all_tags) - len(filtered)
    if excluded_count > 0:
        log_lines.append(f"🗑️ 除外タグ数: {excluded_count}")

    entry = (
        f"[{section_name}]\n"
        f"positive:\n"
        f"{positive}\n"
        f"\n"
        f"negative:\n"
        f"{negative_prompt}\n"
    )

    return entry, "\n".join(log_lines)
