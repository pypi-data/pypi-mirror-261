
'''
	import legumes.goals.human.FDA as human_FDA_goal
	goal = human_FDA_goal.retrieve ()
'''

'''
	https://ods.od.nih.gov/HealthInformation/nutrientrecommendations.aspx
'''

'''
	https://www.fda.gov/food/nutrition-facts-label/daily-value-nutrition-and-supplement-facts-labels
'''

#
#	 of 4 or more years
#

def retrieve ():
    return {
		"label": "FDA goals for average adult humans",
		"cautions": [
			"These guidelines have not been checked by any high status nutritionists.",
			"Please consult with your actual physician or nutritionist also."
		],
		
        "ingredients": [
            {
                "goal": [ "2000", "kcal" ],
                "labels": [ "calories" ]
            },
		],
        
        "limiters": [
            {
                "includes": [
                    "human"
                ],
                "label": "species"
            },
            {
                "includes": [
                    [
                        "4",
                        "eternity"
                    ]
                ],
                "kind": "slider--integer",
                "label": "age"
            },
            {
                "includes": [
                    "pregnant",
                    "breast feeding"
                ],
                "label": "exclusions"
            }
        ],
		
        "sources": [
            "https://www.fda.gov/food/new-nutrition-facts-label/daily-value-new-nutrition-and-supplement-facts-labels",
            "https://www.fda.gov/media/99069/download",
            "https://www.fda.gov/media/99059/download"
        ]
    }
