import os
import pandas

# Supported languages: https://github.com/elimu-ai/model/blob/main/src/main/java/ai/elimu/model/v2/enums/Language.java
languages = [
    'ENG',
    'HIN',
    'TGL',
    'THA'
]
print(f'languages: {languages}')

# Download datasets for each language
for language in languages:
    print()
    print(f'language: {language}')

    os.makedirs(f'lang-{language}', exist_ok=True)

    # TODO: letter-sound learning events

    # TODO: word learning events

    # TODO: number learning events
    
    storybook_learning_events_csv_url = f'http://{language.lower()}.elimu.ai/analytics/storybook-learning-event/list/storybook-learning-events.csv'
    print(f'storybook_learning_events_csv_url: {storybook_learning_events_csv_url}')
    storybook_learning_events_dataframe = pandas.read_csv(storybook_learning_events_csv_url)
    print(f'storybook_learning_events_dataframe: \n{storybook_learning_events_dataframe}')
    storybook_learning_events_file_path = f'lang-{language}/storybook-learning-events.csv'
    print(f'storybook_learning_events_file_path: {storybook_learning_events_file_path}')
    storybook_learning_events_dataframe.to_csv(storybook_learning_events_file_path, index=False)

    # video_learning_events_csv_url = f'http://{language.lower()}.elimu.ai/analytics/video-learning-event/list/video-learning-events.csv'
    # print(f'video_learning_events_csv_url: {video_learning_events_csv_url}')
    # video_learning_events_dataframe = pandas.read_csv(video_learning_events_csv_url)
    # print(f'video_learning_events_dataframe: \n{video_learning_events_dataframe}')
    # video_learning_events_file_path = f'lang-{language}/video-learning-events.csv'
    # print(f'video_learning_events_file_path: {video_learning_events_file_path}')
    # video_learning_events_dataframe.to_csv(video_learning_events_file_path, index=False)
