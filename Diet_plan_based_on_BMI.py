# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 07:07:09 2019

@author: khushal
"""

# https://spoonacular.com/food-api/docs

## https://www.dataquest.io/blog/web-scraping-tutorial-python/
user_name ="khushal" #str(input('Enter the User name := '))    
user_gender = "male" #str(input('Enter Your gender details (MALE/FEMALE) := '))    
user_age = 27 # int(input('Please enter your Age in number := '))
height = 1.94 #float(input('Please enter your height input meters(decimals) := '))
weight = 109 #int(input('Please enter your weight input kg := '))
meal_preference = "non-vegetarian" #str(input('Enter your meal preference (vegetarian/non-vegetarian/eggetarian) := '))    
diabetic_flag = "no" #str(input("Are you diabetic (YES/NO) := "))
print(                           '1. Very Light = Typical Office job (sitting,studying,little walking throughout the day) \n',
                                 '2. Light = Any job where you mostly walk or stand(teaching,shop/lab work,some walking throughout the day) \n',
                                 '3. Moderate = Jobs requiring physical activity (landscaping,cleaning,maintaince,jogging,biking/working out 2hrs/day) \n',
                                 '4. Heavy = Heavy manual labor (construction,dancer,athlete,hard physical activity min 4 hrs/day) \n',
                                 '5. Very Heavy = Moderate to hard physical activity min 8 hrs/day \n')
daily_activity_level = 'moderate' # str(input('Enter your Daily activity := \n'))

def bmi_calculator(height,weight):
    bmi = round((weight/(height**2)),2)
    
    if bmi <= 18.5:
        bmi_flag = "underweight"
        print('Your BMI is', bmi,',which means you are underweight.')
    elif bmi > 18.5 and bmi < 25:
        bmi_flag = "healthy"
        print('Your BMI is', bmi,',which means you are normal.')
    elif bmi > 25 and bmi < 30:
        bmi_flag = "overweight"
        print('your BMI is', bmi,',which means you are overweight.')
    elif bmi > 30:
        bmi_flag = "obese"
        print('Your BMI is', bmi,',which means you are obese.')
    else:
        print('There is an error with your input')
        print('Please check you have entered whole numbers\n'
              'and decimals were asked.')
    return bmi,bmi_flag

def calculate_body_fat_percentage (bmi,age,gender):
    if gender.lower() == 'female':
        Body_Fat_Percentage = round(((1.20 * bmi) + (0.23 * age) - 5.4),2)
        body_fat_flag = set_body_fat_flag(Body_Fat_Percentage,age,gender)
    elif gender.lower() == 'male':
        Body_Fat_Percentage = round(((1.20 * bmi) + (0.23 * age) - 16.2),2)
        body_fat_flag = set_body_fat_flag(Body_Fat_Percentage,age,gender)
    else: 
        print('There is an error with your input')
        print('Please check you have entered whole numbers\n'
              'and decimals were asked.')    
    return Body_Fat_Percentage,body_fat_flag

def set_body_fat_flag(Body_Fat_Percentage,age,gender):
    if gender.lower() == 'female':
        if age >= 20 and age < 40:
            
            if Body_Fat_Percentage < 21 :
                body_fat_flag = 'underfat'
            elif Body_Fat_Percentage >= 21 and Body_Fat_Percentage < 33 :
                body_fat_flag = 'healthy'
            elif Body_Fat_Percentage >= 33 and Body_Fat_Percentage < 39 :
                body_fat_flag = 'overweight'
            else:
                body_fat_flag = 'obese'
                
        elif age >= 41 and age < 60:
            
            if Body_Fat_Percentage < 23 :
                body_fat_flag = 'underfat'
            elif Body_Fat_Percentage >= 23 and Body_Fat_Percentage < 35 :
                body_fat_flag = 'healthy'
            elif Body_Fat_Percentage >= 35 and Body_Fat_Percentage < 40 :
                body_fat_flag = 'overweight'
            else:
                body_fat_flag = 'obese'
                
        elif age >= 61 and age < 79:

            if Body_Fat_Percentage < 24 :
                body_fat_flag = 'underfat'
            elif Body_Fat_Percentage >= 24 and Body_Fat_Percentage < 36 :
                body_fat_flag = 'healthy'
            elif Body_Fat_Percentage >= 36 and Body_Fat_Percentage < 42 :
                body_fat_flag = 'overweight'
            else:
                body_fat_flag = 'obese'            
            
        else:
            print("Kindly check the entered input")
            
    elif gender.lower() == 'male':
        if age >= 20 and age < 40:
            
            if Body_Fat_Percentage < 8 :
                body_fat_flag = 'underfat'
            elif Body_Fat_Percentage >= 8 and Body_Fat_Percentage < 19 :
                body_fat_flag = 'healthy'
            elif Body_Fat_Percentage >= 19 and Body_Fat_Percentage < 25 :
                body_fat_flag = 'overweight'
            else:
                body_fat_flag = 'obese'
                
        elif age >= 41 and age < 60:
            
            if Body_Fat_Percentage < 11 :
                body_fat_flag = 'underfat'
            elif Body_Fat_Percentage >= 11 and Body_Fat_Percentage < 22 :
                body_fat_flag = 'healthy'
            elif Body_Fat_Percentage >= 22 and Body_Fat_Percentage < 27 :
                body_fat_flag = 'overweight'
            else:
                body_fat_flag = 'obese'
                
        elif age >= 61 and age < 79:

            if Body_Fat_Percentage < 13 :
                body_fat_flag = 'underfat'
            elif Body_Fat_Percentage >= 13 and Body_Fat_Percentage < 25 :
                body_fat_flag = 'healthy'
            elif Body_Fat_Percentage >= 25 and Body_Fat_Percentage < 30 :
                body_fat_flag = 'overweight'
            else:
                body_fat_flag = 'obese'            
    
        else:
            print("Kindly check the entered input")
    return body_fat_flag

def create_dict_from_variables(user_name, user_gender,height,weight,bmi,bmi_flag,Body_Fat_Percentage,body_fat_flag,meal_preference,diabetic_flag):
    return {'user_name':user_name,'user_gender':user_gender, 'height':height,'weight':weight,
            'bmi':bmi,'bmi_flag':bmi_flag,'Body_Fat_Percentage':Body_Fat_Percentage,'body_fat_flag':body_fat_flag,
            'meal_preference':meal_preference,
            'diabetic_flag':diabetic_flag}

def calculate_your_daily_calorie_needs(weight,gender,Body_Fat_Percentage,daily_activity_level):
    if daily_activity_level.lower() == 'very light':
        activity_level = 1.3
    elif daily_activity_level.lower() == 'light':
        activity_level = 1.55
    elif daily_activity_level.lower() == 'moderate':
        activity_level = 1.65
    elif daily_activity_level.lower() == 'heavy':
        activity_level = 1.80
    elif daily_activity_level.lower() == 'very heavy':
        activity_level = 2.00
    else:
        print("Kindly check the entered input")
        
    if gender.lower() == 'female':
        if Body_Fat_Percentage >=14  and  Body_Fat_Percentage < 19:
            lean_factor = 1.0
        elif Body_Fat_Percentage >=19  and  Body_Fat_Percentage < 29:
            lean_factor = 0.95
        elif Body_Fat_Percentage >=29  and  Body_Fat_Percentage <= 38:
            lean_factor = 0.90
        else:
            lean_factor = 0.85
            
        Basal_Metabolic_Rate = (weight *0.9) * 24 * lean_factor
        
    elif gender.lower() == 'male':
        
        if Body_Fat_Percentage >=10  and  Body_Fat_Percentage < 15:
            lean_factor = 1.0
        elif Body_Fat_Percentage >=15  and  Body_Fat_Percentage < 21:
            lean_factor = 0.95
        elif Body_Fat_Percentage >=21  and  Body_Fat_Percentage <= 28:
            lean_factor = 0.90
        else:
            lean_factor = 0.85        
        Basal_Metabolic_Rate = (weight* 1.0) * 24 * lean_factor

    else: 
        print('There is an error with your input')
        print('Please check you have entered whole numbers\n'
              'and decimals were asked.')   
    
    daily_calorie_need = round((Basal_Metabolic_Rate * activity_level),2)
    print("daily_calorie_need = ",daily_calorie_need)
    return daily_calorie_need

bmi,bmi_flag = bmi_calculator(height,weight)
Body_Fat_Percentage,body_fat_flag = calculate_body_fat_percentage (bmi,user_age,user_gender)
daily_calorie_need = calculate_your_daily_calorie_needs(weight,user_gender,Body_Fat_Percentage,daily_activity_level)

user_info_dict = create_dict_from_variables(user_name.lower(),user_gender.lower(),height,weight,
                                            bmi,bmi_flag.lower(),Body_Fat_Percentage,body_fat_flag.lower(),
                                            meal_preference.lower(),diabetic_flag.lower())
print("user_info_dict = ",user_info_dict)