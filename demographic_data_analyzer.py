import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = pd.Index(df['race']).value_counts()


    # What is the average age of men?
    average_age_men = round(df.loc[df['sex']=='Male','age'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage = pd.Index(df['education']).value_counts(normalize = True)*100
    percentage_bachelors = round(percentage.loc['Bachelors'],1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    df['advanced']= ["Yes" if x in ['Bachelors','Masters','Doctorate'] else 'No' for x in df['education']]

   
    advanced_df = df[df['advanced']=='Yes']

    advanced_percentage = pd.Index(advanced_df['salary']).value_counts(normalize=True)*100
    # print(advanced_percentage)
    advanced_percentage_greater50 = round(advanced_percentage.loc['>50K'],1)


    no_advanced_df = df[df['advanced']=='No']

    no_advanced_percentage = pd.Index(no_advanced_df['salary']).value_counts(normalize=True)*100
 

    no_advanced_percentage_greater50 = round(no_advanced_percentage.loc['>50K'],1)

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    # higher_education = None
    # lower_education = None

    # percentage with salary >50K
    higher_education_rich = advanced_percentage_greater50
    lower_education_rich = no_advanced_percentage_greater50
    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = min(df['hours-per-week'])

    # print(min_work_hours)

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week']==min_work_hours]

    min_per = pd.Index(num_min_workers['salary']).value_counts(normalize=True)*100

    rich_percentage = round(min_per.loc['>50K'],1)

    # What country has the highest percentage of people that earn >50K?

    country2 = df.groupby('native-country')

    value_after_group = country2['salary'].value_counts(normalize=True)*100

    country3 = value_after_group.reset_index(name='percentage')

    country4 = country3[country3['salary']=='>50K'].sort_values(by=['percentage'], ascending = False)

    # print(country4.loc[[0],['native-country']])
    # print(type((country4[0:1]['native-country']).values[0]))
    highest_earning_country = (country4[0:1]['native-country']).values[0]
    highest_earning_country_percentage = round((country4[0:1]['percentage']).values[0],1)

    # Identify the most popular occupation for those who earn >50K in India.

    india_df = df[(df['native-country']=='India')& (df['salary']=='>50K')]

    india_value = (india_df['occupation'].value_counts()).reset_index(name='count')
    
    #first value 
    
    top_IN_occupation = (india_value[0:1]['index']).values[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
