import os
import pandas

# Supported languages: https://github.com/elimu-ai/model/blob/main/src/main/java/ai/elimu/model/v2/enums/Language.java
languages = [
    'ENG',
    'HIN',
    'TGL',
    'THA',
    'VIE'
]
print(f'languages: {languages}')

# Download datasets for each language
for language in languages:
    print()
    print(f'language: {language}')

    os.makedirs(f'lang-{language}', exist_ok=True)

    students_csv_url = f'http://{language.lower()}.elimu.ai/analytics/students/students.csv'
    print(f'students_csv_url: {students_csv_url}')
    students_dataframe = pandas.read_csv(students_csv_url)
    print(f'students_dataframe: \n{students_dataframe}')
    students_file_path = f'lang-{language}/students.csv'
    print(f'students_file_path: {students_file_path}')
    students_dataframe.to_csv(students_file_path, index=False)

    for index, student in students_dataframe.iterrows():
        print()
        print(f'student.id: {student.id}')

        os.makedirs(f'lang-{language}/student-id-{student.id}', exist_ok=True)

        letter_sound_assessment_events_csv_url = f'http://{language.lower()}.elimu.ai/analytics/students/{student.id}/letter-sound-assessment-events.csv'
        print(f'letter_sound_assessment_events_csv_url: {letter_sound_assessment_events_csv_url}')
        letter_sound_assessment_events_dataframe = pandas.read_csv(letter_sound_assessment_events_csv_url)
        print(f'letter_sound_assessment_events_dataframe: \n{letter_sound_assessment_events_dataframe}')
        letter_sound_assessment_events_file_path = f'lang-{language}/student-id-{student.id}/letter_sound-assessment-events.csv'
        print(f'letter_sound_assessment_events_file_path: {letter_sound_assessment_events_file_path}')
        letter_sound_assessment_events_dataframe.to_csv(letter_sound_assessment_events_file_path, index=False)
        
        letter_sound_learning_events_csv_url = f'http://{language.lower()}.elimu.ai/analytics/students/{student.id}/letter-sound-learning-events.csv'
        print(f'letter_sound_learning_events_csv_url: {letter_sound_learning_events_csv_url}')
        letter_sound_learning_events_dataframe = pandas.read_csv(letter_sound_learning_events_csv_url)
        print(f'letter_sound_learning_events_dataframe: \n{letter_sound_learning_events_dataframe}')
        letter_sound_learning_events_file_path = f'lang-{language}/student-id-{student.id}/letter_sound-learning-events.csv'
        print(f'letter_sound_learning_events_file_path: {letter_sound_learning_events_file_path}')
        letter_sound_learning_events_dataframe.to_csv(letter_sound_learning_events_file_path, index=False)

        word_assessment_events_csv_url = f'http://{language.lower()}.elimu.ai/analytics/students/{student.id}/word-assessment-events.csv'
        print(f'word_assessment_events_csv_url: {word_assessment_events_csv_url}')
        word_assessment_events_dataframe = pandas.read_csv(word_assessment_events_csv_url)
        print(f'word_assessment_events_dataframe: \n{word_assessment_events_dataframe}')
        word_assessment_events_file_path = f'lang-{language}/student-id-{student.id}/word-assessment-events.csv'
        print(f'word_assessment_events_file_path: {word_assessment_events_file_path}')
        word_assessment_events_dataframe.to_csv(word_assessment_events_file_path, index=False)
        
        word_learning_events_csv_url = f'http://{language.lower()}.elimu.ai/analytics/students/{student.id}/word-learning-events.csv'
        print(f'word_learning_events_csv_url: {word_learning_events_csv_url}')
        word_learning_events_dataframe = pandas.read_csv(word_learning_events_csv_url)
        print(f'word_learning_events_dataframe: \n{word_learning_events_dataframe}')
        word_learning_events_file_path = f'lang-{language}/student-id-{student.id}/word-learning-events.csv'
        print(f'word_learning_events_file_path: {word_learning_events_file_path}')
        word_learning_events_dataframe.to_csv(word_learning_events_file_path, index=False)

        # TODO: number assessment events
        
        # TODO: number learning events
        
        storybook_learning_events_csv_url = f'http://{language.lower()}.elimu.ai/analytics/students/{student.id}/storybook-learning-events.csv'
        print(f'storybook_learning_events_csv_url: {storybook_learning_events_csv_url}')
        storybook_learning_events_dataframe = pandas.read_csv(storybook_learning_events_csv_url)
        print(f'storybook_learning_events_dataframe: \n{storybook_learning_events_dataframe}')
        storybook_learning_events_file_path = f'lang-{language}/student-id-{student.id}/storybook-learning-events.csv'
        print(f'storybook_learning_events_file_path: {storybook_learning_events_file_path}')
        storybook_learning_events_dataframe.to_csv(storybook_learning_events_file_path, index=False)

        video_learning_events_csv_url = f'http://{language.lower()}.elimu.ai/analytics/students/{student.id}/video-learning-events.csv'
        print(f'video_learning_events_csv_url: {video_learning_events_csv_url}')
        video_learning_events_dataframe = pandas.read_csv(video_learning_events_csv_url)
        print(f'video_learning_events_dataframe: \n{video_learning_events_dataframe}')
        video_learning_events_file_path = f'lang-{language}/student-id-{student.id}/video-learning-events.csv'
        print(f'video_learning_events_file_path: {video_learning_events_file_path}')
        video_learning_events_dataframe.to_csv(video_learning_events_file_path, index=False)
