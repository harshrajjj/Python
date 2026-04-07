class chaiUtils:
    @staticmethod
    def clean_ingredients(ingredients):

        return [ingredient.strip() for ingredient in ingredients]
    

raw = "water , milk , ginger , honey"

cleaned = chaiUtils.clean_ingredients(raw)
print(cleaned)