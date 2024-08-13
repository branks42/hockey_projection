import pandas as pd  
from sklearn.ensemble import RandomForestRegressor  
from sklearn.preprocessing import OneHotEncoder  
from sklearn.compose import ColumnTransformer  
import numpy as np

from utilities import print_goalie_stats, print_skater_stats, show_nationality_options, show_position_options
  
  
def main():  
    file_path = 'data/final_nhl_data.csv'  
    ndd = pd.read_csv(file_path) 

    # Only use data from 2015 or earlier
    ndd = ndd[ndd['year'] <= 2015]
  
    # This model is used to predict the number of games played, goals, assists, points, and plus_minus
    # You initialize the model with the number of trees you want to use, and a random state for reproducibility
    projection_model = RandomForestRegressor(n_estimators=100, random_state=42)  
  
    # ColumnTransformer allows you to apply different transformations to different columns in your dataset
    # In our case, we want to apply OneHotEncoding to the position and nationality columns, and leave the overall_pick and age columns as they are
    # OneHotEncoding is used to convert categorical data into a format that can be provided to ML algorithms to do a better job in prediction
    preprocessor = ColumnTransformer(  
        transformers=[  
            ('num', 'passthrough', ["overall_pick", "age"]),  
            ('cat', OneHotEncoder(), ['position', 'nationality'])  
        ])  
  
    # Define the features and target variable
    x = ndd[["overall_pick", "position", 'nationality', "age"]]  
    y = ndd[['year', 'to_year', 'games_played', 'goals', 'assists', 'points', 'plus_minus', 'goalie_games_played', 'goalie_wins', 'goalie_losses', 'goalie_ties_overtime', 'save_percentage', 'goals_against_average']]  
  
    # Fit and transform X to the preprocessor
    x = preprocessor.fit_transform(x)  
    
    # Fit the model
    projection_model.fit(x, y)  

    # Show user the options for position and nationality
    show_nationality_options()
    show_position_options()

    project_another = True

    while project_another:
        overall_pick = int(input("Enter the draft pick number: "))  
        player_age = float(input("Enter the player's age: "))  
        position = input("Enter the player's position: ")  
        nationality = input("Enter the player's nationality: ")  
    

        new_data = np.array([[overall_pick, position, nationality, player_age]])  
        new_data_df = pd.DataFrame(new_data, columns=["overall_pick", "position", 'nationality', "age"])  
        new_data_transformed = preprocessor.transform(new_data_df)  
    
        prediction = projection_model.predict(new_data_transformed)  
    
        for p in prediction:
            func = print_goalie_stats if position == 'G' else print_skater_stats  
            func(p)
        
        project_another = input("Would you like to project another player? (y/n): ").lower() == 'y'
    
  
if __name__ == '__main__':  
    main()  
