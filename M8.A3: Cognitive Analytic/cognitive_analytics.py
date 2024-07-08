'''
# Exploratory Data Analysis of Food Ingredients and Recipes Dataset
## Importing Necessary Libraries
In this section, we import the necessary libraries for data manipulation and visualization.
'''
  # Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Display settings to make DataFrames more readable
pd.set_option('display.max_columns', None)

'''
## Loading the Dataset
We load the dataset from the specified file path and display the first few rows to get an initial understanding of the data.
'''

# Load the dataset
# Use the correct path to your CSV file
file_path = '/Users/omaraziz/Desktop/M8.A3Cognitive_Analytics_deep_learning/Data/recipies.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
df.head()

'''
## Inspecting the Data
We inspect the data to understand its structure, data types, and basic statistics.
'''

# Inspect the data to understand its structure and basic statistics
df.info()

# Display summary statistics of the dataset
df.describe(include='all')

'''
## Checking for Missing Values
We check for any missing values in the dataset to handle them appropriately.
'''
# Check for missing values in the dataset
missing_values = df.isnull().sum()
missing_values

'''
## Analyzing the Ingredients

We analyze the ingredients to find the most common ones. This involves splitting the ingredients, counting their frequency, and visualizing the top ingredients.
'''
# Analyze the ingredients
# Assuming 'Cleaned_Ingredients' already contains lists of ingredients

# Flatten the list of ingredients and strip whitespace
all_ingredients = [ingredient.strip().lower() for sublist in df['Cleaned_Ingredients'] for ingredient in sublist]

# List of non-ingredient terms to filter out
non_ingredients = [
    'divided', 'chopped', 'peels', 'finely chopped', 'thinly sliced', 'sliced', 'grated',
    'minced', 'diced', 'optional', 'to taste', 'and', 'or', 'for garnish', 'peeled', 'finely',
    'freshly', 'ground', 'fresh', 'large', 'small', 'medium', 'tablespoon', 'teaspoon', 'cup',
    'ounce', 'pound', 'halved', 'quartered', 'whole', 'extra', 'virgin', 'olive', 'oil', 'clove',
    'inch', 'piece', 'head', 'cloves', 'head', 'pieces'
]

# Filter out non-ingredient terms from the list
filtered_ingredients = [ingredient for ingredient in all_ingredients if ingredient not in non_ingredients]

# Count the frequency of each filtered ingredient
filtered_ingredient_freq = pd.Series(filtered_ingredients).value_counts()

# Display the top 20 most common filtered ingredients
top_filtered_ingredients = filtered_ingredient_freq.head(20)
print(top_filtered_ingredients)

'''
## Visualizing the Top Ingredients
We plot a bar chart to visualize the top 20 most common ingredients.
'''
# Plot the top 20 most common ingredients
top_ingredients.plot(kind='bar', title='Top 20 Most Common Ingredients')
plt.xlabel('Ingredients')
plt.ylabel('Frequency')
plt.show()

'''
## Generating Word Cloud for Ingredients
We generate a word cloud to visualize the most frequent ingredients in a visually appealing manner.
'''
# Generate a word cloud for the ingredients
wordcloud = WordCloud(width=800, height=400).generate(' '.join(all_ingredients))

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Ingredients Word Cloud')
plt.show()

'''
## Analyzing Recipe Titles
We analyze the length of recipe titles to understand their distribution.
'''
# Analyze the length of recipe titles
# Ensure the 'Title' column exists and contains valid data
if 'Title' in df.columns:
    # Fill NaN values with an empty string and ensure all titles are strings
    df['Title'] = df['Title'].fillna('').astype(str)
    
    # Calculate the length of each title
    df['Title_Length'] = df['Title'].apply(len)
    
    # Plot the distribution of title lengths
    plt.hist(df['Title_Length'], bins=20)
    plt.title('Distribution of Title Lengths')
    plt.xlabel('Title Length')
    plt.ylabel('Frequency')
    plt.show()
else:
    print("The 'Title' column is not found in the DataFrame.")

'''
## Generating Word Cloud for Titles
We generate a word cloud to visualize the most common words in recipe titles.
'''
# Generate a word cloud for the titles
title_words = ' '.join(df['Title'])
wordcloud = WordCloud(width=800, height=400).generate(title_words)

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Titles Word Cloud')
plt.show()

'''
## Analyzing Recipe Instructions
We analyze the length of recipe instructions to understand their distribution.
'''
# Analyze the length of recipe instructions
# Ensure the 'Instructions' column exists and contains valid data
if 'Instructions' in df.columns:
    # Fill NaN values with an empty string and ensure all instructions are strings
    df['Instructions'] = df['Instructions'].fillna('').astype(str)
    
    # Calculate the length of each instruction
    df['Instructions_Length'] = df['Instructions'].apply(len)
    
    # Plot the distribution of instruction lengths
    plt.hist(df['Instructions_Length'], bins=20)
    plt.title('Distribution of Instructions Lengths')
    plt.xlabel('Instructions Length')
    plt.ylabel('Frequency')
    plt.show()
else:
    print("The 'Instructions' column is not found in the DataFrame.")

'''
## Documentation Links

- [pandas.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)
- [pandas.read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)
- [pandas.DataFrame.head](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.head.html)
- [pandas.DataFrame.info](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.info.html)
- [pandas.DataFrame.describe](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html)
- [pandas.DataFrame.isnull](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.isnull.html)
- [pandas.Series.value_counts](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.value_counts.html)
- [matplotlib.pyplot](https://matplotlib.org/stable/api/pyplot_api.html)
- [matplotlib.pyplot.hist](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html)
- [matplotlib.pyplot.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html)
- [matplotlib.pyplot.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html)
- [matplotlib.pyplot.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html)
- [wordcloud.WordCloud](https://github.com/amueller/word_cloud)
- [pandas.Series.apply](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.apply.html)
- [pandas.Series.fillna](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.fillna.html)
- [pandas.Series.astype](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.astype.html)
'''
