


'''
	import legumes.recipe_with_goals.formulate as formulate_recipe_with_goals
	formulate_recipe_with_goals.beautifully ([
		[ retrieve_supp ("coated tablets/multivitamin_276336.JSON"), 10 ]
	])
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
			"days of nutrients per recipe": {
				"fraction string": "123/4"
			}
		}
	}
'''



import legumes.goals.human.FDA as human_FDA_goal

import apoplast.shows.ingredient_scan_recipe.formulate as formulate_recipe

def beautifully (ingredients):
	recipe = formulate_recipe.adroitly (ingredients)
	
	
	
	return;
	
	
	
	
	
	
	
	
	
	# goal = human_FDA_goal.retrieve ()