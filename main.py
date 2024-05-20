import os
import json
import matplotlib.pyplot as plt
def result_plot(subject: str, year: int):
    try:
        with open(os.path.join('results', str(year) , subject + '.json'), encoding='utf-8') as f:
            data = json.load(f)
        grades={}
        for grade in data.values():
            try:
                grades[grade] += 1
            except:
                grades[grade] = 1
        grades = dict(sorted(grades.items()))
    except FileNotFoundError:
        exit("A fájl nem található!")

    max_y = max(grades.values())

    plt.bar((grades.keys()), grades.values())
    plt.title(f'Eloszlás {year} {subject}')
    plt.xlabel('Érdemjegy')
    plt.ylabel('Darab')
    plt.xticks([0,1,2,3,4,5])
    plt.yticks(range(max_y+1))
    plt.savefig(f'{subject}_{year}_results1.png')


def result_plot_over_years(subjects: list):
    all_percentage={}
    for year in os.listdir('results'):
        for subject in subjects:
            passed = 0
            try:
                with open(os.path.join('results', year, subject + '.json')) as f:
                    data=json.load(f)
                for value in data.values():
                    if value > 1:
                        passed += 1
                passed_percentage = passed/len(data)*100
                try:
                    all_percentage[subject].append(passed_percentage)
                except KeyError:
                    all_percentage[subject] = [passed_percentage]
            except FileNotFoundError:
                try:
                    all_percentage[subject].append(0)
                except KeyError:
                    all_percentage[subject] = [passed_percentage]
    title = ', '.join(map(str, subjects)) + ' átmeneti grafikon'
    output = '_'.join(map(str, subjects)) + '_results.png'
    for sub in subjects:
        plt.plot(os.listdir('results'), all_percentage[sub], label=sub)
        plt.xlabel('Év')
        plt.ylabel('Átment százalék')
        plt.title(title)
        plt.legend()
        plt.savefig(output)
            

result_plot_over_years(['math', 'music'])