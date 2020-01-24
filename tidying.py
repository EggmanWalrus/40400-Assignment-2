# Import libraries
import pandas as pd


# Define functions
def tidying(data):
    selected_columns = ['V2: Country Code',
                        'V4: Important in life: Family',
                        'V5: Important in life: Friends',
                        'V6: Important in life: Leisure time',
                        'V7: Important in life: Politics',
                        'V8: Important in life: Work',
                        'V9: Important in life: Religion',
                        'V10: Feeling of happiness',
                        'V11: State of health (subjective)',
                        'V23: Satisfaction with your life',
                        'V24: Most people can be trusted',
                        'V28: Active/Inactive membership: Labor Union',
                        'V29: Active/Inactive membership: Political party',
                        'V55: How much freedom of choice and control over own life',
                        'V59: Satisfaction with financial situation of household',
                        'V60: Aims of country: first choice',
                        'V61: Aims of country: second choice',
                        'V62: Aims of respondent: first choice',
                        'V63: Aims of respondent: second choice',
                        'V64: Most important: first choice',
                        'V65: Most important: second choice',
                        'V84: Interest in politics',
                        'V85: Political action: Signing a petition',
                        'V86: Political action: Joining in boycotts',
                        'V87: Political action: Attending peaceful demonstrations',
                        'V88: Political action: Joining strikes',
                        'V89: Political action: Any other act of protest',
                        'V90: Political action recently done: Signing a petition',
                        'V91: Political action recently done: Joining in boycotts',
                        'V92: Political action recently done: Attending peaceful demonstrations',
                        'V93: Political acition recently done: Joining strikes',
                        'V94: Political action recently done: Any other act of protest',
                        'V95: Self positioning in political scale',
                        'V96: Income equality',
                        'V99: Competition good or harmful',
                        'V100: Hard work brings success',
                        'V101: Wealth accumulation',
                        'V112: Confidence: Labour Unions',
                        'V115: Confidence: The government (in your nation’s capital)',
                        'V116: Confidence: Political Parties',
                        'V137: Democracy: The state makes people\'s incomes equal',
                        'V140: Importance of democracy',
                        'V142: How much respect is there for individual human rights nowadays in this country',
                        'V238: Social class (subjective)',
                        'V239: Scale of incomes',
                        'V240: Sex',
                        'V242: Age'
                        ]
    renames_columns = ['Country',
                       'Family',
                       'Friends',
                       'Leisure',
                       'Politics',
                       'Work',
                       'Religion',
                       'Happiness',
                       'Health',
                       'Satisfaction',
                       'Trust',
                       'Active_labor_union',
                       'Active_party',
                       'Freedom',
                       'Satisfaction_financial',
                       'Aim_country_first',
                       'Aim_country_second',
                       'Aim_respondent_first',
                       'Aim_respondent_second',
                       'Most_important_first',
                       'Most_important_second',
                       'Interest_politics',
                       'Politics_petition',
                       'Politics_boycotts',
                       'Politics_peaceful_demo',
                       'Politics_strikes',
                       'Politics_protest',
                       'Politics_done_petition',
                       'Politics_done_boycotts',
                       'Politics_done_peaceful_demo',
                       'Politics_done_strikes',
                       'Politics_done_protest',
                       'Political_scale',
                       'Income_equality',
                       'Competition',
                       'Hard_work',
                       'Wealth_accumulation',
                       'Confidence_labor_union',
                       'Confidence_govern',
                       'Confidence_parties',
                       'Democracy_state_income_equal',
                       'Democracy_importance',
                       'Human_rights',
                       'Social_class',
                       'Income_scale',
                       'Sex',
                       'Age'
                       ]
    country_region_dict = {156: 'China', 344: 'Hong Kong', 158: 'Taiwan', 840: 'US'}

    data = data[selected_columns]
    data.columns = renames_columns
    data = data.replace({'Country': country_region_dict})
    return data


# Import datasets
China = pd.read_excel('Data_raw/China/China_code.xlsx')
HongKong = pd.read_excel('Data_raw/Hong Kong/HongKong_code.xlsx')
Taiwan = pd.read_excel('Data_raw/Taiwan/Taiwan_code.xlsx')
US = pd.read_excel('Data_raw/US/US_code.xlsx')
