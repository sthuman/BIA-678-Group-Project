# Final Project related
from flask import Flask, request, jsonify
from your_recipe_finder import find_recipes_with_ingredients, clean_recipes, recipes_with_ingredient, recipes_with_tags

app = Flask(__name__)

@app.route('/find_recipes', methods=['POST'])
def get_recipes():
    data = request.json
    ingredients = data.get('ingredients', [])
    tags = data.get('tags', [])
    max_cooking_time = data.get('max_cooking_time', 60)
    similarity_threshold = data.get('similarity_threshold', 80)
    
    matching_df = find_recipes_with_ingredients(ingredients, tags, max_cooking_time, similarity_threshold)
    
    recipes = matching_df[['name', 'minutes', 'ingredients', 'tags']].to_dict('records')
    
    return jsonify(recipes)

if __name__ == '__main__':
    app.run(debug=True)
