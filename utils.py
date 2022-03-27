import json

def convert_string_time_to_seconds(time_youtube_string):
    # Go by trials
    time_not_codified = time_youtube_string.split(":")
    if len(time_not_codified) == 3:
        h, m, s = [int(x) for x in time_not_codified]
        return (h * 3600) + (m * 60) + s
    elif len(time_not_codified) == 2:
        m, s = [int(x) for x in time_not_codified]
        return (m * 60) + s
    else:
        return int(time_not_codified)


def load_config_text_languages():
    with open("data/config_text_languages.json", "r") as f:
        return json.load(f)