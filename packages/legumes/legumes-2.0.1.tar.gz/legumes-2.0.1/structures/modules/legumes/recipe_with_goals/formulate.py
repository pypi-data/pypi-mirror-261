


'''
	import legumes.recipe_with_goals.formulate as formulate_recipe_with_goals
	formulate_recipe_with_goals.beautifully (
		ingredients = [
			[ retrieve_supp ("coated tablets/multivitamin_276336.JSON"), 10 ]
		],
		goals = {}
	)
'''

'''
	fake data: {
		"info": {
			"includes": [],
			"names": [
				"protein"
			],
			"region": 1
		},
		"measures": {
			"mass + mass equivalents": {
				"per recipe": {
					"grams": {
						"fraction string": "65193545255861875341/11258999068426240"
					}
				},
				"portion of grove": {
					"fraction string": "1303870905117237506820000/3661863958435401439007099"
				}
			}
		},
		"goals": {
			"per day"
				"mass + mass equivalents": {
					"per recipe": {
							"grams": {
								"fraction string": "3/100000"
							}
					}
				}
			}
		}
	}
'''

'''
	{
		"labels": [ "Biotin" ],
		"goal": {
			"mass + mass equivalents": {
				"per day": {
					"grams": {
						"fraction string": "3/100000"
					}
				}
			}
		}
	}
'''

'''
	days = amount in recipe / amount of goal
'''

import legumes.goals.human.FDA as human_FDA_goal
import apoplast.shows.ingredient_scan_recipe.formulate as formulate_recipe
import ships.modules.exceptions.parse as parse_exception

'''
	find_goal (
		ingredient_names = [ 
			"protein" 
		],
		goals_ingredients = [{
			"labels": [
			  "Vitamin E"
			],
			"goal": {
				"mass + mass equivalents": {
					"per day": {
						"grams": {
							"fraction string": "3/200"
						}
					}
				}
			}
		}]
	)
'''
import rich

from fractions import Fraction
import copy

def find_goal (
	ingredient_names = [],
	goals_ingredients = []
):
	for ingredient_name in ingredient_names:
		ingredient_name_lower = ingredient_name.lower ()
	
		for goal in goals_ingredients:
			for goal_label in goal ["labels"]:
				print ("goal?", goal_label.lower (), ingredient_name_lower)
			
				if (goal_label.lower () == ingredient_name_lower):
					return goal;
			
				
	return None

def beautifully (
	ingredients = [],
	goals = {}
):
	recipe = formulate_recipe.adroitly (
		ingredients
	)
	essential_nutrients = recipe ["essential nutrients"]
	essential_nutrients_grove = essential_nutrients ["grove"]
	cautionary_ingredients = recipe ["cautionary ingredients"]
	
	recipe ["goals"] = goals
	goals_ingredients = goals ["ingredients"];
	
	skipped = []
	
	for ingredient in essential_nutrients_grove:
		ingredient_names = ingredient ["info"] ["names"]
		
		print ('ingredients:', ingredient_names)
		
		ingredient ["goals"] = {}
		
		#ingredient ["00000"] = 1;
		#continue;
		
		goal = None;
		try:
			goal = find_goal (
				ingredient_names = ingredient_names,
				goals_ingredients = goals_ingredients
			)
		except Exception as E:
			print (parse_exception.now (E))
		
			print ("goal not found:", ingredient_names)
			skipped.append (ingredient_names)
			continue;
		
		
		#
		#	grams:
		#	
		try:
			rich.print_json (data = {
				"goal": goal,
				"ingredient": ingredient
			})
			
			grams_per_recipe = (
				ingredient ["measures"] ["mass + mass equivalents"] ["per recipe"] ["grams"] ["fraction string"]
			)
			grams_per_goal = (
				goal ["goal"] ["mass + mass equivalents"] ["per Earth day"] ["grams"] ["fraction string"]
			)
			goal_per_day = (
				Fraction (grams_per_recipe) / 
				Fraction (grams_per_goal)
			)

			ingredient ["goals"] = {
				"days of ingredient": {
					"mass + mass equivalents": {
						"per recipe": {
							"fraction string": str (goal_per_day)
						}
					}
				}
			}
			
			#print ("ingredient:", ingredient ["info"] ["names"])
			#print ("	grams:", grams)
			
		except Exception as E:
			print (parse_exception.now (E))
			skipped.append (ingredient_names)
			pass;


	return {
		"recipe": recipe,
		"skipped": skipped
	};
	
	
