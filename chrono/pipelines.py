
from itemadapter import ItemAdapter


class WatchCleaningPipeline:
    def process_item(self, item, spider):

        # Clean watch_title and watch_price
        if item.get('watch_title'):
            item['watch_title'] = item['watch_title'].strip()
        if item.get('watch_price'):
            item['watch_price'] = item['watch_price'].replace(
                '$', '').replace(',', '').strip()

        # Clean watch_details
        cleaned_details = {}
        for section_name, section_data in item['watch_details'].items():
            if section_name:
                cleaned_section_name = section_name.strip()
                cleaned_section_data = {}
                for key, value in section_data.items():
                    cleaned_key = key.strip()
                    cleaned_value = value.strip() if value else ''  # Set to an empty string if None
                    if cleaned_value:
                        cleaned_section_data[cleaned_key] = cleaned_value
                if cleaned_section_data:
                    cleaned_details[cleaned_section_name] = cleaned_section_data

        item['watch_details'] = cleaned_details

        return item
