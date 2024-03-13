


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



#
#	ingredient = "ThiamIn"
#
def find_goal_ingredient (ingredient):
	def for_each (essential):
		try:
			for name in essential ["names"]:
				if (name.lower () == ingredient.lower ()):
					return True;
					
		except Exception:
			pass;
			
		return False

	nutrient = seek_nutrient.presently (
		for_each = for_each
	)
	
	return nutrient;

'''
	using: apoplast ingredients database
	
	find where:
		goal ingredient region == composition ingredient region
'''
def find_goal (
	ingredient_names = [],
	goals_ingredients = []
):
	for ingredient_name in ingredient_names:
		ingredient_name_lower = ingredient_name.lower ()
		
		try:
			composition_DB_entry_region = find_goal_ingredient (ingredient_name_lower) ["region"]
		except Exception:
			#print ("region not found", ingredient_name_lower)
			continue;
		
	
		for goal in goals_ingredients:
			for goal_label in goal ["labels"]:
				try:
					goal_DB_entry_region = find_goal_ingredient (goal_label) ["region"]
				except Exception:
					#print ("		region not found")
					pass;
			
				if (
					composition_DB_entry_region ==
					goal_DB_entry_region
				):
					return goal;
			
				
	return None