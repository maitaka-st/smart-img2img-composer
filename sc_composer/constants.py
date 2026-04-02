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
    "active_profile": "Standard / SDXL",
    "auto_filename": False,
    "fallback_enabled": True,
    "auto_lora_enabled": True,
    "output_sort_mode": "None",
    "inventory_mode": False,
    "smart_negative": False,
    "smart_negative_mode": "append",
    "lora_offset": 0.0,
    "last_sequential_index": 0,
    
    # Tagger / Generator settings
    "gen_conf_base": 0.35,
    "gen_conf_char": 0.35,
    "gen_conf_nsfw": 0.35,
    "gen_conf_total": 0.35,
    "use_global_conf": True,
    "gen_positive": "(masterpiece:1.1), (best quality:1.0), ",
    "gen_negative": "lowres, blurry, artifact, bad anatomy, worst quality, low quality, jpeg artifacts",
    "gen_custom_dict": (
        "night, city > cyberpunk cityscape, neon lights, cinematic lighting, rain reflections, highly detailed\n"
        "sunset, skyline > golden hour lighting, dramatic sky colors, atmospheric perspective\n"
        "indoor, room > detailed background, interior design"
    ),
    "gen_custom_dict_enabled": False,
    "wildcard_1_path": WILD_1_PATH,
    "wildcard_2_path": WILD_2_PATH,
    "wildcard_3_path": WILD_3_PATH,
    "presets": {},
    "gen_categories": None,
    "custom_base_tags": "masterpiece, best quality, 1girl, solo",
    "auto_optimize_prompt": False,
    "prompt_polish": False,
    "gen_mosaic_auto": False,
    "gen_mosaic_level": "Mosaic Med",
    "limit_base": 10,
    "limit_char": 10,
    "limit_nsfw": 15,
    "debug": False,
}

IMAGE_EXTENSIONS = [".png", ".jpg", ".jpeg", ".webp", ".bmp", ".gif"]

