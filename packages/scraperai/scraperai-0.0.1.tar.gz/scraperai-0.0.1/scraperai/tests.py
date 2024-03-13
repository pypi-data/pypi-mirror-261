import json
import re


def postprocess_json(data):
    def clean_price(price):
        # Remove non-numeric characters except decimal point
        return float(re.sub(r'[^\d.]', '', price))

    def clean_key(key):
        # Convert to lowercase and replace spaces with underscores
        return re.sub(r'\s+', '_', key.strip()).lower()

    def clean_value(value):
        # Remove excessive whitespace and newline characters
        return ' '.join(value.split())

    # Initialize a new dictionary for the cleaned data
    cleaned_data = {}

    for key, value in data.items():
        new_key = clean_key(key)

        # Process price differently to convert it into a float
        if 'price' in new_key:
            cleaned_data[new_key] = clean_price(value)
        else:
            cleaned_data[new_key] = clean_value(value)

    # Optionally, remove redundant or irrelevant entries
    # For this example, let's assume all keys are relevant.
    # If needed, you can delete keys like this:
    # if 'irrelevant_key' in cleaned_data:
    #     del cleaned_data['irrelevant_key']

    return cleaned_data


# Example usage with the provided JSON data
json_data = {
    "Product Title": "Сервиз чайный (14 предметов)",
    "Product Price": "10 468 ₽",
    "Product Material": "Фарфор, грунт, олифа, эмаль, натуральные пигменты-красители, лак пригодный для\nконтакта с пищевыми продуктами.",
    "Main Image": "/proxy.php?secret=70afdc1781375774058ee86adcdfc8fa&url=https%3A%2F%2Fcdn.goldenhohloma.com%2Fupload%2Fresize_cache%2Fiblock%2Fe78%2F548_714_1%2Fe78339bf3e78f49de2fb4727920e81aa.jpg",
    "Посуда": "/goods-company/view/21?filter[tags][]=30",
    "Изделия из фарфора и металла": "/goods-company/view/21?filter[tags][]=1214",
    "Материалы: ........................................................................................................................................................................................................": "Фарфор, грунт, олифа, эмаль, натуральные пигменты-красители, лак пригодный для\nконтакта с пищевыми продуктами."
}

cleaned_json = postprocess_json(json_data)
print(json.dumps(cleaned_json, indent=4, ensure_ascii=False))
