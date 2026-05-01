# Klass uchun tavsif
class PricingTable:
    def __init__(self):
        self.tiers = [
            {"name": "Basic", "price": 9.99, "features": ["Feature 1", "Feature 2", "Feature 3"]},
            {"name": "Premium", "price": 19.99, "features": ["Feature 1", "Feature 2", "Feature 3", "Feature 4", "Feature 5"]},
            {"name": "Enterprise", "price": 29.99, "features": ["Feature 1", "Feature 2", "Feature 3", "Feature 4", "Feature 5", "Feature 6", "Feature 7", "Feature 8"]}
        ]

    def create_table(self):
        html = "<table class='w-full text-left border-collapse border border-gray-400'>"
        html += "<thead><tr>"
        html += "<th class='py-2 px-4 border border-gray-400'>Tier</th>"
        html += "<th class='py-2 px-4 border border-gray-400'>Price</th>"
        html += "<th class='py-2 px-4 border border-gray-400'>Features</th>"
        html += "</tr></thead>"
        html += "<tbody>"
        for tier in self.tiers:
            html += "<tr>"
            html += f"<td class='py-2 px-4 border border-gray-400'>{tier['name']}</td>"
            html += f"<td class='py-2 px-4 border border-gray-400'>${tier['price']}</td>"
            html += f"<td class='py-2 px-4 border border-gray-400'>{', '.join(tier['features'])}</td>"
            html += "</tr>"
        html += "</tbody></table>"
        return html

# Klassni ishlatish
pricing_table = PricingTable()
print(pricing_table.create_table())