# ▼ 詳細なタグ定義 (v1.2.4 参照URL反映版)
_TAG_CATEGORIES = {
    # ── ベース系 ────────────────────────────────────────────────
    "cat_composition": [
        # 正規表現
        "re:.*_view", "re:.*_shot", "re:.*_perspective", "re:.*_angle",

        # アングル・フレーミング
        "portrait", "upper_body", "lower_body", "full_body", "wide_shot",
        "from_above", "from_below", "from_side", "from_behind",
        "cowboy_shot", "close-up", "closeup", "extreme_close-up",
        "dutch_angle", "dynamic_angle", "bird's_eye_view", "worm's_eye_view",
        "fisheye", "panorama", "three-quarter_view",

        # POV・主観
        "pov", "pov_hands", "over_shoulder", "selfie", "profile",

        # カット種別（11_アングル.yml）
        "headshot", "bust_shot", "knee_up", "waist_up",
        "face_focus",

        # 方向（11_アングル.yml / 24_体位.yml）
        "straight-on", "sideways", "overhead_shot", "upside-down",
        "shoot_from_above", "shoot_from_below",
        "looking_at_viewer", "looking_away", "looking_up", "looking_down",
        "looking_back", "looking_to_the_side",

        # 構図スタイル
        "symmetry", "isometric", "negative_space", "multiple_views",
        "split_view", "zoom_layer", "tachi-e", "lineup",

        # 遠近
        "perspective", "atmospheric_perspective", "depth_of_field",
        "blurry_background", "vanishing_point",
    ],
    "cat_pose": [
        # 正規表現
        "re:.*_standing", "re:.*_sitting", "re:.*_lying", "re:.*_leaning",
        "re:.*_kneeling", "re:.*_pose",

        # 立ち・基本動作
        "standing", "sitting", "lying", "kneeling", "crouching", "squatting",
        "walking", "running", "jumping", "dancing", "stretching", "bending",
        "floating", "falling", "flying",

        # 体勢（24_体位.yml 体勢_基本）
        "on_back", "on_stomach", "on_side", "arched_back", "bent_over",
        "reclining", "leaning_back", "leaning_forward",
        "spread_legs_squatting", "yokozuwari", "knees_apart",
        "pushed_down",

        # 足・柔軟（24_体位.yml 体勢_足_柔軟）
        "legs_over_head", "leg_lift", "leg_up", "legs_up",
        "split", "standing_split", "spread_legs", "flexible",
        "firmly_toes_straight", "bowlegged_pose",
        "jack-o'_challenge",

        # 特殊体勢（24_体位.yml 体勢_特殊）
        "head_back", "pole_dancing", "against_glass",
        "upside_down", "top-down_bottom-up", "glory_wall",
        "through_wall", "stuck",

        # 手・腕（11_アングル.yml ポーズ）
        "arm_up", "arms_up", "arms_behind_back", "arms_behind_head",
        "hand_on_hip", "hand_on_own_chest", "hand_to_mouth", "hand_on_own_face",
        "hands_up", "reaching_out", "outstretched_arms", "crossed_arms",
        "v_arms", "hands_clasped", "hands_in_pockets", "hand_up",
        "finger_to_mouth", "index_finger_raised", "pointing",
        "peace_sign", "thumbs_up", "salute", "waving",
        "clenched_fist", "claw_pose", "paw_pose",

        # 脚
        "crossed_legs", "bent_knees", "on_one_knee", "tiptoes",
        "feet_together", "legs_apart", "wariza", "lotus_position",

        # 全身ポーズ
        "all_fours", "fetal_position",
        "lying_on_back", "lying_on_stomach", "lying_on_side",
        "contrapposto", "own_hands_together",

        # 髪・小物への接触（11_アングル.yml）
        "adjusting_headwear",

        # 一本腕ポーズ（ポーズ.yml）
        "leaning_on_one_arm",

        # ジェスチャー追加（11_アングル.yml / ポーズ.yml）
        "finger_pointing", "put_index_finger_on_mouth",
        "elbows_on_table", "hands_together",
        "ojou-sama_pose", "ghost_pose", "rabbit_pose", "fox_shadow_puppet",
        "hat_tip", "skirt_lift_gesture",

        # 体勢追加（24_体位.yml）
        "facing_partner", "arm_support", "yoga",
        "own_hugging_feet", "crossed_leg",
        "head_tilt", "shaking_head", "stroking_own_chin", "facepalm",
        "covering_own_eye", "feel_horny_face",

        # 盗撮・露出シチュ向けポーズ（青姦/露出プレイ参照）
        "presenting", "presenting_self", "upskirt_pose",
        "nude_outdoors", "naked_outdoors",
    ],
    "cat_background": [
        # 屋内・居住空間
        "indoors", "indoor", "room", "bedroom", "living_room", "dining_room",
        "kitchen", "bathroom", "toilet", "shower", "sauna", "bathtub",
        "apartment", "balcony", "veranda", "porch", "entryway", "hallway",
        "corridor", "staircase", "elevator", "attic", "basement", "closet",
        "laundry_room", "dormitory",

        # 室内詳細・表面
        "wood_floor", "flooring", "carpet", "rug", "tatami", "tile_floor",
        "marble_floor", "concrete_floor", "mats", "yoga_mat",
        "on_bed", "on_sheets", "on_couch", "on_sofa", "on_chair",
        "on_table", "on_desk", "under_table", "under_desk",
        "against_wall", "window_sill",

        # 学校・施設
        "school", "classroom", "school_hallway", "science_room", "laboratory",
        "library", "gym", "infirmary", "science_lab", "music_room", "clubroom",
        "student_council_room", "teachers'_desk", "auditorium", "school_rooftop",
        "locker_room", "changing_room", "cafeteria", "sports_field", "track",

        # 都市・公共空間
        "outdoors", "outdoor", "cityscape", "city", "town", "village", "suburb",
        "street", "alley", "alleyway", "sidewalk", "road", "crosswalk", "bridge",
        "park", "garden", "playground", "fountain", "bench", "bus_stop",
        "train_station", "subway_station", "airport", "harbor", "port", "dock",
        "parking_lot", "gas_station", "construction_site", "industrial_area",
        "factory", "warehouse", "office", "bank", "post_office", "hospital",
        "clinic", "pharmacy", "store", "supermarket", "convenience_store",
        "shopping_mall", "department_store", "market", "marketplace",
        "cafe", "restaurant", "fast_food_restaurant", "bar", "pub", "tavern",
        "izakaya", "cinema", "theater", "museum", "art_gallery", "aquarium",
        "zoo", "amusement_park", "theme_park", "fairground", "arena", "stadium",

        # 乗り物
        "car_interior", "bus_interior", "train_interior", "subway_interior",
        "airplane_interior", "ship_cabin", "car", "bus", "train", "airplane",

        # 自然・景観
        "forest", "jungle", "woods", "grove", "bamboo_forest",
        "mountain", "valley", "canyon", "cliff", "cave", "cavern", "tomb",
        "glacier", "ice_cave", "volcano", "desert", "oasis", "sand_dune",
        "field", "meadow", "grassland", "savanna", "swamp", "marsh",
        "wetland", "flower_field", "sunflower_field", "wheat_field",
        "farm", "orchard", "vineyard",
        "waterfall", "river", "stream", "lake", "pond", "spring",
        "ocean", "sea", "beach", "seaside", "shore", "island", "pier",

        # 建築・歴史・ファンタジー
        "castle", "palace", "throne_room", "manor", "mansion", "estate",
        "ruins", "abandoned", "temple", "shrine", "church", "cathedral",
        "inn", "dungeon", "prison_cell", "colosseum",
        "steampunk_city", "cyberpunk_city", "fantasy_world",

        # 特殊背景
        "simple_background", "white_background", "black_background",
        "gradient_background", "bokeh_background",
        "abstract_background", "starry_sky", "night_sky", "sunset_sky",
        "blue_sky", "cloudy_sky",

        # 青姦・露出シチュ向け背景（参照URL: 青姦/露出プレイ）
        "public_place", "crowded_place", "open_air", "rooftop",
        "back_alley", "park_at_night", "forest_clearing",
        "hidden_spot", "secluded_area",
    ],
    "cat_nature": [
        # 正規表現
        "re:sky", "re:cloud", "re:sun", "re:rain", "re:snow", "re:wind",
        "re:.*_petals", "re:.*_leaves",

        # 天候・時間帯
        "sunny", "cloudy", "rainy", "snowy", "foggy", "stormy", "windy",
        "clear_sky", "overcast", "thunder", "lightning", "aurora",
        "sunrise", "sunset", "golden_hour", "dusk", "dawn", "night", "noon",

        # 植物
        "flower", "tree", "grass", "cherry_blossoms", "autumn_leaves",
        "rose", "sunflower", "leaves", "vines", "moss", "bamboo",

        # 自然要素
        "sand", "rock", "ice",

        # 季節的
        "summer", "autumn", "winter",
    ],
    "cat_lighting": [
        # 正規表現
        "re:.*_lighting", "re:.*_light", "re:.*_shadow",

        # 光源種別
        "sunlight", "moonlight", "candlelight", "firelight", "starlight",
        "neon_lights", "fluorescent_light", "streetlight",

        # ライティング手法
        "backlighting", "rim_lighting", "soft_lighting", "hard_lighting",
        "cinematic_lighting", "dramatic_lighting", "dynamic_lighting",
        "volumetric_lighting", "god_rays", "caustics",
        "warm_lighting", "cool_lighting", "natural_lighting", "studio_lighting",

        # 光の効果
        "lens_flare", "glowing", "bloom", "sparkle", "shiny",
        "dappled_light", "light_particles", "light_rays",
        "spotlight", "shadow", "silhouette", "dark", "bright",
    ],
    "cat_atmosphere": [
        # 雰囲気・ムード
        "moody", "calm", "vibrant", "colorful", "monochrome", "sepia",
        "light", "dreamy", "ethereal", "surreal",
        "gritty", "eerie", "mysterious", "romantic", "melancholic",
        "whimsical", "serene", "tense", "peaceful", "chaotic",

        # 視覚スタイル
        "bokeh", "motion_blur", "chromatic_aberration",
        "film_grain", "vignette", "lens_distortion",

        # 色調
        "warm_colors", "cool_colors", "pastel_colors", "saturated",
        "desaturated", "high_contrast", "low_contrast", "vibrant_colors",
    ],
    "cat_meta": [
        # 品質タグ（00_お気に入り.yml 優先）
        "masterpiece", "best_quality", "highres", "absurdres", "ultra-detailed",
        "highly_detailed", "extremely_detailed", "intricate_details",
        "sharp_focus", "high_quality", "quality",
        "highresolution", "bestquality", "perfect_eye",
        "animescreencap", "anime_coloring", "official_art",

        # スコア系（Pony/Illustrious）
        "score_9", "score_8_up", "score_7_up", "score_6_up",
        "rating_safe", "rating_questionable", "rating_explicit",
        "source_anime", "source_manga",

        # 人数
        "solo", "duo", "trio",
        "1girl", "2girls", "2boys", "3girls", "3boys",
        "multiple_girls", "multiple_boys", "group",

        # 特殊演出（お気に入り.yml）
        "onomatopoeia", "heartmark",
    ],
    # ── キャラ系 ────────────────────────────────────────────────
    "cat_char_base": [
        # 正規表現
        "re:.*_skin", "re:.*_body", "re:.*_breasts", "re:.*_build",

        # 体型（20_人物.yml）
        "slim", "slender", "petite", "short_stature", "tall", "athletic",
        "curvy", "muscular", "chubby", "plump", "thicc",
        "lean_body", "svelte_body", "curvy_body", "narrow_waist",
        "model-like_body", "normal_build", "medium_build",

        # 胸（20_人物.yml + お気に入り.yml）
        "flat_chest", "small_breasts", "medium_breasts", "large_breasts",
        "huge_breasts", "gigantic_breasts", "perky_breasts", "saggy_breasts",
        "pointy_breasts", "sagging_breasts", "bouncing_breasts",
        "cleavage", "underboob", "sideboob", "backboob",

        # 肌（20_人物.yml）
        "pale_skin", "fair_skin", "tan_skin", "dark_skin", "brown_skin",
        "tanned", "light_skin", "olive_skin", "shiny_skin",
        "tanlines", "body_blush", "tattoo", "oil",

        # 年齢感
        "young", "mature", "adult", "aged", "baby_face",

        # 体の特徴（20_人物.yml）
        "abs", "toned", "pregnant", "large_ass", "wide_hips",
        "long_legs", "thick_thighs", "thigh_gap",
        "collarbone", "navel", "armpits", "groin", "groin_tendon",
        "pubic_hair", "sparse_pubic_hair",

        # 耳・尻尾（亜人）
        "cat_ears", "dog_ears", "fox_ears", "bunny_ears", "elf_ears",
        "animal_ears", "tail", "cat_tail", "fox_tail", "wolf_ears",
        "horns", "wings", "halo", "demon_horns", "dragon_wings",
        "bat_wings", "butterfly_wings",

        # 属性・キャラタイプ（20_人物.yml）
        "tsundere", "kuudere", "ojousama", "delinquent", "idol",
        "magical_girl", "mesugaki",

        # 肌質・体表追加
        "oiled_skin", "oiled_body", "glistening",
        "sweaty_body", "sunburned", "flushed_skin",
        "glowing_skin", "wet_skin", "glossy_skin",

        # 体型追加
        "hourglass_figure", "pear_shaped", "apple_shaped",
        "lithe", "willowy", "stocky", "buxom",

        # 年齢表現追加
        "kogal", "gal",
        "lolibaba", "christmas_cake",
        "yuri", "futa_with_female", "boy_on_top", "onee-loli",
    ],
    "cat_char_hair": [
        # 正規表現
        "re:.*_hair", "re:.*_bangs", "re:.*_bun", "re:.*_braid",

        # 長さ（21_髪.yml）
        "short_hair", "medium_hair", "long_hair", "very_long_hair",
        "absurdly_long_hair", "shoulder-length_hair", "chin-length_hair",
        "pixie_cut", "very_short_hair", "bob_cut",

        # 質感・地毛（21_髪.yml）
        "wavy_hair", "curly_hair", "straight_hair", "messy_hair",
        "drill_hair", "twin_drills", "ringlets", "dreadlocks", "cornrows",

        # テール系（21_髪.yml）
        "ponytail", "high_ponytail", "low_ponytail", "side_ponytail",
        "front_ponytail", "split_ponytail", "folded_ponytail", "short_ponytail",
        "braided_ponytail", "twintails", "high_twin_tails", "low_twintails",
        "side_twin_tails", "short_twintails", "pigtails", "tri_tails",

        # お団子系（21_髪.yml）
        "hair_bun", "bun", "double_bun", "high_bun", "low_bun", "side_bun",
        "braided_bun", "hair_rings", "topknot", "odango",
        "messy_bun", "bow-shaped_hair",

        # 編み込み（21_髪.yml）
        "braid", "french_braid", "crown_braid",
        "single_braid", "twin_braids", "tri_braids", "multiple_braids",

        # ハーフアップ（21_髪.yml）
        "half_updo", "two_side_up", "one_side_up",

        # 前髪（21_髪.yml）
        "bangs", "blunt_bangs", "hime_cut", "diagonal_bangs", "arched_bangs",
        "asymmetrical_bangs", "crossed_bangs", "long_bangs", "short_bangs",
        "choppy_bangs", "parted_bangs", "swept_bangs", "bangs_pinned_back",
        "side_bangs", "no_bangs",
        "hair_over_one_eye", "hair_over_eyes", "hair_between_eyes",

        # メカクレ関連
        "hair_intakes", "sidelocks", "hair_flaps",

        # アホ毛・特殊（21_髪.yml）
        "ahoge", "dyed_ahoge", "heart_ahoge", "antenna_hair",
        "swept_back", "slicked_back", "spiky_hair",
        "flipped_hair", "layered_hair",

        # 色補完
        "silver_hair", "white_hair", "grey_hair", "platinum_blonde_hair",
        "multicolored_hair", "gradient_hair", "streaked_hair",
        "two-tone_hair", "dyed_hair", "ombre_hair", "colored_inner_hair",
        "split-color_hair",

        # アクセ
        "hair_ribbon", "hair_bow", "hair_ornament", "hair_flower",
        "hair_clip", "hair_tie", "hair_band", "headband", "hairpin",

        # 21_髪.yml 追加分
        "quad_tails",
        "multi-tied_hair",
        "quad_braids",
        "half_up_braid",
        "double_parted_bangs",
        "hair_slicked_back", "hair_pulled_back",
        "hair_over_both_eyes",
        "ahoge_wag",
        # (追加タグ)
        "adjusting_hair", "hair_behind_ear", "playing_with_own_hair", "tucking_hair", "hands_in_hair", "twirling_hair",
    ],
    "cat_char_eyes": [
        # 正規表現
        "re:.*_eyes",

        # 色
        "blue_eyes", "red_eyes", "green_eyes", "yellow_eyes",
        "brown_eyes", "purple_eyes", "pink_eyes", "orange_eyes",
        "aqua_eyes", "grey_eyes", "silver_eyes", "gold_eyes",
        "amber_eyes", "teal_eyes", "heterochromia",

        # 目の形・特徴
        "tsurime", "tareme", "sanpaku_eyes", "wide_eyes", "narrow_eyes",
        "half-closed_eyes", "half_closed_eyes", "hooded_eyes",
        "upturned_eyes", "downturned_eyes",
        "glowing_eyes", "slit_pupils", "heart_eyes", "star_eyes",
        "spiral_eyes", "empty_eyes", "blank_eyes", "reflective_eyes",

        # 目の状態
        "wink", "closed_eyes", "one_eye_closed", "tears", "teary_eyes",
        "watery_eyes", "sparkling_eyes", "shiny_eyes", "moist_eyes",
        "eye_contact",
    ],
    "cat_char_face": [
        # 正規表現
        "re:.*_smile",
        "smile", "grin", "smirk", "evil_smile", "evil_grin",
        "seductive_smile", "angelic_smile", "smug", "smug_face",
        "excited", "rapturous",

        # 怒り・不満（23_表情.yml）
        "angry", "annoyed", "frustrated", "pout", "pouting", "sulking",
        "glaring", "frown", "v-shaped_eyebrows", "clenched_teeth",
        "disdain", "disgust", "anger_vein",

        # 悲しみ・泣く（23_表情.yml）
        "sad", "crying", "sad_smile", "disappointed", "depressed",

        # 驚き・恐怖・困惑（23_表情.yml）
        "scared", "confused", "surprised", "screaming",
        "troubled", "dumbfounded", "wide-eyed",

        # 照れ・羞恥（23_表情.yml）
        "blush", "heavy_blush", "full-face_blush", "embarrassed",
        "sweatdrop", "nose_blush", "blush_stickers", "flustered",

        # 無表情・冷静（23_表情.yml）
        "expressionless", "serious", "bored", "sleepy", "exhausted",
        "jitome", "narrowed_eyes", "kubrick_stare",

        # 誘惑・恍惚（23_表情.yml）
        "naughty_face", "incoming_kiss",

        # 口元
        "open_mouth", "closed_mouth", "parted_lips", "biting_lip",
        "tongue_out", "licking_lips", "teeth", "saliva", "drool",
        "hand_over_mouth", "wavy_mouth",

        # 笑い
        "laughing", "giggling", "crying_with_eyes_open",

        # 顔の特徴
        "freckles", "mole", "beauty_mark", "scar", "dimples",
        "rosy_cheeks", "makeup", "eyelashes", "thick_eyebrows",
        "thin_eyebrows", "troubled_eyebrows", "raised_eyebrows",

        # 口のパーツ（23_表情.yml）
        "long_tongue", "buck_teeth", "fang",
        "panting",

        # 23_表情.yml 追加分
        "innocent_smile", "teasing_smile", "forced_smile",
        "envy", "downturned_mouth",
        "guilt",
        "determined", "sigh",
        "solid_circle_eyes",
        "chestnut_mouth",
        "one_eye_covered", "duck_face", "dark_persona", "tehepero",
        "upper_teeth", "round_teeth",

        # 顔パーツ追加（20_人物.yml）
        "round_face", "slender_face", "small_face", "chubby_face",
        "sharp_features", "high_cheekbones", "narrow_chin",
        "light_eyebrows", "dark_eyebrows",
        "straight_eyebrows", "natural_eyebrows", "angled_eyebrows",
        "arched_eyebrows", "groomed_eyebrows", "bushy_eyebrows",
        "sparse_eyebrows", "wide-set_eyebrows", "lowered_eyebrows",
    ],
    "cat_char_clothes": [
        # 正規表現
        "re:.*_wear", "re:.*_outfit", "re:.*_dress", "re:.*_uniform",
        "re:.*_costume", "re:.*_clothes", "re:.*_skirt", "re:.*_bra",
        "re:.*_panties", "re:.*_pantyhose", "re:.*_legwear",

        # ── ファッションスタイル（30_服装.yml / お気に入り服装.yml 優先） ──
        "lolita_fashion", "gothic_lolita", "sweet_lolita", "classic_lolita",
        "qi_lolita", "wa_lolita", "jirai_kei", "yami_kawaii", "yume_kawaii",
        "gyaru", "cybergoth", "techwear", "steampunk", "punk",
        "bodycon", "harajuku_fashion",

        # ── アウター（30_服装.yml） ──
        "jacket", "blazer", "suit_jacket", "letterman_jacket", "sukajan",
        "coat", "trench_coat", "peacoat", "long_coat", "fur_coat",
        "fur-trimmed_coat", "duffel_coat", "raincoat",
        "hoodie", "cardigan", "sweater", "turtleneck_sweater", "sweater_vest",
        "open_robe", "bathrobe", "robe", "cape", "capelet", "shawl",
        "poncho", "haori", "happi",

        # ── トップス（30_服装.yml） ──
        "shirt", "t-shirt", "collared_shirt", "dress_shirt", "blouse",
        "crop_top", "tank_top", "tube_top", "camisole", "halterneck",
        "off-shoulder", "off_shoulder_shirt", "bare_shoulders",
        "taut_shirt", "frilled_shirt", "tunic", "waistcoat", "vest",
        "corset", "underbust",

        # ── ボトムス（30_服装.yml） ──
        "skirt", "miniskirt", "pleated_skirt", "high-waist_skirt",
        "long_skirt", "bubble_skirt", "overskirt", "suspender_skirt",
        "pants", "jeans", "leggings", "yoga_pants", "sweatpants",
        "shorts", "denim_shorts", "bike_shorts", "dolphin_shorts",
        "hot_pants", "micro_shorts", "buruma", "bloomers",

        # ── ワンピース・ドレス（30_服装.yml 全カラー・全スタイル） ──
        "dress", "short_dress", "long_dress", "sundress", "casual_dress",
        "wedding_dress", "evening_gown", "cocktail_dress", "formal_dress",
        "maid_dress", "sailor_dress", "pinafore_dress", "nightgown",
        "negligee", "babydoll",
        "white_dress", "black_dress", "red_dress", "blue_dress",
        "pink_dress", "purple_dress", "green_dress", "yellow_dress",
        "striped_dress", "plaid_dress", "polka_dot_dress", "frilled_dress",
        "lace-trimmed_dress", "see-through_dress",
        "strapless_dress", "off-shoulder_dress", "backless_dress",
        "side_slit", "high-low_skirt",

        # ── 和装（30_服装.yml / お気に入り服装.yml） ──
        "kimono", "short_kimono", "furisode", "yukata", "hakama",
        "hakama_short_skirt", "hakama_skirt", "uchikake", "obi",
        "miko", "priestess", "see-through_kimono",

        # ── 東アジア民族衣装 ──
        "china_dress", "cheongsam", "hanfu", "hanbok", "tangzhuang",
        "ao_dai", "longpao",

        # ── 制服・職業服（30_服装.yml / お気に入り服装.yml） ──
        "serafuku", "school_uniform", "sailor_uniform", "gym_uniform",
        "meiji_schoolgirl_uniform", "band_uniform", "track_suit",
        "bunny_suit", "reverse_bunnysuit", "leotard", "bodysuit",
        "maid", "maid_outfit", "waitress", "secretary", "nurse",
        "nun", "cassock", "kunoichi", "ninja",
        "cheerleader", "idol_costume", "bellydancer",
        "school_swimsuit", "competition_swimsuit",
        "racing_suit", "jumpsuit", "hazmat_suit", "space_suit",

        # ── 水着・ランジェリー（お気に入り服装.yml / 31_服装下着.yml 優先） ──
        "swimsuit", "bikini", "micro_bikini", "one-piece_swimsuit",
        "slingshot_swimsuit",
        "lingerie", "bra", "panties", "underwear",
        "bustier", "chemise", "sarashi",
        "thong", "string_panties", "loincloth", "fundoshi",
        "garter_belt", "naked_apron",
        "bridal_lingerie", "crotchless_panties",

        # ブラバリエーション（31_服装下着.yml）
        "sports_bra", "strapless_bra", "front-hook_bra", "cupless_bra",
        "shelf_bra", "bra_pull", "torn_bra",

        # パンティバリエーション（31_服装下着.yml）
        "blue_panties", "red_panties", "black_panties", "white_panties",
        "pink_panties", "frilled_panties", "lace_panties", "highleg_panties",
        "lowleg_panties", "polka_dot_panties",

        # ── レッグウェア（30_服装.yml / 35_パンスト.yml） ──
        "thighhighs", "over-kneehighs", "kneehighs", "pantyhose",
        "socks", "loose_socks", "ankle_socks", "bobby_socks",
        "fishnet_stockings", "fishnet_thighhighs",

        # パンスト色（35_パンスト.yml）
        "black_pantyhose", "white_pantyhose", "grey_pantyhose",
        "pink_pantyhose", "blue_pantyhose", "brown_pantyhose",

        # パンストデザイン（35_パンスト.yml）
        "striped_pantyhose", "polka_dot_legwear", "lace_legwear",
        "see-through_legwear", "thighband_pantyhose", "torn_pantyhose",
        "pantyhose_under_shorts", "socks_over_pantyhose",

        # ── 靴（30_服装.yml） ──
        "boots", "thigh_boots", "knee_boots", "high_heel_boots",
        "ankle_boots", "lace-up_boots", "rubber_boots",
        "high_heels", "pumps", "wedge_heels", "sandals", "flip-flops",
        "sneakers", "loafers", "dress_shoes", "slippers", "uwabaki",
        "geta", "zouri", "tabi", "mary_janes", "platform_footwear",
        "barefoot",

        # ── 帽子・頭部アクセ ──
        "hat", "cap", "beret", "witch_hat", "tiara", "crown", "veil", "hood",

        # ── アクセサリー ──
        "ribbon", "bow", "bowtie", "tie", "choker", "necklace",
        "earrings", "bracelet", "ring", "belt", "suspenders",
        "gloves", "long_gloves", "fingerless_gloves", "paw_gloves",
        "apron", "scarf", "arm_warmers", "detached_sleeves",
        "glasses", "sunglasses",

        # ── 透け・露出・状態（お気に入り.yml / 30_服装.yml） ──
        "see-through", "see-through_clothes", "see-through_shirt",
        "see-through_skirt", "see-through_bra", "see-through_panties",
        "revealing_clothes", "clothes_lift",
        "clothes_pull",
        "torn_underwear",
        "bodypaint", "latex", "fishnets",
        "oversized_clothes", "baggy_clothes", "loose_clothes",
        "short_sleeves", "long_sleeves", "sleeves_past_fingers",

        # 31_服装下着.yml 追加分
        "adhesive_bra", "belt_bra", "bow_bra", "bridgeless_bra",
        "front-tie_bra", "lace_bra", "training_bra",
        "adjusting_bra", "bra_on_head", "bra_strap", "holding_bra",
        "camisole_lift", "camisole_pull", "frilled_camisole", "lace-trimmed_camisole",
        "see-through_camisole",
        "c-string", "strapless_bottom", "backless_panties",
        "rabbit_panties", "side-tie_panties", "strawberry_panties",
        "cat_panties", "checkered_panties",
        "micro_panties", "latex_panties", "bear_panties",

        # 35_パンスト.yml 追加分
        "orange_pantyhose", "yellow_pantyhose", "green_pantyhose",
        "purple_pantyhose", "red_pantyhose",
        "argyle_legwear", "lowleg_pantyhose",
        "polka_dot_legwear_pantyhose", "vertical-striped_pantyhose",
        "back-seamed_legwear", "front-seamed_legwear",
        "seamed_legwear", "side-seamed_legwear",
        "adjusting_legwear", "panties_under_pantyhose", "panties_over_pantyhose",
        "pantyhose_around_one_leg", "pantyhose_on_head", "pantyhose_pull",
        "pantyhose_under_swimsuit",
        "unworn_pantyhose", "thighhighs_over_pantyhose",

        # お気に入り服装.yml 追加分
        "denim_dress",
        "mizu_happi",
        "pinstripe_dress", "santa_dress",
        "pelvic_curtain", "clothing_cutout",

        # パンティーアクション（24_体位.yml）
        "pantyshot", "holding_panties",
        "licking_panties", "panty_lift", "smelling_underwear",
        "loose_panties", "trefoil", "wedgie",
        "panties_around_tail", "panties_on_breasts",
        "penis_in_panties", "panties_on_penis",
        "nipple_cutout", "paw_shoes",
    ],
    "cat_char_male": [
        # 正規表現
        "re:.*_male",

        # 基本
        "1boy", "male_focus", "male", "man", "guy", "boy",

        # 体型
        "muscular_male", "slim_male", "tall_male",
        "pectorals", "broad_shoulders",

        # 顔の特徴
        "beard", "stubble", "mustache", "short_beard", "goatee",
        "eyepatch",

        # 髪型（男性的なもの）
        "undercut",
        "suit", "business_suit", "tuxedo", "shirtless", "topless_male", "open_shirt",
        "butler", "butler_outfit", "butler_suit",

        # 属性
        "ikemen", "bishounen",
    ],
    # ── NSFW系 ────────────────────────────────────────────────
    "cat_nsfw_action": [
        "re:.*_sex", "re:.*_position", "re:.*_fucking",

        # 基本体位（24_体位.yml 体位_基本）
        "sex", "missionary", "doggy_style", "prone_bone",
        "cowgirl_position", "reverse_cowgirl_position",
        "upright_straddle", "reverse_upright_straddle",
        "spooning", "girl_on_top",
        "suspended_congress", "reverse_suspended_congress",
        "full_nelson", "69_position",
        "piledriver_sex", "amazon_position",
        "standing_sex", "standing_split_sex", "anvil_position",
        "cooperative_paizuri", "straddling_paizuri",
        "human_stacking",

        # 行為・愛撫（24_体位.yml）
        "cunnilingus", "fellatio", "blowjob", "irrumatio", "deep_throat",
        "oral_sex", "handjob", "footjob", "paizuri",
        "fingering", "mutual_fingering", "masturbation",
        "breast_sucking", "self_breast_sucking",
        "tribadism", "symmetrical_docking", "grinding",
        "groping", "torso_grab",

        # 自慰（24_体位.yml）
        "female_masturbation", "male_masturbation", "clothed_masturbation",
        "mutual_masturbation", "stealth_masturbation",
        "crotch_rub", "table_humping",

        # 挿入・性行為
        "penetration", "vaginal", "anal", "group_sex",
        "gangbang", "threesome", "orgy",
        "public_sex", "outdoor_sex",
        "spanking", "flogging", "impact_play",
        "pegging", "frotting", "scissoring",

        # 24_体位.yml 追加分
        "take_your_pick",
        "tail_masturbation", "building_sex",
        "teddy_bear_sex", "pillow_sex", "g-spot_masturbation",
        "handjob_over_clothes", "fingering_through_clothes",
        "hand_in_anothers_panties",
        "breast_grab", "breast_squeeze", "breast_press", "clitoral_stimulation",

        # 挿入・性行為詳細追加
        "rape", "non-consensual", "forced_sex",
        "double_penetration", "triple_penetration",
        "airtight", "spitroast",
        "intercrural_sex", "intercrural",
        "pullout",
        "multiple_penetration", "cervical_penetration",
        "object_insertion", "toy_insertion",

        # 口腔行為追加（イマラチオ/フェラチオ参照）
        "kissing", "french_kiss", "neck_kiss",
        "licking", "sucking", "throat_fuck",
        "anilingus", "rimjob",
        "mouth_full_of_cum",
        "tongue_out_blowjob", "eye_contact_blowjob",

        # 胸追加（パイズリ参照）
        "titfuck", "underboobjob",
        "breast_between_penis",

        # 足追加（足コキ参照）
        "leg_lock", "ankles_together",
        "foot_on_penis", "feet_on_penis",
        "sole_on_penis", "toe_licking",

        # 手コキ追加（参照URL）
        "two-handed_handjob", "handjob_under_skirt",
        "prostate_massage",

        # 耳舐め・首責め（参照URL）
        "ear_licking", "ear_bite", "neck_licking", "neck_bite",

        # 乳首責め（参照URL）
        "nipple_tweak", "nipple_bite", "nipple_suck",
        "double_nipple_licking", "nipple_pinch",

        # クリ責め（参照URL）
        "clitoris_licking", "clitoris_sucking",
        "clitoris_pinch", "clitoris_bite",

        # 和姦（参照URL: 和姦）
        "consensual_sex", "lovers_sex", "gentle_sex",
        "after_date_sex", "intimate_sex",

        # 青姦（参照URL: 青姦）
        "sex_in_public", "forest_sex",
        "beach_sex", "park_sex", "car_sex",

        # 放置プレイ
        "left_alone", "vibrator_left_in", "abandoned_mid_act",

        # オナサポ
        "masturbation_support", "watching_masturbation",
        "giving_instructions",
        # URL追加分: SM・青姦・足コキ・口腔行為
        "open-air_sex", "public_intimacy", "al_fresco", "wilderness_play", "forest_rendezvous",
        "pedal_play", "foot_stimulation", "sole_massage", "foot_rubbing", "heel_play", "toe_play",
        "foot_caress", "foot_play", "toe_tease", "foot_squeeze", "toe_manipulation",
        "copulation", "sexual_intercourse", "foreplay",
    ],
    "cat_nsfw_creature": [
        "tentacles", "monster", "demon", "orc", "goblin",
        "beast", "creature", "alien", "dragon", "werewolf",
        "tentacle_play", "monster_sex", "tentacle_sex",
        "vore",

        # 機械姦（参照URL: 機械姦・異種姦・フェチ）
        "machine_sex", "mechanical_sex", "fucking_machine_sex",
        "robot_sex", "android_sex", "cyborg_sex",
        "mechanical_tentacles_sex",

        # 異種姦追加
        "tentacle_rape", "plant_sex", "slime_sex",
        "insect_sex", "parasite_sex",
        "alien_sex", "monster_rape",
        "forced_by_creature",
    ],
    "cat_nsfw_item": [
        # バイブ・ディルド（24_体位.yml）
        "vibrator", "egg_vibrator", "vibrator_under_clothes",
        "vibrator_in_thigh_strap", "vibrator_on_clitoris",
        "dildo", "suction_cup_dildo", "double_dildo", "sex_toy",
        "hitachi_magic_wand",

        # アナル系
        "butt_plug", "anal_beads",

        # 拘束系（24_体位.yml + 緊縛詳細）
        "handcuffs", "rope", "bondage", "shibari", "suspension",
        "box_tie", "frogtie", "hogtie", "strappado",
        "bound_wrists", "bound_arms", "bound_legs", "bound_ankles",
        "bound_breasts", "bound_torso", "spreader_bar",
        "collar", "chain", "leash", "harness", "crotch_rope",
        "chastity_belt", "chastity_cage", "straitjacket",

        # 猿轡・目隠し
        "blindfold", "gag", "ball_gag", "bit_gag", "o-ring_gag", "muzzle",

        # 責め・調教
        "whip", "paddle", "crop", "flogger",
        "nipple_clamps", "nipple_chain",

        # 搾乳
        "milking_machine", "breast_pump",

        # マシン系
        "fucking_machine", "spanking_machine", "sybian",
        "strap-on",

        # 特殊（24_体位.yml）
        "condom", "used_condom",
        "dilation_tape", "thigh_strap", "crotch_tattoo",

        # 24_体位.yml 緊縛詳細追加
        "cuffs-to-collar", "bound_fingers", "bound_knees",
        "bound_calves", "bound_feet", "bound_toes", "bound_tail",
        "bound_penis", "separated_arms", "separated_wrists",
        "separated_legs", "shibari_over_clothes", "shibari_under_clothes",

        # 特殊アイテム追加
        "ofuda_on_pussy", "slime", "octopus",
        "tentacle_pit", "tentacle_clothes", "mechanical_tentacles",
        "pussy_tentacle", "penis_tentacle",

        # 機械・特殊器具（機械姦/フェチ参照）
        "electrostimulation", "e-stim",
        "vacuum_pump", "penis_pump", "clitoris_pump",
        "sounding_rod", "urethral_sound",
        "enema_bag", "enema_tube",
        "candle_wax", "wax_play",
        "ice_play", "temperature_play",
        "clothespins", "clamps",
        "dental_gag", "ring_gag",
        "stocks", "pillory",
        "cross", "saint_andrew's_cross",
        "sex_machine", "automated_vibrator",

        # SM道具追加（参照URL: SM）
        "tether", "bondage_gear",
        "sensory_deprivation_hood",
        "paddle_with_holes",
        "wartenberg_wheel",
        # URL追加分: 拘束・SM道具
        "cuffs", "enema",
    ],
    "cat_nsfw_focus": [
        "re:.*_focus",
        "ass_focus", "breast_focus", "pussy_focus", "penis_focus",
        "crotch_focus", "feet_focus", "armpit_focus", "navel_focus",
        "thigh_focus", "back_focus", "leg_focus",
        "foot_focus", "hand_focus", "neck_focus", "shoulder_focus",

        # 性器フォーカス詳細
        "vulva_focus", "nipple_focus", "clitoris_focus",
        "testicle_focus", "anus_focus",

        # 体パーツフォーカス追加
        "waist_focus", "belly_focus", "hip_focus",
        "knee_focus", "sole_focus", "toe_focus",
        "chest_focus",

        # 耳フォーカス（耳舐め参照）
        "ear_focus",

        # 口フォーカス（フェラ/イマラチオ参照）
        "mouth_focus", "tongue_focus",
    ],
    "cat_nsfw_fluids": [
        # 精液系（24_体位.yml）
        "cum", "cum_on_body", "cum_on_face", "cum_on_breasts",
        "cum_in_pussy", "cum_in_mouth", "cum_in_ass", "cum_inside",
        "cum_on_clothes", "cum_all_over", "dripping_cum", "leaking_cum",
        "creampie", "cum_drip",

        # 愛液・潮吹き（24_体位.yml + お気に入り.yml）
        "pussy_juice", "pussy_juice_drip", "pussy_juice_trail",
        "wet_stain_on_panty",
        "female_squirting",

        # 母乳（24_体位.yml + お気に入り.yml）
        "lactation", "projectile_lactation", "lactation_through_clothes",
        "breast_milk",

        # 一般体液
        "sweat", "urine",
        "body_fluids", "splash", "gush", "spurt", "precum",

        # 射精バリエーション
        "multiple_creampie", "internal_cumshot",
        "cum_string", "cum_trail", "cum_overflow",
        "gokkun", "snowballing",
        "cum_on_hair", "cum_on_ass", "cum_on_feet",
        "cum_on_stomach", "cum_on_back",
        "dripping", "overflow",

        # 愛液追加
        "squirting", "gushing", "flowing",

        # 母乳追加
        "milk_squirt", "dripping_milk",

        # 顔射（参照URL: 顔射）
        "facial", "cum_on_forehead",
        "cum_on_glasses", "covered_in_cum",
        "multiple_facial",

        # 口内射精（参照URL: 口内射精）
        "mouthful_of_cum", "swallowing_cum",
        "cum_string_from_mouth",
        # 潮吹き追加（参照URL: 潮吹き）
        "squirt", "female_ejaculation",
        "squirting_on_partner",
    ],
    "cat_nsfw_fetish": [
        "re:.*_fingering", "re:.*_fisting",

        # 恍惚系
        "ahegao", "eyes_rolled_back",
        "orgasm", "orgasm_convulsion", "heavy_breathing",
        "convulsion", "trembling", "body_shaking", "torogao", "bareback",

        # フェティッシュ（24_体位.yml）
        "foot_fetish", "armpit_fetish", "toe_sucking",
        "foot_worship", "sole_licking", "foot_trample",
        "navel_fetish", "belly_fetish", "thigh_fetish",
        "neck_fetish", "hair_fetish", "ear_fetish",

        # 心理・状態（24_体位.yml 心理_状態）
        "corruption", "mind_break", "mind_control", "brainwashing",
        "hypnosis", "hypnosis_app", "drugged", "aphrodisiac",
        "humiliation", "degradation", "embarrassment",
        "exhibitionism", "voyeurism", "femdom",
        "in_heat", "feel_horny", "fucked_silly",
        "defloration", "before_sex", "after_sex", "after_vaginal",
        "drunk", "defeat",

        # 特殊（24_体位.yml）
        "inflation", "transformation",
        "peeing", "public_urination",

        # 24_体位.yml 排泄・心理追加
        "have_to_pee", "bedwetting", "pee_stain", "pee_pad",
        "peeing_on_penis", "drinking_pee", "peeing_in_cup",
        "peeing_in_bottle", "peeing_self", "urethral_insertion",

        # 心理・状態追加
        "before_rape", "body_stiffening",
        "zettai_ryouiki", "sweat_skin",
        "ovum", "fertilization", "sperm_cell",

        # 特殊関係性
        "faceless_bald_male", "silhouette_man",
        "disembodied_tongue", "disembodied_penis",
        "disembodied_limb", "invisible_penis", "clear_insertion",
        "cross-section_focus", "vagina_shape",

        # 関係性・シナリオ追加
        "netorare", "ntr", "cuckold", "cheating",
        "reluctant",
        "blackmail", "coercion", "seduction",
        "consensual", "mutual_consent",

        # 状態追加
        "used", "ruined", "broken_in",
        "multiple_orgasms", "forced_orgasm",
        "edging", "denial",
        "afterglow", "post_orgasm",

        # 特殊フェチ追加
        "impregnation", "pregnancy_risk",
        "collar_and_leash", "slave", "pet_play",
        "age_difference", "size_difference",
        "navel_licking", "navel_insertion",
        "armpit_sex", "thighjob", "sockjob",

        # フェチ追加（参照URL: フェチwiki / SM参照）
        "foot_tickling", "foot_bondage",
        "stockings_fetish", "pantyhose_fetish",
        "smell_fetish", "sniffing_panties",
        "used_panties", "stained_panties",
        "pantyhose_rip", "pantyhose_sex",
        "latex_fetish", "rubber_fetish",
        "uniform_fetish", "cosplay_sex",
        "crossdressing", "femboy",
        "submission", "dominance",
        "masochism", "sadism",
        "pain_play", "sensory_play",
        "orgasm_denial", "ruined_orgasm",
        "body_writing", "degradation_play",
        "spit_play", "drool_fetish",
        "ear_cleaning_fetish",

        # 淫乱・オホ声（参照URL）
        "lewd_expression", "slutty", "wanton",
        "ahegao_tongue", "rolling_eyes_orgasm",
        "loud_moaning", "ahegao_face",

        # 羞恥/恥辱（参照URL）
        "shame", "public_humiliation",
        "forced_exposure", "clothed_female_nude_male",
        "clothed_male_nude_female",
        "inspection", "spread_and_displayed",

        # 盗撮・盗み見（参照URL）
        "voyeur", "hidden_camera", "peeping",
        "public_flashing", "seen_by_others",
        "exhibitionist_fantasy",

        # 孕ませ（参照URL）
        "creampie_pregnancy", "fertilization_fantasy",
        "womb_tattoo", "baby_making",

        # レズ追加（参照URL）
        "lesbian_sex", "girl_on_girl", "yuri_sex",
        "strap-on_sex", "mutual_cunnilingus",
        "breast_to_breast", "tribadism_on_bed",

        # 男性受けプレイ（参照URL）
        "male_receiving", "reverse_cowgirl_male",
        "male_anal", "prostate_orgasm",

        # 悪堕ち（参照URL）
        "moral_corruption", "dark_persona_sex",
        "evil_smile_sex", "villain_transformation",
        # URL追加分: 悪堕ち・SM・フェティッシュ
        "depravity", "descent", "betrayal", "wickedness", "malevolence",
        "dominant", "submissive", "s&m", "roleplay", "role_reversal",
        "safe_word", "aftercare", "consent", "naturism", "voyeuristic_fantasy",
        "pedal_fetish", "foot_fantasy", "foot_desire", "climax", "arousal",
    ],
    "cat_nsfw_clothes_mess": [
        "re:.*_lift", "re:.*_pull", "re:.*_removal", "re:.*_aside",

        # 脱衣・露出（24_体位.yml 服装_位置_状態）
        "undressing", "stripping", "naked", "nude", "topless", "bottomless",
        "no_panties", "no_bra",
        "clothes_torn", "torn_clothes", "tattered_clothes",
        "public_exposure", "flashing",
        "clothing_around_ankles", "pulled_down", "pulled_up",
        "skirt_lift", "shirt_lift", "dress_lift", "bra_lift",
        "panties_around_ankles", "panties_around_one_leg",
        "panties_around_knees", "panties_aside", "clothing_aside",
        "panties_on_head", "panties_in_mouth",
        "open_clothes", "half-undressed", "partially_undressed",
        "open_bra", "bra_removed",

        # お気に入り.yml
        "panty_pull", "adjusting_panties",
        "hand_in_panties", "fingering_through_panties",

        # 完全全裸・露出バリエーション
        "completely_nude", "completely_naked", "nude_cover",
        "strategically_covered", "ribbon_bondage",
        "naked_ribbon", "naked_bow",
        "topless_nude", "bottomless_nude",
        "clothes_removed", "uniform_removed",
        "swimsuit_removed", "bikini_removed",
        "panties_removed",

        # 着衣状態詳細
        "see-through_wet", "wet_shirt", "wet_clothes",
        "no_shoes", "no_socks", "no_legwear",
        "single_shoe", "single_thighhigh",
        "mismatched_legwear",
        "bra_pull_down", "panties_lift_up_with_both_hands", "show_navel",
        "lifting_shirt_with_one_hand", "lifting_shirt_with_both_hands",
        "pulling_down_strap", "strap_slip", "open_skirt",

        # 露出プレイ追加（参照URL: 露出プレイ）
        "outdoor_nudity", "nude_in_public",
        "exposed_in_crowd", "naked_in_nature",
        "flashing_skirt", "flashing_breasts",
        "surprise_exposure", "accidental_exposure",
        "uniform_disheveled", "serafuku_disheveled",
        # URL追加分: 野外露出
        "outdoor_exposure", "public_display",
    ],
    "cat_nsfw_genitals": [
        # 女性器（24_体位.yml 性器_状態 + クリトリス）
        "pussy", "vagina", "vulva", "labia", "clitoris", "large_clitoris",
        "erect_clitoris", "clitoris_slip",
        "spread_pussy", "open_pussy", "gaping", "cleft_of_venus",
        "wet_shiny_vagina", "cervix", "urethra", "stomach_bulge",

        # 男性器
        "penis", "cock", "erection", "flaccid", "huge_penis", "small_penis",
        "testicles", "balls", "scrotum",

        # 共通
        "anus", "asshole",

        # 乳首（24_体位.yml 胸_乳首）
        "nipples", "erect_nipples", "inverted_nipples", "puffy_nipples",
        "nipple_stimulation", "nipple_pull", "areola_slip",
        "areolae", "large_areolae",

        # その他
        "genitals", "cameltoe", "bulge",

        # 24_体位.yml クリトリス詳細追加
        "clitoral_hood", "clitoris_pull", "clitoris_tweak",
        "clitoris_stimulation_through_clothing",
        "clitorises_touching", "half-spread_pussy",
        "spreading_anothers_pussy", "close_up_pussy",

        # 胸・乳首詳細追加
        "presenting_nipples", "covering_own_nipples",
        "presenting_crotch", "covering_own_crotch",
        "breast_measuring", "breast_conscious",
        "innie_pussy", "pink_areola", "pubic_stubble",

        # 全裸・検閲
        "uncensored", "mosaic_censoring", "bar_censor",
        "convenient_censoring", "nude_filter",

        # 女性器バリエーション
        "shaved_pussy", "hairy_pussy", "dripping_pussy",
        "prolapse", "vaginal_insertion", "anal_insertion",
        "vaginal_object_insertion", "anal_object_insertion",
        "pussy_peek", "visible_through_clothes",

        # 男性器バリエーション
        "foreskin", "phimosis", "cumming", "ejaculation",

        # 乳首詳細
        "nipple_rings", "nipple_piercing",
        "dark_nipples", "light_nipples", "brown_nipples",
        "large_nipples", "small_nipples", "perky_nipples",
        "covered_nipples", "pasties",

        # 体毛
        "shaved", "pubic_tattoo", "armpit_hair",

        # 胸バリエーション（genitals寄り）
        "breast_lift",
        "self_breast_grab", "grabbing_anothers_breast",
        "nipple_licking", "breast_feeding",

        # アナル詳細（参照URL: アナル）
        "anal_gape", "anal_prolapse",
        "anal_fisting", "anal_fingering",
        "anal_wink", "anal_close-up",
        "rectum_visible",
        # URL追加分: 局部詳細
        "rectum", "sphincter", "perineum", "anal_canal",
    ],
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
